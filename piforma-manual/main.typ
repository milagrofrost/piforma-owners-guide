#import "styles/book.typ": *
#import "styles/typography.typ": accent
#show: book
#cover()
#cover-reverse()
#pagebreak()
#counter(page).update(1)
#set page(numbering:"i")
#current-title.update("Contents")
#contents()
#front("Welcome to the Macintosh PiForma",[
  #include "chapters/00-front-matter.typ"
])
#set page(numbering:"1")
#chapter(1,"Getting Started",[#include "chapters/01-getting-started.typ"])
#chapter(2,"Inside the Macintosh PiForma",[#include "chapters/02-inside-piforma.typ"])
#chapter(3,"How the Macintosh PiForma Works",[#include "chapters/03-how-piforma-works.typ"])
#chapter(4,"Caring for Your Macintosh PiForma",[#include "chapters/04-caring-for-piforma.typ"])
#end-section("Appendix A: Technical Information",[#include "chapters/05-technical-information.typ"])
#end-section("Appendix B: When Something Goes Wrong",[#include "chapters/07-troubleshooting.typ"])
#end-section("Glossary",[#include "chapters/06-glossary-and-credits.typ"])
#back-cover()
