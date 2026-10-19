// Generated from manuscript\07-troubleshooting.md; edit Markdown and rebuild.
#import "../styles/book.typ": *
#import "../styles/screenshots.typ": screen-figure
#import "../styles/typography.typ": accent
#para([#text("Start with what you can see and hear. Make one check at a time, then observe the result. Note any message before dismissing it. Stop using the PiForma if there is unusual heat, swelling, a hot smell or damaged power wiring; those symptoms are a reason to speak to the builder, not try another restart.")])
#block(breakable:false)[
#heading(level:2,"No green light, chime or picture")
#para([#text("Check the right-side physical power control. Press the rear battery plunger and read the battery percentage through the top slits. Try the intended external power connection, then retry startup. A battery that previously showed full has sometimes needed a brief power connection; Chapter 1 describes this observation without promising a recovery time. If there is still no response, stop short of internal adjustments and consult the builder.")])
]
#block(breakable:false)[
#heading(level:2,"Battery does not appear to charge")
#para([#text("Check the intended cable and external power connection without opening the computer. For the bag arrangement, check the rear/bottom seating in the foam indents and the charging cable in the back pocket. The battery display can indicate charging from the wireless receiver, but you cannot see it while the computer is packed in the bag. A USB power monitor on the bag charger's supply can show power draw, but does not directly measure charging at the battery. Without that additional evidence, whether the bag is charging remains uncertain. Do not substitute an unidentified supply.")])
]
#block(breakable:false)[
#heading(level:2,"Green light or chime, but no desktop")
#para([#text("Allow approximately one to two minutes for startup, with some variation. Check that the rear display source is set for HDMI. A chime does not prove that the computer has finished booting. If the startup picture persists, note where it stops. If the image is blank, flickers or distorts, do not tap the case or adjust internal cables while powered. Ask the builder to investigate a persistent display problem.")])
]
#block(breakable:false)[
#heading(level:2,"Mouse pointer does not move")
#para([#text("Check the underside power switch and put the mouse on its pad. Keep the optical tracking window facing the pad. Check that the mouse's USB receiver is present and seated where accessible without dismantling the computer; check any accessible hub connection. The Sync button is not part of normal setup. If the pointer works elsewhere but stays inside one emulator, it may be captured; see Chapter 3 rather than assuming the mouse has failed.")])
]
#block(breakable:false)[
#heading(level:2,"Keyboard does not type")
#para([#text("If letters come out as capitals or the number keys type symbols, Caps Lock is down: press it again so it sits level with the other keys. Otherwise, check the switch near the upper-right edge and click in the intended text field. Try another available text field. The keyboard uses Bluetooth; a working mouse does not prove that connection. If typing fails everywhere, check keyboard power, charge and connection with the builder. Use the configured pairing procedure, not guessed key combinations.")])
]
#block(breakable:false)[
#heading(level:2,"No sound, or no startup chime")
#para([#text("For normal program sound, turn the side volume control clockwise a little and check that the program has something playing and its own sound is enabled. The installed side knob has no usable push-to-mute action. Keep the initial volume modest. If sound has been switched to the rear audio socket, it plays only through whatever is plugged in there, not the internal speaker.")])
#para([#text("For a missing startup chime, remember that some rear selector positions are silent. Follow Chapter 1's powered-on selector check without expecting immediate playback at every position. The chime and normal program sound use separate hardware; hearing one does not prove that the other is working. Describe which sound is missing before asking for help.")])
]
#block(breakable:false)[
#heading(level:2,"A website or network service will not open")
#para([#text("Try another known page or service. Check the visible connection status and intended network. If another device on that network also fails, the problem may be outside the PiForma. Bluetooth and the mouse receiver do not establish Wi-Fi access. Keep error wording; ask for the installed reconnect procedure if needed.")])
]
#block(breakable:false)[
#heading(level:2,"A program will not respond")
#para([#text("Wait briefly, then look for a dialog waiting behind the main window. Check whether the pointer and other applications respond. Save unaffected work if you can and try the troubled program's own Quit or close control.")])
#para([#text("If necessary, the owner-confirmed Apple-logo hold of about six seconds closes only the active application. Check which application is active first. Unsaved work may be lost; this does not guarantee a game save. Use View → Show Desktop to uncover the launcher when the menu bar is accessible.")])
#para([#text("If the entire desktop remains unresponsive, use Special → Shut Down if you can reach it. Abrupt physical power-off is a last resort and may lose work or damage files. A sleeping screen is not completed shutdown. Note what was running and what stopped responding.")])
#para([#text("If the launcher or menu bar does not return after leaving a full-screen program, save accessible work and consult the builder. Do not try longer logo holds.")])
]
