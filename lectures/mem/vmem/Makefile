FILES=		vmem.tex literature.bib
FILES+= 	copyonwritechange.eps copyonwrite.eps lazyswap.eps needreplace.eps
FILES+= 	pagefault.eps pagereplace.eps sharedpages.eps swapping.eps
FILES+= 	vaddrspace.eps vmem.eps

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: vmem.pdf

vmem.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
