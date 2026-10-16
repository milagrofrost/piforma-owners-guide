# Current battery-display correction

Owner-confirmed battery reading: **84%**. The battery display can indicate charging from the wireless receiver, but is hidden while packed in the bag. This supersedes earlier wording below. Current 63-page PDF recompiled and affected pages visually reviewed; all 22 editorial checks and 372 source-text checks pass. Copy baseline: `output/battery-display-correction/manuscript-lock.json`.

# Current interior-photo integration — October 15, 2026

The [63-page reviewed guide](output/macintosh-piforma-layout-reviewed.pdf) now includes all three supplied labeled interior photos in Chapter 2. Source images and labels remain unchanged. Captions distinguish the 94% stored-charge reading from wireless charging verification. Updated capture checklist records the received views. Compiled without warnings or preflight issues; new figure pages and surrounding Chapter 2 flow visually reviewed. Current copy baseline: `output/interior-photos/manuscript-lock.json`.

# Current charging clarification — October 15, 2026

The 59-page reviewed PDF now reflects the owner-confirmed uncertainty of bag wireless charging. Chapters 1/4 and Appendix B explain the optional USB supply power monitor without claiming direct battery-charge confirmation. Recompiled with no preflight issues; affected pages visually reviewed; all 22 editorial checks and all 369 source-text checks pass. Current copy baseline: `output/charging-clarification/manuscript-lock.json`.

# Current screenshot integration — October 15, 2026

Open the [59-page reviewed guide](output/macintosh-piforma-layout-reviewed.pdf). All 11 supplied screenshots are placed with their instructions, including the approved home-folder examples and Clippy's message entry. The original PNGs remain unchanged. See the [integration report](screenshot-integration-report.md), [capture checklist](photo-and-illustration-checklist.md), and [facing-page proof](output/screenshot-integration/facing-pages.pdf).

Rebuild using `scripts/build-manuscript.py --iteration next --ppi 144`, then run `scripts/review-screenshots.py --iteration next` and review the rendered pages. Use `--final` only after review to refresh the frozen layout-reviewed PDF. The new copy baseline is `output/screenshot-integration/manuscript-lock.json`; pass it to `scripts/verify-layout-copy.py --baseline`. The 51-page layout review below is historical; its PDF is preserved as `output/screenshot-integration/before-screenshots.pdf`.

# Current layout review — October 15, 2026

Open [layout-reviewed trim PDF](output/macintosh-piforma-layout-reviewed.pdf) for the current 51-page layout. The manuscript text is unchanged. [Layout review report](layout-review-report.md) links the audit, comparisons, spread previews, resolution report, styles and print checklist. The existing Letter production PDF is the archived four-page prototype, not the current book.

Rebuild with `scripts/build-manuscript.py --iteration next --ppi 144`. Figure groups, size caps and layout-only placements are in `assets/illustration-layout.json`. Run `scripts/layout-review.py --pass N` after a render to produce measured page/spread evidence; `scripts/verify-layout-copy.py` checks unchanged text against the layout baseline. The layout-reviewed PDF is a frozen proof of the reviewed build; refresh it only after reviewing a new render.

# Current editorial production revision — October 15, 2026

Open `output/macintosh-piforma-working-proof.pdf` for the complete current book, or `output/chapter-1-working-proof.pdf` for the first chapter. The full book retains four chapters, adds a first session and everyday operations, and includes Appendix B troubleshooting. These are editable manuscript proofs.

Read `editorial-production-plan.md` for the proposal recorded before revision, `working-outline.md` for current detailed contents, `editorial-production-change-report.md` for the completed review, and `editorial-production-tracker.md` for unpublished questions, missing illustrations and device checks. The older reports below describe earlier versions.

# Macintosh PiForma Owner’s Guide — working manuscript

The current `main.typ` builds the complete editable manuscript proof. Begin with `working-outline.md` and `manuscript/01-getting-started.md`. `manuscript/00-front-matter.md` contains Welcome and About This Manual. Chapters 2–4, Appendix A, glossary and credits are also drafted, with explicit verification and photograph gaps.

Canonical project specifications remain in [Macintosh-PiForma-docs](https://github.com/milagrofrost/Macintosh-PiForma-docs). The `research/` directory contains provenance, immutable read snapshots and discrepancies for this adaptation; it is not a second authoritative build manual. No live software or upstream files were changed.

From the workspace root:

```powershell
& .\.venv\Scripts\python.exe .\piforma-manual\scripts\build-manuscript.py --iteration next --ppi 240
```

This regenerates editable `chapters/*.typ` from the single-source `manuscript/*.md`, compiles `output/macintosh-piforma-working-proof.pdf` and `output/chapter-1-working-proof.pdf`, exports every full-book page as PNG, creates contact sheets and Apple comparisons, and checks geometry, embedded fonts, text bounds and span overlaps. Edit the Markdown and rerun; generated chapter edits would be overwritten. Edit `styles/book.typ` for the book's flowing layout. Direct Typst compilation works once the chapter includes have been generated.

Read `chapter-1-checklist.md`, `outstanding-questions.md`, `editorial-change-log.md`, `research/fact-register.md`, and `manuscript-review-report.md` before treating a proof as approved. A six-second active-app-only hold is confirmed by the owner; other gesture timings are not. The new book is a **working reading proof**, with missing photographs and unresolved device facts. No new full-book print-service copy is produced until factual approval, required by `PiForma_Manual_Handoff/plans/production-workflow.md`.

October 14 artwork: `output/new-artwork-proof.pdf` reviews the twelve newly supplied images at their manuscript sizes. Per-image size limits are editable in `assets/illustration-layout.json`; proportions are preserved automatically. Run `scripts/review-artwork.py --iteration next` after the matching build to verify image positions and generate the size/location review. The normal battery check uses the rear plunger and top slits; optional top opening is now documented from the owner's latch instructions.

## Archived four-page design study

Open `prototype.typ` to inspect the earlier four-page layout study. Its linked SVG illustrations are editable but are not verified drawings of the finished hardware. The original `../PiForma_Guide_v2` project and earlier prototype output PDFs are preserved.

## Build and review

From the workspace root in PowerShell:

```powershell
& .\PiForma_Guide_v2\typst.exe compile .\piforma-manual\prototype.typ .\piforma-manual\output\piforma-owners-guide.pdf
& .\.venv\Scripts\python.exe .\piforma-manual\scripts\visual-compare.py --iteration next --ppi 300
& .\.venv\Scripts\python.exe .\piforma-manual\scripts\measure-references.py
& .\.venv\Scripts\python.exe .\piforma-manual\scripts\print-production.py
```

The review script accepts `--typst PATH` for another Typst CLI. Python dependencies are `pymupdf` and `pillow`; installed versions are pinned in `scripts/requirements.txt`. A normal Python 3.12 environment also works. The provided workspace `.venv` uses the installed managed Python runtime; recreate it if relocating the project. The Windows App Execution Alias Python was unusable in this session.

Each review compiles both PDF and PNGs through the Typst CLI, captures errors/warnings, checks page count/dimensions/font embedding/text bounds, updates `output/page-previews`, and creates a numbered review folder. Open all four images after running; the script does not itself certify visual fidelity. Reference renders use the same physical scale. Overlays include scan defects and are diagnostic, not a similarity score. Final reviewed comparisons are in `output/iteration-4/`.

## Edit the system

`styles/page-layout.typ` and `styles/components.typ` belong to the older fixed-coordinate prototype. `styles/typography.typ` supplies shared color/font definitions. `prototype.typ` preserves explicit four-page breaks. The new book uses `styles/book.typ` and flow-based chapter includes, so growing paragraphs repaginate instead of colliding with later content.

Read `reference-analysis.md` for measurements, verified-versus-estimated distinctions, original TOC design, and Plus/SE choices. Read `fidelity-report.md` for iteration findings, remaining font/art limitations, and print instructions. The task's visual goal is only partially met in those explicitly documented areas.

Print the production PDF at Actual Size on Letter, long-edge duplex, and trim to 6 × 7¼ inches using the crop marks. It has six carrier pages to preserve the blank cover reverse and chapter parity; the reading PDF has exactly four pages. No bleed is required. Proof the red and confirm the binding punch positions before ordering copies.
