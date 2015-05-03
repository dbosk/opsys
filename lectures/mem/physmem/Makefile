FILES=		physmem.tex literature.bib
FILES+= 	hwbaselimit.pdf loadlink.pdf membaselimit.pdf relocation.pdf
FILES+= 	pagealloc.pdf pagehash.pdf pagehierbig.pdf pagehier.pdf
FILES+= 	pageidx.pdf pagemap.pdf pagenew.pdf sharedpage.pdf pageseg.pdf
FILES+= 	pagetable.pdf pagevalid.pdf tlb.pdf
FILES+= 	safereloc.pdf seghw.pdf segmap.pdf segments.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: physmem.pdf

physmem.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
