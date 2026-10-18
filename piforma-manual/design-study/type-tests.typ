#let sample = json("selected-copy.json")
#set page(width:432pt,height:522pt,margin:32pt)
#set text(fill:rgb("242424"))
#let test(label,font,size,squeeze:false) = block(above:12pt,below:12pt)[
  #text(font:"Times New Roman",size:9pt,weight:"bold",label)
  #v(7pt)
  #set text(font:font,size:size)
  #set par(leading:6pt,spacing:8pt)
  #if squeeze {
    scale(x:85%,origin:top+left,reflow:true,block(width:242pt/.85,sample.intro))
  } else { block(width:242pt,sample.intro) }
]
#text(font:"Times New Roman",size:17pt)[Natural proportion trials]
#test("Current: Times New Roman 10 pt / 85% width", "Times New Roman",10pt,squeeze:true)
#test("Times New Roman 10 pt / natural width", "Times New Roman",10pt)
#test("EB Garamond 10.5 pt / natural width", "EB Garamond",10.5pt)
#test("Palatino Linotype 10 pt / natural width", "Palatino Linotype",10pt)
