.PHONY: default clean all tidy

TESTS = quiz6.tex

SOLUTIONS = quiz6_sol.tex

PIC_SRC := $(wildcard *.pic)

PIECES = pointers0.tex pointers0_soln.tex pointers1.tex autocomplete.tex autocomplete_soln.tex

%.tex: %.pic
	pic -t $< > $@

%.ps: %.tex
	latex $< </dev/null
	dvips -o $@ $*.dvi
	$(RM) $*.out $*.dvi

%.pdf: %.ps
	ps2pdf $< $@

PDF = $(patsubst %.pic,%.pdf,$(patsubst %.tex,%.pdf,$(TESTS) $(SOLUTIONS)))

PS = $(PDF:.pdf=.ps)

default: all

all: $(PDF)

quiz6.ps quiz6_sol.ps: $(PIECES)

$(PIC_SRC:.pic=.tex): box-utils.pic

$(PS): utils.sty

tidy:
	$(RM) *~ *.aux *.log *.dvi

clean: tidy
	$(RM) $(PDF) $(PS) $(PIC_SRC:.pic=.tex)
