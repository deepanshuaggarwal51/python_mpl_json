# Matplotlib rcParams JSON/YAML Schema

- [Matplotlib rcParams JSON/YAML Schema](#matplotlib-rcparams-jsonyaml-schema)
    - [Directory layout](#directory-layout)
    - [Writing the rcParams YAML](#writing-the-rcparams-yaml)
      - [Example (`mpl_rcparams.yml`)](#example-mpl_rcparamsyml)
    - [Loading the YAML at runtime](#loading-the-yaml-at-runtime)

This repository ships a **JSON Schema** that describes all valid Matplotlib `rcParams` keys, value types and allowed enumerations.

The goal is to let you write your Matplotlib configuration in **YAML**, get IDE‑level validation via **yaml‑language‑server (YLS)**, and load the settings into Python with a single call.

### Directory layout
```code
|- matplotlib-rcparams-schema.json      # the JSON Schema file
|- mpl_rcparams.yml                     # sample YAML configuration
|- README.md                            # (this file)
```

### Writing the rcParams YAML
The YAML file must be a mapping where each top‑level key corresponds to a Matplotlib rcParam name.
Values follow the types defined in the schema (string, number, boolean, list, etc.).

#### Example (`mpl_rcparams.yml`)

```yaml
# yaml-language-server: $schema=matplotlib-rcparams-schema.json

figure:
  figsize: [8, 6]
  dpi: "high"
  autolayout: true

axes:
  titlesize: large
  labelsize: 12
  grid: true

lines:
  linewidth: 2.5
  linestyle: '--'
  color: '#1f77b4'

savefig:
  bbox: "tight"
  pad_inches: 1e-2
```
The schema will flag:
- wrong types (e.g., dpi: "high" → error)

### Loading the YAML at runtime

A tiny helper script `load_rcparams.py` reads the YAML and updates Matplotlib’s rcParams.

```python
from pathlib import Path

import matplotlib.pyplot as plt
import yaml

# loading the yaml file and converting as a python's dictionary
mpl_yaml_file = Path("mpl_rcparams.yml")
rcparams = yaml.safe_load(mpl_yaml_file.read_text())

# changing the matplotlib rcParams
for k in rcparams:
    plt.rc(group=k, **rcparams[k])
```