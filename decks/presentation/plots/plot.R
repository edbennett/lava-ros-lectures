library(tidyverse)
library(ggplot2)
library(latex2exp)

data <- read_table("data.dat", col_names = c("m", "M", "dM"))

(ggplot(data)
  + xlim(0, 5)
  + xlab(TeX("$m$"))
  + ylab(TeX("$M$"))
  + geom_function(fun = function(m) m**2, aes(color = factor(1)))
  + geom_point(mapping = aes(x=m, y=M, color="Data plot"))
  + geom_errorbar(mapping=aes(x=m, y=M, ymin=M-dM, ymax=M+dM, color="Data plot"), width=0.1)
  + scale_color_discrete(labels=c(TeX("Function plot $M = m^2$"), "Data plot"))
  + guides(color = guide_legend(title = ""))
)

ggsave("../images/ggplot2-plot.svg", width = 6, height = 4)
