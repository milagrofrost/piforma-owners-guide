# Layout system — Macintosh PiForma Owner's Guide

Editable source: `styles/book.typ`; content converter: `scripts/build-manuscript.py`; figure presentation: `assets/illustration-layout.json`. Manuscript wording and source images are unchanged.

| Element | Reusable treatment |
|---|---|
| Page | 432 × 522 pt (6 × 7.25 in); top 39 pt, body foot 479 pt; 242 pt main column at x=152. The left annotation rail is retained on both faces, following the reference's asymmetrical grid. It is deliberately not a modern mirrored two-column layout. |
| Chapter opener | Small letterspaced CHAPTER, black number, 16 pt condensed serif title, 1.8 pt warm red rule; original 123 pt opening interval retained; chapters start on rectos. |
| Section / subsection | 13 pt condensed bold with 1.4 pt red rule / 10.5 pt bold; fixed gaps and keep-with-next. |
| Body | Times New Roman 10 pt at 85% horizontal scale, 6 pt leading, 8 pt paragraph gap; ragged right, automatic hyphenation disabled. Each paragraph stays whole. This remains a documented substitute for Apple's original lettering. |

October 19, 2026: body is now EB Garamond 10.5 pt with 4.5 pt leading (11.3 pt line pitch) and a 12 pt paragraph gap, about half a line, after the Macintosh Plus manual's tight lines and clearly separated paragraphs. Numbered steps and bullets use an 8 pt gap.
| Numbered instructions | `instruction`: 13 pt number column, 229 pt text column; red bold number; wrapped lines align with the instruction text. No step wording changed. |
| Bullets | `bullet`: 10 pt marker column, 232 pt text; 3 pt red square and hanging continuation. Links remain live. |
| Captions | `caption`: uncondensed 8 pt, 2.5 pt leading; 4 pt image gap, kept with illustration; left aligned to plate or individual photograph. |
| Side notes / warnings | `side-note`, `important`, `warning`: fine red rail rule, small bold label, restrained serif text. No cards or backgrounds. These reusable styles do not add new warning copy. |
| Technical specifications | `spec-row`: 76 pt bold label, 8 pt gutter, 158 pt value; rows stay whole; no boxes or vertical rules. Original labels, colons and values retained. |
| Glossary | `glossary-term`: bold term kept with its full first definition paragraph. |
| Contents | 9.5 pt; 4.5 pt leading; no dotted leaders; deliberate break before Chapter 3 gives a two-page contents spread. |
| Running furniture | 8 pt at the original foot position; number outside; empty versos carry no title or folio. Logical numbering still includes intentional blanks. |

## Illustration classes

- Large packing and connector plates: up to 366 pt wide, with a mirrored full-width anchor (recto x=40, verso x=26). Minimum nominal inside clearance is 40 pt for these plates.
- Unlabelled bag photographs: paired at 176 pt each with a 14 pt gutter and separate original captions. Neither is cropped.
- Related side-control drawings: stacked at the same 288 pt source width. Only measured empty canvas above/below is omitted by a centered Typst viewport. Full objects and labels remain; the original PNG bytes and object aspect ratios are untouched.
- Stand: a small setup drawing, 150 pt high; the arrow is clear and the caption stays complete. It shares a spread with all setup steps and a page with the wide keyboard diagram.
- Keyboard: wide plate to preserve small labels and visible key legends.
- Mouse: matched 300 pt height, preserving source proportions and space for explanatory prose. Labels and jokes remain in their original artwork.
- Battery slit view: large orientation drawing. Latch detail: 180 pt height, held with the procedure and closing joke.
- Software screenshots, when supplied: use a full 366 pt plate when necessary for interface text; choose size by pixel resolution and readable native labels. None is fabricated here.

Do not increase raster size merely to fill a page. Edit individual size caps and layout-only keep/group rules rather than changing the manuscript. The standalone artwork proof uses the same image scale; it retains full source canvas for individual asset inspection.
