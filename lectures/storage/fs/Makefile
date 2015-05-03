FILES=		fs.tex literature.bib
FILES+= 	contiguous.pdf fat.pdf fcb.pdf fshier.pdf indexed.pdf
FILES+= 	inode.pdf linked.pdf nfs.pdf openread.pdf vfs.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: fs.pdf

fs.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
