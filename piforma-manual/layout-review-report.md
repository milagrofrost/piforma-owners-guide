# Layout review — Macintosh PiForma Owner's Guide

Completed October 15, 2026. Layout only: all eight manuscript files remain byte-for-byte unchanged. All 346 manuscript text units, including captions, instructions, technical explanations and jokes, are present in the final PDF. No source image was rewritten. The page count changed from 59 to 51 through presentation and spacing.

## Deliverables

- [Layout-reviewed trim PDF](output/macintosh-piforma-layout-reviewed.pdf)
- [Current working PDF](output/macintosh-piforma-working-proof.pdf) and [Chapter 1 proof](output/chapter-1-working-proof.pdf)
- [Baseline and final page-by-page audit](layout-audit.md)
- [Before-and-after comparisons](output/layout-review/before-and-after.pdf)
- [Complete facing-page preview](output/layout-review/facing-pages.pdf)
- [Image-resolution report](image-resolution-report.md)
- [Print-readiness checklist](print-readiness-checklist.md)
- [Reusable style specification](layout-style-guide.md)
- [Rendered reusable-style verification sheet](output/layout-review/style-specimen.pdf), including the side-note, Important and Warning treatments that are not inserted into publication copy.
- Editable source: [book styles](styles/book.typ), [figure presentation](assets/illustration-layout.json), [converter](scripts/build-manuscript.py), [full book](main.typ).

## Corrections

The contents now occupies two deliberately divided pages. Blank cover/chapter versos carry no running furniture. The rear diagram and caption use the correct mirrored plate anchor, increasing verso binding clearance. All main text remains on the established asymmetrical rail grid; the text column was not replaced with a contemporary symmetric design.

Numbered instructions and bullets have hanging continuation lines. Section heads and glossary terms keep their following paragraphs. Captions use uncondensed 8 pt text, a fixed image gap and consistent plate alignment. Technical inventory rows have a reusable label/value layout. The body keeps its restrained serif treatment, ragged edge and whole paragraphs, with a slightly tighter 6 pt leading setting and no automatic hyphenation.

Chapter 1 now pairs the two bag photographs, groups the matching side controls, holds the Forbidden Latch introduction with its top view, and keeps the complete opening procedure, close-up and joke together. The stand diagram faces the complete setup instructions and shares a page with the keyboard explanation/drawing. Mouse views use matched heights and stay with their explanations. The front and rear drawings stay beside their respective control descriptions.

The final side-control plate uses the same 288 pt source width for both views. A centered Typst viewport omits only measured empty top/bottom canvas. Threshold measurements and visual inspection confirm that the computer outlines and original callouts remain complete. Image aspect ratios and original PNG files are unchanged. This allowed larger labels than the initial grouped test without returning to two mostly empty pages.

## Render-and-review record

| Pass | Pages | Complete review and next correction |
|---|---:|---|
| 1 | 59 | Compiled and rendered all pages; opened all ten contact sheets and representative spreads. Audited every page. Found contents spill, rear-plate binding intrusion, blank-page furniture and separated Chapter 1 figures. |
| 2 | 51 | Opened all nine contact sheets, side-control spread and actual-size side/specification pages. Binding check clear. Contents looked too compressed; the stand step and drawing still separated at a turn. |
| 3 | 51 | Opened all nine contact sheets and generated all spread previews. Contents rhythm improved with a deliberate break. Stand/keyboard needed further balancing; rear illustration benefited from keeping both explanatory paragraphs with it. |
| 4 | 51 | Opened all nine contact sheets. Balanced stand/keyboard page and rear paragraph group. The experimental side-view viewport clipped an edge and was rejected; raw image bounds also exposed the need for clip-aware measurements. |
| 5 | 51 | Replaced the rejected viewport with symmetric empty-canvas masking. Opened all nine contact sheets, enlarged/actual-size side plate and representative packing/control/setup spreads. Full objects and callouts visible; no binding, trim, overlap or compilation issues. |

Each pass has its compiled PDF, per-page metrics, 72 ppi actual-size images, full spread PDF and image-resolution evidence under `output/layout-review/pass-N/`. All pages were also rendered at 144 ppi under `output/manuscript-iteration-layout-pass-N/`. The supplied Macintosh Plus and SE reference instruction pages were used for the rail, rule, restrained caption and facing-page conventions, without pixel-difference scoring of aged scans.

## Digital verification

- Exact page size and trim: 432 × 522 pt, or 6 × 7.25 inches.
- Every font embedded; no compiler warnings, text overlaps or overflow.
- No measured essential text or visible image intrusion into the nominal 36 pt binding-safe area; full-width plates retain at least 40 pt inside clearance.
- Four chapters open on physical right-hand pages; blank physical PDF pages 2, 26, 42 and 48 are deliberate and have no furniture.
- All 15 images accounted for; lowest effective source resolution is 251 ppi, with no artificial upsampling.
- All 346 manuscript text units present, zero missing; all eight source hashes unchanged. Existing 22 editorial preservation checks still pass.
- Saved trim PDF retains vector text/rules, source-resolution images and the original working-proof designation. No imposed/Letter carrier edition was created without printer specifications.

## Remaining compromises

Times New Roman condensed to the established proportions remains an approximation of the references' type, not the original Apple typeface. Some labels are raster artwork with small native lettering; digital actual-size and enlarged views were inspected, but paper/press legibility requires a physical proof. The lowest-resolution outline is 251 ppi; vector originals would improve its finest strokes. The supplied illustration leaders retain their source red, while editable rules and type use one warm red; press color matching requires the printer's profile/proof.

Generous chapter openings, whole paragraphs, short chapter/glossary endings and recto starts intentionally leave white space. The stand is a compact diagram so the keyboard can remain wide enough to read. No text was cut to fill or shorten a page. Printer punch depth, stock, cover handling and color profile remain unspecified; the checklist distinguishes those decisions from completed digital checks. Existing editorial/device questions remain in their separate tracker.
