# How the Macintosh Plus and SE manuals are laid out

I studied all 118 pages of the Macintosh Plus Owner's Guide and all 136 of the SE guide, and measured the scans. The two books follow the same rules. Each rule below has a purpose, and next to it is what the PiForma guide now does.

## The page

The page has two zones: a narrow **left rail** of about 96 pt and a **main column** of about 242 pt. Running text always sits in the main column. The rail holds anything that helps you find, label or qualify that text, so you can scan the rail to find your place.

| Apple rule | Why | PiForma guide now |
|---|---|---|
| Body type is about 10 pt condensed Garamond, close to single-spaced (x-height 3.85 pt on a 10.4 pt line) | Fits about 75 characters on a short line and keeps pages calm | 9.5 pt EB Garamond on a 10.5 pt line, down from 10.5 pt, with the same x-height as Apple. EB Garamond isn't condensed, so lines hold about 65 characters. |
| Paragraphs aren't indented and are separated by about half a line | Short paragraphs stay distinct without looking double-spaced | Half-line gap |
| Main section heads are 14 pt bold under a thick red rule across the main column | Marks a new topic | 13 pt bold under the red rule |
| **Subsection heads sit in the left rail**, under a fine red rule, level with the first line of their text | Lets you scan the rail for "The keyboard" or "The power cord" | All subsection heads moved to the rail |
| Important and Warning labels go in the rail with a triangle | Stands out without breaking the text | Already did this |
| Short definitions sit in the rail next to the bold term they explain | A glossary entry right where it's needed | Eight terms have one: source selector, microSD, composite video, Bluetooth LE, AtEase, EmulationStation, save state, emulator. Write `[RAIL term|definition]` on its own line before the paragraph; `rail-def()` places it, so it never moves page breaks. |

## Pictures

| Apple rule | Why | PiForma guide now |
|---|---|---|
| **Figures have no numbers.** Text says "the illustration" or "shown on the opposite page" | Numbers read like a technical report, not an owner's guide | All "Figure 1-6b" numbers and references removed |
| Captions are rare and short. The SE puts a small red square before each one | The picture should explain itself | Small red square, no number |
| A picture narrower than the main column stays in it, with its label in the rail beside it | Uses the rail for annotation and keeps the text column clean | Narrow screenshots and drawings now carry their caption in the rail |
| A large picture spans the rail and main column together, with callout labels on fine red leader lines | Big hardware pictures get the whole page width | Wide pictures already did this |

## Variety, and when it's used

| Apple rule | Why | PiForma guide now |
|---|---|---|
| **Two or three narrow columns, in smaller type**, only for optional background (such as "Bits and bytes"), set off by a thin black line across the whole page with its title in the rail | Says "you can skip this" visually | The startup chime list is now a two-column sidebar like this |
| Small tables with bold column heads over a thin line, for reference data (pins, specs, sizes) | Makes lookup fast | The Apple-logo shortcuts are now a table |
| Numbered steps: the action is set in **bold**, and the explanation follows in roman | You can follow the bold lines alone | First sentence of every numbered step is bold |
| Bold for terms at first use, step actions and glossary terms. Italic for book and disk titles and the odd stressed word | Each style has one job | Bold used as Apple uses it; italic is available in the manuscript |
| Glossary entries run in: **term:** then the definition | Compact and scannable | Glossary now runs in this way |

## Page breaks

- **Chapters always start on a right-hand page.** The page facing the opener is a full-page sketch of the computer (in the Plus, a gray tinted leaf comes first). **The PiForma guide already starts chapters on right-hand pages; Every chapter now has a facing black-and-white picture (`art-page()` in `styles/book.typ`, set by `art:` in `main.typ`).**
- **Sections don't force page breaks.** A new section starts wherever the last one ended. Apple only moves a section to a new page to keep a step next to its picture, and accepts some white space at the bottom of a page to do it. The PiForma guide works the same way.
- **A thin black line across the full page is not a break.** It sets off a sidebar.
