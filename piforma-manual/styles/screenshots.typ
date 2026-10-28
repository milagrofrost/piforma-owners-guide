// Screenshot viewports preserve original UI geometry; no regenerated interfaces.
#import "book.typ": content-mark, figure-anchor, caption, rail-figure
#let screen-figure(id,file,copy,width:366pt) = block(width:242pt,above:9pt,below:12pt,breakable:false)[
  #content-mark()
  #if width > 242pt {
    figure-anchor(block(width:366pt)[
      #align(center,image("../assets/screenshots/"+file,width:width))
      #caption(id,copy)
    ])
  } else {
    rail-figure(image("../assets/screenshots/"+file,width:width),copy)
  }
]
