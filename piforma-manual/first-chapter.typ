#import "styles/book.typ": *
#import "styles/typography.typ": accent
#show: book
#current-title.update("Contents")
#set page(numbering:"i")
#contents()
#front("Welcome to the Macintosh PiForma",[#include "chapters/00-front-matter.typ"])
#set page(numbering:"1")
#chapter(1,"Getting Started",[#include "chapters/01-getting-started.typ"],art:"art-glamor.jpg")
