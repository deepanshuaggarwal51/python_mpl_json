"""Helper script load_rcparams.

Reads the YAML and updates Matplotlib's rcParams.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import yaml

# loading the yaml file and converting as a python's dictionary
mpl_yaml_file = Path("mpl_rcparams.yml")
rcparams = yaml.safe_load(mpl_yaml_file.read_text())

# changing the matplotlib rcParams
for k in rcparams:
    plt.rc(group=k, **rcparams[k])
