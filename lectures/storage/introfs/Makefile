FILES=		introfs.tex literature.bib
FILES+= 	acyclicdir.pdf graphdir.pdf treedir.pdf
FILES+= 	mounted.pdf unmounted.pdf
FILES+= 	onelvldir.pdf twolvldir.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: introfs.pdf

introfs.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
