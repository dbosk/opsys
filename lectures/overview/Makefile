FILES=		overview.tex literature.bib
FILES+= 	arch.pdf cache.pdf cluster.pdf dualmode.pdf
FILES+= 	interrupt.pdf multiprog.pdf services.pdf smp.pdf
FILES+= 	storagehier.pdf syscomponents.pdf sysstruct.pdf vm.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: overview.pdf

overview.pdf: ${FILES}

literature.bib: ../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../miuntex
INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
