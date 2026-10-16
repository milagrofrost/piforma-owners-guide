# Reference analysis

## Evidence and coordinate convention

Both supplied PDFs were inspected visually: contact sheets of the first 24 pages of each, enlarged Plus cover (PDF 1), chapter opener (15), Unpacking (16), and illustrated power-cord instructions (22), and the enlarged SE chapter opener (17). Covers, contents, prefaces, annotation pages, and illustration pages were included. PDF numbers below are one-based, not the printed folios.

Coordinates are points from the upper-left scan corner; 72 points = one inch. OCR bounding boxes were checked against rendered page images. OCR font names and sizes are recognition metadata, **not proof of the original fonts**. Machine-readable scan boxes and threshold measurements are in `output/reference-measurements.json`; rerun `scripts/measure-references.py` to reproduce them.

## Verified measurements versus interpretation

| Element | Evidence / measurement | Status |
|---|---|---|
| Plus document | 118 PDF pages; cover 435.85 × 522.70 pt (6.0535 × 7.2597 in) | Verified PDF box, not physical trim |
| Plus interior | Opener 432 × 520.30 pt; Unpacking 432 × 519.60 pt; other pages vary; a 748.8 × 516 pt scan is also present | Verified; the scan is not a uniform production master |
| SE document | 136 PDF pages; cover 558.72 × 642.96 pt; most sampled interiors 484.56 × 642.96 pt | Verified PDF boxes; do not infer physical size from these scans |
| Plus chapter rule | PDF 15: threshold envelope x=163.5–404, y=47.5–50 pt | Verified raster measurement at 144 dpi; includes skew and edge antialiasing |
| Plus contents rule | PDF 5: x=162.5–401.5, y=49.5–52 pt | Verified raster measurement |
| Plus body section rule | PDF 16: x=151–392, y=106.5–109.5 pt | Verified raster measurement; intended thickness is smaller than the skew envelope |
| Plus narrow rail rule | PDF 22: x=26.5–138, y=38.5–39 pt | Verified raster measurement |
| SE chapter rule | PDF 17: x=160.5–457.5, y=40.5–43.5 pt | Verified scan coordinates; larger scale than Plus |
| Plus body start | Opener x≈164; verso body x≈152 | OCR coordinates confirmed visually; approximate intended alignment |
| Plus text column | About 240–242 pt (3.33–3.36 in) | Estimate based on rule lengths and text edges |
| Plus cover title | x≈84 pt; first title glyphs y≈28; second line y≈51 | OCR glyph boxes, visually confirmed |
| Plus cover computer | Visible artwork approximately x=108–395, y=218–427 pt | Visual estimate; irregular photographic silhouette |
| Plus chapter introduction | Large T near x=155, y=193; small-cap line near y=210; following line near y=226 | Visual/OCR estimate |
| Plus opener list | Bullet text x≈174; rows near y=251, 269, 287, 304 pt | OCR boxes, visually confirmed |
| Plus footer | Folio near y=489–495; verso x≈27 and running text x≈65; recto folio x≈404 | Approximate printed glyph positions |

## Intended printed design

The Plus page is approximately 6 × 7¼ inches (ratio 0.828). **This is a trim estimate**, supported by the scan boxes, not a verified measurement of a physical copy. The template uses exactly 432 × 522 pt consistently. The SE cover scan ratio is 0.869 and its interior scan ratio about 0.754; cropping and scale changes prevent a reliable physical aspect-ratio conclusion.

The main text is asymmetrical, with a broad annotation rail on the left. Recto main-column x=164 leaves 26 pt outside the 242 pt column; verso x=152 leaves 38 pt at the inside right edge. Narrow rail text starts around 27 pt on versos and 40 pt on rectos. General top rules sit around 39 pt; chapter rules around 49 pt. The footer sits about 27 pt above the bottom. Main body paragraphs have no first-line indentation, ragged right edges, and modest paragraph gaps. Paragraph baselines on the Plus opener are about 14–15 pt apart.

The original lettering visually resembles Apple's condensed Garamond family: narrow serif forms, tall capitals, close-fitting bold heads, and compact body text. Exact family/version is unverified. Estimated type sizes: body 9–10 pt, section heads 12–14 pt, chapter title 15–16 pt, cover 21–23 pt, footers 7–8 pt, notes 8–9 pt. The template uses installed Times New Roman, body 10 pt at 85% horizontal scale, 7 pt paragraph leading, and bold headings also narrowed. This approximates proportions, not letterforms. The original document did not bundle a usable font.

Red is a warm orange-red. `#f34836` is a visual scan-based approximation, not a verified ink formulation or Pantone match. Major rules use 1.8 pt; annotation rules use 0.55 pt. No red chapter numeral: both enlarged openers show a small, dark chapter number on the letterspaced CHAPTER line. Small red square bullets align with text, rather than hanging far into the rail.

The chapter opening has a long white interval before the introductory capital. The large pale T rises above the first small-cap line; it is a raised initial rather than a conventional multi-line wrapped drop cap. Instruction pages use bold run-in directions, red bullets, and illustrations between actions. Warnings pair a small outlined red triangle and bold black Important/Warning in the annotation rail with text in the main column, ending with a second triangle. Narrow rail subsection heads have finer red rules.

Technical drawings are fine gray/black perspective line art, with red leader lines and small serif labels. Some chapter art retains pencil-like construction lines. The covers instead show grayscale photographic/halftone hardware. Figure captions are small roman serif where present; adding a caption is required for the PiForma prototype, but the selected power-cord comparator has no numbered caption. The PiForma computer and mouse assets remain editable SVGs. Their simpler forms and different perspective are a fidelity limitation.

The contents uses the same right-shifted column and rule, with a wide gap before entries, bold chapter names, red chapter numerals, compact indented subordinate items, and plain folio numbers without modern dotted leaders. The first Plus contents spread carries a letterspaced product line; the SE sampled contents omits it. Contents is analyzed but not added to the four-page prototype.

## Decisions where the manuals differ

Use Plus trim proportions and coordinate system; SE scan dimensions are unsuitable for direct adoption. Use the shared condensed serif, square bullets, thin annotation rules, outlined warning triangles, and chapter label. The Plus opener has additional prose beneath the safety sentence; retain corresponding PiForma prose. The SE opener has more conspicuous mouse artwork and no matching lower paragraph; use an editable construction-line mouse, without copying scan noise or allowing a cable to run into the binding edge.

Retain the supplied PiForma product content rather than imply Macintosh-specific ports or accessories. The required illustrated prototype has three numbered steps and a figure caption, while the selected original power-cord page has two square-bulleted directives. This is a deliberate content-driven difference. The original covers use an Apple symbol; omit it because the source project supplied no equivalent product mark. Remove the unrelated stripe logo and bottom slogan from the older template. Do not reproduce holes, stains, shadows from the binding, paper discoloration, or reverse-page show-through.

## Binding and physical printing

Logical chapter folios control parity: 1 and 3 are rectos; 2 is verso. Recto rail starts at 40 pt, mouse at 36 pt, and verso main content ends at 394 pt, leaving 38 pt inside. This allows a nominal ½-inch binding allowance; confirm the printer's actual punch pattern. Outside verso notes/folios can sit 27 pt from the edge. The reading PDF lists cover then chapter pages 1–3 for review. Its physical sheet parity is corrected in the separate production PDF by inserting a blank cover reverse.
