#!/usr/bin/env python
# coding: utf-8
import numpy as np

from matplotlib.pyplot import cm, colorbar, tight_layout
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['figure.figsize'] = (2*(3+3/8), (3+3/8))
plt.rc('text.latex', preamble=r'\usepackage{bm}')

import matplotlib.pyplot as plt
import pandas as pd

xlbl = "x"
ylbl = "y"
zlbls = ["f(x,y) = \cos(x)\cos(y)"]
zlbls.append("f(x,y) = \cos(x)\sin(y)")
zlbls.append("f(x,y) = \sin(x)\sin(y)")

data = pd.read_csv(f"data.csv")
fig = plt.figure()

for (idd, d) in enumerate(['Z1', 'Z2', 'Z3']):
    ax = fig.add_subplot(1,3,idd+1,projection='3d')
    ax.scatter(data['X'], data['Y'], data[d], c='black')
    ax.set_xlabel(f"${xlbl}$")
    ax.set_ylabel(f"${ylbl}$")
ax.set_zlabel(f"$f(x,y)$")
# plt.tight_layout()
plt.savefig("data_3d.pdf")