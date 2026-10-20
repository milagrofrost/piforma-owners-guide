"""Check high-value owner instructions against the manuscript, not word counts."""
from pathlib import Path
import json, hashlib
P=Path(__file__).resolve().parents[1]
chapter=(P/'manuscript/01-getting-started.md').read_text(encoding='utf-8')
unpack=chapter.split('## Unpacking the equipment',1)[1].split('## Taking a closer look',1)[0]
packing=chapter.split('## Packing the equipment',1)[1]
checks=[]
def check(name,ok):
    checks.append({'requirement':name,'passed':bool(ok)})
    assert ok,name
def in_order(text,needles):
    positions=[text.index(s) for s in needles];return positions==sorted(positions)
check('Exact removal sequence',in_order(unpack,['1. Remove the small brown accessory pouch','2. Take out the mouse and the collapsible','3. Lift out the mouse pad','4. Remove the velvet-covered foam board']))
check('Pouch inventory',all(s in unpack for s in ['two Nintendo 64 controllers','USB hub','power cable']))
check('Side keyboard and three orientations',all(s in unpack for s in ['not another layer','keys face the bag wall','thicker edge faces the rear','thinner edge faces the front']))
check('Handle access and alternate removal',all(s in unpack for s in ['inside front wall','top side of the PiForma','handle outward','lay the bag on its back']))
check('Startup sequence',in_order(chapter.split('## Starting up the computer',1)[1],['physical power control on the right side','green light at the front','startup chime','startup picture or sequence','one to two minutes']))
check('Battery recovery observation without guarantee',all(s in chapter for s in ['outside plunger mechanically presses','roughly a minute','battery previously showed full','do not count on one minute as a fixed recovery time']))
check('Distinct startup symptoms',all(s in chapter for s in ['If there is no green light','If the light is on but there is no chime','If the light and chime work but the screen stays blank','If the desktop is slow to appear','If it never sounds']))
check('Graceful shutdown before physical off',in_order(chapter.split('## Stopping the computer',1)[1],['Save your work','Special → Shut Down','operating system finish','turn off the right-side physical power control']))
check('Packing and charge confirmation',all(s in packing for s in ['monitor/screen facing upward','rear/bottom','molded indents','Gently shift or wiggle','does not prove that charging has started']))
check('Reverse packing order',in_order(packing,['5. Place the velvet-covered foam board','6. Put the mouse pad','7. Put the mouse and collapsible stand','8. Return the two controllers']))
check('Latest six-second owner confirmation', 'about six seconds closes only the active application on the current PiForma' in chapter)
tracker=(P/'editorial-production-tracker.md').read_text(encoding='utf-8')
check('Dedicated Bose section and externally tracked model','### Bose speakers and stands' in chapter and 'Speaker models, power requirements' in tracker)
check('Input audio direction and tracked adapter limit','external audio into the computer' in chapter and 'acceptable signal levels' in tracker)
check('Expected chapter headings',all((P/'manuscript'/name).exists() for name in ['00-front-matter.md','01-getting-started.md','02-inside-piforma.md','03-how-piforma-works.md','04-caring-for-piforma.md','05-technical-information.md','06-glossary-and-credits.md']))
check('Normal battery check uses rear plunger and slits',all(s in chapter for s in ['press the rear battery plunger','peer through the slits','do not have to open the compartment']))
opening=chapter.split('### A closer look, strictly off the record',1)[1].split('### If there is no green light',1)[0]
check('Unlock before lifting; close before locking',in_order(opening,['1. Slide the top latch toward the open-padlock','2. With the latch unlocked, lift at the slider','3. Close the compartment before sliding the latch']))
check('New setup details preserved',all(s in chapter for s in ['Seat the support leg in its final position','port and switch themselves are not visible from above','one USB wireless receiver','Eye Correction Laser','Forbidden Latch']))
software=(P/'manuscript/03-how-piforma-works.md').read_text(encoding='utf-8')
troubleshooting=(P/'manuscript/07-troubleshooting.md').read_text(encoding='utf-8')
publication='\n'.join(f.read_text(encoding='utf-8') for f in (P/'manuscript').glob('*.md'))
check('Complete first session in setup',in_order(chapter.split('## Your first session',1)[1],['Move the mouse','Find the menu bar','In AtEase','Quit or Exit','return to the launcher']))
check('Everyday operations covered',all(s in software for s in ['## Using the keyboard','## Using the mouse','## Files and folders','## Saving and reopening','## Working with application windows','## Controllers and games']))
check('No guessed operational gesture or mapper',all(s not in software for s in ['Ctrl+Esc','2/6/10','four taps','two-second hold']))
check('All requested troubleshooting areas',all(s in troubleshooting for s in ['No green light','Battery does not appear to charge','no desktop','Mouse pointer','Keyboard does not type','No sound','network service','program will not respond']))
check('Publication free of editorial placeholders',all(s not in publication for s in ['[VERIFY:','[PHOTO NEEDED','[MODEL TO CONFIRM:']))
handoff=P.parent/'PiForma_Manual_Handoff'
manifest=[{'path':str(f.relative_to(handoff)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(handoff.rglob('*')) if f.is_file()]
(P/'research/handoff-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(P/'output/editorial-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(f'{len(checks)} editorial preservation checks passed; {len(manifest)} handoff files recorded.')
