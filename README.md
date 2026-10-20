# Macintosh PiForma Owner's Guide

Editable manuscript and Typst production source for the Macintosh PiForma Owner's Guide. Start with the [current 78-page reviewed proof](piforma-manual/output/macintosh-piforma-layout-reviewed.pdf) and [continuation handoff](CONTINUING.md).

The manual retains four chapters, technical information, symptom-based troubleshooting, a glossary and the owner's personality. It follows the original Macintosh Plus and SE guides as instructional and visual references. PiForma is a privately built computer in an Apple IIc Monitor shell, not an Apple product.

## What to edit

- [Manuscript](piforma-manual/manuscript/): the single source for prose. Edit these Markdown files, then rebuild. Generated `chapters/*.typ` will be overwritten.
- [Styles](piforma-manual/styles/), [main document](piforma-manual/main.typ), and [illustration sizes](piforma-manual/assets/illustration-layout.json): editable Typst layout and image sizing.
- [Original owner handoff](PiForma_Manual_Handoff/CODEX_START_HERE.md): read it and all referenced handoff files before revising instructions or voice.
- [Photo checklist](piforma-manual/photo-and-illustration-checklist.md) and [editorial tracker](piforma-manual/editorial-production-tracker.md): remaining work, outside publication copy.
- [Fact register](piforma-manual/research/fact-register.md): source evidence and owner corrections. Canonical hardware/software documentation remains [Macintosh-PiForma-docs](https://github.com/milagrofrost/Macintosh-PiForma-docs).

## Build

Use Python 3.12+ and Typst **0.15.1**. Install the fonts named in `piforma-manual/styles/typography.typ` (currently EB Garamond). Fonts and executables are not bundled; font substitution can alter pagination. Dependencies are pinned in `requirements.txt`.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r piforma-manual/scripts/requirements.txt
.\.venv\Scripts\python.exe piforma-manual/scripts/build-manuscript.py --iteration next --ppi 144
.\.venv\Scripts\python.exe piforma-manual/scripts/verify-editorial.py
.\.venv\Scripts\python.exe piforma-manual/scripts/verify-layout-copy.py
```

On macOS/Linux, use `.venv/bin/python` instead. Typst must be on PATH, or pass `--typst /path/to/typst` (also accepts `TYPST_BIN`). For a quick compile of the included generated chapters:

```text
typst compile piforma-manual/main.typ piforma-manual/output/macintosh-piforma-working-proof.pdf
```

The full build regenerates chapters, working and Chapter 1 PDFs, page PNGs, contact sheets, reference comparisons and preflight results. Render outputs and environments are ignored by Git. Review changed pages and facing-page flow before replacing the tracked reviewed PDF. `verification/manuscript-lock.json` locks the current handoff text: intentional prose changes require a newly recorded baseline after review; never update hashes just to hide missing text.

## Included and excluded

Includes original illustration PNGs, screenshot originals/presentation crops, Apple reference PDFs, owner instructions, source snapshots, editorial/layout reports, the original template archive, and one current proof. Reports describe dated iterations; current handoff corrections in `CONTINUING.md` take precedence over older observations.

Excludes virtual environments, caches, bundled binaries, temporary image/contact-sheet exports, duplicate working PDFs and the obsolete four-page print prototype. The reviewed guide remains a working editorial proof; it has not received a physical print test or complete device verification.

Apple reference manuals and third-party source snapshots retain their respective ownership. They are reference material, not original PiForma operating instructions. No new blanket license is asserted for this collection.
