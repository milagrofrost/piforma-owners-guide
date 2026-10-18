# Technical Information

<!-- evidence: repo-verified D-HARDWARE D-BOM D-SOFTWARE; needs-confirmation Q-POWER -->
This appendix describes the PiForma’s hardware, connections and software. Use the project documentation for maintenance and recovery instructions.

## Hardware inventory and identification

<!-- evidence: repo-verified D-HARDWARE D-BOM -->
- Donor: Apple IIc Monitor A2M4090, February 1985.
- Computer: Raspberry Pi 4 Model B, 4 GB RAM.
- Storage: 256 GB microSD.
- Display: 9-inch LCD kit, working mode 800 × 480.
- Main battery: Anker Prime 26K 300W.
- Internal charger: 100W USB-C adapter.
- Keyboard: Apple A9M0330 ADB keyboard, BLE conversion, ZMK, USB-C charging, nice!view.
- Mouse: Bambu kit electronics in a printed shell, USB receiver.
- Startup sound: YS-M3, CK1028 selector, separate salvaged speaker.
- Normal sound: internal USB speaker.

## Power architecture

<!-- evidence: repo-verified D-HARDWARE D-SAFETY -->
Power path: rear AC inlet → internal charger → main battery → original power switch → custom 5V JST rail → Pi, LCD controller, startup-chime module, and touch sensor. The USB speaker is supplied through the Pi. The switch does not disconnect the AC charging path. The rail has no separate installed fuse protection.

## Connections and GPIO

<!-- evidence: repo-verified D-GESTURE D-SOFTWARE -->
- Apple-logo sensor: TTP223 on BCM GPIO23, active-low.
- EC11 volume encoder: BCM GPIO17/27; push input GPIO22 exists in software but is not physically usable on the installed knob.
- Display source: physical switch to LCD controller source control, not a GPIO relay selector in this build.
- Composite RCA input: video only.
- External audio: USB capture source and audio-loop helper.
- External USB access: one rear port; do not infer exterior access from the Pi’s board connector count.

## Software, services and recovery

<!-- evidence: repo-verified D-SOFTWARE D-AUDIO -->
The software includes Raspberry Pi OS, X11/LXDE, Openbox, LightDM, PCManFM, PipeWire, and WirePlumber. System services include apple-gesture-button, volume-knob, atease, and flyingtoasters. User services include piforma-panel, controlstrip-simulator, and the optional usb-audio-loop.

Use the canonical repository's software page, service inventory, configuration archive and installation guide for recovery. Archived helpers describe an earlier installation; do not substitute them for deployed scripts without checking the running configuration.

## Keyboard conversion and sources

<!-- evidence: repo-verified D-HARDWARE D-BOM; historic-record H03-dosbox -->
The build credits Matt Chesters’ `zmk-apple-desktop-bus-keyboard` conversion. Special keys follow the deployed keymap.

The keyboard conversion uses a Seeed XIAO nRF52840, MCP23017 I/O expander, custom board, small battery and nice!view display.
