# Week 6: Add a calculator and inspect the loop

In tool calling, the model requests an action. Your program validates the request, runs the function and sends the result back. The model then generates another response. That surrounding code is part of the agent harness. The calculator experiment tests one narrow intervention; it does not demonstrate general autonomy.

## My deliverable

A paired arithmetic report and one annotated calculator trace.

## Sessions

### Draw the tool loop · 60 minutes

- [ ] Read Building effective agents and Agents Course Unit 1 fundamentals.
- [ ] Draw user task → model tool request → validation → calculator → tool result → model answer. Mark which steps are ordinary code.

### Run the paired experiment · 90 minutes

- [ ] Run the five arithmetic tasks with --calculator for the same selected models. This records baseline and calculator-available conditions.
- [ ] Inspect the trace: the model is allowed to use a tool, but may choose not to. Compare only matched tasks.

### Test limits and explain a failure · 120 minutes

- [ ] Inspect calculate() and its tests. Try division by zero and an unsupported expression. Explain why no arbitrary Python is executed.
- [ ] Inspect multi-turn usage: each follow-up request can add tokens and time.
- [ ] Write whether the tool changed accuracy, tool usage and elapsed time in your small sample.

## My notes

What I can explain now:

What still confuses me:

Evidence / output location:

One change I made myself:

## Checkpoint

1. Does the language model itself execute the Python calculator?

My answer:

2. Does tool availability prove tool use?

My answer:

3. Why cap the number of tool turns?

My answer:

## Teach it back

Explain the week’s main idea to someone who has never used these tools. Use one example.

## Extension

Change one arithmetic prompt and predict whether a calculator call will help before running it.
