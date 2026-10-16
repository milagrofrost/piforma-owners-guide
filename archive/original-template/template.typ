// PiForma Owner's Guide, V2.
// Four editable pages inspired by the 1988 Macintosh Plus and 1989 Macintosh SE guides.
// Compile with Typst using this folder as the project root.
// Images are linked locally. Keep piforma-artwork.png beside template.typ.
// This is a hand-authored, closely matched source for the supplied print PDF.
#set page(width: 6.1in, height: 7.3in, margin: 0pt, fill: white)
#set text(font: "EB Garamond", size: 10.5pt, fill: rgb("252521"))
#set par(leading: 0.35em)
#let accent = rgb("db514e")
#let gray = rgb("696965")
#let at(x, y, content) = place(top + left, dx: x, dy: y, content)
#let bar(x,y,w) = at(x,y,line(length: w, stroke: 1.15pt + accent))
#let body(x,y,w,content) = at(x,y,block(width:w, content))
#let heading(name) = {
  bar(2.23in, 0.54in, 3.43in)
  at(2.23in, 0.61in, text(size: 14pt, weight:"bold")[#name])
}
#let foot(n) = {
  at(0.42in, 6.91in, text(size:7.4pt, fill:gray)[Chapter 1: Getting Started])
  at(5.55in, 6.91in, text(size:8pt, fill:gray)[#n])
}
#let mark(y) = at(2.25in,y,text(fill:accent, size:10pt)[▪])

// Page 1: cover. Replace the bundled image with an actual photograph of PiForma.
#for (i, color) in (rgb("65a5cf"),rgb("8665a9"),rgb("cf4d61"),rgb("e3a349"),rgb("79a560")).enumerate() {
  at(0.52in, 0.43in + i * 3.1pt, rect(width: 15pt, height: 3pt, fill: color, stroke: none))
}
#at(1.14in, 0.35in, text(size:18pt,fill:gray)[PiForma])
#at(1.14in, 0.68in, text(size:18pt,fill:gray)[Owner’s Guide])
#at(0.92in, 2.52in, image("piforma-artwork.png", width:4.61in))
#at(0.46in, 6.65in, text(size:7.5pt,fill:gray)[PI FORMA   •   PERSONAL MACINTOSH PROJECT])
#pagebreak()

// Page 2: chapter opener.
#at(0.44in,0.38in,text(size:8pt,fill:gray,tracking:1pt)[C H A P T E R])
#at(2.06in,0.31in,text(size:17pt,weight:"bold",fill:accent)[1])
#bar(2.25in,0.49in,3.43in)
#at(2.25in,0.57in,text(size:17pt,weight:"bold")[Getting Started])
#body(2.25in,2.72in,3.3in,[
  #text(size:24pt,fill:gray)[T]#smallcaps[his chapter will help you get started with your PiForma computer.]
])
#body(2.25in,3.50in,3.29in,[This guide introduces the PiForma system and walks you through the first setup. Start by checking the components and finding a comfortable place to work.])
#mark(4.90in)
#at(2.52in,4.90in,[Unpacking the equipment])
#mark(5.28in)
#at(2.52in,5.28in,[Connecting the keyboard and mouse])
#mark(5.66in)
#at(2.52in,5.66in,[Starting the PiForma computer])
#foot(1)
#pagebreak()

// Page 3: body page with left annotation rail.
#heading([Before you begin])
#body(2.24in,1.26in,3.28in,[Before unpacking your PiForma, choose a sturdy, level surface with room for the keyboard, mouse, and connecting cables. Keep the equipment away from liquids, excessive heat, and direct sunlight.])
#bar(0.42in,2.60in,1.55in)
#at(0.42in,2.72in,text(weight:"bold",size:10pt)[A little preparation])
#body(0.42in,3.02in,1.55in,text(size:8.6pt)[Keep the packing materials until the system is working correctly.])
#at(2.24in,2.67in,text(size:12.7pt,weight:"bold")[Unpacking])
#body(2.24in,3.08in,3.29in,[Remove the components one at a time and place them on the work surface. Check that each item is present before connecting power.])
#mark(4.23in)
#at(2.47in,4.23in,[PiForma computer and display])
#mark(4.56in)
#at(2.47in,4.56in,[Keyboard and pointing device])
#mark(4.89in)
#at(2.47in,4.89in,[Power supply and cables])
#bar(0.42in,5.60in,1.55in)
#at(0.42in,5.70in,text(size:10pt,weight:"bold")[Important])
#body(0.42in,6.02in,1.53in,text(size:8.7pt)[Check the correct power supply for your particular build.])
#body(2.24in,5.65in,3.29in,[Before connecting or changing internal components, disconnect power completely. Follow the electrical and hardware instructions for your specific PiForma configuration.])
#foot(2)
#pagebreak()

// Page 4: illustration, technical caption and three numbered procedures.
#heading([Putting it all together])
#body(2.24in,1.30in,3.28in,[Arrange the components before connecting the PiForma system for the first time.])
#at(1.92in,1.93in,image("piforma-artwork.png",width:3.63in))
#at(2.24in,4.48in,text(size:8pt,style:"italic",fill:gray)[Figure 1-1   The PiForma computer and accessories])
#bar(0.42in,4.97in,1.55in)
#at(0.42in,5.08in,text(size:10pt,weight:"bold")[Getting connected])
#body(0.42in,5.39in,1.55in,text(size:8.5pt)[Check the shape and orientation of each connector. Never force a plug into a socket.])
#at(2.24in,4.96in,text(fill:accent,weight:"bold")[1.])
#at(2.52in,4.96in,text(weight:"bold")[Position the computer.])
#body(2.52in,5.18in,3.03in,[Place the computer near the rear of your work surface.])
#at(2.24in,5.73in,text(fill:accent,weight:"bold")[2.])
#at(2.52in,5.73in,text(weight:"bold")[Arrange the keyboard.])
#body(2.52in,5.96in,3.03in,[Allow space to operate the mouse comfortably.])
#at(2.24in,6.29in,text(fill:accent,weight:"bold")[3.])
#at(2.52in,6.29in,text(weight:"bold")[Connect the cables.])
#body(2.52in,6.49in,3.03in,[Confirm connections before applying power.])
#foot(3)
