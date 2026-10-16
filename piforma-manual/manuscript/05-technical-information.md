# Technical Information

<!-- evidence: repo-verified D-HARDWARE D-BOM D-SOFTWARE; needs-confirmation Q-POWER -->
This appendix summarizes the inspected project records. It is not a wiring plan or a certification. Compare identifying labels and the running configuration before using it as a current-device specification.

## Hardware inventory and identification

<!-- evidence: repo-verified D-HARDWARE D-BOM -->
- Donor: Apple IIc Monitor A2M4090, recorded February 1985.
- Computer: Raspberry Pi 4 Model B, recorded 4 GB RAM.
- Storage: recorded 256 GB microSD.
- Display: recorded 9-inch LCD kit, working mode 800 × 480.
- Main battery: recorded Anker Prime 26K 300W.
- Internal charger: recorded 100W USB-C adapter.
- Keyboard: recorded Apple A9M0330 ADB keyboard, BLE conversion, ZMK, USB-C charging, nice!view.
- Mouse: recorded Bambu kit electronics in a printed shell, USB receiver.
- Startup sound: recorded YS-M3, CK1028 selector, separate salvaged speaker.
- Normal sound: recorded internal USB speaker.

## Recorded power architecture

<!-- evidence: repo-verified D-HARDWARE D-SAFETY -->
Recorded path: rear AC inlet → internal charger → main battery → original power switch → custom 5V JST rail → Pi, LCD controller, startup-chime module, and touch sensor. The USB speaker is supplied through the Pi. The switch does not disconnect the AC charging path. The rail has no separate installed fuse protection in the records.

## Connections and GPIO

<!-- evidence: repo-verified D-GESTURE D-SOFTWARE -->
- Apple-logo sensor: recorded TTP223 on BCM GPIO23, active-low.
- EC11 volume encoder: recorded BCM GPIO17/27; push input GPIO22 exists in software but is not physically usable in the installed-knob record.
- Display source: physical switch to LCD controller source control, not a GPIO relay selector in the final record.
- Composite RCA input: video only.
- External audio: USB capture source and audio-loop helper.
- External USB access: one rear port in the owner’s current account; do not infer exterior access from the Pi’s board connector count.

## Software, services and recovery records

<!-- evidence: repo-verified D-SOFTWARE D-AUDIO -->
The canonical software page records Raspberry Pi OS, X11/LXDE, Openbox, LightDM, PCManFM, PipeWire, and WirePlumber. System services include apple-gesture-button, volume-knob, atease, and flyingtoasters. User services include piforma-panel, controlstrip-simulator, and the optional usb-audio-loop.

Use the canonical repository's software page, service inventory, configuration archive and installation guide for recovery. Archived helpers describe a recorded installation; do not substitute them for deployed scripts without checking the running configuration.

## Keyboard conversion and source records

<!-- evidence: repo-verified D-HARDWARE D-BOM; historic-record H03-dosbox -->
The build credits Matt Chesters’ `zmk-apple-desktop-bus-keyboard` conversion. Special keys follow the deployed keymap.

The keyboard conversion records list a Seeed XIAO nRF52840, MCP23017 I/O expander, custom board, small battery and nice!view display.
