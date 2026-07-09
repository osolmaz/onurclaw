---
title: Memory power and KV-aware bounds for local LLM inference
author: Onur Solmaz <onur@solmaz.io>
date: 2026-06-30
---

# Memory power and KV-aware bounds for local LLM inference

This note builds, from first principles, a memory-side upper bound on how fast a
local machine can serve large language models. It is the mathematical contract
behind the local frontier hardware calculator: a roofline that, for a given
hardware and model pair under a stated set of assumptions, says what the pair
*cannot exceed*. Its outputs are ceilings for comparing machines; a real
implementation lands somewhere below them.

The argument is built in layers, each one created by a problem the previous
layer cannot solve:

1. A memory system is two numbers, capacity and bandwidth. Their product is a
   natural measure of what the system can fund. We justify that product instead
   of asserting it, and give it a name.
2. That product turns into a clean but loose throughput ceiling for batched
   decoding.
3. The loose ceiling ignores per-session context traffic, so it is too generous
   for real serving. Repairing it gives the bound the calculator actually uses.
4. The repaired bound is filled in per architecture by small adapters, run by a
   short algorithm, and checked against real hardware.

Source conversation: <https://chatgpt.com/share/6a4379ca-3ec4-83ec-8dc5-afcee73b1d3b>.
The converted transcript is `2026-06-30-chatgpt-local-llm-inference-conversation.md`
and the raw share state is `2026-06-30-chatgpt-local-llm-inference-state.json`.

## What the model bounds

Local inference raises three separate questions, and conflating them is the most
common way to be wrong about a machine.

| Question | What it asks |
| --- | --- |
| Resident fit | Can the model plus runtime overhead be held in memory at all? |
| Single-session speed | What is the memory-side ceiling for one active conversation? |
| Useful serving throughput | Across many active sessions, how many tokens per second can the device produce while each session stays above a minimum useful rate? |

The third question is the hard one. A machine can fit many sessions in memory
and still be too slow per session at that concurrency. So the calculator must
report both whether sessions fit and whether the fitting sessions are fast
enough to be worth running.

Every number produced here is an upper bound. A real system can fall below it
for reasons the memory model deliberately ignores: compute limits, kernel
quality, quantization overhead, scheduling, CPU involvement, paging,
interconnects, thermal throttling, sampling, and application overhead. The value
of a clean upper bound is that it tells you the best case you are allowed to hope
for, and therefore how much room an implementation still has.

## Memory system as a fundable resource

Before any model-specific detail, ask what a memory system fundamentally offers.
When people compare accelerators for local inference they list many specs:
capacity, bandwidth, compute throughput, precision support, cache hierarchy, PCIe
lanes, multi-GPU links, power and thermals, host RAM. For the *decode* phase of
autoregressive generation, two of these recur in almost every bound: how much
state the memory can hold, and how fast it can move that state. We start there.

### Two numbers and their product

Model an idealized memory system by exactly two quantities.

```math
C = \text{usable memory capacity}, \qquad R = \text{sustained memory bandwidth}.
```

Capacity is a stock: how much resident state can exist at once. Bandwidth is a
flow: how much state can be moved per second. They have different units and
answer different questions, so any single product of them needs justifying before
we rely on it.

Define **memory power** as

```math
D = C R .
```

If $C$ is in GB and $R$ is in GB/s, then $D$ is in $\mathrm{GB}^2/\mathrm{s}$.
The units look strange. The rest of this section explains why this particular
combination of $C$ and $R$ is the right scalar.

### Units: bytes, shannons, and the dennard

For engineering we use decimal GB and GB/s, because those are the units in a
hardware catalog. For the information-theoretic justification it is cleaner to
measure memory in *shannons*, the maximum-entropy content of a binary memory
cell:

```math
1\ \text{byte} = 8\ \mathrm{Sh}.
```

In shannon units, capacity $C$ is in $\mathrm{Sh}$, bandwidth $R$ is in
$\mathrm{Sh}/\mathrm{s}$, and memory power has units $\mathrm{Sh}^2/\mathrm{s}$.
That product unit deserves a name. We call it the **dennard**:

```math
1\ \mathrm{Dn} = 1\ \mathrm{Sh}^2/\mathrm{s}.
```

The eponym is Robert H. Dennard, who invented DRAM — the random-access memory
lineage that GPU VRAM and unified memory belong to, as opposed to persistent
flash or disk storage. The name collides slightly with *Dennard scaling*, the
transistor-scaling law, but the association with memory is the point and the
collision is tolerable. A worked feel for the unit: a 24 GB GPU at 1000 GB/s has
$H = 24 \times 8 = 192$ gigashannons of capacity and $\Phi = 8000$
gigashannons/s of flux, so its memory power is $192 \times 8000 \approx
1.54 \times 10^{24}\ \mathrm{Sh}^2/\mathrm{s} = 1.54$ yottadennards.

Be careful with one thing throughout: every memory quantity in a given
calculation must use the *same* unit system. The equations are identical whether
you work in shannons or in GB; only the numeric value of $D$ changes. The name
matters far less than the product, and the next two results explain why the
product is forced.

### Resident-Flux Feasibility Theorem

Here is the toy problem that justifies $CR$, in the same spirit that the
noisy-channel theorem justifies the bit and the shannon.

A pure memory workload is a pair $w = (h, r)$, where $h$ is the resident
information it must keep alive and $r$ is the information flow rate it must
sustain. The workload is *feasible* on the system $M(C, R)$ when the memory can
both hold the state and carry the traffic. There are exactly two ways to fail.

The first is a capacity failure. If a workload needs more resident state than the
memory can store, it cannot fit, and no scheduling trick repairs that:

```math
h \le C .
```

The second is a flux failure. If a workload needs more traffic per second than
the interface can deliver, it cannot be sustained, and no surplus capacity
repairs that:

```math
r \le R .
```

In the idealized model these two conditions are also sufficient: if $h \le C$
and $r \le R$, allocate $h$ of state and stream at rate $r$. Therefore the
feasible set is precisely the rectangle

```math
F(C, R) = \{(h, r) : 0 \le h \le C,\ 0 \le r \le R\},
```

whose area is

```math
\mu(F) = C R .
```

So memory power has a concrete meaning: it is the *measure of the feasible
workload region*. A workload lives at a point $(h, r)$ in the plane; the system
can serve every workload inside its rectangle and none outside; the size of that
rectangle is $CR$.

### A uniqueness argument

The feasibility theorem shows $CR$ is *a* natural measure. A short axiomatic
argument shows it is essentially the *only* one. Suppose we want a scalar
capability measure $D(C, R)$ and require three mild properties.

First, a zero law: a system with no capacity or no bandwidth can fund nothing.

```math
D(0, R) = 0, \qquad D(C, 0) = 0 .
```

Second, additivity along the capacity axis: splitting the resident-information
range into two disjoint parts splits the capability additively.

```math
D(C_1 + C_2,\ R) = D(C_1, R) + D(C_2, R).
```

Third, the same additivity along the flux axis.

```math
D(C,\ R_1 + R_2) = D(C, R_1) + D(C, R_2).
```

With mild continuity to exclude pathological solutions, the only function
satisfying all three is bilinear,

```math
D(C, R) = k\, C R ,
```

and choosing the unit so that $k = 1$ gives $D = CR$. Under these axioms the
product is the unique admissible measure.

### A caveat that keeps the metric honest

One misreading is worth heading off. The product $CR$ measures the
*workload-feasibility region*: the set of jobs the device can support at an
instant. A different question — "how many distinct memory histories can this
device produce over a time $T$?" — has a different answer, the resident
information plus the information streamed over that window,

```math
C + R T .
```

The feasibility-region reading is the one an inference-throughput bound will
need, because serving is the business of keeping feasible workloads resident and
streaming — which is the subject of the next chapter.

## From memory power to a decode bound

The feasibility theorem describes static workloads. Decoding is dynamic: it emits
tokens over time. This chapter turns memory power into a throughput ceiling for
batched decoding, and in doing so shows *where* the product $CR$ enters a real
performance bound.

### A toy decoder

Consider the decode phase of an autoregressive transformer, simplified to the
memory system alone. Let

```math
W = \text{model weight footprint}, \qquad K = \text{per-session KV/state footprint},
```

let $b$ be the batch size (number of concurrent sequences), and let $s$ be the
number of decode steps per second. Each decode step emits one token per active
sequence, so aggregate output throughput is

```math
T = b \, s .
```

Throughput is a product of two things — how many sequences run in parallel, and
how fast the shared model can be swept — and the memory system caps each factor
separately.

### Capacity limit

The model weights must be resident once, and every active sequence needs its own
KV cache. So the resident state is $W + bK$, and it must fit:

```math
W + bK \le C \quad\Longrightarrow\quad b \le \frac{C - W}{K} .
```

This is the capacity limit: it sets the *maximum parallelism*. It is exactly the
$h \le C$ condition of the feasibility theorem, with $h = W + bK$.

### Bandwidth limit

In a dense transformer, each decode step must apply the model weights. In the
memory-bound idealization, applying the weights means streaming roughly $W$ of
data per step. With bandwidth $R$, the step rate obeys

```math
s W \le R \quad\Longrightarrow\quad s \le \frac{R}{W} .
```

This is the bandwidth limit: it sets the *maximum step rate*. It is the
$r \le R$ condition, with the per-step traffic playing the role of the flux.

### Dennard Decode Bound

Multiply the two caps. Throughput is parallelism times step rate, and each is
separately bounded, so

```math
T = b\, s \le \frac{C - W}{K}\cdot\frac{R}{W} = \frac{R\,(C - W)}{K W} .
```

Substituting $D = CR$ and factoring out $C$ exposes the memory-power term:

```math
T \le \frac{D}{K W}\left(1 - \frac{W}{C}\right).
```

When the model is much smaller than memory, $W \ll C$, the correction vanishes
and the bound collapses to the memorable form

```math
T \lesssim \frac{D}{K W} .
```

This is the **Dennard Decode Bound**. The product $CR$ appears because maximum
throughput genuinely factors into maximum parallelism times maximum step rate:

```math
\underbrace{\frac{C}{K}}_{\text{how many sessions resident}}\times
\underbrace{\frac{R}{W}}_{\text{how many sweeps per second}} = \frac{CR}{KW} = \frac{D}{KW} .
```

The numerator $D = CR$ is the machine. The denominator $KW$ is the workload: the
per-session state times the model sweep size. The whole law reads as *throughput
is memory power divided by memory cost per active model-token*.

### When the bound applies, and when it does not

The Dennard Decode Bound governs batched throughput. Set $b = 1$ and it
degenerates:

```math
T \lesssim \frac{R}{W},
```

so for a single session only bandwidth matters and capacity is merely a fit
constraint. That is the correct behavior, and it sharpens what each metric is
for:

| Use case | The metric that governs it |
| --- | --- |
| Single-user local chat | bandwidth $R$, with capacity $C$ as a fit gate |
| Largest model that fits | capacity $C$ first, then bandwidth |
| Maximum batched decode throughput | memory power $D = CR$ |

Memory power is the right scalar precisely for the third row. The next chapter
attacks the reason even that row's bound is too optimistic.

## The loose bound is too generous

The Dennard Decode Bound assumes the only per-token memory traffic worth counting
is the model sweep $W$, shared across the batch. Real decoding also reads each
session's growing KV cache, and that traffic is *private*: it is not amortized
over the batch. Ignoring it makes the bound promise throughput that long-context
serving can never reach. This chapter introduces the correct per-token
accounting, and shows the Dennard bound falls out of it as a loose corollary.

### Universal resource bound

Step back to the most general statement, which holds regardless of architecture.
If each output token costs at least $q_{\min}$ of unavoidable memory traffic and
at least $a_{\min}$ of unavoidable compute, and the device delivers at most $R$
bytes/s and $F$ FLOP/s, then over all setups that fit,

```math
T_{\max} \le \max_{\text{setup fits}} \min\!\left(\frac{R}{q_{\min}},\ \frac{F}{a_{\min}}\right).
```

Two rooflines, and the workload lives under the lower of them. Throughout this
note we assume decode is memory-bound, which is the usual case for local serving,
and keep the memory roofline:

```math
T_{\max} \le \frac{R}{q},
```

where $q$ is the memory traffic per output token. Everything now reduces to
estimating $q$ honestly. The reason we focus on the memory side is also
practical: a hardware catalog can collect capacity and bandwidth consistently
across consumer and workstation devices, while comparable sustained-compute
numbers are much harder to obtain.

### A bytes-per-token model

Split the per-token traffic into the two kinds that behave differently under
batching. The model (or active-expert) weights are *shared*: one sweep serves the
whole batch, so its per-token cost is divided by the batch. The KV/context read
is *private*: each session reads its own cache, so its per-token cost is not
divided at all. With $W_{\mathrm{active}}$ the shared weight traffic per
iteration, $\rho$ the tokens emitted per session per iteration (one for ordinary
decoding), and $K_{\mathrm{read}}(L)$ the private context traffic per output
token at active context length $L$,

```math
q_{\text{simple}}(b) = \frac{W_{\mathrm{active}}}{b\,\rho} + K_{\mathrm{read}}(L).
```

The first term shrinks as the batch grows — more sessions share each weight
sweep. The second term does not move: a larger batch does not make any session's
context cheaper to read. This asymmetry is the entire reason long-context serving
behaves differently from short-context serving.

### Inequality chain

Treat $q_{\text{simple}}$ as an optimistic *lower* estimate of the true
bytes/token, $q_{\text{simple}}(b) \le q_{\text{actual}}(b)$. Dividing $R$ by a
smaller denominator gives a larger quotient, so substituting $q_{\text{simple}}$
keeps the result an upper bound:

```math
T_{\max} \le \max_{b\,:\,W_{\mathrm{resident}} + b K_{\mathrm{store}} + O \le C}\ \frac{R}{\dfrac{W_{\mathrm{active}}}{b\rho} + K_{\mathrm{read}}(L)} .
```

Here the maximization runs over batches that fit in memory, with
$W_{\mathrm{resident}}$ the resident model footprint, $K_{\mathrm{store}}$ the KV
memory stored per session, and $O$ the runtime overhead. This is the honest
simple bound: bandwidth divided by shared-per-token cost plus private-per-token
cost, maximized over fitting batches.

### The Dennard Ceiling is a corollary

Now recover the previous chapter's bound by deliberately throwing information
away. Since $K_{\mathrm{read}}(L) \ge 0$, dropping it only loosens the
denominator:

```math
\frac{R}{\dfrac{W_{\mathrm{active}}}{b\rho} + K_{\mathrm{read}}(L)} \le \frac{R}{\dfrac{W_{\mathrm{active}}}{b\rho}} = \frac{b\,\rho\,R}{W_{\mathrm{active}}} .
```

The capacity constraint caps the batch at
$b \le (C - W_{\mathrm{resident}} - O)/K_{\mathrm{store}}$, so

```math
T_{\max} \le \rho\,\frac{R\,(C - W_{\mathrm{resident}} - O)}{K_{\mathrm{store}}\,W_{\mathrm{active}}} = \rho\,\frac{D}{K_{\mathrm{store}}\,W_{\mathrm{active}}}\left(1 - \frac{W_{\mathrm{resident}} + O}{C}\right).
```

This is the Dennard Decode Bound again, now revealed as what you get by
*discarding the private context term and using the largest batch that fits*. That
is why it can sit far above achievable throughput while remaining a true ceiling.
The ordering is

```math
\text{actual throughput} \;\le\; \text{simple (KV-aware) bound} \;\le\; \text{Dennard bound}.
```

The Dennard bound is the orientation line; the KV-aware bound is the one to
serve from. The next chapter develops it into the operational calculator.

## KV-Aware Bound

This chapter turns the simple bytes-per-token bound into the model the calculator
runs. Three refinements are needed: context must be split into the part that
controls memory and the part that controls speed; the shared weight traffic must
be allowed to grow with the batch (for mixture-of-experts models); and the batch
must be filtered so that we never count concurrency at which every session has
become uselessly slow.

### Two context lengths

A serving system usually *reserves* KV space for a long maximum context but
*reads*, on average, a shorter active context. These two lengths drive different
parts of the bound, so we keep them separate.

```math
L_{\mathrm{alloc}} = \text{reserved (maximum) context}, \qquad L_{\mathrm{read}} = \text{average active context}, \qquad L_{\mathrm{read}} \le L_{\mathrm{alloc}}.
```

The allocation length controls how much KV memory each session reserves, and
therefore how many sessions fit. The read length controls how much context each
output token must stream, and therefore per-token cost. Collapsing them into one
number is a common modeling error: it either overcharges memory or overcharges
speed.

### Model quantities

A model contributes five quantities. Two are about fitting, two are about speed,
and one is about decoding style.

| Symbol | Role |
| --- | --- |
| $W_{\mathrm{resident}}$ | Full resident footprint (for MoE, all resident weights, including the inactive experts) |
| $W_{\mathrm{batch}}(b)$ | Shared weight traffic per decode iteration at batch $b$ |
| $K_{\mathrm{alloc}}(L_{\mathrm{alloc}})$ | KV/cache memory reserved per session — controls concurrency |
| $K_{\mathrm{read}}(L_{\mathrm{read}})$ | Private context traffic per output token — controls decode cost |
| $\rho$ | Tokens emitted per session per iteration ($\rho = 1$ ordinary, $\rho > 1$ speculative) |

The split between $K_{\mathrm{alloc}}$ and $K_{\mathrm{read}}$ mirrors the split
between the two context lengths: allocation controls how many sessions fit, read
controls how fast each one decodes. Note that $W_{\mathrm{batch}}$ now
depends on the batch size $b$ — the next refinement explains why.

### Memory-fit batch

The first gate is whether sessions fit. Load the model, reserve overhead, and
divide the remainder by the per-session allocation:

```math
b_{\mathrm{mem}}(L_{\mathrm{alloc}}) = \left\lfloor \frac{C - W_{\mathrm{resident}} - O}{K_{\mathrm{alloc}}(L_{\mathrm{alloc}})} \right\rfloor .
```

This is memory-fit concurrency only. It is necessary but not sufficient: it is
exactly the trap that makes a machine look like it can serve a hundred sessions
when it cannot serve them *usefully*.

### Traffic per token and the aggregate bound

The per-token traffic is the shared weight sweep amortized over the emitted
tokens, plus the private context read:

```math
q_{\mathrm{KV}}(b, L_{\mathrm{read}}) = \frac{W_{\mathrm{batch}}(b)}{b\,\rho} + K_{\mathrm{read}}(L_{\mathrm{read}}) .
```

Then the memory roofline $T \le R/q$ gives the aggregate ceiling at batch $b$,

```math
T(b, L_{\mathrm{read}}) \le \frac{R}{q_{\mathrm{KV}}(b, L_{\mathrm{read}})},
```

and dividing by the batch gives the per-session rate,

```math
r(b, L_{\mathrm{read}}) = \frac{T(b, L_{\mathrm{read}})}{b} = \frac{\rho R}{W_{\mathrm{batch}}(b) + b\,\rho\,K_{\mathrm{read}}(L_{\mathrm{read}})} .
```

As $b$ grows, the aggregate $T$ rises but the per-session $r$ falls. That tension
is the whole serving tradeoff, and it is why a fit-only bound is not enough.

### Usable-batch correction

The fix is to refuse batches at which a session would crawl. Impose a per-session
floor $r_\star$, the minimum useful tokens/s/session, and solve $r(b) \ge r_\star$
for $b$. Replacing the batch-dependent $W_{\mathrm{batch}}(b)$ by its shared lower
bound $W_{\mathrm{active}}$ keeps a closed form. Because
$W_{\mathrm{batch}}(b) \ge W_{\mathrm{active}}$, the substitution only weakens the
condition, so the implication runs one way — the closed form is a necessary
condition on the admissible batch, not a sufficient one:

```math
r(b) \ge r_\star \quad\Longrightarrow\quad b \le \frac{\rho R / r_\star - W_{\mathrm{active}}}{\rho\,K_{\mathrm{read}}(L_{\mathrm{read}})} ,
```

which defines a rate-limited batch

```math
b_{\mathrm{rate}}(L_{\mathrm{read}}, r_\star) = \left\lfloor \frac{\rho R / r_\star - W_{\mathrm{active}}}{\rho\,K_{\mathrm{read}}(L_{\mathrm{read}})} \right\rfloor .
```

The usable batch is whichever gate binds first:

```math
b_{\mathrm{usable}} = \min\!\big(b_{\mathrm{mem}}(L_{\mathrm{alloc}}),\ b_{\mathrm{rate}}(L_{\mathrm{read}}, r_\star)\big).
```

Because $b_{\mathrm{rate}}$ comes from a necessary condition, $b_{\mathrm{usable}}$
is itself an upper bound on the truly admissible batch; the calculator applies
the exact floor test with the true $W_{\mathrm{batch}}(b)$ in the next section.
This is what stops the "hundred sessions" illusion. As context grows,
$K_{\mathrm{read}}(L)$ grows, so $b_{\mathrm{rate}}$ falls quickly even while
$b_{\mathrm{mem}}$ stays large. The KV slots fit; the useful rate does not. (An
implementation cap could be folded in as a third term in the minimum, but the
local frontier app does not impose one, so we omit it.)

### The bound the calculator uses

Collecting the pieces, define the usable batch set as the fitting batches that
also clear the floor,

```math
\mathcal{B}(L_{\mathrm{alloc}}, L_{\mathrm{read}}, r_\star) = \left\{ b : 1 \le b \le b_{\mathrm{mem}}(L_{\mathrm{alloc}}),\ \frac{1}{b}\,\frac{R}{q_{\mathrm{KV}}(b, L_{\mathrm{read}})} \ge r_\star \right\},
```

and take the best aggregate over that set:

```math
T_{\max}(L_{\mathrm{alloc}}, L_{\mathrm{read}}, r_\star) \le \max_{b \in \mathcal{B}}\ \frac{R}{\dfrac{W_{\mathrm{batch}}(b)}{b\,\rho} + K_{\mathrm{read}}(L_{\mathrm{read}})} .
```

This is the **KV-Aware Bound**, the main practical formulation. In words: try
every batch that fits, reject the ones too slow per session, and for the rest take
bandwidth divided by bytes per output token, keeping the best.

The looser **Dennard Bound** is its corollary, obtained as before by dropping the
private term and using the largest fitting batch:

```math
T_{\max} \le \rho\,\frac{D}{K_{\mathrm{alloc}}(L_{\mathrm{alloc}})\,W_{\mathrm{active}}}\left(1 - \frac{W_{\mathrm{resident}} + O}{C}\right), \qquad D = CR.
```

The two stand in a fixed relation — the headline result of the whole derivation,
written first by name and then in full:

```math
\begin{aligned}
T_{\max} \;&\le\; \text{KV-Aware Bound} \;\le\; \text{Dennard Bound} \;\le\; \text{Large-Memory Limit} \\[6pt]
T_{\max} \;&\le\; \max_{b \in \mathcal{B}}
\frac{R}{\dfrac{W_{\mathrm{batch}}(b)}{b\rho} + K_{\mathrm{read}}(L_{\mathrm{read}})} \\[8pt]
\;&\le\; \rho\,\frac{D}{K_{\mathrm{alloc}}(L_{\mathrm{alloc}})\,W_{\mathrm{active}}}
\left(1 - \frac{W_{\mathrm{resident}} + O}{C}\right) \\[8pt]
\;&\le\; \rho\,\frac{D}{K_{\mathrm{alloc}}(L_{\mathrm{alloc}})\,W_{\mathrm{active}}}
\end{aligned}
```

The gap across these terms is the point of the whole derivation. The KV-aware
line is the tight, practical bound; the Dennard line shows the memory system's
large theoretical capacity-bandwidth product, and the distance between them is the
private context traffic, expert diversity, and per-session floor that consume most
of that optimism. The final term drops the resident-model factor
$\left(1 - (W_{\mathrm{resident}} + O)/C\right)$ as well, so the right-hand side
is exactly the simplified $D/(KW)$ from the Dennard Decode Bound, now with
$K = K_{\mathrm{alloc}}(L_{\mathrm{alloc}})$ and $W = W_{\mathrm{active}}$. It is
the loosest, most optimistic reading, since the resident model and overhead always
claim a real share of $C$.

### Single-session case

Set $b = 1$ to recover the latency-style bound for one conversation. There is no
batch to amortize the weight sweep over:

```math
T_{1,\max} \le \frac{R}{W_{\mathrm{batch}}(1)/\rho + K_{\mathrm{read}}(L_{\mathrm{read}})},
```

and for ordinary decoding ($\rho = 1$) this is just
$R / (W_{\mathrm{batch}}(1) + K_{\mathrm{read}}(L_{\mathrm{read}}))$. Capacity has
dropped out except as the gate that decides whether the model fits at all —
consistent with the earlier observation that bandwidth governs single-session
speed.

### Speculative decoding

Speculative decoding lets $\rho > 1$: a draft model proposes several tokens and
the target verifies them in one iteration, so $\rho$ is the expected number of
accepted tokens per session per verification step, bounded by the draft length
$\gamma$ as $1 \le \rho \le \gamma + 1$. The temptation is to multiply throughput
by $\rho$ and stop. That is wrong, because the draft model and verification are
not free: their traffic belongs in $W_{\mathrm{batch}}(b)$ or in the per-token
term. The safe rule is to never scale by $\rho$ without charging the draft cost in
the denominator. With both effects included, speculative decoding moves through
the same KV-aware formula unchanged.

## Model adapters

The KV-aware bound is architecture-agnostic; an architecture enters only through
the five quantities. So each model family is captured by a small adapter that
supplies them:

```math
\mathrm{Adapter}(M) = \big[\, W_{\mathrm{resident}},\ W_{\mathrm{batch}}(b),\ K_{\mathrm{alloc}}(L_{\mathrm{alloc}}),\ K_{\mathrm{read}}(L_{\mathrm{read}}),\ \rho \,\big].
```

Three adapters cover the catalog: dense transformers, mixture-of-experts, and
hybrid/sliding/recurrent attention.

### Dense transformer

For a dense model with $P_{\mathrm{total}}$ parameters at $e_w$ bytes each, all
weights are touched every step, so the resident footprint and the per-step sweep
coincide:

```math
W_{\mathrm{resident}} = W_{\mathrm{batch}}(b) = P_{\mathrm{total}}\, e_w .
```

With $N_{\mathrm{layers}}$ layers, $N_{\mathrm{kv}}$ key/value heads, head
dimension $d_h$, and KV byte widths $e_{\mathrm{KV,store}}$ and
$e_{\mathrm{KV,read}}$, full-context attention reserves and reads

```math
K_{\mathrm{alloc}}(L) = 2\, N_{\mathrm{layers}}\, N_{\mathrm{kv}}\, d_h\, e_{\mathrm{KV,store}}\, L, \qquad K_{\mathrm{read}}(L) \approx 2\, N_{\mathrm{layers}}\, N_{\mathrm{kv}}\, d_h\, e_{\mathrm{KV,read}}\, L,
```

where the factor $2$ counts keys and values. Note that weight precision and KV
precision are independent settings: NVFP4 weights do not imply an NVFP4 cache, so
$e_w$ and $e_{\mathrm{KV}}$ are tracked separately.

### Mixture-of-experts

An MoE model is where the constant-$W_{\mathrm{batch}}$ assumption breaks, and
fixing it is the single most important adapter correction. Let
$P_{\mathrm{total}}$ be total parameters, $P_{\mathrm{active}}$ the active
parameters per token, $E$ the number of routed experts, and $k$ the experts
selected per token. Assuming uniformly sized routed experts, each routed expert
holds

```math
p_{\mathrm{expert}} = \frac{P_{\mathrm{total}} - P_{\mathrm{active}}}{E - k},
```

and the always-on remainder — dense trunk, shared experts, embeddings, attention
— is

```math
P_{\mathrm{fixed}} = P_{\mathrm{active}} - k\, p_{\mathrm{expert}} .
```

The naive model assumes a batch touches the same active experts every session,
keeping $W_{\mathrm{batch}}$ constant. That is false: independent sessions route
to different experts, so a larger batch touches more *distinct* experts. With
$b\rho$ token-routings, each independently missing a given expert with
probability $1 - k/E$, the expected number of distinct experts touched is

```math
m(b\rho) = E\left(1 - \left(1 - \frac{k}{E}\right)^{b\rho}\right),
```

and the per-iteration shared traffic is the fixed part plus the touched experts:

```math
W_{\mathrm{batch}}(b) = e_w\big[\, P_{\mathrm{fixed}} + p_{\mathrm{expert}}\, m(b\rho) \,\big].
```

At $b\rho = 1$ this reduces to the active-parameter footprint; as $b\rho \to
\infty$ it saturates at all $E$ experts. This rising $W_{\mathrm{batch}}(b)$ is
why MoE batching does not amortize for free, and why the MoE rows in the worked
table reach their throughput optimum at modest batch sizes.

One caveat keeps the upper-bound contract honest. Every other traffic term in
the bound is a deliberate *under*-estimate of real traffic, which is what makes
$R/q$ a true ceiling. The expert count $m(b\rho)$ is different: it is an
*expectation* under independent, uniform routing, not a lower bound. Real
routing is correlated — load-balancing losses push toward uniform, but hot
experts and topically similar sessions pull the other way — and correlated
routing touches *fewer* distinct experts than the formula predicts. In that
case the modeled traffic overstates the actual traffic, and the computed
ceiling can sit slightly below the true one. When a guaranteed ceiling is
required, replace $m(b\rho)$ by its minimum $k$, i.e. replace
$W_{\mathrm{batch}}(b)$ by $W_{\mathrm{active}}$; the expectation form is the
better estimate, the floor form is the safe bound.

### Hybrid, sliding, and recurrent attention

Models with local or sliding-window attention, compressed or latent attention, or
linear/recurrent state must not use the full-KV formula blindly, because their
cache does not grow linearly in $L$ everywhere. Split both KV terms into global,
local, and fixed-state parts:

```math
K_{\bullet}(L) = K_{\mathrm{global},\bullet}(L) + K_{\mathrm{local},\bullet}(L) + K_{\mathrm{state},\bullet}, \qquad \bullet \in \{\mathrm{alloc}, \mathrm{read}\}.
```

A simple read approximation with sliding-window width $w$ is

```math
K_{\mathrm{read}}(L) = \kappa_{\mathrm{global}}\, L + \kappa_{\mathrm{local}}\,\min(L, w) + K_{\mathrm{state}} .
```

Full-attention layers pay for the whole context; sliding-window layers pay only
up to the window; recurrent or latent state adds a fixed or slowly growing term.
The same shape covers Gemma-style local/global attention and DeepSeek-style
compressed/sparse attention; only the coefficients change.

## Calculator

The bound is now operational. Because the same computation runs for every
hardware-and-model pair, it is worth stating once as a procedure.

**Inputs.** A hardware row $(C, R, O)$; a model adapter
$(W_{\mathrm{resident}}, W_{\mathrm{batch}}(\cdot), K_{\mathrm{alloc}}(\cdot),
K_{\mathrm{read}}(\cdot), \rho)$; and workload assumptions
$(L_{\mathrm{alloc}}, L_{\mathrm{read}}, r_\star)$.

**Steps.**

1. Compute the resident margin $C - W_{\mathrm{resident}} - O$. If it is
   negative, the model does not fit; stop.
2. Compute $K_{\mathrm{alloc}}(L_{\mathrm{alloc}})$ and the memory-fit batch
   $b_{\mathrm{mem}}$.
3. For each integer batch $1 \le b \le b_{\mathrm{mem}}$, compute
   $W_{\mathrm{batch}}(b)$ and $q_{\mathrm{KV}}(b, L_{\mathrm{read}})$.
4. Compute the aggregate ceiling $R / q_{\mathrm{KV}}$ and the per-session
   ceiling $R / (b\, q_{\mathrm{KV}})$ at each batch.
5. Keep the batches whose per-session ceiling is at least $r_\star$.
6. Among the kept batches, choose the one with the largest aggregate ceiling;
   report it as the KV-aware result and its batch as $b^\star$.
7. Separately compute the Dennard ceiling for orientation.

**Reading the result.** The output is a stack of gates, and the right phrasing
depends on which gate bound:

| State | Meaning |
| --- | --- |
| Resident fit | The model plus overhead fits in memory |
| Session fit | At least one reserved-context session fits |
| Floor fit | Some fitting batch clears $r_\star$ |
| No floor | Sessions fit, but no batch clears $r_\star$ |

**The common invalid reading.** Fitting in memory does not imply serving
usefully. A model can pass resident fit and session fit and still have an empty
usable batch set, because every fitting batch is below the floor. The honest
report for that case is "fits, but no batch satisfies the floor," a distinct
verdict from a true fit failure. Keeping the two apart is the reason the floor
gate exists.

## Worked examples

The theory earns its keep on real hardware. The conversation centered on two
128 GB machines, one bandwidth-rich and one bandwidth-poor, which isolate the
effect of $R$ at fixed $C$.

### Two machines

DGX Spark carries 128 GB of LPDDR5x unified memory at 273 GB/s. An Apple M5 Max
with a 40-core GPU reaches 614 GB/s and is configurable to 128 GB of unified
memory. At equal capacity their memory powers are

| Hardware | $C$ | $R$ | $D = CR$ |
| --- | ---: | ---: | ---: |
| DGX Spark | 128 GB | 273 GB/s | 34,944 $\mathrm{GB}^2/\mathrm{s}$ |
| Apple M5 Max 128GB | 128 GB | 614 GB/s | 78,592 $\mathrm{GB}^2/\mathrm{s}$ |

### Models

Three MoE models, modeled from their published cards as adapter parameters, not
re-measured here:

- **Qwen3.6-35B-A3B**: 35B total / 3B active, $E = 256$ routed experts, $k = 8$
  routed (plus one shared) per token; weights quantized NVFP4.
- **Gemma 4 26B-A4B-it**: 26B total / 4B active, $E = 128$, top-8 routing;
  hybrid local/global attention; weights NVFP4.
- **DeepSeek V4 Flash (DS4)**: 284B total / 13B active, $E = 256$ routed plus one
  shared, $k = 6$ per token, million-token context via compressed/sparse
  attention; weights at a Q2-style mixed quantization.

### Assumptions

All rows use the local frontier defaults: reserved context
$L_{\mathrm{alloc}} = 100{,}000$, active context $L_{\mathrm{read}} = 32{,}000$,
per-session floor $r_\star = 20$ tok/s/session, ordinary decoding $\rho = 1$,
runtime overhead $O = 8$ GB, and the memory roofline only. The numbers are
memory-side upper bounds from the simplified adapters; read them as ceilings for
comparing hardware.

### Main table

| Hardware | Model | Single-session | $b^\star$ | KV-aware aggregate | Dennard ceiling |
| --- | --- | ---: | ---: | ---: | ---: |
| DGX Spark | Qwen3.6-35B-A3B | $\le$ 149 tok/s | 17 | $\le$ 345 tok/s | $\le$ 18.2k tok/s |
| DGX Spark | Gemma 4 26B-A4B-it | $\le$ 120 tok/s | 16 | $\le$ 333 tok/s | $\le$ 23.7k tok/s |
| DGX Spark | DeepSeek V4 Flash (Q2) | $\le$ 83 tok/s | 7 | $\le$ 154 tok/s | $\le$ 13.1k tok/s |
| Apple M5 Max 128GB | Qwen3.6-35B-A3B | $\le$ 336 tok/s | 50 | $\le$ 1,006 tok/s | $\le$ 41.0k tok/s |
| Apple M5 Max 128GB | Gemma 4 26B-A4B-it | $\le$ 271 tok/s | 66 | $\le$ 1,326 tok/s | $\le$ 53.3k tok/s |
| Apple M5 Max 128GB | DeepSeek V4 Flash (Q2) | $\le$ 188 tok/s | 22 | $\le$ 446 tok/s | $\le$ 29.5k tok/s |

Two things stand out. First, with capacity held equal, the higher M5 Max
bandwidth lifts every memory-side ceiling roughly in proportion to $R$, once the
adapter and the floor are applied — the bandwidth-rich machine wins exactly where
the theory says it should, in batched throughput. Second, the Dennard column sits
one to two orders of magnitude above the KV-aware column. That gap is private
context traffic and expert diversity eating the memory system's theoretical
optimism, which is the lesson the whole derivation exists to make visible.

### Forcing the concurrency

What if concurrency is fixed by policy rather than chosen at the floor-satisfying
optimum? On DGX Spark, pushing past $b^\star$ buys aggregate throughput at the
cost of per-session rate:

| Model | Batch $b$ | Aggregate ceiling | Per-session ceiling |
| --- | ---: | ---: | ---: |
| Qwen3.6-35B-A3B | 32 | $\le$ 394 tok/s | $\le$ 12.3 tok/s/session |
| Qwen3.6-35B-A3B | 64 | $\le$ 478 tok/s | $\le$ 7.5 tok/s/session |
| Gemma 4 26B-A4B-it | 32 | $\le$ 430 tok/s | $\le$ 13.4 tok/s/session |
| Gemma 4 26B-A4B-it | 64 | $\le$ 575 tok/s | $\le$ 9.0 tok/s/session |

This is the serving tradeoff in numbers. For DGX Spark under these assumptions,
32 and 64 sessions are too high if the goal is around 20 tok/s/session — exactly
the regime the usable-batch correction is built to reject, and the reason
$b^\star$ for these models settles near 16.

### An empirical sanity check

A reported DGX Spark run served Gemma at concurrency 16 at roughly 16 to 18
tok/s/session, an aggregate of $16 \times 16 = 256$ to $16 \times 18 = 288$
tok/s. The KV-aware aggregate ceiling for Gemma at this batch is $\le 333$ tok/s,
so observed throughput is

```math
\frac{256}{333} \approx 77\% \quad\text{to}\quad \frac{288}{333} \approx 86\%
```

of the simplified ceiling. That is close enough to suggest the implementation is
near the memory-side roofline. It does *not* prove the quantization is optimal:
the bound omits compute, scheduler behavior, kernel details, and exact cache
traffic, and proving optimality would require profiler evidence of bandwidth
saturation with no compute, scheduler, or CPU stalls. A bound this close simply
means there is little memory headroom left to capture.

## What the bound leaves out

The memory roofline is one wall of a larger room. Real throughput is the minimum
over several rooflines,

```math
T_{\max} \le \min\big(T_{\mathrm{memory}},\ T_{\mathrm{compute}},\ T_{\mathrm{kernel}},\ T_{\mathrm{scheduler}},\ T_{\mathrm{interconnect}}\big),
```

and the memory term we computed can be undercut by compute throughput and
tensor-core utilization, dequantization kernels, attention kernels and KV layout,
prefill/decode phase mixing, scheduler overhead and request churn, CPU and PCIe
involvement, multi-GPU communication, allocator fragmentation, thermal and power
limits, tokenization and sampling, speculative rejection rates, and prefix-cache
hit rates. Each belongs as its own limit term. The memory model remains useful
because it makes the *first unavoidable* ceiling explicit and cheap to compute,
and because for memory-bound decode it is usually the binding one.

A recurring caution lives in the recurrent/linear-state row of any catalog. A
model with tiny fixed state and tiny private read traffic produces an enormous
memory-side aggregate at high concurrency, because almost nothing in the
denominator grows with the batch. That is precisely the signal that compute,
kernel, scheduler, and recurrent-state details must be added before the aggregate
number is treated as realistic. The memory bound describes the best case the
hardware allows; reaching it is the implementation's job.

## Compact template

For any hardware row and model adapter, the operational core is four boxed
relations. Fit:

```math
b_{\mathrm{mem}}(L_{\mathrm{alloc}}) = \left\lfloor \frac{C - W_{\mathrm{resident}} - O}{K_{\mathrm{alloc}}(L_{\mathrm{alloc}})} \right\rfloor .
```

Per-token traffic:

```math
q(b, L_{\mathrm{read}}) = \frac{W_{\mathrm{batch}}(b)}{b\,\rho} + K_{\mathrm{read}}(L_{\mathrm{read}}) .
```

Usable batch set, gated by the per-session floor:

```math
\mathcal{B} = \left\{ b : 1 \le b \le b_{\mathrm{mem}},\ \frac{R}{b\, q(b, L_{\mathrm{read}})} \ge r_\star \right\} .
```

KV-aware bound, with the Dennard ceiling for orientation:

```math
T_{\max} \le \max_{b \in \mathcal{B}} \frac{R}{q(b, L_{\mathrm{read}})} \;\le\; \rho\,\frac{D}{K_{\mathrm{alloc}}(L_{\mathrm{alloc}})\,W_{\mathrm{active}}}\left(1 - \frac{W_{\mathrm{resident}} + O}{C}\right), \qquad D = CR .
```

When reporting a result, always state the assumptions that move it:
$L_{\mathrm{alloc}}$, $L_{\mathrm{read}}$, $\rho$, $r_\star$, the weight
precision, and the KV-cache precision or attention adapter. Without them, a
single tok/s number is not reproducible.
