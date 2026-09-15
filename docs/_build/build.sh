#!/bin/bash
# Build PDFs for the M0 documents with pandoc + tectonic.
# Usage:
#   ./build.sh              # build all five PDFs (numbered as on disk)
#   ./build.sh all          # same
#   ./build.sh build NAME md1.md md2.md ...
set -e
cd "$(dirname "$0")/.."
build() { # $1 = output name, $2.. = input md files in order
  out="$1"; shift
  pandoc "$@" -o "$out.pdf" --pdf-engine=tectonic --toc --toc-depth=2 -N --columns=50 \
    -V mainfont="Helvetica Neue" -V monofont="Menlo" -V geometry:margin=2.2cm -V fontsize=11pt \
    -V mainfontoptions="Ligatures=NoCommon" -V monofontoptions="Ligatures=NoCommon" \
    -V linkcolor=NavyBlue -V urlcolor=NavyBlue -V colorlinks=true --resource-path=.:diagrams --lua-filter=_build/breaklong.lua -H _build/header.tex \
    --metadata date="2026-09-14" 2> "_build/$out.err" && echo "built $out.pdf ($(du -h "$out.pdf" | cut -f1))" || { echo "FAILED $out"; tail -20 "_build/$out.err"; }
}

build_all() {
  build 1-read-this-first \
    read-this-first.md
  build 2-damodaran-essentials \
    damodaran-essentials/00-preface.md \
    damodaran-essentials/c[1-7]-*.md
  build 3-the-other-side \
    other-side/00-preface.md \
    other-side/00-read-me-first.md \
    other-side/0[1-6]-*.md
  build 4-the-guide \
    guide/00-preface.md \
    guide/00-how-to-learn-with-an-ai-tool.md \
    guide/0[1-9]-*.md \
    guide/1[0-7]-*.md
  build 5-the-plan-explained \
    plan-explained/00-preface.md \
    plan-explained/0[1-9]-*.md \
    plan-explained/1[0-2]-*.md
}

if [ $# -eq 0 ] || [ "$1" = "all" ]; then
  build_all
else
  "$@"
fi
