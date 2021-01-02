PY = $(wildcard *.py)
PDF = $(PY:.py=.pdf)

all: $(PDF)

%.pdf: %.py
	python $<
	pdfcrop $@ $@

cleanall:
	rm -f $(PDF)

.PHONY: all cleanall
