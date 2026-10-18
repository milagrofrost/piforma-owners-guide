// Standalone art-direction study. Does not import or modify production styles.
#let copy = json("selected-copy.json")
#let red = rgb("ed493c")
#let ink = rgb("242424")
#set document(title:"Macintosh PiForma — Six-page design study",author:"Macintosh PiForma")
#set page(width:432pt,height:522pt,margin:0pt)
#set text(font:"EB Garamond",size:10.5pt,fill:ink,hyphenate:false)
#set par(leading:6pt,spacing:7pt,justify:false)
#let at(x,y,w,body) = place(top+left,dx:x,dy:y,block(width:w,body))
#let body(x,y,copy,w:242pt) = at(x,y,w,copy)
#let rule(x,y,w:242pt) = at(x,y,w,line(length:w,stroke:1.3pt+red))
#let head(title,x:152pt,y:42pt,w:242pt) = {
  rule(x,y,w:w)
  at(x,y+6pt,w,text(size:15pt,weight:"bold",title))
}
#let note(label,copy,x:40pt,y:100pt) = at(x,y,96pt)[
  #set text(size:8.5pt)
  #set par(leading:4.5pt,spacing:5pt)
  #text(weight:"bold",label)
  #v(5pt)
  #copy
]
#let cap(id,copy,x:40pt,y:400pt,w:354pt) = at(x,y,w)[
  #set text(size:8pt)
  #set par(leading:4.2pt,spacing:0pt)
  #text(weight:"bold",[Figure #id.]) #copy
]
#let art(file,x,y,w) = at(x,y,w,image("../assets/illustrations/"+file,width:w))
#let folio(n,title) = {
  if calc.odd(n) {
    at(152pt,494pt,242pt,align(right,text(size:8pt)[#title #h(12pt) #n]))
  } else {
    at(40pt,494pt,354pt,text(size:8pt)[#n #h(26pt) #title])
  }
}
#let step(n,copy,x:152pt,y:75pt,w:242pt) = at(x,y,w,grid(columns:(13pt,w - 13pt),text(fill:red,weight:"bold",str(n)+"."),copy))

// 1. Chapter opening: a title horizon, pause, then first-person voice;
// the true front drawing occupies the open corner rather than a text row.
#let chapter-opening(intro:copy.intro,lead:copy.unpack_intro) = {
  at(40pt,43pt,110pt,text(size:7pt,tracking:3pt)[CHAPTER 1])
  head("Getting Started",y:42pt)
  art("1-3b.png",26pt,319pt,184pt)
  at(141pt,210pt,30pt,text(size:35pt,fill:rgb("b8b6ae"))[T])
  body(164pt,223pt,intro.slice(1),w:230pt)
  body(152pt,445pt,lead)
  folio(1,"Getting Started")
}

// 2. Text-led instruction: stable reading column; genuine secondary prose
// becomes a parallel note, not a label stranded next to body copy.
#let text-instructions(steps:copy.startup_steps,caution:copy.silent_note,battery:copy.battery) = {
  head("Starting up the computer")
  for (i,y) in (80pt,116pt,142pt,190pt).enumerate() {
    step(i+1,steps.at(i).replace(regex("^[0-9]+\\. "),""),y:y)
  }
  note("The startup chime",caution,y:142pt)
  at(152pt,255pt,242pt,text(size:12pt,weight:"bold")[Checking the battery])
  body(152pt,281pt,battery.at(0))
  body(152pt,365pt,battery.at(1))
  folio(2,"Getting Started")
}

// 3. Illustration-led plate: the bag owns the page. Existing caption
// becomes a useful marginal explanation; no new packing sequence is invented.
#let packing-plate(file:"bag-arrangement.png",caption:copy.bag_caption) = {
  at(40pt,43pt,96pt,text(size:11pt,weight:"bold")[Unpacking the equipment])
  rule(152pt,42pt)
  art(file,66pt,82pt,320pt)
  cap("1-1",caption,x:40pt,y:444pt,w:354pt)
  folio(3,"Getting Started")
}

// 4. Grouped controls: two views form a deliberate visual unit;
// the paragraph works as the bridge between the component and the owner.
#let grouped-controls(intro:copy.controls_intro) = {
  head("Taking a closer look")
  body(152pt,80pt,intro)
  art("1-3d.png",40pt,231pt,170pt)
  art("1-3e.png",224pt,231pt,170pt)
  cap("1-3d","The side volume control.",x:40pt,y:377pt,w:170pt)
  cap("1-3e","The physical power button on the opposite side. This is separate from the Apple-logo touch control.",x:224pt,y:377pt,w:170pt)
  folio(4,"Getting Started")
}

// 5. Illustrated step sequence: two visual stations, each with its own
// paragraph. Crop retains the actual tab and program buttons without redrawing.
#let screen-sequence(instructions:copy.software) = {
  head("Opening programs with AtEase")
  at(40pt,80pt,96pt,text(size:10.5pt,weight:"bold")[AtEase])
  body(152pt,80pt,instructions.at(0))
  at(152pt,163pt,242pt,image("atease-detail.svg",width:242pt))
  at(40pt,319pt,96pt,text(size:10.5pt,weight:"bold")[Show Desktop])
  body(152pt,319pt,instructions.at(1))
  at(152pt,411pt,242pt,image("../assets/screenshots/piforma-show-desktop.svg",width:242pt))
  folio(5,"How the Macintosh PiForma Works")
}

// 6. Full-width technical plate: consistent labels/values, no grid boxes.
#let reference-plate(intro:copy.tech_intro,rows:copy.tech_rows) = {
  head("Technical Information")
  body(152pt,80pt,intro)
  at(40pt,146pt,354pt,text(size:12pt,weight:"bold")[Hardware inventory and identification])
  rule(40pt,168pt,w:354pt)
  at(40pt,182pt,354pt)[
    #set text(size:10pt)
    #set par(leading:6pt)
    #grid(columns:(91pt,251pt),column-gutter:12pt,row-gutter:6pt,
      ..rows.map(row => {
        let parts = row.replace(regex("^- "),"").split(": ")
        (text(weight:"bold",parts.first()),parts.slice(1).join(": "))
      }).flatten())
  ]
  folio(6,"Appendix A: Technical Information")
}
#chapter-opening()
#pagebreak()
#text-instructions()
#pagebreak()
#packing-plate()
#pagebreak()
#grouped-controls()
#pagebreak()
#screen-sequence()
#pagebreak()
#reference-plate()
