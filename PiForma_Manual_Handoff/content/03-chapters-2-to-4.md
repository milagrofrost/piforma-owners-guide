# Detailed editorial directions: Chapters 2, 3, 4 and technical appendix

## Chapter 2: Inside the Macintosh PiForma

This chapter is a friendly tour of physical components. Introduce what a part does and why it was chosen before technical minutiae. Explain that PiForma is a custom-built machine, not a restored stock Macintosh and not an Apple product.

### Provenance and display

The core cabinet is a repurposed **Apple IIc Monitor model A2M4090** (recorded historically as '4090 Apple IIc Monitor'; verify exact marking from photos), originally circa February 1985. Its nostalgic casing now houses a **Raspberry Pi 4 Model B, 4GB RAM**, with approximately **256GB microSD storage**, an **800 × 480 display**, and bespoke power/control hardware. These specifications were owner-confirmed in June 2026 but should be rechecked before publication. Distinguish monitor donor shell from original Mac Plus/SE hardware: PiForma is deliberately not an Apple Macintosh computer.

### Power and controls

Battery-powered, with external charging and a Qi-alignment arrangement in the travel bag. The owner reports that the internal pack can charge while the PiForma is turned off. Exact battery manufacturer, voltage/current, capacity, charger specifications, wireless charging connections and operational safety limits require hardware records. Current owner narrative: right-side hard power button, green front indicator, rear chime-selector knob, battery-check/wake plunger under/open top, front Apple-logo touch button, and collapsible supporting stand.

Older technical notes mention a **volume encoder using GPIO17/27/22** (rotation and push-to-mute) and an external source switch that cycles **HDMI / RCA / VGA / RCA2** with the last two unused. These are dated project observations: check whether those features still exist in the build and confirm their labels. Older notes also describe a dedicated **YS-M3 chime module** and a USB audio speaker. Confirm wiring and distinct roles of chime hardware vs audio playback.

### Keyboard

This is a vintage **Apple Desktop Bus (ADB) keyboard**, model **A9M0330**, converted for **Bluetooth Low Energy** using work based on the project `mattchesters/zmk-apple-desktop-bus-keyboard`. Historical records say it charges through **USB-C** and has a **nice!view** display. Do not treat conversion as the owner's original invention; credit upstream design and implementation accurately after checking documentation. Owner reports the keyboard has an on/off switch at the upper-right. Confirm location, pairing, charge indicator and exact keyboard model revision with photographs.

There is a real shortcut caveat: the older keyboard has function keys only through **F9**, while DOSBox-X normally needs Ctrl+F10 to release mouse capture. The owner selected **Ctrl+Esc** as the intended replacement. Check the present DOSBox-X mapper configuration before telling readers that this shortcut currently works. The manual should describe this accessible 'how to free the mouse' issue in plain language.

### Mouse

Wireless mouse with an on/off switch underneath, paired by a **USB receiver connected inside/to the Pi**, according to prior notes. Its idle state is power-efficient enough that the owner generally leaves it on, though turning it off for transport is reasonable. Confirm battery/charging method rather than assuming.

### Bose speakers and stands

The owner **wants a dedicated discussion** of the two Bose speakers purchased for use with PiForma and the accompanying stands, including what they do, how to position them, and how to transport/store them. **Exact Bose model, power, connection type, dimensions, and whether the speakers and stands go inside the PiForma bag are presently unknown.** Do not derive the model from photos of unrelated bags. Insert clear placeholders and ask for product photographs/model labels. Once verified, include a brief set-up subsection in Chapter 1, a feature description in Chapter 2, and handling notes in Chapter 4.

### Credits

Credit preexisting open-source projects, Apple-era source inspirations and reused electronic designs. Repositories and third-party licenses are to be checked rather than deduced from names. A candid, understated 'Built from lots of good ideas by other people' introduction fits the intended voice.

## Chapter 3: How the Macintosh PiForma Works

### Operating environment

PiForma uses **Raspberry Pi OS** with a classic Mac OS 9-ish appearance, custom apps and emulators. Owner-confirmed software in historical notes: **AtEase**, **PiForma Panel**, **Control Strip Simulator**, **Clippy**, **RetroPie**, a browser, and an **About This PiForma** information/documentation experience. Some notes also mention Flying Toasters, Weather Channel and Winamp. Avoid implying these are currently installed and working without checking the device and repos.

The historical boot chain was described as power button -> dedicated hardware chime -> Pi boot -> splash -> graphical login -> custom PiForma desktop. Exact initialization scripts, service manager and compositor may have changed, so present this only after checking live configuration.

### AtEase and app launching

Explain the period-inspired AtEase launcher as the friendly place for opening apps and games. Earlier design discussions refer to tiled buttons and groups/tabs, but not every proposed feature was implemented. Inspect actual `AtEase-simulator` source to document real controls and accurate screenshots. Describe desktop control, closing and switching windows with reader-facing instructions, not implementation jargon.

### PiForma Panel / Control Strip

Explain visually with labeled screenshots. Previous app identities include `piforma-panel`, `ControlStrip-Simulator`, `AtEase-simulator`, and `Clippy`. Historical development involved Show Desktop and window filtering so persistent shell apps remain present. No need to describe internals in a user chapter unless they affect instructions.

### The Apple-logo touch button

**Do not publish the hold timing or action map without testing the current build.** Older owner-confirmed descriptions: 1 tap Internet Explorer, 2 taps Mac OS 9, 3 taps Winamp, 4 taps RetroPie; holding several seconds closes a game/EmulationStation. A separate June 2026 software audit described more differentiated holds: approximately **2 s closes active window**, **6 s closes all windows**, **10 s shuts down**. The owner's October account describes **holding about six seconds to exit a full-screen application**, which does not fully resolve those differences. The final manual should give short, testable outcomes and not assert all versions simultaneously. Illustrate gesture press versus hold clearly. Mention that some RetroPie or emulation windows have no visible X, making this control important.

### Software and credits

Potential sources to inspect under `milagrofrost` on GitHub:

- `Macintosh-PiForma-docs` (owner preferred source of truth)
- `Macintosh-PiForma-docs-viewer`
- `AtEase-simulator`
- `piforma-panel`
- `ControlStrip-Simulator`
- `about-this-pi`

Names, capitalization, branches and current behavior should be taken from actual repos. If access fails, ask for local copies rather than fabricate app descriptions. The owner explicitly prefers **one underlying Markdown documentation source**, not duplicate and diverging hardware/software facts across apps and manual. Manual prose can be adapted for readers, but authoritative specifications should link back to or be derived from those documents.

## Chapter 4: Caring for Your Macintosh PiForma

Keep care instructions practical and occasionally wry. Cushioning is not armor. Do not slam the bag or the PiForma into surfaces. The collapsible stand may permit some side-to-side motion, so use a **solid flat table**, center the computer, and don't bump it.

The owner recommends that the battery commonly stay **above roughly 25–50%** rather than frequently running all the way down. Present that as the owner's storage/usage preference pending manufacturer-specific battery guidance, not a universally proven ideal charge percentage. It is fine to run the battery down occasionally, but avoid blanket chemical claims. Clean gently; do not use liquids or solvents inside the machine. Give applicable safe transport/charging advice only when specifications are known.

### Service and support

The desired tone is deliberately deadpan and personal, e.g. a short playful statement that the PiForma is a home-built experiment made for fun, with **absolutely no official service-and-support department**. This is not permission to dismiss safety problems. Include a practical sentence about ceasing use if the device becomes unusually hot, damaged, or behaves electrically abnormally, without pretending that any formal warranty or technical support exists.

## Appendix A: Technical Information

Deeper than Chapter 2, organized as factual tables, verified diagrams, optional pinouts and software inventory. Precise electrical and pin details may be included when authenticated against source code, schematics or physical labels. Do not create fictional circuits. Cover the keyboard BLE conversion and credit its upstream design, power and charging architecture, audio path, physical button circuitry, internal hub/USB, ports, display signal, GPIO mappings, source-selection logic, boot services, shutdown process, and documents/repo references as verified.

## Glossary

Short, useful definitions for nontechnical readers. Initial candidate terms: Apple Desktop Bus (ADB), Bluetooth LE, GPIO, Qi, USB hub, Raspberry Pi, RetroPie, emulator, AtEase, Control Strip, chime selector, Raspberry Pi OS, microSD, full-screen application. No index for first edition.
