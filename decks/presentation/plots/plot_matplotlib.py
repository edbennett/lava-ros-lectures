#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--styles", default="default")
args = parser.parse_args()

if args.styles != "default":
    plt.style.use(f"styles/{args.styles}.mplstyle")

data = pd.read_csv("data.dat", sep=r"\s+", names=["x", "y", "dy"])
x = np.linspace(0, 5, 1000)

fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")

ax.plot(x, x ** 2, label="Function plot $M=m^2$")
ax.errorbar(data.x, data.y, yerr=data.dy, fmt="x", label="Data plot")

ax.set_xlabel("$m$")
ax.set_ylabel("$M$")

ax.set_xlim(0, 5)

ax.legend(loc="best")

fig.savefig(f"../images/matplotlib-plot-{args.styles}.svg", transparent=True)
