#!/usr/bin/env python3
"""
Fiber orientation figure.
Panel a: overlaid Directionality histograms (Fourier, 2 deg bins).
Panel b: fitted main angle ± dispersion.

Looks for histA.dat, histB.dat, histC.dat in the same folder
(tab-separated: angle_deg, amount, fit). If they are missing,
the script still draws panel b from the official FIJI fit values.

Output: Figure_orientation_journal.png / .pdf
"""

from pathlib import Path
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

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

# Official FIJI Directionality Gaussian-fit summary
CENTERS = np.array([-7.50, -1.99, -10.50])  # deg
DISPS   = np.array([16.71, 23.72, 19.17])   # deg
LABELS  = ["A", "B", "C"]


def load_hist(path):
    ang, amt, fit = [], [], []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.replace(",", " ").split()
            a, b, c = map(float, parts[:3])
            ang.append(a); amt.append(b); fit.append(c)
    return np.array(ang), np.array(amt), np.array(fit)


hists = {}
for key, name in zip(LABELS, ["histA.dat", "histB.dat", "histC.dat"]):
    p = HERE / name
    if p.exists():
        hists[key] = load_hist(p)

fig, axes = plt.subplots(
    1, 2, figsize=(7.5, 3.25),
    gridspec_kw={"width_ratios": [1.35, 1], "wspace": 0.36},
)

ax = axes[0]
styles = {"A": ("-", 1.15), "B": ("--", 1.15), "C": (":", 1.15)}
if hists:
    for key in LABELS:
        ang, amt, _fit = hists[key]
        ls, lw = styles[key]
        ax.plot(ang, amt, color="black", lw=lw, ls=ls, label=key)
else:
    ax.text(0.5, 0.5, "histA/B/C.dat not found", ha="center", transform=ax.transAxes)

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
