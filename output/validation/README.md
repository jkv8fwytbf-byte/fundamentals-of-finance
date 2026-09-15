# Reading edition validation

- Original checkout remains on `dev`. The `dev` and `main` commit references, Git index, status, and all 73 recorded original files are unchanged.
- All 49 Markdown source comparisons passed after removing reading-only guidance and unwrapping visual emphasis through the standard build filter.
- Five original PDFs are preserved byte for byte in `docs/`.
- All five reading editions build successfully. All 33 reading-map links resolve, and all internal link destinations were checked.
- All 262 final pages were rendered and visually reviewed; selected dense content was inspected at larger size. No clipped or overlapping text was observed. The single sub-point build warning is recorded in the JSON report.
- Complete SVG diagrams were rendered as vector PDFs for PDF 1. The old square PNG exports and original SVG files were preserved.
- Nothing was staged, committed, merged, pushed, or submitted as a pull request.

`original-checkout-baseline.json` records the original branch references, status, index hash and file hashes. `verification.json` records checks and SHA-256 hashes of the five delivered PDFs.

Note added 2026-09-15: the SHA-256 hashes in `verification.json` are from the Codex build of that morning. All ten PDFs were rebuilt later the same day after the folder moved to `~/Desktop/Valuation` and the paths inside the documents were updated, so the current PDF hashes differ. The checks described above were not rerun.
