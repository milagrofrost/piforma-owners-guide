> Historical study: the owner approved this direction on October 17, 2026. It is now applied to the full guide. This folder preserves the review-stage artifacts; its source lock describes the older manuscript. See ../approved-redesign-report.md for implementation.

# Six-page art-direction study

Prepared October 16, 2026. **Proposal only. The production manuscript, production styles, illustration-layout manifest and main document are unchanged.**

Open these in order:

1. [Six proposed trim pages](design-study.pdf) — exactly 6 × 7.25 inches; print at **100% / actual size**.
2. [Current beside proposed](current-versus-proposed.pdf) — six comparison boards; each current/proposed page remains 432 × 522 pt inside a wider sheet.
3. [Current / proposed / Apple reference](current-proposed-reference.pdf) — six three-way boards, with the specific reference PDF page named above each scan.
4. [Facing-page study](facing-page-study.pdf) — actual 12 × 7.25 inch spreads, including intentional blank mates at the beginning/end.
5. [Font trials](type-tests.pdf) and [design rationale](design-rationale.md).

The design study uses complete selected paragraphs/instructions, not the entire contents of each current page. It is an art-direction sample, not a six-page abridgment or a proposed new pagination of the whole guide. [Current source context](current-source-context.pdf) preserves the surrounding current pages in this order: physical PDF pages 7, 8, 13, 19, 20, 23, 24, 39, 40, 55. All page citations here and in the boards are **physical PDF page numbers**, not printed folios.

## Rebuild only the study

Run from the workspace root with Python/PyMuPDF/Pillow already installed and Typst 0.15.1 available. The proposal additionally requires the locally installed **EB Garamond** family; it is not bundled or identified as the original Apple typeface. Font trials also use Times New Roman and Palatino Linotype.

```powershell
.\.venv\Scripts\python.exe piforma-manual/design-study/prepare-study.py
.\PiForma_Guide_v2\typst.exe compile --root piforma-manual piforma-manual/design-study/study.typ piforma-manual/design-study/design-study.pdf
.\PiForma_Guide_v2\typst.exe compile --root piforma-manual piforma-manual/design-study/type-tests.typ piforma-manual/design-study/type-tests.pdf
.\.venv\Scripts\python.exe piforma-manual/design-study/review-study.py
```

Alternatively use `typst` on PATH. `study.typ` defines six named composition functions and shared primitives; the default arguments point to the selected manuscript copy. These are trial composition templates with deliberate art direction, not a general-purpose automatic pagination engine. New passages require checking their fit; text must continue to another page rather than shrink to fit.

`renders/proposed-*-72ppi.png` are 432 × 522 pixels and `*-144ppi.png` are 864 × 1044 pixels. The PDF supplies the actual physical dimensions; a screen viewer cannot guarantee physical size. `validation.json` records trim, embedded fonts, 24 selected text-unit checks and unchanged production hashes. `production-lock.json` records the production sources as they were before the study.

Stop at this review stage. No proposed typography or layout has been applied to the full guide or pushed to the repository.
