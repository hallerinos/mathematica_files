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

data = pd.read_csv(f"data.csv")

fig,axs = plt.subplots(1,2,sharey=True)
axs[0].scatter(data['X'],data['Z2'], c='black', alpha=0.25)
axs[0].set_xlabel(f"$x$")
axs[0].set_ylabel(f"$f(x,y)$")
axs[1].scatter(data['Y'],data['Z2'], c='black', alpha=0.25)
axs[1].set_xlabel(f"$y$")
plt.tight_layout()
# plt.show()
plt.savefig("data_2d_grid.pdf")