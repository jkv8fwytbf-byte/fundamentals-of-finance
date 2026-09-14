#!/usr/bin/env bash
# Idempotent Cloud Agent setup for the valuation docs (PDF) build pipeline.
#
# The repository's only build step is docs/_build/build.sh, which turns the
# Markdown sources under docs/ into PDFs with `pandoc --pdf-engine=tectonic`.
# This script installs that toolchain: pandoc, the tectonic LaTeX engine, the
# fonts the build expects, and the helpers used to inspect the output.
set -euo pipefail

TECTONIC_VERSION="0.15.0"
FONT_DIR="/usr/local/share/fonts/macos-substitutes"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

log() { printf '\n=== %s ===\n' "$*"; }

log "Installing system packages (pandoc, fonts, fontconfig, tooling)"
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
  ca-certificates curl \
  pandoc \
  fontconfig fonts-texgyre fonts-dejavu-core \
  python3-fonttools \
  poppler-utils

log "Installing tectonic ${TECTONIC_VERSION}"
if command -v tectonic >/dev/null 2>&1 && tectonic --version 2>/dev/null | grep -q "${TECTONIC_VERSION}"; then
  echo "tectonic ${TECTONIC_VERSION} already present"
else
  tmp="$(mktemp -d)"
  url="https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%40${TECTONIC_VERSION}/tectonic-${TECTONIC_VERSION}-x86_64-unknown-linux-musl.tar.gz"
  curl -fsSL "${url}" -o "${tmp}/tectonic.tar.gz"
  tar -xzf "${tmp}/tectonic.tar.gz" -C "${tmp}"
  sudo install -m 0755 "${tmp}/tectonic" /usr/local/bin/tectonic
  rm -rf "${tmp}"
fi
tectonic --version

log "Building macOS font substitutes (Helvetica Neue, Menlo)"
tmp_fonts="$(mktemp -d)"
python3 "${SCRIPT_DIR}/setup/make-macos-substitute-fonts.py" "${tmp_fonts}"
sudo mkdir -p "${FONT_DIR}"
sudo cp "${tmp_fonts}"/*.otf "${tmp_fonts}"/*.ttf "${FONT_DIR}/"
rm -rf "${tmp_fonts}"
sudo fc-cache -f "${FONT_DIR}" >/dev/null
echo "Installed substitute fonts:"
fc-list | grep -iE "Helvetica Neue|Menlo" | sort

log "Pre-warming the tectonic package bundle"
# First real run downloads the LaTeX package bundle; do it now so later builds
# are fast (and work even without network) and are baked into the snapshot.
warm="$(mktemp -d)"
cat > "${warm}/warm.md" <<'EOF'
# Warm-up

Body text in `Helvetica Neue`; code in `Menlo`.
EOF
( cd "${warm}" && pandoc warm.md -o warm.pdf --pdf-engine=tectonic \
    -V mainfont="Helvetica Neue" -V monofont="Menlo" >/dev/null 2>&1 ) \
  && echo "tectonic bundle warmed" || echo "WARNING: warm-up build failed (non-fatal)"
rm -rf "${warm}"

log "Environment ready. Build the docs with:"
echo "  cd ${REPO_ROOT}/docs && ./_build/build.sh all"
