# load_rcparams_toml.py
"""Helper script for loading maptplotlib rcParams from toml.

Reads the `toml` and updates Matplotlib's rcParams.
"""
import tomllib
from pathlib import Path

import matplotlib.pyplot as plt

# loading the toml file and converting as a python dictionary
mpl_toml_file = Path("./mpl_rcparams.toml")
rcparams = tomllib.load(mpl_toml_file)

# updating the matplotlib rcParams
for k in rcparams:
    plt.rc(group=k, **rcparams[k])
