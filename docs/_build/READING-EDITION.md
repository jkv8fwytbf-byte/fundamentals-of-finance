# Reading editions

Build all five editions from this worktree:

```sh
./docs/_build/build.sh reading
```

Final PDFs are written to `output/pdf/`; original PDFs under `docs/` are preserved. The existing no-argument and `all` targets still build the standard documents. Build one reading edition with `reading build NAME` followed by its Markdown inputs in the existing order.

## Editing the reading guidance

- `::: {.reading-only .read-first}` adds reading guidance. The other labels are `.key-idea`, `.watch-out`, and `.optional`. Close with `:::`.
- `::: {.reading-emphasis .key-idea}` styles existing takeaway or checkpoint text without adding or removing it.
- `[short phrase]{.reading-highlight}` highlights selected original words. Keep each phrase short enough to fit on a line; the highlight is an unbroken color box.
- Stable `r1-` through `r5-` heading identifiers are linked from `_build/reading-maps/`.
- `_build/reading.lua` removes guidance and unwraps emphasis for standard builds. `_build/reading.tex` defines the shared reading style. Existing path and ligature fixes remain in place.
- PDF 1 uses the complete original SVG diagrams, exported as zoomable vector PDFs by `_build/render-reading-diagrams.cjs`. This uses Node.js, Playwright (local or the bundled runtime), and installed Chrome in a fresh headless session. It never opens the user's browser profile. The old square PNG exports are preserved.

The reading edition preserves the original prose and its historical figures and references. It adds reading guidance, not fact updates. Update sources explicitly if a future task changes the underlying material.
