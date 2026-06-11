# Options for maintaining OpenClaw local model configurations


tl;dr I propose instead of a binary `localModelLean` toggle, we should either: 

- add to ClawHub an ability for Hugging Face model publishers to set a "model profile" that best matches the model's capabilities (HF is already the de facto "registrar" for open models). Then once we have our own benchmarks, we can do things like automatic prompt optimization for each model, and automatic profile generation, all on Clawhub.
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

## Complexity

My mental model of the complexity of our main goal is like this: trying to make Linux work with all the hardware, but squared, maybe even cubed.

Because we are trying to handle complexities on 3 fronts:

- Model providers -> companies/people putting all sorts of models on Hugging Face.
- Consumer hardware/GPUs -> Nvidia, Apple, CUDA, MLX.
- Features and functionality demanded by users on OpenClaw side, e.g. all the different tools, tasks, contexts the agent can run in.

## Model profiles as a possible solution

Each model can define a "profile"

Should we then run benchmarks, ShellBench or ClawBench, on each model, and curate the optimum profile?

Peter had previously disagreed with such an idea. But my counter point would be that we already did so much work making the harness work with Claude, and then GPT. Making local models can be equally complicated, so wouldn't we benefit from having more configurability to optimize OpenClaw for each model?


To begin with, we will have benchmarks that define the set of tasks a personal agent should be able to accomplish. That gives us a constraint to optimize against.

Second, there are already and will be a ton of models coming out, that people can use in OpenClaw.

Hugging Face is the de facto registrar/single source of truth for model ownership and status, similar to how GitHub is for open source software.

There will be some system that automatically runs aforementioned benchmarks against each model automatically.

I don't know if this will be done on agent side: OpenClaw foundation running OpenClaw benchmarks, for major models on Hugging Face.

Or some third party or Hugging Face side: Hugging Face runs benchmarks for each relevant personal agent.

Or both.

Each personal agent framework, say OpenClaw, will need a registry of model configurations, specifically how it runs best on OpenClaw.

On this registry, model publishers will want to publish the right configuration for their model on OpenClaw, as informed by the automatically run benchmark I've mentioned above.

My feeling is, since OpenClaw will control its configuration interface, it will also be the one hosting this registry, most likely under ClawHub.

## How This Would Look Tangibly

ClawHub would recognize Hugging Face users and organizations by their permanent ID.

You would be able to sign into ClawHub, e.g. as Google, and submit a proposed configuration for e.g. how Gemma 4 12B should run. Maybe even per each quantization/GGUF file.

Then, when a user specifies in their OpenClaw config that they want to run Gemma 4 12B, that would automatically download the configuration Google optimized for that model, and run in the best way possible.

Alternatives to this could be a manifest format OpenClaw defines, and model publishers include in the model repo.

But the bottom line is, OpenClaw should provide benchmarks to run, those benchmarks should be run automatically, and coming up with the right configuration and publishing it should be possible in an easy, AI-assisted way.

In the meanwhile, I would be interested who from the team might be a good candidate to get feedback about this. Someone who worked with standardization, manifest formats, and such.

## An alternative that I don't like

Introducing like "model strength tiers". Like `tiny`, `small`, `medium`, `large`. Meaning no binary toggle, but a multi-step toggle.

But this still conflicts things like tool profiles.
