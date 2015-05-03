FILES=		sync.tex literature.bib
FILES+= 	deadlock.pdf deadtruck.pdf dining.pdf nodeadlock.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: sync.pdf

sync.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
