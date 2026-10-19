# Owner direction — October 17, 2026

Owner approved the six-page art-direction study for the complete guide and requested direct, confident details without “recorded.” Publication specifications now state the existing facts directly; this does not add new hardware facts or constitute a new physical verification. Original evidence and unresolved device checks remain in this file and the editorial tracker.

# Owner correction — battery display and bag visibility

The owner confirms the photographed battery reading is 84%, correcting the earlier 94% transcription. The battery display CAN indicate whether charging from the wireless receiver is working; it cannot be seen while the computer is packed in the bag. Earlier claims that no dependable indicator exists are superseded. No specific symbol or indicator appearance is inferred.

# OWNER-INTERIOR-PHOTOS — October 15, 2026

Received and inspected inside-1.png, inside-2.png and inside-3.png. Owner labels identify the internal assembly, display controls/driver, Raspberry Pi, 5V rail, adapter, ordinary speaker, separate chime assembly, battery, AC inlet, chime selector, plunger and wireless receiver. The battery display visibly reads 94%. This does not establish wireless charging status or the meaning of smaller display symbols. Original images and labels remain unchanged.

# OWNER-WIRELESS-CHARGING — October 15, 2026

Owner directly confirms wireless charging verification is uncertain: no dependable visible charging indication; a USB power monitor may provide evidence of supply-side draw. Updated Chapters 1/4, troubleshooting and capture checklist. Do not infer a charge-status symbol or successful battery charging from physical fit or supply draw.

# OWNER-SCREENSHOTS-1-11 — October 15, 2026

Source: numbered PNGs in assets/illustrations, owner's screenshot-integration brief, and explicit approval of captures 9/10 plus later capture 11. Manifest and SHA-256 provenance: assets/screenshots/manifest.json. Visible labels and controls are primary evidence for this installed interface. Owner brief supplies minimize-to-Dock/return behavior; static captures alone do not demonstrate outcomes. Capture 11 visibly states Enter to send and shows Send. The Clippy opening gesture remains unverified. Snapshot memory figures are not fixed specifications; highlighted Save and Shut Down do not prove completed operations. PiForma Guide launches a window titled Macintosh PiForma Guided Tour. Clippy close is upper right, unlike the illustrated themed document window. No unobserved shortcuts or network controls were inferred.

# October 15 editorial evidence update

Re-read the accessible canonical documentation checkout and compared software, hardware, maintenance, known-issues, safety and AtEase configuration with the inspected snapshots: all six match byte-for-byte. Hashes are in `october-15-source-check.json`. Inspected panel menu/action source confirms About This PiForma, Show Desktop, Open Home Folder and shutdown command implementation; AtEase source confirms click-to-launch and tabs. No fresh device observation is claimed.

Ordinary mouse/typing/file/save explanations are general editorial instruction, conditional on the application's visible controls. They do not establish installed document apps or shortcut maps. Owner-confirmed six-second close-active behavior remains authoritative. Archived gesture maps and proposed Ctrl+Esc are unpublished operating instructions, preserved in the production tracker. Rear-drawing Audio Out function needs confirmation. No source asset was altered.

# Manuscript evidence register

Inspected October 11, 2026. Canonical build facts remain in [Macintosh-PiForma-docs](https://github.com/milagrofrost/Macintosh-PiForma-docs). The manuscript adapts those facts for readers; this register tracks provenance and contradictions, not a competing hardware specification. No source repository or live-device software was edited.

## Evidence keys

| Key | Source | Status / limit |
|---|---|---|
| H01 / H01-* | Handoff `content/02-chapter-1-getting-started.md` | owner-current October operating account; suffix names the operation |
| H03 / H03-* | Handoff `content/03-chapters-2-to-4.md` | owner-current narrative plus explicitly dated historical records |
| H04 / H04-support | Handoff `content/04-voice-and-sample-prose.md` | voice model and owner support preference |
| OWNER-UPDATE-1 | Owner's reply during this chat: “Six seconds closes only the active app” | latest owner-current confirmation; supersedes six-second close-all instructions |
| OWNER-IMAGES-2026-10-14 | Owner descriptions of 1-2a/b, 1-3b–e, 1-4a–d, 1-6a/b, plus the supplied assets | owner-current: foam seating, keyboard orientation, identified controls, support-leg seating, optional latch opening, normal rear-plunger/top-slit battery check; deliberate latch/right-click/optical-sensor humor |
| OWNER-TALK-2026-10-19 | Owner's spoken answers in the project thread, October 19, 2026 | owner-current: AtEase tabs (At Ease Items, sites; no paging); quit a game and then EmulationStation with two six-second logo holds (N64 controllers have no spare hotkey); Bose are optional 1984 RoomMates, do not fit in the bag; rear socket is audio output, switching needs a command for now; browser is Chromium styled as Netscape; Winamp is QMMP, songs in ~/Music; runtime ~6 h, ~4 h for N64; mouse one AA, keyboard USB-C on right; Weather approximates location; composite input for VCR/console; no microSD backup; brightness/color fixed, dim, uncalibrated; ~600 × 480 visible; exterior unchanged; 8 lb 13 oz; Flying Toasters manual only |
| D-README | `Macintosh-PiForma-docs/README.md` | remote source inspected; local file matches remote blob |
| D-HARDWARE | `docs/hardware.md` in that repo | remote and matching local source; reported final hardware, not new physical inspection |
| D-SOFTWARE | `docs/software.md` | remote and matching local source; July 2026 audit-backed architecture, not October device test |
| D-BOM | `docs/bom.md` | remote and matching local source; some purchase/representative entries, not all physically measured |
| D-SAFETY | `docs/safety.md` | remote and matching local source; documented AC path, battery and unfused rail |
| D-GESTURE | `scripts/apple_gesture_button.py` | remote and matching local archive; conflicts with OWNER-UPDATE-1; not assumed deployed |
| D-AUDIO | `scripts/usb-audio-loop.sh` | remote and matching local source; C-Media Cable Creation capture → normal output |
| D-KNOWN | local `docs/known-issues.md` | inspected local archive; sensitive ribbon and heat/shelf pressure history |
| D-MAINTENANCE | local `docs/maintenance.md` | inspected local archive; source selector, chime checks, plunger, bag charger |
| D-RELATED | local `docs/related-projects.md` | inspected local integration/credit map; no runtime verification |
| D-ATEASE | local `config/atease/config.yaml`, app folders | two configured folders: At Ease Items / sites |
| P-README | `piforma-panel/README.md` | source/design overview |
| P-MENU | `piforma-panel/src/menuDefinitions.ts` | source confirms Special → Shut Down and Apple → About This PiForma |
| P-ACTIONS | `piforma-panel/src-tauri/src/panel_actions.rs` | About action launches `about-piforma` |
| P-POWER | `piforma-panel/src-tauri/src/system_actions.rs` | OS poweroff/reboot calls and confirmation support; actual installed dialog flow untested |
| A-APP | `AtEase-simulator/src/app.ts` | selectable tabs and folder-specific app loading; README contradicts this |
| C-README / C-MAIN / C-WINDOW | ControlStrip README, `src/main.ts`, `src/windowMenu.ts` | launch/focus support; source invokes individual selection while README says it only closes popup; deployed version unknown |
| ABOUT-README / ABOUT-CONFIG | `about-this-pi/README.md`, `ui/config.js` | system-information app titled About This PiForma; not itself established as tutorial viewer |
| VIEWER-README / VIEWER-STACKS | Docs Viewer README, `src/stacks.ts` | separate canonical-docs viewer with bundled/cached offline content and Update Stack |
| OUTLINE / editorial-advice | `working-outline.md` and original conservative editorial guidance | organization, plain-language definitions, handling suggestions; no medical approvals or invented electrical ratings |
| PHOTO-* / Q-* / needs-confirmation | shot list, outstanding questions and embedded draft notes | deliberately unresolved, never promoted to verified |

`source-manifest.json` stores exact remote file/blob SHAs, retrieved URLs, branch and date. These are **blob SHAs, not commit SHAs**. Immutable content was captured under `snapshots/`. `local-source-manifest.json` records absolute source paths and SHA-256 hashes. Seven overlapping canonical files were checked against Git blob hashes and matched. This identifies the read versions without claiming a release commit or deployment version. `paragraph-provenance.json` ties each paragraph/list item to its evidence comment, section, and content hash or preview.

Other inspected upstream evidence: Matt Chesters' keyboard README (blob e35e6964e442ad230d81844bc5ca94e88c042014, first 80 lines); Flight-of-the-Toasters README and the Clippy fork README. `milagrofrost/clippy-rpi` metadata resolves to renamed `milagrofrost/clippy`; the old-path README fetch failed, then the canonical-name fetch succeeded. Individual license files have not been fully audited; do not certify a complete attribution inventory.

## Decisions and contradictions

| Topic | Finding | Draft treatment |
|---|---|---|
| Six-second hold | Owner now confirms active app only; archive closes all | Use owner confirmation in Chapters 1/3; retain discrepancy here; other timings and tap targets untested |
| Battery access | Resolved October 14: both routes exist | Normal check uses rear plunger and viewing through top slits. Optional top access: slide toward open padlock, then lift at slider. Instructions distinguish viewing from internal repair. |
| Battery/charger | Repository names Anker Prime 26K 300W and internal 100W adapter | Fill hardware tour and appendix as documented records; exact labels, ratings and manufacturer precautions still pending |
| Bag charging | Hardware/maintenance place transmitter under velvet and cable in back pocket | Fill placement gap from docs; preserve molded-foam seating and separate charge-status verification; supply and orientation unconfirmed |
| Chime dial | Owner powered-on listening check versus archive power-on sound description | Retain check without promising instant replay; silence not diagnostic; separate desktop and chime audio |
| External audio | Helper captures USB source and loops to system output | Preserve external sound into PiForma; do not relabel as output-only adapter; socket/model/levels pending |
| About/viewer | Source implements separate information and documentation apps | Distinguish them; bottom-right icon target remains unconfirmed |
| AtEase | README single-folder claim conflicts with tab code and two-folder archived config | Describe tabs where installed; exact current labels/version remain pending; do not silently amend upstream README |
| ControlStrip | README denies functional row selection; newer code invokes selection | Describe ordinary launch/focus; withhold a guaranteed window-list procedure until installed behavior is checked |
| Volume push | Software supports mute, hardware docs say inaccessible | Do not tell the reader to push the installed knob to mute |
| Display faults | Local issue record includes heat-deformed shelf/controller pressure | Retain symptom-driven checks; do not diagnose every blank screen as a bad ribbon |
| Controllers | Owner says N64; maintenance says USB but no full connector inventory | No native-versus-USB assumption for both supplied devices |
| Speakers | Bose models/stands/power/packing absent | Dedicated sections in Chapters 1,2,4 plus figures and explicit placeholders |
| Pouch | Felt versus velvet unresolved | Neutral “brown accessory pouch”; exact layer order unchanged |
| Shutdown | Menu source verifies Shut Down; wiring source says hard switch cuts rail | Graceful OS shutdown first, hard switch last resort; completion indicator and installed UI still pending |

No SSH or live PiForma session was available/used. Remote code inspection does not resolve deployed-versus-archived discrepancies. No electrical pinout, runtime promise, certification, warranty, speaker model, charging limit or firmware shortcut was invented.
