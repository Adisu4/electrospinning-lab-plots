#!/usr/bin/env python3
"""
Fiber diameter figure (mean ± SD + histogram).
Output: Figure_diameter_journal.png / .pdf in the same folder.

Requires: matplotlib, numpy
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
    "savefig.pad_inches": 0.04,
    "savefig.facecolor": "white",
    "pdf.fonttype": 42,
})

# Length column from FIJI, 1000x images (µm). 20 fibers per image.
A = np.array([
    0.76, 1.26, 0.612, 0.679, 0.39, 0.589, 0.315, 1.164, 0.383, 0.871,
    1.228, 0.428, 0.464, 1.231, 0.745, 0.92, 0.406, 0.499, 1.252, 0.341,
])
B = np.array([
    0.805, 0.977, 0.905, 0.944, 0.48, 0.467, 0.71, 0.874, 0.765, 1.008,
    0.722, 0.749, 0.782, 0.436, 0.45, 0.645, 1.052, 1.114, 0.47, 0.585,
])
C = np.array([
    0.905, 0.255, 0.651, 0.337, 0.674, 0.382, 0.618, 0.604, 0.744, 0.235,
    0.302, 0.337, 0.375, 0.242, 0.52, 0.45, 0.954, 0.577, 0.645, 0.375,
])
allv = np.concatenate([A, B, C])

means = [A.mean(), B.mean(), C.mean()]
sds = [A.std(ddof=1), B.std(ddof=1), C.std(ddof=1)]

fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2), gridspec_kw={"wspace": 0.34})

ax = axes[0]
x = np.arange(3)
ax.bar(
    x, means, yerr=sds, width=0.52,
    facecolor="#C8C8C8", edgecolor="black", linewidth=0.9,
    capsize=3.2, error_kw=dict(ecolor="black", lw=0.9, capthick=0.9),
    zorder=3,
)
ax.set_xticks(x)
ax.set_xticklabels(["A", "B", "C"])
ax.set_xlabel("Image")
ax.set_ylabel("Fiber diameter (µm)")
ax.set_ylim(0, 1.35)
ax.set_xlim(-0.55, 2.55)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for i, (m, s) in enumerate(zip(means, sds)):
    ax.text(i, m + s + 0.06, f"{m:.2f} ± {s:.2f}", ha="center", va="bottom", fontsize=8)
ax.text(-0.55, 1.35, "a", fontsize=13, fontweight="bold", va="bottom", ha="right")

ax = axes[1]
bins = np.arange(0.20, 1.40, 0.10)
ax.hist(allv, bins=bins, color="#C8C8C8", edgecolor="black", linewidth=0.8, zorder=3)
ax.axvline(allv.mean(), color="black", lw=1.15, linestyle="--")
ax.set_xlabel("Fiber diameter (µm)")
ax.set_ylabel("Count")
ax.set_xlim(0.15, 1.40)
ax.set_ylim(0, 18)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.text(allv.mean() + 0.04, 16.4, f"mean = {allv.mean():.2f} µm", fontsize=8)
ax.text(0.15, 18, "b", fontsize=13, fontweight="bold", va="bottom", ha="right")

fig.savefig(HERE / "Figure_diameter_journal.png")
fig.savefig(HERE / "Figure_diameter_journal.pdf")
print("wrote", HERE / "Figure_diameter_journal.png")
print(f"combined mean ± SD = {allv.mean():.2f} ± {allv.std(ddof=1):.2f} µm  n={len(allv)}")
