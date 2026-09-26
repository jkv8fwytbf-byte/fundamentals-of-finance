# Model comparison lab

A readable Python project for learning APIs, model evaluation and tool calling.
Python 3.10 or newer. The core project uses only the standard library; no package
installation, GPU, API key or network is needed for the demo and tests.

## Start with the offline demonstration

Open a terminal in this `project` folder:

```sh
python3 compare.py demo
python3 -m unittest discover -s tests -v
```

Open `runs/demo/report.html` in your browser. A pre-generated copy is supplied at
`sample/report.html`. All three demo identities and their answers, times and token
counts are fictional fixtures. They teach report inspection and do not measure
any real model. The calculator expressions in the demo are genuinely evaluated
by the local arithmetic function; its surrounding model interaction is simulated.

The sample contains 60 baseline attempts (20 tasks × 3 fixtures) and 15 additional
calculator attempts (5 arithmetic tasks × 3 fixtures). Summary answers await your
review. Every pass/failure can be inspected in the saved JSON and HTML.

## Run one real task

1. Obtain your own OpenRouter API key from your account. Keep it out of code,
   worksheets, shared reports and screenshots.
2. In your terminal, set `OPENROUTER_API_KEY`. On a Mac's default zsh you can enter
   it without displaying it or placing its value in shell history:

```sh
read -s 'OPENROUTER_API_KEY?OpenRouter API key: '
export OPENROUTER_API_KEY
```

3. Discover currently available free models:

```sh
python3 compare.py models --free --tools
```

4. Replace `MODEL_ID` with an ID from the list:

```sh
python3 compare.py run --models MODEL_ID --limit 1 --output runs/first-live
```

This sends the selected synthetic task to OpenRouter and its provider. It does
not send your résumé, curriculum notes or other local documents. Free access may
still require an account and is subject to rate limits and current availability.
Catalogue access alone does not establish that an authenticated model call works.

For a first standalone request you can also inspect and run:

```sh
python3 examples/first_request.py MODEL_ID
```

That example saves `runs/first-response.json` and prints the returned response.
After your session, `unset OPENROUTER_API_KEY` removes it from that terminal.

## Choose three models and run the baseline

Read the model cards, prices and task suitability first. Record your reasons in
`../worksheets/model-selection.md`. Then use three distinct IDs:

```sh
python3 compare.py run --models MODEL_A MODEL_B MODEL_C --output runs/baseline
```

Or let the runner choose the first three compatible, zero-price model IDs in
alphabetical order. This is a convenience rule, not a quality recommendation:

```sh
python3 compare.py run --free-auto --limit 1 --output runs/free-smoke
```

To retain your own choice, put the IDs in `config.json`'s `models` array. You can
then omit `--models`. Every run records a dated catalogue snapshot, requested and
returned IDs where available, settings, provider information, task definitions
and a task-content hash. Job order is shuffled with a fixed seed of 17.
Temperature zero is not a guarantee of identical answers on repeated runs.

## Review summaries

1. In your report, filter Task type to Summaries and expand an answer.
2. Compare it with the passage and required points. Grade faithfulness (0–2),
   coverage (0–2), and brevity (0–1). Write one evidence-based note.
3. Click **Download review scores** before closing the page. Reviews are not
   automatically stored by the report page.
4. Apply the downloaded file (replace its path as needed):

```sh
python3 compare.py review runs/baseline/results.json /path/to/scores.json --output runs/reviewed
```

The original results remain unchanged. You can instead edit the supplied
`review-template.json` and pass that file. Completely blank rows are skipped;
partially filled rows are rejected. All three integer scores and a note are
required for a completed review. Failed requests remain failures.

## Add the calculator

Choose models whose catalogue lists tool support. This command runs both
conditions on the five arithmetic tasks:

```sh
python3 compare.py run --models MODEL_A MODEL_B MODEL_C --category arithmetic --calculator --output runs/calculator
```

For all 20 tasks plus the five calculator pairs:

```sh
python3 compare.py run --models MODEL_A MODEL_B MODEL_C --calculator --output runs/full
```

The program exposes only decimal arithmetic with `+ - * /` and parentheses.
It parses expressions with an allowlisted syntax tree, never `eval()`.
Expressions, magnitudes and tool turns are bounded. Tools are available to the
model, not forced, so inspect the action trace and the “actually called tool”
column. A tool request is not evidence that its calculation was useful.

## Costs and limits

Default live runs require current catalogue prices of zero for prompt,
completion and per-request charges. Requests include zero price caps and require
support for the requested parameters. There is no automatic paid fallback and
no automatic retry after an error.

Paid models require an explicit positive `--budget-usd` value. Example syntax:

```sh
python3 compare.py run --models PAID_MODEL_ID --limit 1 --budget-usd 1 --output runs/paid-small
```

Before a paid request, the runner reserves a conservative upper estimate using
the model's entire advertised context at the selected prompt-price cap, the
output-token cap, and any per-request charge. Provider routing is constrained to
those price caps. Actual reported usage is accumulated between calls. This can
reject a request that would in practice have been cheaper. Missing billing data
or an uncertain failure stops further paid calls. Set an account/API-key spending
limit as well: the client cannot guarantee provider billing, additional account
charges, or charges for a request interrupted before its response is saved.

The kit never estimates a missing reported charge as zero. A report displays
unavailable or incomplete cost when usage data is absent. Multi-turn usage is
summed across every returned call, not just the final response. Catalogues and
provider support can change. A model unavailable under your price/capability
constraints fails visibly.

## What each file teaches

| File | Purpose |
| --- | --- |
| `compare.py` | Commands, experiment selection, job order and saving results |
| `lab.py` | HTTP requests, bounded calculator, tool loop and grading |
| `report.py` | Transparent tables, per-task answers, review controls and calculator pairs |
| `data/tasks.json` | Twenty original synthetic tasks and prewritten grading rules |
| `config.json` | Model IDs and generation settings |
| `examples/first_request.py` | One inspectable API request |
| `examples/hf_demo.py` | Optional CPU sentiment-classification exercise |
| `tests/test_lab.py` | Checks for graders, failures, tool behaviour and reporting |

## Optional Hugging Face exercise

This is separate from the dependency-free comparison project. In a virtual
environment, install the packages and run the example:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install torch transformers
python3 examples/hf_demo.py
```

The first run downloads model files, which can occupy hundreds of MB; it runs
on CPU. Record your installed versions with `python3 -m pip freeze` and retain
the model revision printed by the script. This optional download/inference step
was not performed while assembling the kit.

## Reproduction and error cases

- Keep a different output folder for each live experiment; reuse would overwrite
  that folder's saved report/results.
- Missing key: set the environment variable; use `demo` until ready.
- Unavailable ID: refresh the catalogue and inspect the new model card.
- 429: free-provider rate limit; wait and start a deliberately selected smaller run.
- Timeout or malformed response: the failed attempt remains in results. There is
  no automatic retry or resume that could silently duplicate calls.
- Unsupported parameters/provider: choose a compatible model or inspect the
  documented settings. The runner does not silently drop requested parameters.
- Empty/truncated output: recorded as unsuccessful, even when text was returned.
- Missing price: the runner refuses to guess whether the model is free.
- Ctrl-C: completed results are saved, and a report is produced where possible.
  An in-flight request may still be charged by the service.

## How to interpret the output

Passage questions use normalized exact answers. This rewards factual and format
compliance; an equivalent unlisted paraphrase can fail. Extraction requires exact
JSON fields, values and types. Arithmetic requires a number-only answer within
0.000001. These rules are visible in advance. Summaries require human review.

Baseline and calculator conditions are kept distinct. Summary quality is not
collapsed into a misleading universal ranking with exact-match scores. Failed
requests count as unsuccessful; unreviewed summaries stay pending. The report
limits candidate recommendations to this run's automatic tasks and flags pending
summary reviews. It does not compute statistical significance from 20 tasks.

## Sources for the API implementation

Documentation checked on 16 September 2026:
- [OpenRouter API reference](https://openrouter.ai/docs/api_reference/overview)
- [Client tool calling](https://openrouter.ai/docs/guides/features/tool-calling)
- [Provider price constraints](https://openrouter.ai/docs/guides/routing/provider-selection)
- [Usage accounting](https://openrouter.ai/docs/cookbook/administration/usage-accounting)
- [Hugging Face pipeline tutorial](https://huggingface.co/docs/transformers/en/pipeline_tutorial)

No API credentials are bundled. Live inference remains to be verified with your
own account. The offline tests use controlled responses, not real model services.
