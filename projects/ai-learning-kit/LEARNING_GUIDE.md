# Siddharth’s AI learning notebook

Eight weeks, 4–6 hours per week. Selected lessons and one finished project.

Start by opening START.html. The notebook saves progress and notes in your browser and can export a backup. This Markdown copy works without JavaScript.

## First session

Watch Karpathy’s one-hour introduction. Inspect the GLM listing. Explain how your application, OpenRouter, an inference provider and a model fit together. Open project/sample/report.html to see the output you will learn to produce.

The supplied results are fictional offline fixtures. Live inference remains a learner exercise with your own credentials.

## Week 1: Make the map

A model is one component inside an application. During training its numerical weights are adjusted; during inference it uses those weights to process your input. A token is a model-specific chunk of text, not necessarily a word. The context window limits the material processed in a request; it is not the same as durable memory.

**Produce:** A one-page explanation of a prompt’s journey, with six definitions and one diagram.

### Read / watch

- [Karpathy · Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g): A one-hour overview. Pause to explain tokens, weights, training and inference in your own words.
- [3Blue1Brown · Transformers, visually](https://www.3blue1brown.com/lessons/gpt/): Connect vectors, embeddings and next-token generation to a picture of the computation.

### Orient yourself — 75 minutes

- [ ] Watch the one-hour Karpathy introduction, pausing when you encounter an unfamiliar word.
- [ ] Write definitions for model, token, weights, training, inference and context. Give a concrete example for each.

### Follow the computation — 75 minutes

- [ ] Read the 3Blue1Brown transformer explanation. Sketch text → tokens → vectors → model computation → next-token probabilities → generated text.
- [ ] Explain embeddings as numerical representations. Distinguish stored model weights from the temporary representations computed for one input.

### Explain it back — 120 minutes

- [ ] Complete worksheets/week-01.md without copying the glossary. Draw where an app, OpenRouter and a provider would sit.
- [ ] Open the sample comparison report. Find one failure and explain why a fluent response can still fail a task.
- [ ] Take the checkpoint, then revise one unclear definition.

### Checkpoint

**Does changing the prompt normally retrain the model?**

No. A prompt changes the input used for inference; it does not normally update weights.

**Can the same model be used in different apps?**

Yes. Apps can connect to the same model through different integrations. Their prompts and tools can still produce different behaviour.

**Is a context window the same as permanent memory?**

No. It bounds the current input/output context. An app may store and retrieve information separately.

**Make one change:** Change the example prompt in your explanation and trace what stays the same.

## Week 2: Make one model request

An API is a defined way for programs to exchange requests and responses. The model creator, API router and inference provider can be different organisations. JSON is a text format for structured data; the API key authenticates the request. A model identifier selects a model rather than naming a library.

**Produce:** One saved response plus a labelled request/response explanation; or a pending live milestone if no account is available.

### Read / watch

- [OpenRouter · Quickstart](https://openrouter.ai/docs/quickstart): Follow one request from your program to a model and back. The kit uses plain HTTP so the pieces stay visible.
- [Z.ai GLM 5.3 Flash · Model listing](https://openrouter.ai/z-ai/glm-5.3-flash): Separate the model name from provider, context length and pricing. This is a discovery exercise; it is not selected for paid runs.
- [Hugging Face · Hub overview](https://huggingface.co/docs/hub/en/index): Find models, datasets and Spaces. The hub is one part of a larger ecosystem of tools.
- [Pi · Coding agent](https://pi.dev/): Read how a coding agent combines model access with tools and a configurable workflow.

### Inspect a model listing — 60 minutes

- [ ] Open the GLM listing. Record the identifier, supported inputs, context length, provider names and dated prices.
- [ ] Find the units in a price label: input and output often have different prices per million tokens. Use the worksheet’s hypothetical numbers to calculate one request.

### Inspect the interface — 90 minutes

- [ ] Read the OpenRouter quickstart and examples/first_request.py. Identify URL, authorisation header, model field, messages and response choices.
- [ ] Run the offline demo using the project guide. Follow a saved answer into results.json and report.html.

### Make a small live request — 120 minutes

- [ ] Use your own key in an environment variable. List current compatible free models and select one. Run one task, following the README.
- [ ] If account access is not ready, trace the request example and sample data; mark the live-call milestone pending.
- [ ] Record any returned provider and usage fields. Explain why unavailable cost must not be recorded as zero.

### Checkpoint

**What does served via OpenRouter mean?**

Your program uses OpenRouter’s API to reach a provider operating the selected model.

**Does a model page on Hugging Face mean the model is running on your computer?**

No. A model repository supplies files and documentation; inference requires a separate runtime or hosted service.

**What is an API key for?**

It authenticates API access. It is not a model identifier and should not be included in shared code or notes.

**Make one change:** Change the prompt yourself, predict the response shape, and inspect the saved result.

## Week 3: Navigate Hugging Face

The Hub stores model and dataset repositories. Transformers is a software library for working with models. A Space is a hosted application or demonstration. A model card documents the intended use and limitations. Downloadable weights do not by themselves establish unrestricted licensing or complete training transparency.

**Produce:** Three model-card reviews and a short observation log from a pretrained-model experiment.

### Read / watch

- [Hugging Face · LLM Course](https://huggingface.co/learn/llm-course/chapter1/1): Start with selected parts of chapters 1–2. Python and introductory deep learning help; full-course completion is a later goal.
- [Hugging Face · Model cards](https://huggingface.co/docs/hub/en/model-cards): Inspect intended use, limitations, licence and evaluation information before using a model.
- [Hugging Face · Spaces overview](https://huggingface.co/docs/hub/en/spaces-overview): A Space hosts an application or demonstration. Try one and identify what it does and does not demonstrate.
- [DistilBERT · Sentiment model card](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english): The optional CPU example uses this sentiment classifier. A high classification score is not proof of general understanding.

### Read selected foundations — 90 minutes

- [ ] Study the introduction and pipeline/tokenizer/model sections of LLM Course chapters 1–2. Do not attempt to complete every fine-tuning exercise this week.
- [ ] Make a table distinguishing Hub, Transformers, Datasets and Spaces.

### Read three model cards — 75 minutes

- [ ] Use the model-card worksheet for three different models. Include the supplied sentiment classifier.
- [ ] Record task, inputs/outputs, licence, limitations, evaluation data and what the card does not disclose. Label absent facts unknown.

### Run and question a small model — 105 minutes

- [ ] Follow examples/hf_demo.py and its setup instructions. This downloads a pretrained sentiment model and runs it on CPU; no GPU is required.
- [ ] Compare a clearly positive sentence, a negative sentence and a sarcastic sentence. Predict before running.
- [ ] Explain tokenization, inference and the output labels; do not interpret the score as a calibrated probability of truth.

### Checkpoint

**How is a model card different from a leaderboard?**

A card documents one model’s context and limits; a leaderboard compares systems using chosen tests. Both need scrutiny.

**What does a tokenizer do?**

It converts input text into the tokens/IDs expected by a particular model.

**Does access to weights imply any licence terms you want?**

No. Read the specific licence and restrictions.

**Make one change:** Add one sentence that you expect to confuse the sentiment model and explain the outcome.

## Week 4: Read a leaderboard carefully

A benchmark is a task collection with an evaluation procedure. Its score depends on those tasks, prompts, tools and scoring choices. Human preference, arithmetic accuracy, cost and speed measure different things. Latency can include network and queueing delays; tokens per second measures a different part of delivery.

**Produce:** A dated three-model selection sheet and a written definition of success.

### Read / watch

- [Artificial Analysis](https://artificialanalysis.ai/): Read methodology alongside scores. Compare capabilities, response speed and cost for your intended tasks.
- [ARC Prize · Leaderboard](https://arcprize.org/leaderboard): Inspect example tasks, benchmark version and evaluation conditions. A leaderboard score alone cannot establish general intelligence.
- [Arena · How it works](https://arena.ai/how-it-works): Compare human preference with task-based evaluation. Preference and factual correctness can diverge.

### Inspect three evaluation styles — 75 minutes

- [ ] Read Artificial Analysis’s index methodology through its site. Record what the index includes and its version.
- [ ] Inspect ARC example tasks and the relevant benchmark version. Try three tasks yourself. Read how Arena collects comparisons.

### Choose candidates — 75 minutes

- [ ] Complete the candidate worksheet for three models. Record why each might suit your tasks, plus dated availability and price information.
- [ ] Use project discovery to identify runnable IDs. Keep the same IDs for the paired experiment. A comparison need not include the currently highest-ranked model.

### Define the decision — 120 minutes

- [ ] Write the use case: answering short passage questions, extracting fields, arithmetic and summaries. State which errors matter.
- [ ] Inspect data/tasks.json. Before running models, explain the success rule for each category and identify an ambiguous task you would rewrite.

### Checkpoint

**Can a higher overall index score guarantee better results for your app?**

No. The task distribution and setup can differ; evaluate the intended use case.

**Why record model version and provider?**

Both affect interpretation and reproducibility. An alias can change and providers can serve different configurations.

**Can preference and factual accuracy disagree?**

Yes. A polished answer can be preferred even when some facts are wrong.

**Make one change:** Replace one task with a task you care about and specify its answer/rubric before viewing model output.

## Week 5: Create an evaluation you can inspect

Write the grader before seeing the answer. Exact output rules are useful for extraction and arithmetic, while summaries need judgement. A missing value means unknown; zero is a measured value. A failed request is a reliability failure and must remain visible. This small set is a learning sample, not a statistically strong leaderboard.

**Produce:** A saved comparison report with manual summary reviews and a limitations paragraph.

### Read / watch

- [Anthropic · Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): Start with task, trial, grader and outcome. Define success before looking at answers.

### Understand the task set — 60 minutes

- [ ] Read the opening evaluation concepts in the Anthropic article. Identify task, attempt, grader and recorded outcome.
- [ ] Read all 20 supplied tasks and inspect their prewritten grading rules. Check the exact-answer format and summary rubric.

### Run the comparison — 90 minutes

- [ ] Run the offline demo first. For live work, start with one task, then run the baseline task set for three chosen models.
- [ ] Inspect failed tasks before aggregates. Keep task content and model settings fixed for the comparison.

### Grade and explain — 120 minutes

- [ ] Use the report’s summary controls to assign faithfulness, coverage and brevity scores, each with a written note. Export and apply the reviews.
- [ ] Write a result paragraph that states the sample size, what worked, one failure and what further evidence you need.
- [ ] Make no broad model recommendation from fixture data.

### Checkpoint

**Why keep human summary review separate from exact-match scores?**

They measure different dimensions using different grading methods. Showing coverage and rubric scores prevents a misleading single number.

**If the service omits cost, is that a free request?**

No. The charge is unknown until verified; the tool displays it as unavailable.

**What should happen to a timeout in the report?**

It remains a failed attempt. It should not quietly disappear from the denominator or look like a valid answer.

**Make one change:** Add one format-failure case to the tests, then explain why the grader should accept or reject it.

## Week 6: Add a calculator and inspect the loop

In tool calling, the model requests an action. Your program validates the request, runs the function and sends the result back. The model then generates another response. That surrounding code is part of the agent harness. The calculator experiment tests one narrow intervention; it does not demonstrate general autonomy.

**Produce:** A paired arithmetic report and one annotated calculator trace.

### Read / watch

- [Anthropic · Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Distinguish a predefined workflow from a model choosing its next action; understand the surrounding tools and code.
- [Hugging Face · Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction): Read Unit 1 fundamentals; trace the model → tool request → tool execution → observation cycle.

### Draw the tool loop — 60 minutes

- [ ] Read Building effective agents and Agents Course Unit 1 fundamentals.
- [ ] Draw user task → model tool request → validation → calculator → tool result → model answer. Mark which steps are ordinary code.

### Run the paired experiment — 90 minutes

- [ ] Run the five arithmetic tasks with --calculator for the same selected models. This records baseline and calculator-available conditions.
- [ ] Inspect the trace: the model is allowed to use a tool, but may choose not to. Compare only matched tasks.

### Test limits and explain a failure — 120 minutes

- [ ] Inspect calculate() and its tests. Try division by zero and an unsupported expression. Explain why no arbitrary Python is executed.
- [ ] Inspect multi-turn usage: each follow-up request can add tokens and time.
- [ ] Write whether the tool changed accuracy, tool usage and elapsed time in your small sample.

### Checkpoint

**Does the language model itself execute the Python calculator?**

No. The application executes the validated tool request and returns an observation.

**Does tool availability prove tool use?**

No. Read the trace to see whether a tool was actually called.

**Why cap the number of tool turns?**

To bound loops, time and requests, and make a failure visible.

**Make one change:** Change one arithmetic prompt and predict whether a calculator call will help before running it.

## Week 7: Read a research claim critically

Alignment asks how to make systems act in accordance with intended objectives and constraints. Interpretability studies internal computations. An observed association differs from an intervention that changes an outcome. A research article’s experiment, interpretation and wider speculation should be kept distinct.

**Produce:** Two one-page research notes distinguishing observation, inference and uncertainty.

### Read / watch

- [BlueDot · AI alignment curriculum](https://bluedot.org/courses/alignment): Start with alignment and interpretability units. Public curriculum is available; organised participation may have separate requirements.
- [MIRI · The Problem](https://intelligence.org/the-problem/): Read as MIRI’s position on advanced-AI risk. Separate premises, evidence, predictions and proposed policy.
- [Anthropic · A global workspace in language models](https://www.anthropic.com/research/global-workspace): Study experimental interventions and limits. The article does not establish subjective experience in AI.

### Build the vocabulary — 60 minutes

- [ ] Read the introductory alignment and mechanistic-interpretability units in BlueDot’s public curriculum.
- [ ] Write definitions for alignment, evaluation, interpretability, correlation and intervention.

### Compare two kinds of writing — 90 minutes

- [ ] Read MIRI’s The Problem and list its premises, predictions and proposed actions. Attribute claims to MIRI.
- [ ] Read the Anthropic global-workspace article. Identify one intervention, an observed result and a limitation.

### Write a research note — 120 minutes

- [ ] Complete one research-note worksheet for each article. Include what was tested, evidence, assumptions, alternative explanations and what remains uncertain.
- [ ] Explain why an experiment about functional information access does not establish subjective experience.
- [ ] Prepare two questions you would ask the authors.

### Checkpoint

**What is stronger evidence of a causal role: association or a controlled intervention?**

A well-controlled intervention provides stronger evidence, though its scope and alternative explanations still matter.

**Does the global-workspace article establish feelings in a model?**

No. Its claims about functional organisation do not establish subjective experience.

**How should you present MIRI’s predictions?**

As attributed predictions/arguments with stated premises and uncertainty, not as a settled measurement.

**Make one change:** Rewrite a dramatic headline into a precise sentence that fits the study’s evidence.

## Week 8: Finish, reproduce and explain

A finished learning project has a clear input, a working output, reproducible instructions and known limitations. The most useful demonstration shows one successful case, one failure and the reasoning behind a design choice. You can use coding assistance while still checking behaviour and understanding the pieces.

**Produce:** A runnable project, a report, a concise README and a five-minute explanation.

### Read / watch

- [Full Stack Deep Learning · LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/): Application-building perspective. Recorded in 2023; use current documentation for APIs and packages.

### Make it reproducible — 75 minutes

- [ ] Follow the README from a fresh project copy. Run tests and the offline demo.
- [ ] Record your Python version, task hash, model identifiers and settings for any real report.

### Explain the result — 75 minutes

- [ ] Write your recommendation for the tasks you tested, with sample size and unresolved limitations.
- [ ] If only fixture data is available, state that the project is demonstrated offline and live model evaluation remains pending.
- [ ] Package your chosen report and instructions; add Docker only if it helps the recipient run it.

### Demonstrate and reflect — 120 minutes

- [ ] Use the five-minute demonstration script in the worksheet. Show a request, a saved result, a failure and a calculator trace.
- [ ] Explain one design decision without reading generated code verbatim.
- [ ] Choose one deeper branch: model internals, statistical learning, application engineering or finance.

### Checkpoint

**Can another person reproduce your sample without your API key?**

Yes. The offline sample and tests use no credentials. Live work uses the other person’s own key.

**What do you claim if all results are fixtures?**

That the software and workflow are demonstrated, not that any real model has been measured.

**What should your final recommendation be limited to?**

The tested tasks, settings and evaluation conditions, with the sample’s uncertainty made clear.

**Make one change:** Choose one feature to simplify or remove and explain how that makes the project easier to understand.

## Glossary

**Model** — A trained system that maps inputs to outputs using learned numerical parameters. The part of a RAG application that generates a response.

**Weights / parameters** — Numbers learned during training that determine much of the model’s computation. Changing a chat prompt normally does not change these numbers.

**Training** — Adjusting parameters using data and an objective. A training run updates weights; a normal API request runs inference.

**Pretraining** — An initial training stage that learns broad patterns from a large dataset. For language models, predicting text is a common training objective.

**Post-training** — Additional training that adapts behaviour, for example instruction following. This can change how a pretrained model responds as an assistant.

**Inference** — Using a trained model to compute an output for an input. Sending a prompt to a hosted model invokes inference.

**Token** — A unit produced by a tokenizer, often a word fragment or punctuation. One word can occupy multiple tokens, with differences across languages and tokenizers.

**Tokenizer** — The component converting content to the token IDs a model expects. Use a tokenizer compatible with the selected model.

**Context window** — The token capacity available for a request’s context and generation, under model/provider limits. Chat history, retrieved text and tool messages consume context.

**Embedding** — A learned numerical representation used to encode information about an item. RAG can compare text embeddings to retrieve related passages.

**Transformer** — A neural-network architecture that uses attention to combine information across positions. Many modern language models use transformer-based architectures.

**Attention** — A mechanism for combining information from different positions according to learned relationships. A token representation can incorporate relevant earlier context.

**API** — A specified interface through which software requests services or exchanges data. Your Python program sends a request and receives a structured response.

**Endpoint** — The address for a particular API operation. The chat-completions endpoint accepts a model and messages.

**Provider** — An organisation or service operating model inference. Several providers may offer access to the same model.

**Router** — A service or component that directs requests to model/provider endpoints. OpenRouter exposes a common interface for accessing supported models.

**Model ID** — The identifier used to select a model in an API. z-ai/glm-5.3-flash is a listed identifier; availability can change.

**Open weights** — Model parameters are available under specified licence terms. Read the licence; downloadable weights alone do not establish full openness.

**Model card** — Documentation describing a model’s purpose, development, evaluations and limitations where provided. Treat a missing disclosure as unknown.

**Framework** — Software providing reusable abstractions for building applications. LangChain helps organise application components; it is not itself a language model.

**RAG** — Retrieval-augmented generation: retrieve relevant information and provide it to generation. A retrieved passage can support an answer, but retrieval alone does not ensure correctness.

**Fine-tuning** — Further training a pretrained model for a dataset or objective. It updates weights; adding a retrieved passage to a prompt normally does not.

**Tool calling** — A model requests a structured action that application code can execute. The model requests calculate; Python computes and returns the result.

**Agent** — A system where a model can choose actions and continue based on observations toward a task. A calculator loop is a small example; different tools create different capabilities.

**Harness** — The surrounding code, tools, context management and execution rules that run an agent. Turn limits and tool validation belong to the harness.

**Workflow** — An arrangement of processing steps, often with predefined control flow. A fixed retrieve → summarize → save pipeline is a workflow.

**Evaluation / eval** — A defined test and a method for judging the result. A task, an attempted response and a grading rule form a simple eval.

**Benchmark** — A task collection and procedure intended to compare systems. Know the task distribution and conditions before interpreting a score.

**Latency** — The delay measured between specified events. This lab measures elapsed time for the whole task, not tokens per second.

**Throughput** — The rate at which work or output is delivered. Output tokens per second differs from time until the first token.

**Temperature** — A sampling setting that affects how tokens are selected. Lower temperature does not guarantee correctness or perfect repeatability.

**Hallucination** — Generated content that is false or unsupported in the relevant context. A plausible invented fact can still fail a passage-grounded task.

**Alignment** — The problem of making system behaviour accord with intended goals and constraints. A specification can be incomplete or learned behaviour can differ from the intent.

**Interpretability** — Methods for investigating how internal computations relate to behaviour. Changing an internal representation and observing an effect is one experimental approach.

## Complete resource shelf

- **Start here / Video: [Karpathy · Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)** — A one-hour overview. Pause to explain tokens, weights, training and inference in your own words.
- **Week 1 / Visual article: [3Blue1Brown · Transformers, visually](https://www.3blue1brown.com/lessons/gpt/)** — Connect vectors, embeddings and next-token generation to a picture of the computation.
- **Go deeper / Visual article: [3Blue1Brown · Attention, step by step](https://www.3blue1brown.com/lessons/attention/)** — Follow how one token representation uses information from other tokens.
- **Week 2 / Documentation: [OpenRouter · Quickstart](https://openrouter.ai/docs/quickstart)** — Follow one request from your program to a model and back. The kit uses plain HTTP so the pieces stay visible.
- **Week 2 / Model page: [Z.ai GLM 5.3 Flash · Model listing](https://openrouter.ai/z-ai/glm-5.3-flash)** — Separate the model name from provider, context length and pricing. This is a discovery exercise; it is not selected for paid runs.
- **Week 2 / Documentation: [Hugging Face · Hub overview](https://huggingface.co/docs/hub/en/index)** — Find models, datasets and Spaces. The hub is one part of a larger ecosystem of tools.
- **Week 2 / Tool overview: [Pi · Coding agent](https://pi.dev/)** — Read how a coding agent combines model access with tools and a configurable workflow.
- **Week 3 / Documentation: [Hugging Face · Model cards](https://huggingface.co/docs/hub/en/model-cards)** — Inspect intended use, limitations, licence and evaluation information before using a model.
- **Week 3 / Course: [Hugging Face · LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)** — Start with selected parts of chapters 1–2. Python and introductory deep learning help; full-course completion is a later goal.
- **Week 3 / Documentation: [Hugging Face · Spaces overview](https://huggingface.co/docs/hub/en/spaces-overview)** — A Space hosts an application or demonstration. Try one and identify what it does and does not demonstrate.
- **Week 3 / Model page: [DistilBERT · Sentiment model card](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)** — The optional CPU example uses this sentiment classifier. A high classification score is not proof of general understanding.
- **Week 4 / Evaluation site: [Artificial Analysis](https://artificialanalysis.ai/)** — Read methodology alongside scores. Compare capabilities, response speed and cost for your intended tasks.
- **Week 4 / Evaluation site: [ARC Prize · Leaderboard](https://arcprize.org/leaderboard)** — Inspect example tasks, benchmark version and evaluation conditions. A leaderboard score alone cannot establish general intelligence.
- **Week 4 / Evaluation site: [Arena · How it works](https://arena.ai/how-it-works)** — Compare human preference with task-based evaluation. Preference and factual correctness can diverge.
- **Week 5 / Article: [Anthropic · Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)** — Start with task, trial, grader and outcome. Define success before looking at answers.
- **Week 6 / Article: [Anthropic · Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)** — Distinguish a predefined workflow from a model choosing its next action; understand the surrounding tools and code.
- **Week 6 / Course: [Hugging Face · Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)** — Read Unit 1 fundamentals; trace the model → tool request → tool execution → observation cycle.
- **Week 7 / Course: [BlueDot · AI alignment curriculum](https://bluedot.org/courses/alignment)** — Start with alignment and interpretability units. Public curriculum is available; organised participation may have separate requirements.
- **Week 7 / Argument: [MIRI · The Problem](https://intelligence.org/the-problem/)** — Read as MIRI’s position on advanced-AI risk. Separate premises, evidence, predictions and proposed policy.
- **Week 7 / Research article: [Anthropic · A global workspace in language models](https://www.anthropic.com/research/global-workspace)** — Study experimental interventions and limits. The article does not establish subjective experience in AI.
- **Go deeper / Video: [Karpathy · Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI)** — A longer conceptual treatment after the introductory talk.
- **Go deeper / Course: [Karpathy · Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)** — Build neural-network components in code when you want deeper implementation knowledge.
- **Go deeper / Course: [Full Stack Deep Learning · LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/)** — Application-building perspective. Recorded in 2023; use current documentation for APIs and packages.
- **Go deeper / Report: [Stanford · AI Index](https://hai.stanford.edu/ai-index)** — Research, adoption, investment and societal trends. This is different from Artificial Analysis’s model-performance index.
- **Go deeper / Book: [ISLP · Book and downloads](https://www.statlearning.com/)** — Statistical learning with Python. Begin with chapters on statistical learning, regression, classification and resampling.
- **Go deeper / Course: [ISLP · Companion courses](https://www.statlearning.com/online-courses)** — Pair selected chapters with Python exercises; the authors link the companion courses here.
- **Go deeper / Book: [Russell & Norvig · Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/)** — Broad AI: agents, search, planning, uncertainty and learning. Start with Introduction and Intelligent Agents.
- **Finance later / Course: [Yale · Financial Markets](https://oyc.yale.edu/economics/econ-252)** — Archived Robert Shiller lectures. Start with risk, diversification and financial institutions; historical examples need context.
- **Finance later / Article: [Investopedia · Buffett’s hedge-fund bet](https://www.investopedia.com/articles/investing/030916/buffetts-bet-hedge-funds-year-eight-brka-brkb.asp)** — Study benchmark selection, costs and active versus passive management. One historical comparison is not a universal theorem.
- **Finance later / Video: [Veritasium · The Equation That Beat Wall Street](https://www.youtube.com/watch?v=A5w-dEgIU1M)** — An introduction to the history around Black–Scholes/Merton and quantitative finance.
- **Finance later / Book: [Hull · Options, Futures, and Other Derivatives](https://www.pearson.com/en-gb/subject-catalog/p/options-futures-and-other-derivatives-global-edition/P200000004519/9781292410654)** — Start with contracts and payoff diagrams, then pricing. Commercial textbook; purchase is optional and not needed for this AI kit.

## Finance afterward

Follow Yale Financial Markets, the Buffett article, the Veritasium video and then Hull. Start with risk, fees, diversification and contracts. Use hypothetical exercises before interpreting historical performance.

## Working defaults

4–6 hours weekly. Core materials are publicly accessible; no paid certificate is required. Current model prices and availability must be checked before live work. The initial eight-week cycle does not imply mastery of every linked course or textbook.

Resources checked while preparing the kit on 16 September 2026.
