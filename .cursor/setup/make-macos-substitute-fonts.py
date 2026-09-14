#!/usr/bin/env python3
"""Build metric-compatible substitutes for the macOS fonts the docs build expects.

docs/_build/build.sh hardcodes "Helvetica Neue" (body) and "Menlo" (mono), which
ship only on macOS and cannot be redistributed on Linux. XeTeX/fontspec (used by
tectonic) resolves fonts by the family name embedded in the font file, so aliasing
via fontconfig alone is not enough. This script clones freely-licensed, metric-
compatible fonts and rewrites their embedded family name so the build finds them:

    Helvetica Neue  <- TeX Gyre Heros   (Helvetica clone, GUST Font License)
    Menlo           <- DejaVu Sans Mono (Bitstream Vera / public domain)

The clones are only a build-time substitute for a private documentation pipeline;
no product is shipped under the macOS family names.
"""
import os
import sys

from fontTools.ttLib import TTFont

# (source file, destination file, family, style)
FACES = [
    ("{tg}/texgyreheros-regular.otf", "HelveticaNeue-Regular.otf", "Helvetica Neue", "Regular"),
    ("{tg}/texgyreheros-bold.otf", "HelveticaNeue-Bold.otf", "Helvetica Neue", "Bold"),
    ("{tg}/texgyreheros-italic.otf", "HelveticaNeue-Italic.otf", "Helvetica Neue", "Italic"),
    ("{tg}/texgyreheros-bolditalic.otf", "HelveticaNeue-BoldItalic.otf", "Helvetica Neue", "Bold Italic"),
    ("{dj}/DejaVuSansMono.ttf", "Menlo-Regular.ttf", "Menlo", "Regular"),
    ("{dj}/DejaVuSansMono-Bold.ttf", "Menlo-Bold.ttf", "Menlo", "Bold"),
    ("{dj}/DejaVuSansMono-Oblique.ttf", "Menlo-Italic.ttf", "Menlo", "Italic"),
    ("{dj}/DejaVuSansMono-BoldOblique.ttf", "Menlo-BoldItalic.ttf", "Menlo", "Bold Italic"),
]

TG_DIR = os.environ.get("TEXGYRE_DIR", "/usr/share/texmf/fonts/opentype/public/tex-gyre")
DJ_DIR = os.environ.get("DEJAVU_DIR", "/usr/share/fonts/truetype/dejavu")


def rename_face(src, dest, family, style):
    ps_name = "{}-{}".format(family.replace(" ", ""), style.replace(" ", ""))
    full_name = family if style == "Regular" else "{} {}".format(family, style)

    font = TTFont(src)
    name = font["name"]

    def set_name(name_id, value):
        name.setName(value, name_id, 3, 1, 0x409)  # Windows / Unicode BMP / en-US
        name.setName(value, name_id, 1, 0, 0)  # Macintosh / Roman / English

    set_name(1, family)  # Font Family
    set_name(2, style)  # Font Subfamily
    set_name(4, full_name)  # Full name
    set_name(6, ps_name)  # PostScript name
    # Drop typographic family/subfamily so the four faces collapse into one family.
    for name_id in (16, 17):
        name.removeNames(nameID=name_id)

    font.save(dest)
    print("wrote {} (family='{}', style='{}')".format(dest, family, style))


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out_dir, exist_ok=True)

    missing = []
    for src_tmpl, dest_name, family, style in FACES:
        src = src_tmpl.format(tg=TG_DIR, dj=DJ_DIR)
        if not os.path.exists(src):
            missing.append(src)
            continue
        rename_face(src, os.path.join(out_dir, dest_name), family, style)

    if missing:
        sys.stderr.write("ERROR: missing source fonts:\n  " + "\n  ".join(missing) + "\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
