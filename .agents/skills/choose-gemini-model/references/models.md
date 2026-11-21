# Gemini model guide

Checked 2026-11-21. The task assignments below are workflow defaults. Google publishes model capabilities and availability separately. [Antigravity model selection](https://antigravity.google/docs/models), [Google DeepMind model cards](https://deepmind.google/models/model-cards/).

| Model | Start here | Reconsider when |
| --- | --- | --- |
| **Gemini 4 Hydrogen** | Small edits, well-defined unit tests, quick source lookup, doc fixes | The change spans several modules or its acceptance criteria need interpretation. [Model card](https://deepmind.google/models/model-cards/gemini-4-hydrogen/) |
| **Gemini 4 Neon** | Day-to-day multi-step coding, refactors, or extracting facts from approved documents with page references | You need a separate design review or a deeper investigation that compares multiple hypotheses. [Model card](https://deepmind.google/models/model-cards/gemini-4-neon/) |
| **Gemini 4 Argon** | Planning or review across components, reviewing a migration plan, tracing a decision across several sources | The investigation repeatedly returns plausible explanations without a way to separate them. [Model card](https://deepmind.google/models/model-cards/gemini-4-argon/) |
| **Gemini 4 Carbon** | Long, ambiguous investigations such as a hard-to-reproduce race or a multi-repo migration plan | You have isolated the cause and can hand off a narrow patch with a focused test. [Model card](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| **Gemini 3.8 Flash** | Scoped work when Gemini 4 is unavailable in your Antigravity session | The task needs sustained planning or review. Break it into smaller steps with explicit evidence. [Antigravity availability](https://antigravity.google/docs/models) |
| **Nano Banana 2.1** | Illustration generation, image editing, covers and sketchnotes | The output needs exact text or paths. Inspect the rendered image against the source. [Model card](https://deepmind.google/models/model-cards/nano-banana-2-1/) |

## Use the model you can verify

- In Antigravity CLI, run `agy models` to see identifiers for your account, and use `/model` to switch in a session. The desktop picker shows what is available in that project. Antigravity documents its built-in image tool separately. Choose a surface that lists Nano Banana 2.1 if you need that specific version. [Antigravity model selection](https://antigravity.google/docs/models)
- You can start a CLI session with a listed ID, for example `agy --model gemini-4-neon-medium`. For the other Gemini 4 models, look for `gemini-4-hydrogen-medium`, `gemini-4-argon-medium` and `gemini-4-carbon-medium` in your account's list.
- On eligible plans, Antigravity Orchestrator can pair a planner such as Neon with Hydrogen for execution. Check the available pair in the model picker. The published options vary by plan. [Orchestrator](https://antigravity.google/docs/models#orchestrator)
- To compare models on your work, use the same starting commit, prompt, tools and acceptance criteria. Record tests passed, review corrections, elapsed time, retries and your own interventions. Keep pricing and quota observations tied to the surface and date of the run.
