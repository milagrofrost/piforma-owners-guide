# How the Macintosh PiForma Works

<!-- evidence: repo-verified D-SOFTWARE; editorial-advice -->
The PiForma wears a familiar face, but Raspberry Pi OS does the work underneath. This chapter explains the everyday business of pointing, typing, opening programs and keeping what you make. You need not learn the wiring to save a file.

## Finding your way around the desktop

<!-- evidence: repo-verified P-MENU A-APP D-ATEASE; editorial-advice -->
The desktop is the working screen behind your application windows. PiForma Panel supplies the menu bar at the top; AtEase is the folder-like launcher for programs. The Control Strip provides another way to open or return to programs.

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 -->
Figure 1-7 in Chapter 1 shows these parts together. The launcher has At Ease Items and sites tabs; Clippy occupies the lower-right corner. The clock appears at the upper right of the system bar.

Choose a menu by clicking its name, then click the command you want. An unavailable command may be dimmed. Read a dialog before answering: it may ask where to save a file, whether to discard changes, or whether to stop the computer.

The Macintosh appearance does not make every classic Macintosh command applicable. Use the commands shown by the running program. Its menus and the desktop's top menu bar can have different jobs.

## Using the mouse

<!-- evidence: owner-current OWNER-IMAGES-2026-10-14; editorial-advice -->
Move the mouse across its pad to move the pointer. If you reach the edge, lift the mouse, set it down nearer the center and continue. The mouse need not point at the screen; the little eye underneath follows the surface below it.

Click means press and release the left button once. A click selects an item or operates a button. Double-click means two quick clicks without moving the pointer between them; many file views use it to open an item. AtEase program buttons need only one click. Repeated clicking while a program starts can produce more windows than you intended.

To drag, point at the object, hold the left button, move the mouse, then release. Drag a window by its title bar, rather than by its contents. Dragging a file may move or copy it, so practice with windows before rearranging your work.

Roll the wheel to scroll through a longer page or list. Point over the area you want to scroll. Scroll bars provide another way to reach material outside a window's visible area.

The right button may show a menu of actions for the item under the pointer. Its behavior depends on the program. This is the mysterious “second left click” in the illustration; it is a real right button, despite our best efforts. The Sync button is unnecessary for the normal one-receiver setup.

## Using the keyboard

<!-- evidence: owner-current H01-keyboard OWNER-IMAGES-2026-10-14; editorial-advice -->
Switch the keyboard on at its upper-right edge. It uses Bluetooth, independently of the mouse's USB receiver. First click in the window or text field where you want to type. The insertion point marks where new text will go; moving the mouse pointer alone does not move it.

Use the letter, number and punctuation keys to enter text. Hold Shift while typing a letter for a capital or a key's shifted symbol. Return commonly ends a paragraph in a document; in a dialog it may accept the current choice, so read the dialog first. Use the arrow keys to move through text where the program supports them.

To replace text, select it by dragging across it, then type the replacement. Deleting selected text removes the whole selection. If you remove something by mistake, look for Undo in that application's Edit menu before doing more work.

Use an application's own Cut, Copy and Paste commands when available. Copy leaves the original selection in place; Cut removes it; Paste inserts the copied or cut material at the insertion point. Check the selection before cutting, and the insertion point before pasting.

The vintage key legends do not establish a modern shortcut map. Follow commands displayed by the program instead of assuming that an Apple-labeled key performs a particular action. Pairing and special key combinations are not covered here. If ordinary typing fails, use the keyboard checks in Appendix B.

## Opening programs with AtEase

<!-- evidence: repo-verified A-APP D-ATEASE; owner-current OWNER-TALK-2026-10-19 -->
AtEase has two folder tabs. At Ease Items holds the programs; sites holds a selection of websites the builder finds interesting, a collection still being tidied. Each tab shows only what fits in its window; there is no second page yet. Click a tab to switch between them, then click a button once. Allow time for the program to open. A launcher button starts a program; it is not the document you may later create inside it.

If application windows cover the launcher, choose View → Show Desktop from PiForma Panel. This reveals the desktop without quitting the programs. You can then select another AtEase button. If the launcher is absent rather than covered, see Appendix B.

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 -->
[SCREENSHOT 3-1|piforma-show-desktop.svg|View → Show Desktop returns you to the launcher without quitting the open applications.]

## Working with application windows

<!-- evidence: repo-verified D-SOFTWARE C-MAIN; editorial-advice -->
Several programs can be open at once. Click a window to bring it forward and direct your typing to it. Before typing a command or entering text, check that the intended window is active. An overlapping window is still open even when you can see only an edge of it.

Where a normal window has a title bar, drag it to a more useful position. Where a resize border or corner is provided, drag that border or corner to change the window's size. Some programs fix their window size or use the whole screen; those controls will not always be present.

Use a program's Quit or Exit command to leave it. A window close control closes that window, which may leave other windows from the same program running. A save question gives you a chance to keep changes; Cancel returns you to the work so you can decide.

Showing the desktop hides windows from view without saving or quitting them. Return to an open window by clicking its visible part or the appropriate Control Strip pane. Give the strip a moment to detect a newly opened program. Returning to a running program is different from deliberately opening another copy of it.

### Window controls

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 OWNER-SCREENSHOT-BRIEF -->
The themed document window in Figure 3-2 has a close control at the upper left. At the upper right, the far-right control maximizes the window; the control immediately to its left minimizes it to the Dock, or Control Strip. Minimizing puts the window out of the way while leaving it open. Use the program's Control Strip pane to return to it.

Use the controls a window actually provides. Some windows omit controls or draw them differently. Clippy's chat, for example, has its close button at the upper right. Closing a window is not the same as minimizing it; save before closing work you want to keep.

### Two menu bars, two different jobs

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 OWNER-SCREENSHOT-BRIEF -->
PiForma OS uses a persistent system menu bar at the top of the desktop. Its system commands do not change to match the active application. This differs from the classic Macintosh global application menu bar, whose contents follow the active program.

Individual programs can provide application-local menu bars inside their own windows. For document work, use that application's own File → Save, Edit → Copy, Edit → Paste, and other available commands. The top system File menu and a document window's File menu have different jobs. Be sure you are opening the one you mean.

[SCREENSHOT 3-2|piforma-application-menus.svg|The persistent system menu bar remains above the document window. Use the application's own File menu for Save and its other document commands. The themed window's close control is at upper left; minimize and maximize are at upper right.]

## Files and folders

<!-- evidence: repo-verified P-MENU P-ACTIONS D-SOFTWARE; editorial-advice -->
A file holds something the computer can keep: a document, picture, sound or other information. A folder groups files and other folders. A program is the tool you use; the document is the work you keep. Closing the tool does not substitute for saving the work.

PiForma Panel's File → Open Home Folder opens your home folder in a file window. Browse by opening the folders shown there. Many file views open a folder or file with a double-click; use the view's Open command if its click setting differs. Opening a document starts the associated program when an association is available. An unfamiliar file type may instead ask which program to use.

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 -->
[SCREENSHOT 3-3a|piforma-open-home-folder.svg|Use the system File menu's Open Home Folder command to reach your files.]

[SCREENSHOT 3-3b|piforma-home-folder.svg|The home-folder window lists files and folders and has its own menu bar. The contents shown belong to this captured session; your list may differ.]

Keep related work in a folder you can recognize. Give documents meaningful names and note which folder contains them. Before moving, renaming or deleting a file, close it in its program and make sure you know which item is selected. Leave unfamiliar system and application files alone.

Moving a file changes where you find it; copying leaves another copy. Neither should be confused with saving edits in an open document. The PiForma has no backup arrangement for its microSD card, and management prefers not to discuss it. The build is documented well enough to rebuild from scratch if the card ever fails, but your own files would not survive that. Copy any work you value to a USB drive or another computer. Two copies on the same card do not protect against failure of that card.

## Saving and reopening your work

<!-- evidence: editorial-advice -->
Programs do not all save in the same way. Use this sequence in a document application that offers Save and Open commands; a web page or game may use a different system.

1. Choose Save from the application's own menu. On the first save, it will usually ask for a name and location.
2. Select a folder you can find again, enter a useful filename, and confirm with the dialog's Save control. Keep the format or filename extension the program supplies unless you understand the alternative.
3. If warned that a file already exists, check its name and folder. Replacing it may overwrite earlier work. Cancel and choose a different name if you want both versions.
4. After further changes, use Save again. Where offered, Save As lets you choose another name or location; read the dialog to see which copy you will be editing afterward.
5. To return later, use the application's Open command and find the saved file, or open the file from its folder. Check that the expected work appears.

Save periodically and before quitting or shutting down. A failed save, an error message or a dialog still waiting for an answer means you should check the result before closing. Where practical, reopen an important file to verify it. Do not assume an automatic save exists merely because no one has asked you to save yet.

## The menu bar and Control Strip

<!-- evidence: repo-verified P-MENU P-ACTIONS C-README C-MAIN -->
Apple menu → About This PiForma opens system information. View → Show Desktop reveals the desktop. Special → Shut Down requests an operating-system shutdown; Special → Sleep Display only blanks or sleeps the display. A sleeping screen is not a stopped computer.

The Control Strip sits at the bottom-left in the documented desktop arrangement. Click a configured program's pane to launch it when closed or return to its detected windows when open. Some running programs appear as temporary panes. Use the ordinary pane action; window-list details can differ between versions.

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 -->
[SCREENSHOT 3-4|piforma-control-strip.svg|The Control Strip at lower left, with a window popup visible above it. The rest of the desktop is omitted so the strip can be read clearly.]

## Controllers and games

<!-- evidence: owner-current H01-usb; repo-verified D-SOFTWARE D-MAINTENANCE; editorial-advice -->
The accessory pouch holds two Nintendo 64 controllers. The rear USB port and hub provide external USB connections. A controller with a different plug needs its matching supplied adapter; the shape of the controller does not establish its connection. Do not force a plug or substitute an unidentified adapter.

<!-- evidence: owner-current OWNER-IMAGES-2026-10-18 -->
[ILLUSTRATION 3-5a|piforma-n64.png|Two Nintendo 64 controllers and a racing game on the PiForma screen.]

Open RetroPie/EmulationStation from AtEase to reach the game collection. Use the controls shown by the launcher to choose a system and game. Follow the game's own instructions for play. Controller assignments, player order and button meanings can differ between games; a button's label is not a universal promise about its action.

Before settling into a game, find out how that game pauses, saves and exits. Use the game's visible menu or established instructions. If a controller-configuration prompt appears, read it before proceeding; do not overwrite an existing setup merely to dismiss the prompt. If there are no usable prompts or known controls, ask the builder to identify the configured bindings.

<!-- evidence: owner-current OWNER-IMAGES-2026-10-18 -->
[SCREENSHOT 3-5b|piforma-emulationstation-n64.svg|EmulationStation's Nintendo 64 game list. The bar along the bottom names the buttons for this screen, including A to launch the highlighted game and B to go back.]

A game's own save and an emulator's save state are different facilities. Use only a save facility the running game or emulator actually provides, and check that it reports success. Closing a game from outside does not guarantee a saved game or state.

## Leaving a full-screen program

<!-- evidence: owner-current OWNER-UPDATE-1; editorial-advice -->
A full-screen game can cover the menu bar and window controls. First use its own Quit or Exit command when available. Save before leaving whenever the program allows it.

On the current PiForma, holding the Apple-logo touch control for about six seconds closes only the active application. Use this confirmed action when you need to leave a full-screen application without an accessible close control. It does not close everything or replace normal shutdown. Unsaved work may be lost.

<!-- evidence: owner-current OWNER-IMAGES-2026-10-19 -->
[ILLUSTRATION 3-6a|closing-app-1.png|An application that has stopped responding, showing only the busy watch.]

[ILLUSTRATION 3-6b|closing-app-2.png|Touch and hold the Apple logo for about six seconds to close the active application.]

<!-- evidence: owner-current OWNER-TALK-2026-10-19 -->
The same hold is how you quit a game. The Nintendo 64 controllers use every button, so none is set aside for quitting. Hold the Apple logo for about six seconds: the game closes and EmulationStation returns. To leave EmulationStation too, hold the logo for another six seconds; EmulationStation closes and the desktop returns.

Some emulators capture the mouse so the pointer stays inside their display. Use that emulator's documented release control if known. This guide supplies no unverified keyboard shortcut for releasing it. If you cannot regain control, follow the frozen-application checks in Appendix B.

## Diversions


<!-- evidence: repo-verified D-SOFTWARE D-RELATED -->
The project includes a browser and a collection of themed diversions, with Clippy, Weather Channel, Flying Toasters and music-player experiments among them. Use the labels in your installed launcher. A familiar old name may open a modern program or themed web application rather than the original software. The costume department has been busy.

<!-- evidence: owner-current OWNER-TALK-2026-10-19 -->
The browser is Chromium, dressed as Netscape Navigator; its AtEase button carries the Netscape name. Browser links and pages use their own controls. Enter an address in the browser's address field when you want a particular site; use the page's links to follow its contents. Online material needs a working network connection. Locally supplied diversions and documents may remain available without one.

<!-- evidence: owner-current OWNER-IMAGES-2026-10-18 -->
A few of the diversions are shown here: Winamp and its playlist, LimeWire Simulator, the Weather Channel and the Flying Toasters.

<!-- evidence: owner-current OWNER-TALK-2026-10-19 -->
Winamp is the QMMP music player wearing a Winamp skin. It plays the songs in the Music folder in your home folder; to add more, copy them into that folder. The Weather Channel estimates your location from your internet connection and shows the nearest weather station. The Flying Toasters are a screen saver you start yourself. Because the animation works the computer hard, they never start on their own when the computer is idle. To stop them, hold the Apple logo for about six seconds.

[SCREENSHOT 3-7a|piforma-winamp.svg|Winamp and its playlist window open over the AtEase launcher.]

[SCREENSHOT 3-7b|piforma-limewire-simulator.svg|LimeWire Simulator, a period-styled take on the old file-sharing program.]

[SCREENSHOT 3-7c|piforma-weatherstar.svg|The Weather Channel diversion showing current conditions in WeatherStar 4000+ style.]

[SCREENSHOT 3-7d|piforma-flying-toasters.svg|The Flying Toasters, airborne.]

## Clippy

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 -->
Clippy is the assistant at the lower-right corner of the desktop. In the Chat with Clippy window, click the message field, type your question, then press Enter or click Send. The field itself reminds you how to send. Read the reply in the conversation area; use its scroll bar to revisit a longer conversation.

[SCREENSHOT 3-8a|piforma-clippy-message-entry.svg|Enter a question in the message field, then press Enter or click Send.]

Clippy can offer suggestions, but check them against the PiForma's actual setup before changing settings or installing anything. He is enthusiastic. We have given him his own corner of the screen, which has only encouraged him.

[SCREENSHOT 3-8b|piforma-clippy-conversation.svg|An example Chat with Clippy conversation. Its suggestions should be checked against the actual PiForma setup.]

## About This PiForma and the project guide

<!-- evidence: repo-verified ABOUT-README ABOUT-CONFIG VIEWER-README VIEWER-STACKS -->
About This PiForma displays computer and operating-system information. Open it from the Apple menu. It is useful when describing the machine to the builder, but it is not the same program as Macintosh PiForma Docs Viewer.

Docs Viewer presents the project's hardware, software, maintenance and other documents. Its Update Stack action checks for updated documentation. If an update fails, the viewer keeps its previous cached material; without a cache it can use its bundled offline snapshot. An offline document is useful, but its age still matters when comparing it with a changed machine.

<!-- evidence: owner-current OWNER-SCREENSHOTS-1-11 -->
The installed launcher calls this application PiForma Guide, and its window is titled Macintosh PiForma Guided Tour. Click PiForma Guide in AtEase, then choose a stack such as Meet PiForma, Hardware or Software to begin reading. It is the built-in guide to the computer and its functions. The bottom line reports documentation status and identifies the snapshot; it is worth checking when the machine and a document seem to disagree.

[SCREENSHOT 3-9|piforma-guide-application.svg|PiForma Guide opens Macintosh PiForma Guided Tour. Choose a documentation stack; the bottom line shows documentation status and the snapshot information.]

## Wi-Fi and Bluetooth

<!-- evidence: repo-verified D-SOFTWARE; editorial-advice -->
Wi-Fi connects the computer to a wireless network. Bluetooth connects devices such as the keyboard. The mouse's USB receiver is a third, separate connection. A working keyboard does not prove that a website can be reached, and a lost internet connection does not mean the mouse needs pairing.

Use only a network you are authorized to join, with its correct name and password. Network menus depend on the installed desktop configuration; this guide does not specify an unconfirmed menu path or pairing sequence. For a failed connection, use Appendix B before changing saved settings.

## Ending a session

<!-- evidence: owner-current H01-shutdown; repo-verified P-MENU P-POWER -->
Save in each application, leave games and programs using their own exit commands, then choose Special → Shut Down. Let the operating system finish before switching off physical power, as described in Chapter 1. A menu disappearing or the display going dark is not by itself proof of completion. If a shutdown error appears, keep its wording for the builder.
