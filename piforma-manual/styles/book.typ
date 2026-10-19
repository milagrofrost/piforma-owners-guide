#import "typography.typ": ink, accent, quiet, manual-font
#let current-title = state("book-running-title", "Macintosh PiForma")
#let phase = state("book-phase", "front")
#let chapter-number = state("book-chapter", 1)
#let content-mark() = metadata("printed-content")
#let folio() = context {
  let populated = query(metadata.where(value:"printed-content")).any(m => m.location().page() == here().page())
  let n = counter(page).get().first()
  let display-number = if phase.get() == "front" { numbering("i", n) } else { str(n) }
  let odd = calc.odd(n)
  if not populated { none } else if odd {
    align(right, text(size:8pt)[#current-title.get() #h(12pt) #display-number])
  } else {
    place(left, dx:-125pt, text(size:8pt)[#display-number #h(28pt) #current-title.get()])
  }
}
#let book(content) = {
  set document(title: "Macintosh PiForma Owner’s Guide — Working Proof", author: "Macintosh PiForma")
  set page(width:432pt,height:522pt,margin:(left:152pt,right:38pt,top:39pt,bottom:43pt),footer:folio(),footer-descent:17pt)
  set text(font:manual-font,size:10.5pt,fill:ink,lang:"en")
  set par(leading:4.5pt,spacing:7pt,justify:false)
  set text(hyphenate:false)
  set list(marker:rect(width:3pt,height:3pt,fill:accent,stroke:none),indent:0pt,body-indent:10pt,spacing:6pt)
  set enum(indent:0pt,body-indent:13pt,spacing:7pt)
  show heading.where(level:1): it => {
    set par(leading:10pt)
    block(breakable:false,sticky:true,below:15pt,
      stack(dir:ttb,spacing:4pt,[#content-mark()#line(length:242pt,stroke:1.8pt+accent)],
        block(width:242pt,text(size:15pt,weight:"bold",it.body))))
  }
  show heading.where(level:2): it => {
    block(above:13pt,below:8pt,breakable:false,sticky:true,
      stack(dir:ttb,spacing:4pt,[#content-mark()#line(length:242pt,stroke:1.4pt+accent)],
      text(size:12pt,weight:"bold",it.body)))
  }
  show heading.where(level:3): it => block(above:10pt,below:6pt,sticky:true,[#content-mark()#text(size:10.5pt,weight:"bold",it.body)])
  content
}
#let para(copy,width:242pt) = block(width:width,above:0pt,below:12pt,breakable:false,
  [#content-mark()#copy])
#let subhead(title) = heading(level:3,outlined:false,title)
#let instruction(n,copy) = block(above:0pt,below:8pt,breakable:false)[
  #content-mark()
  #grid(columns:(13pt,229pt),gutter:0pt,
    text(fill:accent,weight:"bold",str(n)+"."),
    block(width:229pt,copy))
]
#let bullet(copy) = block(above:0pt,below:8pt,breakable:false)[
  #content-mark()
  #grid(columns:(10pt,232pt),gutter:0pt,
    box(inset:(top:4pt),rect(width:3pt,height:3pt,fill:accent,stroke:none)),
    block(width:232pt,copy))
]
#let spec-row(label,copy) = block(width:354pt,above:0pt,below:6pt,breakable:false)[
  #content-mark()
  #set text(size:10pt)
  #grid(columns:(91pt,251pt),gutter:12pt,
    text(weight:"bold",label),copy)
]
#let glossary-term(title) = subhead(title)
#let side-note(label,copy) = block(above:7pt,below:9pt,breakable:false)[
  #place(top+left,dx:-112pt,block(width:96pt)[
    #line(length:96pt,stroke:.55pt+accent)
    #text(size:8.5pt,weight:"bold",label)
  ])
  #para(text(size:9pt,copy))
]
#let important(copy) = side-note("△ Important",copy)
#let warning(copy) = side-note("△ Warning",copy)
#let contents() = {
  set text(size:9.5pt)
  set par(leading:4.5pt,spacing:3pt)
  set outline.entry(fill:none)
  show outline.entry: it => {
    if it.level == 1 and it.element.body == [How the Macintosh PiForma Works] { pagebreak() }
    [#content-mark()#text(weight:if it.level == 1 { "bold" } else { "regular" },it)]
  }
  outline(title:[Contents],depth:2,indent:8pt)
}
#let caption(id,copy,width:366pt) = block(width:width,above:4pt,below:0pt,breakable:false)[
  #content-mark()
  #set text(size:8pt)
  #set par(leading:4.2pt,spacing:0pt,justify:false)
  #text([Figure #id. #copy])
]
#let figure-anchor(body) = context {
  let odd = calc.odd(here().page())
  move(dx:if odd { -112pt } else { -126pt },body)
}
#let figure-image(file,width,trim:none) = {
  if trim == none { image("../assets/illustrations/"+file,width:width) }
  else {
    // Remove only measured empty canvas above/below the two side views.
    // The source PNG and the aspect ratio of every depicted object stay intact.
    image("../assets/illustrations/"+file,width:width,
      height:width*(trim.bottom - trim.top)/trim.source_width,fit:"cover")
  }
}
#let figure-slot(id,copy) = block(above:9pt,below:12pt,breakable:false)[
  #rect(width:100%,height:64pt,stroke:.45pt+rgb("999999"),fill:none)[
    #align(center+horizon,text(size:8pt,fill:rgb("666666"))[PHOTO NEEDED · #id])
  ]
  #v(4pt)
  #para(text(size:8pt)[Figure #id. #copy])
]
#let wide-illustration(id,file,copy,width:366pt) = block(width:242pt,above:8pt,below:10pt,breakable:false)[
  #content-mark()
  #figure-anchor(block(width:366pt)[
    #align(center,image("../assets/illustrations/" + file,width:width))
    #caption(id,copy)
  ])
]
#let figure-group(items,mode:"columns") = block(width:242pt,above:6pt,below:8pt,breakable:false)[
  #content-mark()
  #figure-anchor(block(width:366pt)[
    #if mode == "columns" {
      grid(columns:(176pt,176pt),column-gutter:14pt,
        ..items.map(a => block(width:176pt)[
          #figure-image(a.file,a.width,trim:a.at("trim",default:none))
          #caption(a.id,a.caption,width:176pt)
        ]))
    } else {
      stack(dir:ttb,spacing:6pt,..items.map(a => block(width:366pt)[
        #align(center,figure-image(a.file,a.width,trim:a.at("trim",default:none)))
        #caption(a.id,a.caption)
      ]))
    }
  ])
]
#let annotated(label,note,body) = block(width:242pt,above:3pt,below:10pt,breakable:false)[
  #content-mark()
  #move(dx:-112pt,block(width:354pt)[
    #grid(columns:(96pt,242pt),column-gutter:16pt,
      block[
        #set text(size:8.5pt)
        #set par(leading:4.5pt,spacing:5pt)
        #text(weight:"bold",label)
        #if note != none { v(5pt); note }
      ],body)
  ])
]
#let reference-plate(body) = block(width:242pt,above:10pt,below:12pt,breakable:false)[
  #content-mark()
  #move(dx:-112pt,block(width:354pt,body))
]
#let illustration-plate(id,file,copy,width:320pt) = {
  pagebreak(weak:true)
  content-mark()
  place(top+left,dx:-112pt,block(width:96pt,text(size:11pt,weight:"bold")[Unpacking the equipment]))
  line(length:242pt,stroke:1.3pt+accent)
  v(22pt)
  wide-illustration(id,file,copy,width:width)
  pagebreak()
}
#let launcher-detail() = block(above:7pt,below:9pt,breakable:false)[
  #content-mark()
  #image("../assets/screenshots/atease-detail.svg",width:242pt)
  #caption("1-7 detail","AtEase folder tabs and program buttons.",width:242pt)
]
#let verification(copy) = block(above:5pt,below:10pt,breakable:false)[
  #place(top+left,dx:-65pt,dy:2pt,polygon((0pt,6pt),(3pt,0pt),(6pt,6pt),fill:none,stroke:.45pt+accent))
  #place(top+left,dx:-53pt,block(width:48pt,text(size:8.5pt,weight:"bold")[Verify]))
  #para(text(size:8.5pt)[#copy])
]
#let chapter(n,title,body) = {
  pagebreak(to:"odd")
  if n == 1 { counter(page).update(1) }
  phase.update("body")
  chapter-number.update(n)
  current-title.update("Chapter " + str(n) + ": " + title)
  place(top+left,dx:-112pt,text(size:7pt,tracking:10pt)[CHAPTER])
  place(top+left,dx:23pt,text(size:7pt)[#n])
  v(10pt)
  heading(level:1,title)
  v(123pt)
  body
}
#let opener(copy) = {
  let initial = copy.first()
  block(breakable:false)[
    #place(top+left,dx:-15pt,dy:-17pt,text(size:35pt,fill:quiet,initial))
    #pad(left:12pt,para(copy.slice(1),width:230pt))
  ]
  // Give each chapter a quiet opening leaf, rather than starting the next
  // procedure in whatever small space remains beneath its introduction.
  context {
    if chapter-number.get() == 1 {
      place(top+left,dx:-136pt,dy:267pt,image("../assets/illustrations/piforma-bw.png",width:200pt))
    }
  }
  pagebreak()
}
#let front(title,body) = {
  pagebreak()
  current-title.update(title)
  heading(level:1,title)
  body
}
#let end-section(title,body) = {
  pagebreak(to:"odd")
  current-title.update(title)
  heading(level:1,title)
  body
}
#let cover() = {
  set page(margin:0pt,footer:none)
  place(top+left,dx:84pt,dy:28pt,text(size:22pt,fill:rgb("777772"))[Macintosh PiForma])
  place(top+left,dx:84pt,dy:60pt,text(size:22pt,fill:rgb("777772"))[Owner’s Guide])
  place(top+left,dx:105pt,dy:218pt,image("../assets/illustrations/piforma-cover.png",width:290pt))
  place(top+left,dx:84pt,dy:477pt,text(size:8pt)[Working manuscript proof · October 19, 2026])
}
#let cover-reverse() = {
  set page(margin:0pt,footer:none)
  pagebreak()
  place(top+left,metadata("intentional-cover-reverse"))
}
