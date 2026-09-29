# Electrospinning lab plots

Python scripts used to make the journal-style figures for the BMCH combined electrospinning and SEM lab report.

All scripts read the FIJI export files in `Lab2Figi/` and write PNG/PDF figures next to the script. Clone the repo and run from the repository root. No local `C:\\` paths are required.

## Data layout

```
Lab2Figi/
  diameter/
    a-Results-1000x.csv
    b-Results-1000x.csv
    c-Results-1000x.csv
  orientation/
    a-Directionality-500x.csv
    b-directionality-x500.csv
    c-directionality-x500.csv
  thickness/
    a-Results-x100.csv
    b-Results-x100.csv
    c-Results-x100.csv
```

Diameter and thickness plots use the FIJI `Length` column (µm). Orientation plots use the Directionality histogram CSVs.

## Requirements

- Python 3
- matplotlib
- numpy

```bash
pip install matplotlib numpy
```

## Run

```bash
git clone https://github.com/Adisu4/electrospinning-lab-plots.git
cd electrospinning-lab-plots
python3 plot_fiber_diameter.py
python3 plot_fiber_orientation.py
python3 plot_fabric_thickness.py
```

Each script writes a PNG and a PDF in this folder.

## Scripts

- `plot_fiber_diameter.py` — mean ± SD bars and pooled histogram from `Lab2Figi/diameter/` (20 fibers per 1000× image).
- `plot_fiber_orientation.py` — Directionality histograms from `Lab2Figi/orientation/` plus the FIJI Gaussian-fit main angle ± dispersion.
- `plot_fabric_thickness.py` — mean ± SD bars from `Lab2Figi/thickness/` (3 measurements per 100× image).
