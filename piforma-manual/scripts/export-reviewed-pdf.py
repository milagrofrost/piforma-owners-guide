"""Reviewed-proof export: images above 300 ppi on the page are resampled to 300 ppi.

The working proof keeps full-resolution artwork; source images are never changed.
"""
from pathlib import Path
import io, re
import pymupdf as pdf
from PIL import Image
P=Path(__file__).resolve().parents[1]
source=P/'output/macintosh-piforma-working-proof.pdf'; target=P/'output/macintosh-piforma-layout-reviewed.pdf'
doc=pdf.open(source)
doc.rewrite_images(dpi_threshold=320,dpi_target=300,quality=90)
# rewrite_images can store a grayscale picture as a three-channel JPEG while
# keeping its one-channel gray color space. Most viewers cope; Microsoft Edge
# reads the mismatch literally and draws the picture cropped and squashed.
# Re-encode any such JPEG with the channel count its color space declares.
for xref in range(1,doc.xref_length()):
    if doc.xref_get_key(xref,'Subtype')[1]!='/Image' or doc.xref_get_key(xref,'Filter')[1]!='/DCTDecode':continue
    picture=Image.open(io.BytesIO(doc.xref_stream_raw(xref)))
    space=doc.xref_get_key(xref,'ColorSpace')
    gray=space[1]=='/DeviceGray' or (space[0]=='xref' and 'ICCBased' in doc.xref_object(int(space[1].split()[0])) and
        doc.xref_get_key(int(re.findall(r'(\d+) 0 R',doc.xref_object(int(space[1].split()[0])))[0]),'N')[1]=='1')
    if gray and picture.mode!='L':
        out=io.BytesIO();picture.convert('L').save(out,'JPEG',quality=90)
        doc.update_stream(xref,out.getvalue(),compress=0)
        doc.xref_set_key(xref,'Filter','/DCTDecode')
# Open as a book: the cover alone, then left/right spreads, so each art page
# shows on the left facing its chapter opening on the right.
doc.set_pagelayout('TwoPageRight')
doc.save(target,garbage=4,deflate=True)
print(f'{len(doc)} pages; {source.stat().st_size/1e6:.1f} MB working proof -> {target.stat().st_size/1e6:.1f} MB reviewed export at 300 ppi.')
