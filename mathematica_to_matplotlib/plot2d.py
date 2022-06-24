#!/usr/bin/env python
# coding: utf-8
import numpy as np
from scipy.interpolate import interp2d

from matplotlib.pyplot import cm, colorbar, tight_layout
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['figure.figsize'] = ((3+3/8), (3+3/8))
plt.rc('text.latex', preamble=r'\usepackage{bm}')

import matplotlib.pyplot as plt
import pandas as pd

xlbl = "x"
ylbl = "y"
zlbl = "f(x,y) = \cos(x)\cos(y)"

data = pd.read_csv(f"data.csv")

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(data['X'],data['Y'], c='black')
ax.set_xlabel(f"${xlbl}$")
ax.set_ylabel(f"${ylbl}$")
plt.tight_layout()
plt.savefig("data_2d.pdf")