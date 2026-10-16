# Current review — October 15, 2026

See [editorial-production-change-report.md](editorial-production-change-report.md) for the current review and validation. Four chapters retained; first session and practical operations added; Appendix B added; production notes moved to the tracker. Build: `output/manuscript-iteration-october-15-editorial-4/`. Full book: 59 pages. 22 editorial checks passed; no compiler warnings or preflight issues. Earlier reports below are archival.

# Working manuscript review

## Current update — October 14, 2026

The current full proof is **55 pages**, Chapter 1 proof **29 pages**, and new-artwork proof **12 pages**. All twelve newly described images are integrated and sized independently, with proportional scaling, complete labels and separate captions. The current builds are `output/manuscript-iteration-october-14-artwork-1/` and `output/manuscript-iteration-october-14-artwork-2/`; the latter is the accepted review build. Compilation has no warnings/errors, text preflight is clear, all twelve image rectangles match configured sizes, and 17 editorial-preservation checks pass. Every full-book page was opened in contact sheets, with enlarged keyboard, mouse and latch pages checked for label/caption readability. See `output/new-artwork-review.md` for figure locations and physical sizes. The photo checklist and evidence register now reflect the supplied artwork and clarified battery access. Earlier results below describe the October 11 draft, not the current page count or available photographs.

## Earlier review — October 11, 2026

The current result is a complete working manuscript adaptation: front matter, four chapters, Appendix A, glossary and credits. The first requested editorial deliverables are `working-outline.md` and `manuscript/01-getting-started.md`; a separate first-chapter proof includes Contents, Welcome, About This Manual and Chapter 1. Later chapters are drafts, not silently approved hardware instructions.

## Compilation and visual review

The final full-book proof has **41 PDF pages**, all **432 × 522 pt** (estimated 6 × 7¼-inch trim). The chapter-one proof has 16 pages. Page count follows the prose, photograph reservations and chapter recto starts; no word-count/page-count matching to Apple was used.

Final build: `output/manuscript-iteration-6/compile.log` and `preflight.json`. Both proof entry points compile without warnings/errors. Font subsets are embedded. Full-book preflight reports no extracted text outside page bounds and no span-to-span overlaps. Every page was rendered by Typst at 240 dpi, inspected in seven numbered contact sheets, and representative Chapter 1 pages/Apple comparisons opened at larger scale. Automatic checks complement image inspection; they do not establish factual correctness or catch every possible typographic defect.

| Manuscript pass | Review / correction |
|---|---|
| 1 | Compiled, but relative-width scaling let paragraphs run past the page edge. Contact sheets and automated bounds checks caught clipping. Raised-initial line boxes also produced apparent overlaps, prompting actual span-level checking. |
| 2 | Fixed absolute column widths and leading; embedded-font/bounds checks passed. Reviewed all 48 pages in eight sheets. Found chapter-number/rule collision, dense contents with glossary terms, detached bullet markers and inconsistent head spacing. |
| 3 | Added hierarchy and roman front-matter folios; omitted glossary terms from contents; made bullets inline; fixed chapter label placement and narrowed large titles. Reviewed all pages in contact sheets; heading rule/title spacing still needed refinement. |
| 4 | Grouped major rule/title into a compact stack. Source/preflight passed; selected geometry reviewed. This was an intermediate geometry check, followed by the full page review in pass 5. |
| 5 | Moved editorial Verify callouts into the annotation rail with outlined red triangles instead of vertical colored bands. Corrected comparator selection to exact heading lines. Reviewed all 41 pages and enlarged chapter-opening comparison. Found literal brackets accidentally emitted around rich-text bullet content. |
| 6 | Removed literal bullet brackets and lowered introductory text to better match the measured original opener. Recompiled both proofs and all page PNGs. Final pages, captions, rail notes, bullets, contents and appendix reviewed; preflight clear. |

The initial editorial-preservation check had an overly literal expected phrase for “no fixed recovery time”; the manuscript already contained the intended caveat. The check was corrected to the actual equivalent wording and rerun. This did not require changing the owner's battery guidance.

## Reference fidelity and remaining work

The geometry retains the Plus's compact proportions, right-shifted narrow body column, large chapter white space, pale raised initial, warm-red rules, small serif folios and annotation rail. Original Plus/SE references and measured analysis remain under `references/` and `reference-analysis.md`. Final comparisons use equal points-to-pixels scaling without scan stretching.

The flowing book uses a consistent main-column x=152 pt and 242 pt width. The original sampled recto column was nearer x=164 pt; that 12 pt recto difference is explicit. The repeated gutter space suits notes and binding but is not an exact coordinate facsimile. Font remains horizontally narrowed Times New Roman rather than a verified original condensed Garamond. Chapter introductions are reader-facing prose, not an exact small-cap opener recreation; running chapter text also remains on opening folios. These details can be refined after the owner accepts the text and supplies real artwork.

No photographs of the finished hardware were supplied. All requested views have specific labeled reservations; the generic earlier SVG is excluded from the book to avoid depicting undocumented ports or shapes. The cover is therefore a working photograph placeholder. This is not a final visual-fidelity claim.

The full-manual manuscript is **not released as a print-production edition**. The handoff `plans/production-workflow.md` says, “Make a printing copy only after factual approval.” The unresolved speaker, charging, access, UI and deployment details are documented in `outstanding-questions.md`. Final physical trim, printer/binding allowance and color proof also remain to be confirmed. The previously created four-page production PDF remains only the archived prototype.

## Reproducible checks

Run `scripts/build-manuscript.py --iteration next --ppi 240` for generated editable Typst, both PDFs, every page PNG, contact sheets, references, side-by-side comparisons and preflight. Run `scripts/verify-editorial.py` for owner-sequence and troubleshooting preservation checks. Edit Markdown for prose, `styles/book.typ` for book layout. The canonical repo and software were inspected read-only, not edited or deployed.
