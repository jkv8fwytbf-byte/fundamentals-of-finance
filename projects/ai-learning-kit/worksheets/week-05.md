# Week 5: Create an evaluation you can inspect

Write the grader before seeing the answer. Exact output rules are useful for extraction and arithmetic, while summaries need judgement. A missing value means unknown; zero is a measured value. A failed request is a reliability failure and must remain visible. This small set is a learning sample, not a statistically strong leaderboard.

## My deliverable

A saved comparison report with manual summary reviews and a limitations paragraph.

## Sessions

### Understand the task set · 60 minutes

- [ ] Read the opening evaluation concepts in the Anthropic article. Identify task, attempt, grader and recorded outcome.
- [ ] Read all 20 supplied tasks and inspect their prewritten grading rules. Check the exact-answer format and summary rubric.

### Run the comparison · 90 minutes

- [ ] Run the offline demo first. For live work, start with one task, then run the baseline task set for three chosen models.
- [ ] Inspect failed tasks before aggregates. Keep task content and model settings fixed for the comparison.

### Grade and explain · 120 minutes

- [ ] Use the report’s summary controls to assign faithfulness, coverage and brevity scores, each with a written note. Export and apply the reviews.
- [ ] Write a result paragraph that states the sample size, what worked, one failure and what further evidence you need.
- [ ] Make no broad model recommendation from fixture data.

## My notes

What I can explain now:

What still confuses me:

Evidence / output location:

One change I made myself:

## Checkpoint

1. Why keep human summary review separate from exact-match scores?

My answer:

2. If the service omits cost, is that a free request?

My answer:

3. What should happen to a timeout in the report?

My answer:

## Teach it back

Explain the week’s main idea to someone who has never used these tools. Use one example.

## Extension

Add one format-failure case to the tests, then explain why the grader should accept or reject it.
