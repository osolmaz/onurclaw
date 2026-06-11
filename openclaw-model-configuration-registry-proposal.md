# Options for maintaining OpenClaw local model configurations


tl;dr I propose that instead of having a binary `localModelLean` toggle, we should either: 

- add to ClawHub an ability for Hugging Face model publishers or community members to publish a "model profile" that best matches the model's capabilities (HF is already the de facto "registrar" for open models). Then once we have our own benchmarks, we can do things like automatic prompt optimization for each model, and automatic profile generation, all on Clawhub.
- or at least have a ladder like approach (tiny, small, medium, large) if we cannot afford.

---

OpenClaw currently has the `localModelLean:true/false` toggle. It is an internally disliked binary toggle which creates a "lite mode" for small models, which e.g. hide the browser and other tools to save context and not confuse the model. It was introduced quickly without grasping the complexity of making OpenClaw work for local models

My goal is to carry OpenClaw configurability beyond `localModelLean`. I believe we should not get deeper and deeper into this mistake, and should deprecate it as soon as possible. It was useful short term, but we will need more than a single toggle long term. It already overlaps with some other configs like tool profiles.

## Local-ness is misleading

Short conceptual point before I begin with the general proposal.

Most local models are small because people's hardware is generally not bigger than 128GB. But some might be running Kimi locally which is big enough to handle full OpenClaw. Or a user could be using a small model like Qwen 8B on an inference provider, which would also need a "lite" mode.

A model being local doesn't mean it has to be weak. We need to change the concepts here. We need to phrase it independently from localness.

Regardless, we should get rid of "localness" from naming. I think it's irrelevant.

## localModelLean conflicts tool profiles

We already have tool profiles: `minimal`, `coding`, `messaging`, `full`. This is conflicting with current behavior of the toggle.

## Other configuration surfaces

Some back and forth with my clanker has yielded the following categories that could have a "profile":

> - Tooling: what capabilities the model can access, and how those capabilities are exposed. (already mentioned above)
> - Context: system prompt, how much history, bootstrap text, tool output, memory, and files enter the prompt.
> - Model behavior: context window, thinking/reasoning mode, verbosity, temperature, and provider params.
> - Memory: whether memory is enabled, what it searches, and how much it returns.
> - Safety: filesystem limits, exec policy, sandboxing, and approvals.
> - Reliability: timeouts, retries, loop detection, fallbacks, and compaction.
> - Workflow scope: whether the model can do long-running, background, multi-agent, or channel-facing workflows.

These are either already configured different for different models in some way, or could be.

This is not a design doc, so I am intentionally not proposing any configuration shape for the categories above.

I personally predict that tool profiles and the system prompt will be the 2 primary things people will want to customize.

## Complexity

My mental model of the complexity of our main goal is like this: trying to make Linux work with all the hardware, but squared, maybe even cubed.

Because we are trying to handle complexities on 3 fronts:

- Model providers -> companies/people putting all sorts of models on Hugging Face.
- Consumer hardware/GPUs -> Nvidia, Apple, CUDA, MLX.
- Features and functionality demanded by users on OpenClaw side, e.g. all the different tools, tasks, contexts the agent can run in.

## Model profiles as a possible solution

Basic idea: Each model can define a "profile", hosted somewhere, editable by community members or the model publishers themselves. + Have default fallback profiles which users can choose from, when there is no profile optimized for a model.

Peter had previously rightfully disagreed with the idea of hardcoding local-model specific configurations into the core (not that I had proposed putting them into the core, that was misunderstood).

There is real work needed when trying to make a harness work well with a certain model. And it is I think obvious that every model might need a different system prompt (take the goblin thing in GPT for example).

We already did so much work making the harness work with Claude, and then GPT. Making local models can be equally complicated, so we would benefit from having more configurability to optimize OpenClaw for each model.

To begin with, we will have benchmarks that define the set of tasks a personal agent should be able to accomplish. That gives us a constraint to optimize against.

Second, there are already and will be a ton of models coming out, that people can use in OpenClaw.

Hugging Face is the de facto registrar/single source of truth for model ownership and status, similar to how GitHub is for open source software.

There will be some system that automatically runs aforementioned benchmarks against each model automatically.

I don't know if this will be done on agent side: 
- OpenClaw foundation running OpenClaw benchmarks, for major models on Hugging Face.
- Or some third party or Hugging Face side: Hugging Face runs benchmarks for each relevant personal agent.
- Or both.

OpenClaw will need a registry of model configurations, specifically how it runs best on OpenClaw.

On this registry, model publishers will want to publish the right configuration for their model on OpenClaw, as informed by the automatically run benchmark I've mentioned above.

My feeling is, since OpenClaw will control its configuration interface, it will also be the one hosting this registry, most likely under ClawHub.

## How this would tangibly look

ClawHub would recognize Hugging Face users and organizations by their permanent ID (the internal Hugging Face ID that stays the same across renames)

You would be able to sign into ClawHub, e.g. as Google, and submit a proposed configuration for e.g. how Gemma 4 12B should run. Maybe even per each quantization/GGUF file.

<details>
<summary>

Models themselves can be identified by their [HF URIs](https://huggingface.co/docs/huggingface_hub/en/package_reference/hf_uris), e.g. `hf://models/unsloth/gemma-4-12b-it-GGUF@v1.0/gemma-4-12b-it-BF16.gguf`.

It is possible to specify exactly which model you mean using a specific revision or tag, click on this to see more.
    
</summary>

```
# branch
hf://models/unsloth/gemma-4-12b-it-GGUF@main/gemma-4-12b-it-BF16.gguf

# another branch
hf://models/unsloth/gemma-4-12b-it-GGUF@dev/gemma-4-12b-it-BF16.gguf

# Git tag
hf://models/unsloth/gemma-4-12b-it-GGUF@v1.0/gemma-4-12b-it-BF16.gguf

# SemVer-ish Git tag
hf://models/unsloth/gemma-4-12b-it-GGUF@v1.0.3/gemma-4-12b-it-BF16.gguf

# release/date tag
hf://models/unsloth/gemma-4-12b-it-GGUF@2025-06-01/gemma-4-12b-it-BF16.gguf

# full commit SHA
hf://models/unsloth/gemma-4-12b-it-GGUF@4d33b01d79672f27f001f6abade33f22d993b151/gemma-4-12b-it-BF16.gguf

# PR ref
hf://models/unsloth/gemma-4-12b-it-GGUF@refs/pr/10/gemma-4-12b-it-BF16.gguf
```
</details>

Similarly, a community member might want to fill in the void when the model publisher is not willing to do that, and publish 3rd party profiles.

Then, when a user specifies in their OpenClaw config that they want to run Gemma 4 12B, that would automatically download the configuration Google optimized for that model, and run in the best way possible. (Or if nonexistent, user might choose from popular community provided ones)

(Alternatives to this could be a manifest format OpenClaw defines, and model publishers include in the model repo. But I think it's a long shot to expect that from model publishers.)

Bottom line: OpenClaw should provide benchmarks to run, those benchmarks should be run automatically, and coming up with the right configuration and publishing it should be possible in an easy, AI-assisted way.


## An alternative that I don't like

Introducing like "model strength tiers". Like `tiny`, `small`, `medium`, `large`. Meaning no binary toggle, but a multi-step toggle.

But this still conflicts things like tool profiles.
