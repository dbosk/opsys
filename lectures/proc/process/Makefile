FILES=		process.tex literature.bib
FILES+= 	fork.pdf ipc.pdf pcb.pdf proc.pdf proctree.pdf queues.pdf
FILES+= 	ready.pdf rpc.pdf states.pdf switch.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

all: process.pdf

process.pdf: ${FILES} miunmisc

literature.bib: ../../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../../miuntex
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
