#let ink = rgb("242424")
#let accent = rgb("f34836")
#let quiet = rgb("b8b6ae")
// Apple Garamond is not bundled. This installed serif is an explicit approximation.
#let manual-font = "Times New Roman"
#let body-size = 10pt
#let typography(content) = {
  set text(font: manual-font, size: body-size, fill: ink)
  set par(leading: 7pt, spacing: 7pt, justify: false)
  content
}
