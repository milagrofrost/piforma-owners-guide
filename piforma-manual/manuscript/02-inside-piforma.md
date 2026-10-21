# Inside the Macintosh PiForma

<!-- evidence: repo-verified D-HARDWARE D-BOM; editorial-advice -->
The PiForma looks like a 1985 monitor, but the computer inside is entirely modern. This chapter introduces the parts and what they do. Appendix A has the finer details for anyone who wants the wiring.

## The monitor that became a computer

<!-- evidence: repo-verified D-HARDWARE -->
The case began as an Apple IIc Monitor. Its original CRT had been removed before this build. The plastic case, metal chassis, power switch, AC inlet, and rear openings were reused; the computer and screen inside are new.

This is a conversion, not a restoration of a stock Macintosh. The old case was a good place to start and a rather particular place to fit everything else.

[ILLUSTRATION 2-1|inside-1.png|The internal assembly, with the Raspberry Pi, display hardware, power adapter, 5V power rail and ordinary internal speaker identified.]

## Raspberry Pi, memory and storage

[RAIL microSD|The small storage card that holds the operating system, the programs and your files.]

<!-- evidence: repo-verified D-HARDWARE D-SOFTWARE D-BOM -->
A Raspberry Pi runs the programs. RAM holds the work the computer is doing now; the microSD storage card keeps the operating system, applications, and saved files when power is off. Saving transfers your work into a file that can remain after shutdown.

The computer runs Raspberry Pi OS beneath its Macintosh-inspired appearance. Appendix A lists the hardware and software specifications.

## The display and source selector

[RAIL Composite video|The older video signal used by VCRs and early game consoles. The RCA jack carries picture only, not sound.]

<!-- evidence: repo-verified D-HARDWARE -->
An LCD screen replaces the original monitor display. The Raspberry Pi supplies its picture over HDMI. A rear RCA input supplies composite video from an external source: a VCR, an older games console or anything else with a composite video output. Its sound comes in separately, through the external audio adapter.

<!-- evidence: owner-current OWNER-TALK-2026-10-19 -->
The screen in this first revision is, frankly, of modest quality: a little dim, with colors that are not quite right, and neither brightness nor color can be adjusted from the computer. We apologize for the economy.

<!-- evidence: owner-current OWNER-TALK-2026-10-20 -->
Each press of the rear source selector moves the screen to its next input. Only two are in use: HDMI, for the Raspberry Pi, and AV1, for the composite RCA input. The selector also passes AV2 and VGA, which had nothing connected when the PiForma was built. A small label at the top left of the screen names the current input. Press until it shows HDMI to return to the Pi’s picture.

[ILLUSTRATION 2-1b|source-cycle.png|Each press of the source selector moves the screen to its next input. HDMI shows the Raspberry Pi; AV1 shows the RCA input.]

## The battery and charging paths

<!-- evidence: repo-verified D-HARDWARE D-BOM D-SAFETY -->
The internal battery lets you use the PiForma without a power cord. The power cable feeds its charger, and the battery can charge while the computer’s physical switch is off. The switch does not disconnect the charger from external power. Appendix A describes the internal power path.

<!-- evidence: owner-current H01-battery; repo-verified D-HARDWARE; needs-confirmation Q-BATTERY -->
An external plunger reaches the battery’s own button. Press it to check the charge, and sometimes to wake the pack. The normal check is to press the rear plunger and read the percentage through the top slits. The top latch can also be unlocked and lifted for a closer look; Chapter 1 describes the optional opening procedure.

[ILLUSTRATION 2-2|inside-3.png|The open top reveals the wireless charging receiver, battery plunger and battery display. The battery is at 84 percent in this photograph. For the normal check, read through the top slits as described in Chapter 1.]

## System sound and startup chimes

<!-- evidence: repo-verified D-HARDWARE; owner-current H01-chime -->
The startup chime and ordinary system audio are separate. Ordinary sound plays through the internal speaker behind the screen or, when chosen in Sound Options, through the rear audio output socket. A separate sound module and speaker play the startup chime; the rear selector chooses among its sounds. Some positions are silent or empty.

[ILLUSTRATION 2-3|inside-2.png|A rear oblique view identifies the separate chime assembly, battery, AC power inlet, chime selector and battery-button plunger.]

#### Startup chimes

<!-- evidence: owner-current OWNER-TALK-2026-10-19 -->
Turning the selector one click at a time gives these sounds, in order:

1. The classic Macintosh startup chime.
2. An older Macintosh chime.
3. A Macintosh Plus floppy drive working at startup.
4. The Game Boy Advance startup sound.
5. The Apple II beep.
6. The PlayStation 2 startup sound.
7. A picture tube warming up.
8. The Windows 98 startup sound.
9. The two-note Windows 3.1 fanfare.

The next three clicks are silent, and the one after that brings back the classic chime.

---

Normal desktop sound uses an internal USB speaker. Its volume has nothing to do with the startup chime, which has its own hardware.

## The physical controls

<!-- evidence: owner-current H01-controls; repo-verified D-HARDWARE D-SOFTWARE -->
The right-side power switch controls the computer’s power rail. The Apple logo on the front is a touch control for shortcuts. The rear source selector chooses the LCD input, while the rear chime dial chooses the startup sound.

Turn the side volume knob clockwise to raise normal system volume and counterclockwise to lower it. Pressing the knob does nothing; it has no mute.

## Ports, wireless links and adapters

<!-- evidence: owner-current H01-usb; repo-verified D-HARDWARE D-SOFTWARE -->
One rear USB-C port is available to the user. The Raspberry Pi’s own ports are inside the case and out of reach. Use the hub for several devices, or for devices with older USB plugs.

[RAIL Bluetooth LE|Bluetooth Low Energy, the wireless link the converted keyboard uses.]

The keyboard uses Bluetooth LE and the mouse uses its USB wireless receiver, which is plugged into the Raspberry Pi inside the case and stays there. Wi-Fi and Bluetooth are handled by the operating system. External audio input uses a separate USB capture adapter and audio-loop helper, not the rear composite-video RCA jack.

## The converted Apple keyboard

<!-- evidence: repo-verified D-HARDWARE D-BOM; historic-record H03 -->
The vintage Apple keyboard has been converted to Bluetooth LE using Matt Chesters’ keyboard-conversion project. It has its own battery, a nice!view display, a volume dial on its left-hand edge, and a power switch and USB-C charging port on its right-hand edge. Appendix A and the credits identify the conversion and its source.

<!-- evidence: owner-current OWNER-TALK-2026-10-20 -->
The keyboard has been painted, not retrobrighted. Old Apple keyboards yellow with age. Today they are often bleached back to their original color, a process called retrobrighting, but in the old days the fix was a coat of paint in the nearest matching color. That is the source of the slight orange-peel texture you can feel on the case.

<!-- evidence: owner-current OWNER-TALK-2026-10-20 OWNER-IMAGES-2026-10-20 -->
The nice!view display, above the number keys, shows four things. The battery level is the keyboard’s own charge. The Bluetooth status shows an X when the keyboard isn’t connected, as in the photograph, where the PiForma was switched off; once connected, it shows a wireless symbol. The Bluetooth selector shows which of five Bluetooth profiles is in use, and the PiForma is profile 2. The graph shows your typing speed in letters per minute, not words.

[ILLUSTRATION 2-4|niceview-labeled.png|The nice!view display: battery level, Bluetooth status, Bluetooth selector and letters per minute.]

The keyboard’s small 100 mAh battery lasts a couple of weeks of being switched on with light use. When the battery level runs low, charge it from the USB-C port on the right-hand edge.

Pressing down on the display changes the Bluetooth profile, one step per press; press on its plastic surround rather than the screen. Leave it alone: there is no reason to press it unless you want the keyboard to talk to a different device, and it should stay on profile 2 for the PiForma. The 3D-printed key around the display is a little too wide for its opening, so it tends to stick down when pressed. If it does, lift it back up with a fingernail.

## The matching mouse

<!-- evidence: repo-verified D-HARDWARE -->
The matching mouse combines Bambu wireless mouse-kit electronics with a printed Retro Wireless Computer Mouse shell. The scroll wheel and axle were replaced after the original wheel broke during modification. A USB wireless receiver provides the connection to the computer.

## Bose speakers and stands

<!-- evidence: owner-current H03-bose OWNER-TALK-2026-10-19 -->
The Bose speakers are optional; the PiForma’s internal speaker works without them. Chapter 1 explains connecting and placing them.

[ILLUSTRATION 2-6|bose-technical.png|A Bose RoomMate speaker on its stand. The pair are optional, and travel outside the bag.]

## The bag and its fitted interior

<!-- evidence: owner-current OWNER-TALK-2026-10-21 -->
The PiForma travels in a waxed canvas backpack, finished with Otter Wax, so it shrugs off the weather and only looks better with age. Colorful embroidery and a set of patches give it a personality all its own. We are known for minimalist design. Here, we went a little rogue.

<!-- evidence: repo-verified D-HARDWARE; owner-current H01-packing OWNER-TALK-2026-10-21 -->
Inside, smooth green velvet holds the computer as if the two were made for each other, because they were. A corrugated-plastic liner gives the bag its shape, a foam bottom cushions it, and alignment grooves set the PiForma in exactly the right place. A wireless charging transmitter is concealed under the lining, with its cable reaching the back pocket, so the computer charges while it rests.

The foam locates the computer as well as cushioning it. The packing sequence in Chapter 1 protects the screen and puts the keyboard in its intended side position. A computer that only roughly fits won’t charge; it has to sit in the grooves.

<!-- evidence: owner-current OWNER-TALK-2026-10-21 -->
It looks right on anyone, and especially right over a tweed jacket between business trips. There is no room left for clothes. You won’t miss them. You’ll be the envy of the departure lounge.

[ILLUSTRATION 2-7|bag-portrait.png|Waxed canvas, embroidered, and fully loaded. The strap loop runs through four grommets and the clasp holds it closed.]
