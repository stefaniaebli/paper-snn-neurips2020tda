TEX = main.tex  # latex sources
PDF = $(TEX:.tex=.pdf)  # produced PDFs
BIB = $(wildcard *.bib)  # bibliography
BST = $(wildcard *.bst)  # bibliographic style
STY = $(wildcard *.sty)  # style (package)

all: $(PDF)

figures:
	#$(MAKE) -C figures

%.pdf: %.tex $(BIB) $(BST) $(STY) figures
	latexmk -pdf -lualatex $<

clean:
	git clean -Xdf $(addprefix -e !, $(PDF))

cleanall: clean
	#$(MAKE) cleanall -C figures
	rm -f $(PDF)

.PHONY: all figures clean cleanall
