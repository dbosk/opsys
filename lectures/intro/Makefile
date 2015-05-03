FILES=			intro.tex literature.bib Unix_history-simple.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: intro.pdf

intro.pdf: ${FILES}

literature.bib: ../../literature.bib
	ln -s $^ $@

Unix_history-simple.pdf: Unix_history-simple.svg
	inkscape -D -z --file=$< --export-pdf=$@

clean:
	${RM} literature.bib
	${RM} Unix_history-simple.pdf


INCLUDE_MIUNTEX=../../miuntex
INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
