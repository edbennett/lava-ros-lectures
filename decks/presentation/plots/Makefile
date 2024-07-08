all: ../images/matplotlib-plot-default.svg \
    ../images/matplotlib-plot-paper.svg \
    ../images/matplotlib-plot-dark.svg \
    ../images/seaborn-plot.svg \
    ../images/ggplot2-plot.svg \
    ../images/gnuplot-plot.svg

../images/matplotlib-plot-%.svg : plot_matplotlib.py styles/%.mplstyle
	python $< --styles $*

../images/seaborn-plot.svg : plot_seaborn.py
	python $<

../images/ggplot2-plot.svg : plot.R
	Rscript $<

../images/gnuplot-plot.svg : plot.gnuplot
	./$<
