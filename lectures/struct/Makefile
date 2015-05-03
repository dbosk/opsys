FILES=		struct.tex literature.bib

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: struct.pdf

struct.pdf: ${FILES}

literature.bib: ../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../miuntex
INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
