# $Id$
# Author:	Daniel Bosk <daniel.bosk@miun.se>

FILES=		overview.tex aims.tex literature.tex examination.tex literature.bib

.PHONY: all
all: overview.pdf

overview.pdf: ${FILES} miunasgn miunmisc

examination.tex: ../examination.tex
literature.bib: ../../literature.bib

examination.tex literature.bib:
	ln -s $^ $@

clean:
	${RM} examination.tex literature.bib


### INCLUDES ###
INCLUDE_MIUNTEX=../../miuntex
INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
