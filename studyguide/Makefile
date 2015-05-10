# $Id$
# Author:	Daniel Bosk <daniel.bosk@miun.se>

FILES=		studyguide.tex literature.bib

THEORY=		overview-lit.tex overview-aim.tex
THEORY+= 	process-lit.tex process-aim.tex
THEORY+= 	memory-lit.tex memory-aim.tex
THEORY+= 	storage-lit.tex storage-aim.tex
#THEORY+= 	distributed-lit.tex distributed-aim.tex
#THEORY+= 	vmtheory-lit.tex vmtheory-aim.tex

FILES+= 	${THEORY}

LABS+= 		paging-lit.tex paging-aim.tex

FILES+=		${LABS}
FILES+= 	exam-aim.tex

LECTURES= 	intro-lit.tex
LECTURES+= 	struct-lit.tex
LECTURES+= 	proc-lit.tex
LECTURES+= 	thread-lit.tex
LECTURES+= 	sched-lit.tex
LECTURES+= 	sync-lit.tex
#LECTURES+= 	mem-lit.tex
LECTURES+= 	physmem-lit.tex
LECTURES+= 	vmem-lit.tex
#LECTURES+= 	store-lit.tex
LECTURES+= 	introfs-lit.tex
LECTURES+= 	lectfs-lit.tex
LECTURES+= 	stor-lit.tex
LECTURES+= 	io-lit.tex
LECTURES+= 	distsys-lit.tex
#LECTURES+= 	special-lit.tex
LECTURES+= 	systems-lit.tex
LECTURES+= 	vm-lit.tex

FILES+= 	${LECTURES}

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

.PHONY: all
all: studyguide.pdf

studyguide.pdf: ${FILES} miunart miunmisc

.PHONY: clean
clean:
	${RM} ${DOCUMENTS}

literature.bib: ../literature.bib

overview-aim.tex: ../theory/overview/aims.tex
overview-lit.tex: ../theory/overview/literature.tex

process-aim.tex: ../theory/process/aims.tex
process-lit.tex: ../theory/process/literature.tex

memory-aim.tex: ../theory/memory/aims.tex
memory-lit.tex: ../theory/memory/literature.tex

paging-aim.tex: ../labs/paging/aims.tex
paging-lit.tex: ../labs/paging/literature.tex

storage-aim.tex: ../theory/storage/aims.tex
storage-lit.tex: ../theory/storage/literature.tex

distributed-aim.tex: ../theory/distributed/aims.tex
distributed-lit.tex: ../theory/distributed/literature.tex

vmtheory-aim.tex: ../theory/vm/aims.tex
vmtheory-lit.tex: ../theory/vm/literature.tex

exam-aim.tex: ../exam/aims.tex

intro-lit.tex: ../lectures/intro/literature.tex
struct-lit.tex: ../lectures/struct/literature.tex
proc-lit.tex: ../lectures/proc/process/literature.tex
thread-lit.tex: ../lectures/proc/thread/literature.tex
sched-lit.tex: ../lectures/proc/sched/literature.tex
sync-lit.tex: ../lectures/proc/sync/literature.tex
#mem-lit.tex: ../lectures/mem/literature.tex
physmem-lit.tex: ../lectures/mem/physmem/literature.tex
vmem-lit.tex: ../lectures/mem/vmem/literature.tex
#store-lit.tex: ../lectures/store/literature.tex
introfs-lit.tex: ../lectures/storage/introfs/literature.tex
lectfs-lit.tex: ../lectures/storage/fs/literature.tex
stor-lit.tex: ../lectures/storage/stor/literature.tex
io-lit.tex: ../lectures/storage/io/literature.tex
distsys-lit.tex: ../lectures/distsys/literature.tex
#special-lit.tex: ../lectures/special/literature.tex
systems-lit.tex: ../lectures/systems/literature.tex
vm-lit.tex: ../lectures/vm/literature.tex

${THEORY} ${LABS} ${LECTURES} exam-aim.tex literature.bib:
	ln -s $^ $@

clean:
	${RM} literature.bib ${THEORY} ${LABS} ${LECTURES}
	${RM} exam-aim.tex studyguide.pdf


### INCLUDES ###

INCLUDE_MIUNTEX=../miuntex
INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/miun.depend.mk
