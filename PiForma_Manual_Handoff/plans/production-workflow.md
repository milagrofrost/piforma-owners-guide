# Codex workflow and checkpoints

## 1. Gather evidence before prose

Read both Apple PDFs visually and inspect existing Typst prototype. Inspect `Macintosh-PiForma-docs` and associated repositories if available; record exact links, commit or version and source file locations. Draft a verified parts/software/behaviors register. Preserve conflicts in the unresolved list. Do not edit live PiForma software as part of writing the manual.

## 2. Build the book's content before perfecting every page

Create chapter Markdown drafts under `manuscript/`; work from the annotated contents. Every physical instruction should have an action, a visible confirmation and a troubleshooting note when useful. No blank fluffy paragraphs just to reach a specific page count.

## 3. Bring content into Typst

Use the existing Typst styles and style system, but restructure as needed into multiple source files. Generate TOC and page numbers automatically. For pictures not yet supplied, reserve figure boxes with accurate captions and `[PHOTO NEEDED]`, without generating fictional hardware images. Keep heading, caption, callout and glossary patterns editable.

## 4. Run quality checks

Compile Typst, export PDF and page PNGs, actually inspect all pages. Check page geometry, text overflow, missing assets, typography, facing margins, footers and line art. Compare against Apple manuals with page-by-page visual references. Remember that Apple's scans may have skew, punch marks and image artifacts which do not belong in newly printed pages.

## 5. Make a printing copy only after factual approval

Produce one reading copy and, if needed, a print-service version with the correct trim and printer-specified bleed/crop settings. Don't assume any specific Office Depot location can trim or bind the desired size. Keep inside binding margins generous enough for the selected binding and verify using a physical one-sheet test before printing a whole book.

## Suggested status notation

- `[VERIFIED]` current physical testing or confirmed repo/config
- `[OWNER]` directly dictated by owner, not yet independently checked
- `[HISTORIC]` documented in earlier project discussions
- `[PHOTO NEEDED]` illustration placeholder
- `[VERIFY]` conflicting or incomplete detail

No status tokens should remain in the final printed edition except deliberately labeled illustrations awaiting completion in a proof edition.
