# Update — October 20, 2026 (senior editor pass)

The guide is 76 pages: the contents now fit two pages (no forced break in `contents()`), so the welcome starts on a recto and the blank page before Chapter 1 is gone. Names are unified: "power switch" (not power control/button), "menu bar" (not system bar), "PiForma Guide" for the built-in guide (glossary explains Docs Viewer and Macintosh PiForma Guided Tour). The glossary adds nice!view, PiForma Guide and Source selector. New `keep_together` entries hold Closing the bag, the battery-slit check, System sound and the EmulationStation screenshot to their pictures; the Shut Down screenshot sits at the top of "Stopping the computer" (its caption avoids "Special → Shut Down" so the verify-editorial order check still passes). "A closer look" now explains the vice president: "He was let go in 1985, but old habits die hard." Open editorial suggestions (plain-English pass over cautious sentences, slashes, browsing extras) are in the review doc linked from the project thread.

# Update — October 20, 2026 (owner notes, round 4)

Still 78 pages. The welcome now says the vice president didn't want customers opening their computers, and frames the PiForma as an early, unofficial Macintosh clone experiment (official clones came about ten years later). "Nintendo 64" controllers are now "game controllers" throughout. Runtime reads "about four hours of emulated games, especially graphics-intensive ones" in Chapter 1 and Appendix A; AV2 and VGA "had nothing connected when the PiForma was built". Every picture should share a page with the text that describes it: `keep_together` entries in `illustration-layout.json` hold each passage to its picture (all chapters), and the PiForma Guide screenshot was narrowed to 300 pt so it fits with its section. Check the contact sheets for this after any edit.

# Update — October 20, 2026 (owner notes, round 3)

The guide is 78 pages. **Must do before printing: build a clickable audio-output switch (internal USB speaker or rear output socket) and then update the Bose section in Chapter 1, which still says to ask the builder.** The owner's October 20 notes (fact register key OWNER-TALK-2026-10-20) are written in; the full to-do list, with what is done and what is open, is `piforma-manual/todo-2026-10-20.md`. Eight new photos are in `assets/illustrations/` (stand-centered, stand-profile, no-signal, boot-screen, keyboard-switch-usbc, niceview-labeled, bag-back-charging, bag-clasp; the two labeled ones are crops, with the full images in `assets/originals/`). The cover carries `assets/logo/piforma-logo.svg` at top left, and `back-cover()` in `styles/book.typ` puts `bag-front-color.png` on the outside back cover. Chapter 1 now runs: unpacking, controls, setup, safety, startup (No Signal then the joke boot picture), first session, power, stopping, packing (charging in the bag, closing the bag), then "If the PiForma doesn't start" with the battery check, symptom checks and the latch. `keep_together` in `illustration-layout.json` now works in every chapter; it holds the text together and makes it sticky to the picture that follows (wrapping the picture itself in a second unbreakable block loses the caption's height). The USB power monitor advice was removed at the owner's request, and so was the printed guide from the unpacking and packing steps (unpacking is now four steps; `verify-editorial.py` checks the new order). The owner's labeled desktop (`desktop-labeled.png`) replaces the first-session screenshot, and `wifi-menu.png` shows the Wi-Fi status menu in Chapter 3.

# Update — October 19, 2026 (Apple layout pass)

The guide is 74 pages. The welcome tells one origin story only: the rogue engineer in the (nonexistent) basement, the unnamed vice president let go in 1985, and an open-minded CEO; management, not the CEO, dislikes the latch. The credits keep one real-world line saying Apple had no part in it. Layout now follows `piforma-manual/apple-manual-layout-rules.md`: 9.5 pt body, subsection heads in the left rail, no figure numbers (captions carry a red square; narrow figures caption in the rail), bold step actions, run-in glossary. The manuscript supports `**bold**`, `*italic*`, pipe tables, and sidebars (`#### Title` … `---`), rendered by `build-manuscript.py`. Still open from that study: facing art pages before chapters and rail definitions for key terms.

# Update — October 19, 2026 (owner answers, round 2)

The guide is 81 pages. The welcome now tells the origin story and addresses display visitors. Chapter 2 lists the chime selector positions, Chapter 1 explains the missing battery warning, and Chapter 3 adds Apple-logo tap shortcuts and the remaining AtEase buttons. The back matter adds a limited warranty, an FCC-style notice and a "Tell us what you think" page; `build-manuscript.py` turns any `# ` section after the credits into a heading. The tap shortcuts are owner-confirmed, so they are written as "tap … four times"; the verify-editorial guard against guessed gestures still applies to other phrasing.

# Update — October 19, 2026 (owner answers)

The owner's spoken answers (fact register key OWNER-TALK-2026-10-19) are written in, at that point 75 pages. New facts include the AtEase tabs, quitting a game, Bose RoomMates, the rear audio output, browser, music, runtime, charging, weather, composite input, backups, display and weight. Bose power and stand assembly are still open. Builder to-do: a clickable audio-output switch.

# Update — October 19, 2026 (mechanical fixes)

Chapter 1: the battery-slit figure is now 1-6a and the latch figure 1-6b, so they run in page order (the files keep their names). "A closer look, strictly off the record" moved after the startup-symptom checks; its keep-together now ends at the figure. The duplicate "About This PiForma and the project guide" section was folded into "Your first session" with Figure 1-8, and "Stopping the computer" now points to Chapter 3 for the six-second hold. Chapter 3: "Clippy and the other diversions" is split into "Diversions" and "Clippy"; the EmulationStation screenshot moved below the game-setup paragraph to close a page gap. The glossary adds Clippy, Composite video, Docs Viewer, EmulationStation, HDMI, PiForma Panel, Save state and Wi-Fi (screen saver waits on the owner). The cover date reads October 19, 2026. `scripts/export-reviewed-pdf.py` writes the tracked `output/macintosh-piforma-layout-reviewed.pdf` from the working proof with images resampled to 300 ppi (about 9 MB instead of 87 MB); run it after every build. The working proof and source images stay full resolution.

# Update — October 19, 2026

`closing-app-1.png` and `closing-app-2.png` now appear side by side as Figures 3-6a/b under the six-second hold in "Leaving a full-screen program". Figure groups in `illustration-layout.json` now work in every chapter, not only Chapter 1. The diversion screenshots stay 3-7a–d; Clippy is now 3-8a/b and PiForma Guide 3-9, so figure numbers run in page order.

# Update — October 18, 2026

Seven owner-supplied images were added, bringing the guide to 73 pages. Figure 1-5 (`complete-setup.png`) shows the assembled setup at the end of the Bose section. Chapter 3 adds the controllers photo (`piforma-n64.png`, Figure 3-5a), the EmulationStation N64 list (3-5b) and four diversions (3-7a–d: Winamp, LimeWire Simulator, the Weather Channel, Flying Toasters); the Clippy and PiForma Guide figures were renumbered 3-6a/b and 3-8. The new screenshots are `assets/illustrations/12.png`–`16.png`, processed by `scripts/prepare-screenshots.py`. The manuscript lock was re-baselined after the copy-preservation check passed.

# Current direction — October 17, 2026

The owner approved the six-page study. The complete guide now uses natural-width EB Garamond and the six composition families, at 69 pages. Specifications state their existing facts directly without “recorded.” Read `piforma-manual/approved-redesign-report.md` for the layout changes and validation. Earlier history below describes the initial repository handoff.

# Continue this project

Handoff prepared October 16, 2026. Current manual: **63 PDF pages**, 6 × 7.25 inches, with four chapters and Appendices A/B. The tracked reviewed PDF includes all eleven software screenshots and three labeled interior photographs. It includes the latest 84% battery correction.

## Read first

1. Read `PiForma_Manual_Handoff/CODEX_START_HERE.md` and every file it references. The original packet records the owner's writing voice, exact packing order, startup and troubleshooting instructions, and scope.
2. Read the current manuscript, `piforma-manual/working-outline.md`, `photo-and-illustration-checklist.md`, and the newest entries in `research/fact-register.md` and `editorial-production-tracker.md`.
3. Inspect the current proof, Typst styles, and original Apple Plus/SE PDFs in `piforma-manual/references/`. Preserve the period layout and occasional jokes. Do not add filler to match an original's length.

## Owner-confirmed corrections that must survive

- Holding the Apple-logo control for about six seconds closes **only the active application**. Older archived gesture scripts disagree; do not substitute their timings or add other unconfirmed gestures.
- The battery in the interior photograph is at **84%**, correcting an earlier 94% transcription. The battery display **can indicate charging from the wireless receiver**, but cannot be seen while the computer is packed in its bag. The practical problem is visibility, not a missing charging indicator. Do not invent indicator symbols. The USB power monitor advice was removed at the owner's request on October 20.
- Normal battery checking uses the rear plunger and a view through the top slits. Optional latch access, unlock/lift/close/lock order, chime troubleshooting, packing layers and keyboard orientation must remain intact.
- Clippy's message field supports Enter or Send, as shown in `11.png`. Its opening gesture has not been established. Clippy's close button is upper right; the themed document window has close upper left. Do not universalize either arrangement.
- The persistent system menu bar and an application's own menu bar have different jobs. The document application's File menu supplies Save. `9.png`/`10.png` were explicitly approved as home-folder examples.
- PiForma Guide is the launcher label; its window is titled Macintosh PiForma Guided Tour. About This PiForma is separate.

## Next work

Use the photo checklist for current capture needs: save/reopen sequence, game/controller interaction, installed network controls, receiver/USB/controller connections, handle removal, assembled setup, keyboard edge controls and Bose speaker details. Interior overview and open-top battery-display photos are supplied. A closed-top battery-reading view and bag cable/alignment detail could still help.

Keep unresolved questions outside publication copy. Static screenshots do not prove successful saving or completed shutdown. Owner corrections take precedence over archived records; surface contradictions rather than guessing. Inspect real software/project documentation when needed, without treating saved research snapshots as live configuration.

## Validation and history

`piforma-manual/verification/` records the handoff manuscript hashes, 22 editorial preservation checks, 372 text-unit checks, source-image hashes and the 63-page preflight. The last content build had no compiler warnings or text geometry issues; affected battery/interior pages were visually reviewed. Rebuild on your machine and check fonts and page flow.

`piforma-manual/README.md` is the build entry point. Historical reports and `docs/history/working-session-readme.md` contain old page counts, local paths and superseded questions. `archive/original-template/` is design history, not the active build. Older scripts for finishing a numbered layout pass or screenshot pass depend on ignored historical iteration folders; use the current build and verification commands in the root README for ongoing work.
