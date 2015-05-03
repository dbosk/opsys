# $Id$
# Author:	Daniel Bosk <daniel.bosk@miun.se>
# Date:		5 Dec 2012

all: paging.pdf report.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

paging.pdf: ${FILES} report.pdf miunasgn miunmisc
report.pdf: report.tex literature.bib fifo-refstr.txt fifo-result.txt

literature.bib: ../../literature.bib
	ln -s $^ $@

clean:
	${RM} literature.bib


INCLUDE_MIUNTEX=../../miuntex
INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
