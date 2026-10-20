"""Reviewed-proof export: images above 300 ppi on the page are resampled to 300 ppi.

The working proof keeps full-resolution artwork; source images are never changed.
"""
from pathlib import Path
import pymupdf as pdf
P=Path(__file__).resolve().parents[1]
source=P/'output/macintosh-piforma-working-proof.pdf'; target=P/'output/macintosh-piforma-layout-reviewed.pdf'
doc=pdf.open(source)
doc.rewrite_images(dpi_threshold=320,dpi_target=300,quality=90)
# Open as a book: the cover alone, then left/right spreads, so each art page
# shows on the left facing its chapter opening on the right.
doc.set_pagelayout('TwoPageRight')
doc.save(target,garbage=4,deflate=True)
print(f'{len(doc)} pages; {source.stat().st_size/1e6:.1f} MB working proof -> {target.stat().st_size/1e6:.1f} MB reviewed export at 300 ppi.')
