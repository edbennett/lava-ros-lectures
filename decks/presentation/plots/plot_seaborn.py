#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("data.dat", sep=r"\s+", names=["x", "y", "dy"])
x = np.linspace(0, 5, 1000)

sns.set_theme()
sns.set_theme(rc={"figure.figsize": (6, 4)})

line_data = pd.DataFrame({"x": x, "x_squared": x**2})
sns.lineplot(line_data, x="x", y="x_squared", label="Line plot $M = m^2$")

sns.scatterplot(data, x="x", y="y", label="Scatter plot")

plt.ylabel("$M$")
plt.xlabel("$m$")

plt.tight_layout()

plt.savefig("../images/seaborn-plot.svg")
