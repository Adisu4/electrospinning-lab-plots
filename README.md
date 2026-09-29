# Electrospinning and SEM analysis plots

Scripts and data used to generate the fiber-diameter, orientation, and thickness figures in the BMCH 8220/9221 lab report.

**Repository:** https://github.com/Adisu4/electrospinning-lab-plots

## Contents

| Path | Description |
|---|---|
| `Lab2Figi/diameter/` | FIJI Results tables (1000× fiber diameter, µm) |
| `Lab2Figi/orientation/` | FIJI Directionality histograms (500×) |
| `Lab2Figi/thickness/` | FIJI Results tables (100× wall thickness, µm) |
| `figures/fiji/` | SEM frames and FIJI histogram screenshots |
| `figures/python/` | Journal figures written by the plotting scripts |
| `plot_fiber_diameter.py` | Diameter mean ± SD and pooled histogram |
| `plot_fiber_orientation.py` | Directionality overlay and fitted main angle |
| `plot_fabric_thickness.py` | Thickness mean ± SD |

Measurements were taken in FIJI/ImageJ. Python is used only to plot those exports.

## Requirements

Python 3 with `matplotlib` and `numpy`.

```bash
pip install matplotlib numpy
```

## Reproduce the figures

```bash
git clone https://github.com/Adisu4/electrospinning-lab-plots.git
cd electrospinning-lab-plots
python3 plot_fiber_diameter.py
python3 plot_fiber_orientation.py
python3 plot_fabric_thickness.py
```

The scripts read CSVs from `Lab2Figi/` and write:

- `figures/python/Figure_diameter_journal.png`
- `figures/python/Figure_orientation_journal.png`
- `figures/python/Figure_thickness_journal.png`

PDF copies are written next to the PNGs.

## Figures

FIJI source images are in [`figures/fiji/`](figures/fiji/). After running the scripts, report-ready plots are in [`figures/python/`](figures/python/).
