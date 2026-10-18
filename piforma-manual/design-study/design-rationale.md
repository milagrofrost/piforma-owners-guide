# Art direction: natural type, purposeful margins, varied plates

The proposal keeps the narrow reading measure and asymmetrical Apple-derived page architecture. It removes synthetic condensation and makes the type of information determine the composition. A quiet chapter opening, a procedure, a visual inventory, paired controls, screen instructions and a reference table should have recognizably different rhythms.

## What the references establish

The Macintosh Plus scan is the primary dimensional reference because its instructional pages are close to this guide's 432 × 522 pt trim. On **Plus PDF 20**, body text begins around x = 152.65–153.60 pt and reaches about x = 388.40 pt; the nearby rules and existing measurements establish an approximately 240 pt column. Successive paragraph baselines in that sample are about **10.55 pt** apart. These are scan/OCR measurements checked against the rendered page, not proof of an original typeface or nominal point size. See `reference-body-summary.json`, `reference-text-measurements.json`, and the earlier production `reference-analysis.md`.

The SE scan has a larger page box. Its comparisons preserve scan proportions inside the same frame; they are useful for composition, not a claim that its original page size equals this guide. Specifically: **SE PDF 17** supplies the chapter-opening pause; **SE PDF 20** groups hardware views; **SE PDF 24** puts the operation name in the rail and lets the illustration occupy a large separate zone; **SE PDF 36** uses a true Important note in parallel with operating text; **SE PDF 96** demonstrates a technical plate with a different grid from the prose column.

The useful lesson is the distribution of information across the page. It is not a requirement that every image follow its nearest paragraph.

## Typography decision and alternatives

The current `book.typ` compresses paragraph, instruction, bullet, specification and heading text to 85% width, often by laying out a 242 / .85 = **284.71 pt** virtual column and then squeezing it into 242 pt. That retains vertical type size while narrowing letterforms and spaces. The result is a long, uniform letterfit in a physically narrow column. `typography.typ` also declares a 7 pt leading value, while the active book style overrides it with 6 pt; the active paragraph helper separately adds 8 pt below each block.

The type trials use exactly the same existing introduction at 242 pt, with a 6 pt Typst leading setting. Measured output:

| Trial | Horizontal proportions | Baseline pitch | Mean characters in full sample lines |
|---|---|---:|---:|
| Current Times New Roman, 10 pt | 85% | 12.62 pt | 70.8 |
| Times New Roman, 10 pt | natural | 12.62 pt | 58.8 |
| EB Garamond, 10.5 pt | natural | 12.82 pt | 58.8 |
| Palatino Linotype, 10 pt | natural | 13.16 pt | 54.0 |

These counts describe this passage, not a universal characters-per-line constant. Typst leading is added space, not the complete baseline pitch; the nominal 6 pt setting must not be reported as “6 pt lines.”

**Recommended direction for review: EB Garamond 10.5 pt at natural width, 242 pt measure, 6 pt Typst leading and a nominal 7 pt paragraph gap.** The six study pages use explicit placement and optical spacing for their different compositions, so this is a starting text style rather than one gap imposed on every object. Headings are natural-width 15 pt bold; secondary headings are 12 pt; notes are 8.5 pt and captions 8 pt with more open leading than the first trial.

The half-point increase is an optical test, not a way to make the book bigger. At 720 ppi, the lowercase x in EB Garamond 10.5 pt measures approximately **4.2 pt** of ink height, versus **4.5 pt** for Times New Roman 10 pt and **4.7 pt** for Palatino 10 pt. Its nominal size is larger while its lowercase remains slightly smaller. See `x-height-measurements.json` and the reproducible `glyph-probe.typ`. The gain is natural counters, wider letters and a less mechanical texture. The 12.82 pt baseline is very close to the current 12.62 pt; this is not accomplished by crushing line spacing.

EB Garamond is a Garamond-family alternative available on this machine, **not Apple Garamond and not an asserted exact match**. Its old-style construction gives a plausible direction to evaluate against the scans. Unscaled Times is the conservative fallback that needs no new family; Palatino's broader, larger lowercase takes more of this small page and changes the texture more strongly. The proposal keeps a looser baseline than the approximately 10.55 pt Plus sample as an explicit readability choice. It does not claim exact typographic facsimile. A physical print proof should decide whether 10.5 pt EB's smaller lowercase is comfortable enough before approving it for the whole book.

## Six compositions

| Study page / reusable function | Current context | Specific Apple comparison | Direction and reason |
|---|---|---|---|
| **1 — Chapter opening**, `chapter-opening` | Current PDF 7 | **Plus PDF 15**, printed 1; **SE PDF 17**, printed 1 | Keep the long title-to-introduction pause and initial. Let the actual front-view drawing inhabit the lower open corner, like the original opener's peripheral device drawing. The original “foam has opinions” paragraph remains intact. The unpacking lead sits below the visual pause. The opening is a threshold, not another section-and-image page. |
| **2 — Text-led instructions**, `text-instructions` | Startup starts on current PDF 19; battery text continues on 19–20 | **Plus PDF 22**, printed 8; **SE PDF 36**, printed 20; text measure on **Plus PDF 20**, printed 6 | The four startup steps become one readable sequence, with stable number alignment. Move the existing silent-startup paragraph into the actual annotation rail beside the chime step. It is secondary explanation precisely where a worried owner needs it. The first two battery paragraphs stay in the main reading stream. No new diagnostic or caution is invented. |
| **3 — Illustration-led packing plate**, `packing-plate` | Current PDF 8 | **Plus PDF 17**, printed 3, the unpacked-equipment visual inventory | Give the bag its own visual field and use the rail for the operation name. Its 320 pt width is only modestly larger than the current approximately 310 pt height-limited image; the stronger emphasis comes from placement and absence of competing body copy. Keep the exact caption explaining the printed guide's invisible layer. The packing sequence remains unchanged in the manuscript. |
| **4 — Grouped hardware controls**, `grouped-controls` | Current PDF 13, with introductory paragraph on 10 | **SE PDF 20**, printed 4, paired machine views; **Plus PDF 18**, printed 4 | Compare the opposite sides together instead of stacking two similarly weighted illustrations. Use equal scale, a shared horizon, and individual captions. The full existing identification paragraph gives orientation first. The small embedded labels are reinforced by readable captions; a larger plate would remain appropriate if these labels had to carry unique technical information. The original image canvases and object proportions are preserved. |
| **5 — Illustrated screen sequence**, `screen-sequence` | Program-opening paragraphs on current PDF 39; menu view on 40; desktop capture on 23 | **Plus PDF 29**, printed 15; operation-rail precedent **Plus PDF 24**, printed 10 / **SE PDF 24**, printed 8 | Make two visual stations: select a collection/program, then reveal the launcher. Each contains its complete existing paragraph and its own actual screen detail. The AtEase crop keeps both tabs and two rows of existing buttons; the second crop keeps View → Show Desktop. The prose itself acts as the legend, avoiding a second small caption repeating the same command. No button pixels or controls are reconstructed. |
| **6 — Full-width reference plate**, `reference-plate` | Current PDF 55 | **Plus PDF 71**, printed 57; alternative technical arrangement **SE PDF 96**, printed 80 | Release the inventory from the prose column. Align labels in a dedicated 91 pt column and values across a 251 pt column, with a 12 pt gutter. A single restrained rule and open rows take their cue from the comparison table, rather than boxed cells or modern cards. Preserve all ten hardware records and the appendix's qualification paragraph. Power architecture and other appendix content remain in the unmodified full manuscript. |

## Rhythm and the annotation rail

The facing-page proof treats study 1 as a recto, followed by spreads 2–3 and 4–5, and a verso technical plate. These are representative excerpts from different sections, not proposed adjacent pages in the final book. They show the intended rhythm: a reading-intensive page can face a large quiet illustration; two related views can balance a screen-based procedure; a reference appendix can switch to a wider information grid.

The rail has three supported jobs in the study: the original chime explanation, operation names alongside a procedure, and shared orientation for a plate. It is not filled with new quotations, decorative factoids or repeated paragraph summaries. The physical note sits in the rail; the current production helper often leaves only a label there and keeps its copy in the body. The study tests the actual parallel reading experience seen in the references.

Illustration aspect ratios remain original. There are no stretched images, regenerated interfaces, tinted panels, cards, ornamental frames or decorative new borders. The red rules and supplied red leaders remain restrained. The hardware group uses the existing canvases unchanged; the software crop changes framing only.

## What was reviewed, and what remains a decision

The study was compiled, rendered at 72 and 144 ppi, reviewed at page/detail scale, and compared to the specific reference scans. The first draft's tight Garamond line spacing and overlapping hardware canvases were rejected and corrected before this delivery. All six final page boxes are 432 × 522 pt, fonts are embedded, selected text reaches the PDF, and production-source hashes remain unchanged. `validation.json` records those checks. A screen render is not a physical print proof.

The study deliberately stops here. Review the natural Garamond texture first, then the six composition types and the actual-size screen details. If the direction is approved, the next phase would map appropriate compositions across the existing manuscript, preserve every instruction and figure, and proof real consecutive spreads. No full-book pagination, production style replacement or repository push is included in this study.
