#let ink = rgb("242424")
#let accent = rgb("f34836")
#let quiet = rgb("b8b6ae")
// Approved natural-proportion Garamond direction; not an exact Apple font claim.
#let manual-font = "EB Garamond"
#let body-size = 10.5pt
#let typography(content) = {
  set text(font: manual-font, size: body-size, fill: ink)
  set par(leading: 6pt, spacing: 7pt, justify: false)
  content
}
