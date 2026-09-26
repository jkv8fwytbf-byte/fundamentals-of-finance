# Start here

Open **START.html** in your browser. It is your eight-week learning notebook,
with 24 sessions, 31 linked resources, a 34-term glossary, checkpoints and notes.
The file works locally without a web server. External lessons need internet.

Your progress and notes are saved in that browser where local storage is
available. Use **Export progress & notes** to keep a portable backup. Moving the
file or changing browsers can create a different storage location; use Import
to restore a backup. No account or API key belongs in these notes.

## What is included

- `START.html`: the interactive notebook.
- `LEARNING_GUIDE.md`: the entire curriculum and glossary as plain text.
- `worksheets/`: eight weekly worksheets and model-selection, research-note,
  and demonstration templates.
- `project/`: runnable Python comparison project with its own instructions.
- `project/sample/report.html`: an already generated offline sample report.
- `resources.json`, `curriculum.json`, `glossary.json`: editable reference data.

The HTML embeds a copy of the reference data so it can open directly from disk.
After editing the reference JSON, run `python3 build_notebook.py` from this
folder to rebuild START.html and LEARNING_GUIDE.md. Your browser notes are
stored separately and are not overwritten by rebuilding these files.

## Your first 75 minutes

1. Open Week 1, Session 1.
2. Watch Karpathy's one-hour introduction, pausing for unfamiliar terms.
3. Write six definitions in your own words: model, token, weights, training,
   inference and context.
4. Save a note describing which terms you can explain and which are unclear.

You can inspect the sample report immediately. Its model identities, responses,
timing and token metrics are fictional teaching fixtures. No live model calls
or paid services were used to produce the sample. You will run real experiments
with your own credentials during the course.

The learning schedule assumes 4–6 hours per week. It covers selected lessons;
the full textbooks and longer courses remain later branches.
