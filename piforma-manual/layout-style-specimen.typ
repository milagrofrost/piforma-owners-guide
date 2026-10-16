// Reusable-style verification sheet; not part of the owner's manuscript.
#import "styles/book.typ": *
#show: book
#current-title.update("Layout style specimen")
#phase.update("body")
= Layout style specimen
#para("This sheet verifies the reusable styles independently of the owner's text. It is a production artifact and is not included in the manual.")
== Instruction rhythm
#instruction(1,[A long sample instruction wraps beneath the instruction text, leaving the red numeral in its own narrow column.])
#bullet([A sample bullet also uses a hanging continuation. The marker stays clear of the following lines.])
#important([This sample checks the rail label, fine rule and main-column notice alignment.])
#warning([This sample checks the matching warning treatment without adding a new notice to the manuscript.])
== Specification rows
#spec-row("Label:",[A short specification value.])
#spec-row("Long label:",[A longer value wraps within its own column while the entire specification row stays together.])
#glossary-term("Glossary term")
#para("A definition remains with its term and follows the normal text rhythm.")
