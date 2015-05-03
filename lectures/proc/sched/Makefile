FILES=		sched.tex literature.bib
FILES+= 	burstcycle.pdf burstdiag.pdf memstall-parallell.pdf memstall.pdf
FILES+= 	multilevel.pdf multilvl-feedback.pdf numa.pdf rr-quantum.pdf
FILES+= 	rr-turnaround.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: sched.pdf

sched.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib

INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
