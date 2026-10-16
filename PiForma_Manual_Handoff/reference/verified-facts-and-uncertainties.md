# Facts and evidence status

This is a **working fact register**, not an independent audit of present-day device hardware. Do not silently promote dated notes to current verified status.

## Owner-dictated October 11, 2026, high-confidence operational observations

| Topic | Owner description | Editorial action |
|---|---|---|
| Bag unpack sequence | Small brown soft accessory pouch -> mouse and collapsible stand -> guide -> mousepad -> velvet foam board -> PiForma screen-up | Preserve exact order, diagram it |
| Accessory pouch | Two N64 controllers, USB hub, power cable | Inspect photo for inventory labels |
| Keyboard packing | Along PiForma's side; keys face bag; thicker edge rear, thinner front | Include annotated orientation photo |
| PiForma removal | Hand inside front bag wall to extract carrying handle; laying bag on back may help | Illustrate carefully |
| Bag charging alignment | Rear/bottom of PiForma seats in foam cutouts; gently wiggle to find low-motion resting position | Verify actual Qi charge status |
| Basic setup | Folding stand; PiForma centered on stand; keyboard directly in front; mouse alongside | Check stand load/placement |
| Keyboard power | Switch near top-right of keyboard | Photograph |
| Mouse power | Underside switch; commonly left on due to efficient idle | Clarify travel/storage choice |
| Extended usage | Plug PiForma into power if operating more than a few hours and power is available | Specify charger after verification |
| User USB access | One back USB port; hub for multiple peripherals | Label in drawing |
| Power-on | Right-side hard button, front green LED, possible chime, screen to desktop within 1-2 minutes | Write symptom-driven startup flow |
| Battery access | Top opens; external plunger depresses battery's button for charge lights / wake | Photograph safely |
| Battery wake anomaly | Sometimes needs brief mains connection even when showing full | State as observation, not diagnosis |
| Chime selection | Rear dial includes silent slots | Test precise behavior |
| Shutdown | Software shutdown preferred; physical switch can forcibly cut power | Verify OS menu names |
| Apple touch | Long press around six seconds to escape full-screen apps (owner's latest recollection) | Resolve with device configuration before publication |
| Carrying | Bag padded but does not protect against hard impacts | Clear, light warning |
| Battery care | Owner wants charge kept above roughly 25-50% most times | Avoid chemistry-wide claim |
| Service | No official support; experimental, for fun | Keep humorous but honest |

## Historically owner-confirmed, now should be verified again

- Name: **Macintosh PiForma**.
- Reused donor cabinet: **Apple IIc Monitor** (recorded 4090, likely label **A2M4090**, verify on device).
- Raspberry Pi 4 Model B, **4 GB RAM**, roughly **256 GB microSD**, **800×480** screen.
- Raspberry Pi OS with vintage desktop theme, RetroPie, and custom apps.
- Apple-logo touch control wired to **GPIO23**.
- Keyboard **A9M0330** vintage Apple Desktop Bus unit converted to Bluetooth LE, USB-C charging, nice!view; upstream `mattchesters/zmk-apple-desktop-bus-keyboard`.
- Wireless mouse with a USB receiver.
- Chime module previously described as YS-M3; independent USB speaker/audio component.
- Volume rotary control formerly reported GPIO17/27/22.
- Source switch formerly reported HDMI/RCA/VGA/RCA2, some unused.
- Keyboard has no F10; user chose Ctrl+Esc as DOSBox-X mouse release mapping, but check whether saved.

## Historical software names / probable sources, not guaranteed current state

`AtEase-simulator`, `piforma-panel`, `ControlStrip-Simulator`, `Clippy`, `about-this-pi`, `Macintosh-PiForma-docs`, `Macintosh-PiForma-docs-viewer`; RetroPie, Raspberry Pi OS, Chromium/browser, old Mac OS 9-inspired shell; possible Flying Toasters and Weather Channel additions.

## Contradictions or unresolved

1. Touch button: October 'about six seconds exits full-screen' versus June audit of ~2 s window close, ~6 s close all, ~10 s shutdown. **Must inspect current script and test device.**
2. Chime dial: active selection versus replay while powered on, plus intentional empty settings. **Test exact sequence.**
3. Battery power path and charger: no authenticated electrical specifications in this packet.
4. Wireless charging: molded foam positioning is known; transmitter/receiver placement and charge confirmation not yet established.
5. Bose speakers and stands: models, audio method, dimensions, power and packing are unknown. Do not conflate speaker carrying-bag searches with PiForma's actual bag.
6. Brown pouch: felt vs velvet; owner's recollection uses both.
7. Audio input adapter signal direction/type unclear.
8. N64 controller connection type unknown; USB hub relationship likely but needs photo.
9. About This PiForma icon position and app title should be checked against desktop.
10. Physical switch behavior after software shutdown is uncertain.
11. The donor monitor's actual model label and February 1985 date should be checked against physical markings.

## Evidence policy for Codex

Mark each technical paragraph internally as one of: `owner-current`, `repo-verified`, `device-tested`, `historic-record`, `editorial-advice`, `needs-confirmation`. Draft readable prose without these labels in the final book, but maintain a separate fact register for unresolved points. Historical assistant suggestions are **not verified implementations**.
