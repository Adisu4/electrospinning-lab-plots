#!/usr/bin/env python3
"""
Fiber orientation figure.
Panel a: Directionality histograms from Lab2Figi/orientation CSVs.
Panel b: official FIJI Gaussian-fit main angle ± dispersion (report Table 3).
Output: Figure_orientation_journal.png / .pdf
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA = HERE / "Lab2Figi" / "orientation"

FILES = {
    "A": DATA / "a-Directionality-500x.csv",
    "B": DATA / "b-directionality-x500.csv",
    "C": DATA / "c-directionality-x500.csv",
}

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "figure.dpi": 200,
    "savefig.dpi": 400,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "savefig.facecolor": "white",
    "pdf.fonttype": 42,
})

# Official FIJI Directionality Gaussian-fit summary (Table 3)
CENTERS = np.array([-7.50, -1.99, -10.50])
DISPS = np.array([16.71, 23.72, 19.17])
LABELS = ["A", "B", "C"]


def load_dir_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run this script from the repo root.")
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    ang, amt, fit = [], [], []
    for r in rows[1:]:
        if len(r) >= 3 and r[0].strip():
            ang.append(float(r[0]))
            amt.append(float(r[1]))
            fit.append(float(r[2]))
    return np.array(ang), np.array(amt), np.array(fit)


hists = {key: load_dir_csv(FILES[key]) for key in LABELS}

fig, axes = plt.subplots(
    1, 2, figsize=(7.5, 3.25),
    gridspec_kw={"width_ratios": [1.35, 1], "wspace": 0.36},
)

ax = axes[0]
styles = {"A": ("-", 1.15), "B": ("--", 1.15), "C": (":", 1.15)}
for key in LABELS:
    ang, amt, _fit = hists[key]
    ls, lw = styles[key]
    ax.plot(ang, amt, color="black", lw=lw, ls=ls, label=key)

ax.axvline(0, color="black", lw=0.7)
ax.set_xlim(-90, 90)
ax.set_ylim(0, 0.034)
ax.set_xlabel("Direction (°)")
ax.set_ylabel("Amount")
ax.set_xticks([-90, -45, 0, 45, 90])
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.legend(frameon=False, fontsize=9, loc="upper right", handlelength=2.2)
ax.text(-90, 0.034, "a", fontsize=13, fontweight="bold", va="bottom", ha="right")
ax.text(2, 0.0322, "0° axial", fontsize=7.5, color="#333333")
ax.text(58, 0.0028, "±90° circum.", fontsize=7.5, color="#333333")

ax = axes[1]
x = np.arange(3)
ax.errorbar(
    x, CENTERS, yerr=DISPS,
    fmt="o", color="black",
    ecolor="black", elinewidth=0.95,
    capsize=3.5, capthick=0.95,
    markersize=6, markerfacecolor="white",
    markeredgecolor="black", markeredgewidth=1.0,
    zorder=3,
)
ax.axhline(0, color="black", lw=0.7)
ax.set_xticks(x)
ax.set_xticklabels(LABELS)
ax.set_xlabel("Image")
ax.set_ylabel("Main orientation angle (°)")
ax.set_ylim(-40, 20)
ax.set_xlim(-0.6, 2.6)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for i, (c, d) in enumerate(zip(CENTERS, DISPS)):
    ax.text(i, c - d - 3.2, f"{c:.1f} ± {d:.1f}", ha="center", va="top", fontsize=7.5)
ax.text(-0.6, 20, "b", fontsize=13, fontweight="bold", va="bottom", ha="right")

fig.savefig(HERE / "Figure_orientation_journal.png")
fig.savefig(HERE / "Figure_orientation_journal.pdf")
print("wrote", HERE / "Figure_orientation_journal.png")
print("combined angle ± disp = "
      f"{CENTERS.mean():.1f} ± {DISPS.mean():.1f} deg")
