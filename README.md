# Electrospinning lab plots

Python scripts used to make the journal-style figures for the BMCH combined electrospinning and SEM lab report.

## Requirements

- Python 3
- matplotlib
- numpy

```bash
pip install matplotlib numpy
```

## Run

```bash
python3 plot_fiber_diameter.py
python3 plot_fiber_orientation.py
python3 plot_fabric_thickness.py
```

Each script writes a PNG and a PDF in the same folder.

## Scripts

- `plot_fiber_diameter.py` — mean ± SD bars and pooled histogram from 60 FIJI diameter measurements (20 per 1000× image).
- `plot_fiber_orientation.py` — Directionality histograms plus fitted main angle ± dispersion. Panel b uses the official FIJI fit values. Panel a needs optional `histA.dat`, `histB.dat`, and `histC.dat`.
- `plot_fabric_thickness.py` — mean ± SD bars from 9 FIJI thickness measurements (3 per 100× image).
