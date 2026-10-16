#import "page-layout.typ": *
#import "typography.typ": *
#let rule(x,y,w: column-width,thickness: 1.8pt) = at(x,y,line(length:w,stroke:thickness+accent))
#let section(x,y,title,w:column-width) = {
  rule(x,y,w:w,thickness:if w < 150pt { .55pt } else { 1.8pt })
  at(x,y+5pt,scale(x:85%,origin:top+left,text(size:if w < 150pt { 10.5pt } else { 13pt },weight:"bold")[#title]))
}
#let bullet(x,y,content,w:230pt) = {
  at(x,y+3pt,rect(width:3.3pt,height:3.3pt,fill:accent,stroke:none))
  body(x+10pt,y,w,content)
}
#let warning(x,y,content,label:[Important]) = {
  at(x - 64pt,y,polygon((0pt,6pt),(3pt,0pt),(6pt,6pt),fill:none,stroke:.45pt+accent))
  at(x - 53pt,y,text(size:10pt,weight:"bold")[#label])
  body(x,y,column-width,[#content #box(polygon((0pt,6pt),(3pt,0pt),(6pt,6pt),fill:none,stroke:.45pt+accent))])
}
#let step(x,y,n,title,content) = {
  at(x,y,text(size:9.5pt,weight:"bold",fill:accent)[#n.])
  body(x+13pt,y,229pt,[#text(weight:"bold")[#title] #content])
}
