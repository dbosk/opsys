SUBDIR= 	intro
SUBDIR+= 	overview
#SUBDIR+= 	struct
SUBDIR+= 	proc
SUBDIR+= 	mem
SUBDIR+= 	storage

osc-book-figures: osc-book-figures.zip
	unzip $^
	mv os-figures osc-book-figures

osc-book-figures.zip:
	wget -O $@ http://codex.cs.yale.edu/avi/os-book/OS9/slide-dir/os-figures.zip

INCLUDE_MIUNTEX=../miuntex
INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
