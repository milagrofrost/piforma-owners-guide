// Coordinates are in points, measured against the Plus PDF's scan box.
#let trim-width = 432pt
#let trim-height = 522pt
#let at(x, y, content) = place(top + left, dx: x, dy: y, content)
#let body(x, y, width, content) = at(x, y, scale(x: 85%, origin: top + left, reflow: true, block(width: width / 0.85, content)))
// Book parity follows logical chapter pages, independent of prototype sheet order.
#let column(odd: true) = if odd { 164pt } else { 152pt }
#let column-width = 242pt
#let footer(n, title: [Getting Started], opening: false) = {
  let odd = calc.odd(n)
  if not opening {
    at(if odd { 285pt } else { 65pt }, 489pt,
      scale(x:85%,origin:top+left,text(size: 8.5pt)[#if odd { title } else { [Chapter 1: Getting Started] }]))
  }
  at(if odd { 404pt } else { 27pt }, 489pt, text(size: 8pt)[#n])
}
