# When Something Goes Wrong

<!-- evidence: owner-current H01-troubleshooting H01-battery H01-chime OWNER-UPDATE-1; repo-verified D-HARDWARE D-KNOWN D-SOFTWARE; editorial-advice -->
Start with what you can see and hear. Make one check at a time, then observe the result. Note any message before dismissing it. Stop using the PiForma if there is unusual heat, swelling, a hot smell or damaged power wiring; those symptoms are a reason to speak to the builder, not try another restart.

## No green light, chime or picture

Check the right-side physical power control. Press the rear battery plunger and read the battery percentage through the top slits. Try the intended external power connection, then retry startup. A battery that previously showed full has sometimes needed a brief power connection; Chapter 1 describes this observation without promising a recovery time. If there is still no response, stop short of internal adjustments and consult the builder.

## Battery does not appear to charge

Check the intended cable and external power connection without opening the computer. For the bag arrangement, check the rear/bottom seating in the foam indents and the charging cable in the back pocket. The battery display can indicate charging from the wireless receiver, but you cannot see it while the computer is packed in the bag. Check that the cord from the bag’s back pocket is plugged into a working USB charger. Whether the bag is charging remains uncertain until you unpack the computer and look. Do not substitute an unidentified supply.

## Green light or chime, but no desktop

Allow approximately one to two minutes for startup, with some variation. A No Signal message and a moment of blank screen are normal at first. If the startup picture doesn't follow within about 15 seconds, press the rear source selector until the screen shows HDMI. A chime does not prove that the computer has finished booting. If the startup picture persists, note where it stops. If the image is blank, flickers or distorts, stop using the computer; do not tap the case or adjust internal cables while powered. Ask the builder to investigate a persistent display problem.

## Mouse pointer does not move

Check the underside power switch and put the mouse on its pad. Keep the optical tracking window facing the pad. The mouse's USB wireless receiver is plugged into the Raspberry Pi inside the case, so there is nothing to check there without dismantling the computer. The Sync button is not part of normal setup. If the pointer works elsewhere but stays inside one emulator, it may be captured; see Chapter 3 rather than assuming the mouse has failed.

## Keyboard does not type

If letters come out as capitals or the number keys type symbols, Caps Lock is down: press it again so it sits level with the other keys. Otherwise, check the switch on the right-hand edge, look at the nice!view display for battery level and an X that means it isn't connected, and click in the intended text field. Try another available text field. The keyboard uses Bluetooth; a working mouse does not prove that connection. If typing fails everywhere, check keyboard power, charge and connection with the builder. Use the configured pairing procedure, not guessed key combinations.

## No sound, or no startup chime

For normal program sound, turn the side volume control or the keyboard's volume dial up a little and check that the program has something playing and its own sound is enabled. The installed side knob has no usable push-to-mute action. Keep the initial volume modest. If sound has been switched to the rear audio socket, it plays only through whatever is plugged in there, not the internal speaker.

For a missing startup chime, remember that some rear selector positions are silent. Follow Chapter 1's powered-on selector check without expecting immediate playback at every position. The chime and normal program sound use separate hardware; hearing one does not prove that the other is working. Describe which sound is missing before asking for help.

## A website or network service will not open

Try another known page or service. Check the Wi-Fi status icon at the far right of the menu bar; its menu can take 20 or 30 seconds to open. If another device on that network also fails, the problem may be outside the PiForma. Bluetooth and the mouse receiver do not establish Wi-Fi access. Keep error wording; ask for the installed reconnect procedure if needed.

## A program will not respond

Wait briefly, then look for a dialog waiting behind the main window. Check whether the pointer and other applications respond. Save unaffected work if you can and try the troubled program's own Quit or close control.

If necessary, the Apple-logo hold of about six seconds closes only the active application. Check which application is active first. Unsaved work may be lost; this does not guarantee a game save. Use View → Show Desktop to uncover the launcher when the menu bar is accessible.

If the entire desktop remains unresponsive, use Special → Shut Down if you can reach it. Abrupt physical power-off is a last resort and may lose work or damage files. A sleeping screen is not completed shutdown. Note what was running and what stopped responding.

If the launcher or menu bar does not return after leaving a full-screen program, save accessible work and consult the builder. Do not try longer logo holds.
