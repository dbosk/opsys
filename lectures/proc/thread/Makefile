FILES=		thread.tex literature.bib
FILES+= 	threads.pdf single-core.pdf multi-core.pdf
FILES+= 	one-to-one.pdf many-to-one.pdf many-to-many.pdf
FILES+= 	lwp.pdf two-level.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: thread.pdf

thread.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
