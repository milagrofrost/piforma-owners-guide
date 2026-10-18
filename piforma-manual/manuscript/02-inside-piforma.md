# Inside the Macintosh PiForma

<!-- evidence: repo-verified D-HARDWARE D-BOM; editorial-advice -->
The PiForma’s familiar case is the starting point, not the specification of the computer inside it. This chapter introduces the parts and their jobs. Appendix A keeps the finer details close at hand without requiring you to read a wiring inventory before switching on.

## The monitor that became a computer

<!-- evidence: repo-verified D-HARDWARE -->
The case began as an Apple IIc Monitor. Its original CRT had been removed before this build. The plastic case, metal chassis, power switch, AC inlet, and rear openings were reused; the computer and display inside are different equipment.

This is a conversion, not a restoration of a stock Macintosh. The old case was a good place to start and a rather particular place to fit everything else.

[ILLUSTRATION 2-1|inside-1.png|The internal assembly, with the Raspberry Pi, display hardware, power adapter, 5V power rail and ordinary internal speaker identified. This is a component tour, not a disassembly procedure.]

## Raspberry Pi, memory and storage

<!-- evidence: repo-verified D-HARDWARE D-SOFTWARE D-BOM -->
A Raspberry Pi runs the programs. RAM holds the work the computer is doing now; the microSD storage card keeps the operating system, applications, and saved files when power is off. Saving transfers your work into a file that can remain after shutdown.

The computer runs Raspberry Pi OS beneath its Macintosh-inspired appearance. Appendix A lists the hardware and software specifications.

## The display and source selector

<!-- evidence: repo-verified D-HARDWARE -->
An LCD screen replaces the original monitor display. The Raspberry Pi supplies its picture over HDMI. A rear RCA input supplies composite video from an external source.

The rear physical source control cycles through HDMI, RCA, VGA, and RCA2 in the documented build. HDMI and RCA are the normally useful inputs; the existence of other controller modes does not mean that matching external sockets have been fitted. Select HDMI to return to the Pi’s picture.

## The battery and charging paths

<!-- evidence: repo-verified D-HARDWARE D-BOM D-SAFETY -->
The internal battery lets you use the PiForma without a power cord. The intended external power cable supplies its charger, and the battery can charge while the computer's physical switch is off. The switch does not disconnect the charger from external power. Appendix A describes the internal power path.

<!-- evidence: owner-current H01-battery; repo-verified D-HARDWARE; needs-confirmation Q-BATTERY -->
An external plunger reaches the battery’s own button. The owner uses it to check charge and sometimes wake the pack. The normal check is to press the rear plunger and read the percentage through the top slits. The owner has also confirmed that the top latch can be unlocked and lifted for a closer look; Chapter 1 describes the optional opening procedure.

[ILLUSTRATION 2-2|inside-3.png|The open top reveals the wireless charging receiver, battery-button plunger and battery display. The battery is at 84% in this photograph, as confirmed by the owner. Its display can also indicate charging from the wireless receiver, but is hidden while the computer is packed in the bag. For the normal check, read through the top slits as described in Chapter 1.]

## System sound and startup chimes

<!-- evidence: repo-verified D-HARDWARE; owner-current H01-chime -->
The startup chime and ordinary system audio are separate. A separate sound module and speaker play the startup chime; the rear selector chooses among its sounds. Some positions are silent or empty.

Normal desktop sound uses an internal USB speaker. Changing its software volume is not necessarily a test of the separate startup-chime hardware.

[ILLUSTRATION 2-3|inside-2.png|A rear oblique view identifies the separate chime assembly, battery, AC power inlet, chime selector and battery-button plunger. The ordinary internal speaker is shown in Figure 2-1.]

## The physical controls

<!-- evidence: owner-current H01-controls; repo-verified D-HARDWARE D-SOFTWARE -->
The right-side power switch controls the computer’s power rail. The front Apple-logo sensor supplies software gestures. The rear source selector chooses the LCD input, while the rear chime dial chooses the startup sound. They do different jobs even when the desktop is not yet visible.

Turn the side volume knob clockwise to raise normal system volume and counterclockwise to lower it. The installed knob has no usable push-to-mute action.

## Ports, wireless links and adapters

<!-- evidence: owner-current H01-usb; repo-verified D-HARDWARE D-SOFTWARE -->
One rear USB port is available to the user. The Pi board’s own connectors should not be mistaken for externally accessible ports. Use the hub for multiple peripherals.

The keyboard uses Bluetooth LE and the mouse uses its USB receiver. Wi-Fi and Bluetooth belong to the operating system’s network and device tools. External audio input uses a separate USB capture adapter and audio-loop helper, not the rear composite-video RCA jack.

## The converted Apple keyboard

<!-- evidence: repo-verified D-HARDWARE D-BOM; historic-record H03 -->
The vintage Apple keyboard has been converted to Bluetooth LE using Matt Chesters’ keyboard-conversion project. It has its own battery, USB-C charging port, nice!view display and power switch near the upper-right edge. It communicates separately from the mouse receiver. Appendix A and the credits identify the conversion and its source.

## The matching mouse

<!-- evidence: repo-verified D-HARDWARE -->
The matching mouse combines Bambu wireless mouse-kit electronics with a printed Retro Wireless Computer Mouse shell. The scroll wheel and axle were replaced after the original wheel broke during modification. A USB receiver provides the connection to the computer.

## Bose speakers and stands

<!-- evidence: owner-current H03-bose; needs-confirmation Q-BOSE -->
The two Bose speakers and their stands extend the setup beyond the internal speaker. Place them on stable supports with cables clear of the computer and its stand.

## The bag and its fitted interior

<!-- evidence: repo-verified D-HARDWARE; owner-current H01-packing -->
The carrying bag is part of the build. It has a corrugated-plastic liner, a foam bottom, green velvet, alignment grooves, and a wireless charging transmitter concealed under the lining. Its cable reaches the back pocket.

The foam locates the computer as well as cushioning it. The packing sequence in Chapter 1 protects the screen and puts the keyboard in its intended side position. A loose fit and a correctly aligned charging position are not interchangeable.
