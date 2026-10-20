// Generated from manuscript\07-troubleshooting.md; edit Markdown and rebuild.
#import "../styles/book.typ": *
#import "../styles/screenshots.typ": screen-figure
#import "../styles/typography.typ": accent
#para([#text("Start with what you can see and hear. Make one check at a time, then observe the result. Note any message before dismissing it. Stop using the PiForma if there is unusual heat, swelling, a hot smell or damaged power wiring; those symptoms are a reason to speak to the builder, not try another restart.")])
#block(breakable:false)[
#heading(level:2,"No green light, chime or picture")
#para([#text("Check the power switch on the right side. Press the rear battery plunger and read the battery percentage through the top slits. Plug in the power cable, then try again. Even a battery that showed full has sometimes needed a minute on power. If nothing works, ask the builder rather than opening it up.")])
]
#block(breakable:false)[
#heading(level:2,"Battery does not appear to charge")
#para([#text("Check that the power cable is plugged in at both ends. For the bag arrangement, check the rear/bottom seating in the foam indents and that the cord from the bag’s back pocket is plugged into a working USB charger. The battery display can indicate charging from the wireless receiver, but you cannot see it while the computer is packed in the bag. The only way to be sure the bag is charging is to unpack the computer and look. Don't swap in a different power supply.")])
]
#block(breakable:false)[
#heading(level:2,"Green light or chime, but no desktop")
#para([#text("Allow approximately one to two minutes for startup, with some variation. A No Signal message and a moment of blank screen are normal at first. If the startup picture doesn't follow within about 15 seconds, press the rear source selector until the screen shows HDMI. The chime plays before the computer has finished starting. If the startup picture persists, note where it stops. If the image flickers or distorts, stop using the computer; do not tap the case or adjust internal cables while powered. Ask the builder to investigate a persistent display problem.")])
]
#block(breakable:false)[
#heading(level:2,"Mouse pointer does not move")
#para([#text("Check the underside power switch and put the mouse on its pad. Keep the optical tracking window facing the pad. The mouse's USB wireless receiver is plugged into the Raspberry Pi inside the case, so there is nothing to check there without dismantling the computer. The Sync button is not part of normal setup. If the pointer works elsewhere but stays inside one emulator, it's probably trapped by that emulator; see Chapter 3.")])
]
#block(breakable:false)[
#heading(level:2,"Keyboard does not type")
#para([#text("If letters come out as capitals or the number keys type symbols, Caps Lock is down: press it again so it sits level with the other keys. Otherwise, check the switch on the right-hand edge, look at the nice!view display for battery level, an X that means it isn't connected, and profile 2 selected, and click in the intended text field. Try another available text field. The keyboard and mouse connect separately, so a working mouse says nothing about the keyboard. If typing still fails everywhere, ask the builder rather than trying guessed key combinations.")])
]
#block(breakable:false)[
#heading(level:2,"No sound, or no startup chime")
#para([#text("For normal program sound, turn the side volume control or the keyboard's volume dial up a little and check that the program has something playing and its own sound is enabled. Pressing the knob doesn't mute. Start with the volume low. If sound has been switched to the rear audio socket, it plays only through whatever is plugged in there, not the internal speaker.")])
#para([#text("For a missing startup chime, remember that some rear selector positions are silent. Turn the dial a click at a time with the power on, as Chapter 1 describes; not every position plays. The chime and normal program sound use separate hardware; one can work while the other doesn't. Describe which sound is missing before asking for help.")])
]
#block(breakable:false)[
#heading(level:2,"A website or network service will not open")
#para([#text("Try another known page or service. Check the Wi-Fi status icon at the far right of the menu bar; its menu can take 20 or 30 seconds to open. If another device on that network also fails, the problem may be outside the PiForma. Note any error message, and ask the builder if Wi-Fi won’t reconnect.")])
]
#block(breakable:false)[
#heading(level:2,"A program will not respond")
#para([#text("Wait briefly, then look for a dialog waiting behind the main window. Check whether the pointer and other applications respond. Save unaffected work if you can and try the troubled program's own Quit or close control.")])
#para([#text("If necessary, the Apple-logo hold of about six seconds closes only the active application. Check which application is active first. Unsaved work may be lost, including game progress. Use View → Show Desktop to uncover the launcher when the menu bar is accessible.")])
#para([#text("If the entire desktop remains unresponsive, use Special → Shut Down if you can reach it. Abrupt physical power-off is a last resort and may lose work or damage files. A sleeping screen is not completed shutdown. Note what was running and what stopped responding.")])
#para([#text("If the launcher or menu bar does not return after leaving a full-screen program, save accessible work and consult the builder. Do not try longer logo holds.")])
]
