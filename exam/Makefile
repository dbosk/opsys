# $Id$
# Author:	Daniel Bosk <daniel.bosk@miun.se>

USE_LATEXMK= 	yes

all: ${DOCUMENTS}

DOCUMENTS=	exam-130426.pdf exam-130118.pdf exam-140113.pdf
DOCUMENTS+= exam-140424.pdf exam-140820.pdf

exam-140820.pdf: exam-140820.tex aims.tex literature.bib miunexam miunmisc
exam-140424.pdf: exam-140424.tex aims.tex literature.bib miunexam miunmisc
exam-140113.pdf: exam-140113.tex aims.tex literature.bib miunexam miunmisc
exam-130118.pdf: exam-130118.tex aims.tex literature.bib miunexam miunmisc
exam-130426.pdf: exam-130426.tex aims.tex literature.bib miunexam miunmisc

literature.bib: ../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


### INCLUDES ###

INCLUDE_MIUNTEX=../miuntex
INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
