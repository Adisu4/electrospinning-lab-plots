# Electrospinning lab plots

Python scripts and FIJI data for the BMCH electrospinning / SEM lab report.

## Folder plan

```
Lab2Figi/              raw FIJI exports only (CSV + original screenshots)
  diameter/
  orientation/
  thickness/
figures/
  python/              plots made by the scripts (use these in the report)
  fiji/                FIJI histogram / SEM screenshots, if you want them separate
plot_*.py              run from this folder
```

Keep measurement tables in `Lab2Figi/`. Keep finished report figures in `figures/python/`.

## Requirements

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

Outputs:

- `figures/python/Figure_diameter_journal.png` (and `.pdf`)
- `figures/python/Figure_orientation_journal.png` (and `.pdf`)
- `figures/python/Figure_thickness_journal.png` (and `.pdf`)
