# The documents

Open `0-START-HERE.txt` first. It gives the reading order for the six PDFs and says where the project stands today.

The markdown files (plain text with simple marks for headings and links) in this folder are the source. The PDFs are built copies. Edit the markdown, then rebuild; never edit a PDF.

To rebuild PDFs 1 to 5, run `docs/_build/build.sh` for the plain PDFs (into `docs/`) or `docs/_build/build.sh reading` for the reading editions (into `output/pdf/`). Both need the pandoc and tectonic programs; the reading build also needs node, Playwright and Chrome. How the reading markup works is in `_build/READING-EDITION.md`.

`build.sh` does not cover PDF 6 (`6-where-we-are.pdf`). It is rebuilt by hand from `docs/`: take the pandoc line from the `build()` function in `_build/build.sh`, set the input to `6-where-we-are.md` and the output to `6-where-we-are.pdf`, and change the date to 2026-09-26 (the recipe is in `CLAUDE.md`). Running `build.sh` itself would stamp the wrong date.

`plan.md` is the full plan (v4, 2026-09-14). `plan-explained/` restates it in shorter sentences. When they differ, `plan.md` wins.

`sources/` contains the nine research reports the documents cite. They are frozen inputs, not documents to edit.

`decisions/` is the decisions log: one short note per decision, written by you. See `decisions/README.md`.

Humans read the PDFs. Claude reads the markdown. The full map of documents, sources and PDFs is in `CLAUDE.md` at the root.
