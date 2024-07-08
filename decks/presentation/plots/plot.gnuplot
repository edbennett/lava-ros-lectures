#!/usr/bin/env gnuplot

set term svg size 450,300 fixed
set output "../images/gnuplot-plot.svg"

set xlabel "m"
set ylabel "M"

set key top left

set xrange [0:5]

plot x**2 title "Function plot M = m^2", 'data.dat' u 1:2:3 with yerror title "Data plot"
