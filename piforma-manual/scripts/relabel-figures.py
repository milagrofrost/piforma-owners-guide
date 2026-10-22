"""Re-set figure callout labels so they match the text's names.

Reads the original labelled pictures from assets/originals/labelled/, finds
each red leader line's label end, whites out the old label and sets the new
one in EB Garamond at a single printed size. Writes assets/illustrations/.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets/originals/labelled"
OUT = ROOT / "assets/illustrations"
FONT = Path.home() / ".local/share/fonts/EBGaramond[wght].ttf"
SIZE_PT = 7.5
INK = (40, 40, 40)

# file: (label side, pixels per printed point, labels top to bottom)
FIGURES = {
    "bag-arrangement.png": ("R", 4.25, ["Accessory Pouch", "Mouse", "Stand", "Mouse Pad",
        "Velvet Foam Board", "PiForma", "Keyboard", "Bottom Foam Insert"]),
    "1-3b.png": ("R", 4.66, ["Screen", "Apple-Logo Touch Control", "Status Light"]),
    "1-3d.png": ("L", 8.23, ["Volume Knob"]),
    "1-3e.png": ("R", 8.23, ["Power Switch"]),
    "rear-inputs.png": ("R", 4.75, ["Source Selector", "Audio Output", "RCA Video Input",
        "USB-C Port", "Battery Plunger", "Chime Selector", "AC Inlet"]),
    "1-3c.png": ("R", 6.31, ["Forbidden Latch"]),
    "1-4b.png": ("R", 4.23, ["Volume Dial", "nice!view Display", "USB-C Port", "Power Switch"]),
    "keyboard-switch-usbc.png": ("R", 4.62, ["Power Switch", "USB-C Port"]),
    "1-4c.png": ("R", 6.68, ["Left Click", "??????", "Scroll Wheel", "Sync Button"]),
    "1-4d.png": ("R", 5.65, ["Eye Correction Laser", "Power Switch", "Battery Compartment"]),
    "inside-3.png": ("L", 5.19, ["Wireless Charging Receiver", "Battery Plunger", "Battery Display"]),
}


def leader_ends(a, side):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    red = (r > 150) & (g < 120) & (b < 120) & (r - g > 60)
    lab, _ = ndimage.label(red, structure=np.ones((3, 3)))
    ends = []
    for i, sl in enumerate(ndimage.find_objects(lab)):
        ys, xs = np.nonzero(lab[sl] == i + 1)
        if len(xs) < 25:
            continue
        ys, xs = ys + sl[0].start, xs + sl[1].start
        x = xs.max() if side == "R" else xs.min()
        ends.append((int(np.median(ys[xs == x])), int(x)))
    return sorted(ends), red


def relabel(name, side, pxpt, labels):
    src = Image.open(SRC / name).convert("RGBA")
    im = Image.new("RGBA", src.size, "white")
    im.alpha_composite(src)
    im = im.convert("RGB")
    a = np.asarray(im).astype(int)
    ends, red = leader_ends(a, side)
    assert len(ends) == len(labels), (name, ends)
    avg = a.mean(axis=2)
    ink = (avg < 215) & ~red
    H, W = avg.shape
    size = round(SIZE_PT * pxpt)
    # Only labels stacked in the same column limit each other's height.
    gaps = [abs(b[0] - a_[0]) for a_, b in zip(ends, ends[1:]) if abs(b[1] - a_[1]) < 50]
    band = min([round(size * 0.9)] + [g // 2 - 1 for g in gaps])
    d = 1 if side == "R" else -1
    draw = ImageDraw.Draw(im)
    for (y, x), text in zip(ends, labels):
        y0, y1 = max(0, y - band), min(H, y + band + 1)
        c, gap, last = x + d * 2, 0, x + d * 2
        while 0 <= c < W:
            col = ink[y0:y1, c]
            if red[y0:y1, c].any():
                break
            if col.any():
                last, gap = c, 0
            else:
                gap += 1
                if gap > size * 1.2:
                    break
            c += d
        xa, xb = sorted((x + d * 2, last + d * 4))
        draw.rectangle((xa, y0, xb, y1 - 1), fill="white")
    font = ImageFont.truetype(str(FONT), size)
    # Widen the canvas if a longer label would run off the edge.
    need = []
    for (y, x), text in zip(ends, labels):
        w = draw.textlength(text, font=font)
        tx = x + d * round(size * 0.3)
        need.append(tx + w if side == "R" else tx - w)
    pad_r = max(0, int(max(need)) + 4 - W) if side == "R" else 0
    pad_l = max(0, 4 - int(min(need))) if side == "L" else 0
    if pad_r or pad_l:
        big = Image.new("RGB", (W + pad_r + pad_l, H), "white")
        big.paste(im, (pad_l, 0))
        im, draw = big, ImageDraw.Draw(big)
    for (y, x), text in zip(ends, labels):
        tx = x + pad_l + d * round(size * 0.3)
        draw.text((tx, y), text, font=font, fill=INK, anchor="lm" if side == "R" else "rm")
    im.save(OUT / name, optimize=True)
    return im.size


if __name__ == "__main__":
    for name, (side, pxpt, labels) in FIGURES.items():
        print(name, relabel(name, side, pxpt, labels))
