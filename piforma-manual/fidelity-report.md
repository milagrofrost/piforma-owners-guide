# Fidelity report

**Archived four-page design-study report.** The current manuscript is described in `manuscript-review-report.md`; `main.typ` now builds that working book. The four-page study remains at `prototype.typ` and its existing output files.

## Result

Editable four-page Typst prototype; final PDF is 432 × 522 pt on every page. Final build has no compilation warnings/errors, all fonts embedded, no extracted text bounds outside the page, and no raster images (the illustrations are SVG/vector). The final 300 dpi PNGs and comparisons were actually opened for visual review. Successful compilation was not treated as visual verification.

This is a substantial layout reconstruction, **not an exact facsimile**. Original font identification, photographic-quality cover art, and physical trim calibration remain unresolved. The supplied artwork and installed fonts limit fidelity; the report does not claim those acceptance criteria are fully met.

## Render-and-review record

Each numbered folder retains all four renders, four Plus side-by-side comparisons, four overlays, representative SE renders, a contact sheet, compiler log, and preflight JSON. Iterations 1–3 used 240 dpi; iteration 4 uses 300 dpi. All four pages were inspected in each iteration's contact sheet; enlarged comparisons and pages were additionally opened. Source changes were recompiled before the next review. The final main source supersedes those earlier renders.

| Pass | Five largest differences found in the rendered output | Corrections / outcome |
|---|---|---|
| 1 | Body lettering too wide; paragraph lines too close; chapter introductory baseline too low; warning triangle came from a fallback typeface; chapter mouse lacked the original sketch character | Narrow body/heads to 85%; increase leading from 3 to 7 pt; move first introductory line up 4 pt and second up 5 pt; replace triangle glyph with an editable polygon; retain mouse correction for next pass. Four pages recompiled and reviewed in pass 2. |
| 2 | Cover computer substantially too small; marginal rules/heads too heavy; footer type too small; chapter heading slightly too narrow; mouse silhouette and stroke far from the reference | Crop the cover SVG's internal whitespace and remove its ellipse shadow; use 0.55 pt rail rules and 10.5 pt rail heads; enlarge/narrow footer lettering; increase chapter head from 15 to 16 pt; replace mouse with a thin construction-line SVG and lighten capital. Four pages recompiled and reviewed in pass 3. |
| 3 | Cover scan box was being treated as trim; comparisons stretched interior scans to target size; section rule 2–3 pt below measured position; excessive gap before second instructional paragraph; art and font still visibly differ | Standardize to estimated 6 × 7¼-inch trim; compare at identical pixel-per-point scale with white padding/cropping; move Unpacking rule to 108 pt; move second paragraph to 173 pt; retain vector artwork and explicit font limitation rather than claim a match. Four pages recompiled and reviewed in pass 4. |
| 4 | Times serif forms differ from original; cover lacks photographic detail; technical art is simpler and heavier than originals; numbered steps/caption differ from selected comparator; actual physical trim/red ink remain uncalibrated | These remaining differences are documented below. No arbitrary embellishment was added. Final build passed preflight; improvements now require better font/artwork or a physical reference rather than further small coordinate nudges. |

A cover-crop helper command failed during pass 2 before compilation, leaving that pass's smaller art unchanged; the crop was applied successfully before pass 3. Initial Typst subtraction syntax was corrected before the first completed render. Final logs contain no warnings. Early comparison folders used slight scan resizing; the final comparisons correct that and should be used for measurement.

## Unresolved differences

1. Times New Roman compressed to 85% approximates width but not the original condensed Garamond letterforms, stroke contrast, or bold shapes. Small capital letters are sized uppercase text, not a verified original small-cap font. Replacing the family with a licensed original requires a new line-wrap review.
2. The cover uses the supplied PiForma SVG converted to exact neutral grayscale. It lacks the original photographic texture, depth, realistic keyboard, and mouse cable. Its illustration occupies a similar region but reaches slightly lower. No unavailable photograph was silently invented.
3. The instructional SVG preserves the supplied computer geometry but has simpler technical detail than Apple's drawings. The mouse construction drawing is an adaptation, not traced original artwork. The SVG computer's screen lettering is outlined during PDF export and is edited in the SVG source.
4. Prototype-specific notes, three numbered steps, and figure caption prevent identical line wrapping and page-density matching. The original selected illustrated page uses square-bulleted power-cord directions; the user explicitly required numbered steps. The original cover's Apple symbol has no supplied PiForma counterpart, so that location remains white.
5. Scanned color, varying PDF page boxes, skew, and show-through cannot establish exact ink or physical trim. The selected 6 × 7¼-inch trim and warm red are documented estimates. No claim of colorimetric or PDF/X certification is made.

## Final checks and printing

`output/iteration-4/preflight.json` records four pages, exact configured dimensions, embedded font subsets, zero compiler warnings, and no text bounds outside the page. Visual review found all expected artwork present, no clipped text/illustrations, no overlaps between text blocks, and coherent logical recto/verso layout. Automated bounds checks do not substitute for that image review.

`output/piforma-owners-guide.pdf` is the four-page reading copy. `output/piforma-owners-guide-print-production.pdf` is a separate six-page Letter carrier document with crop marks and vector placement: cover, blank reverse, chapter 1, chapter 2, chapter 3, blank reverse. Artwork does not run to the trim edge, so no bleed is needed. Crop marks are outside the trim. It is intended for actual-size, long-edge duplex printing followed by trimming. Do not print the reading copy duplex as a bound book without arranging the cover reverse.

Request a proof at 100%/Actual Size, no Fit/Shrink, no booklet imposition, and no driver-added margins. The printer may use uncoated white stock appropriate to its equipment; choose paper after viewing the proof. Confirm the ½-inch punch/binding allowance and check a measured 6 × 7¼-inch trim before the full run. Color is RGB and should be proofed on the actual printer. Font files are not redistributed; the PDF embeds the used subsets. All illustrations are vector, so raster resolution is not a production constraint.
