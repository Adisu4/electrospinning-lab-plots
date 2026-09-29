#!/usr/bin/env python3
"""Fabric thickness figure (mean ± SD)."""

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
    "savefig.dpi": 400,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.04,
    "savefig.facecolor": "white",
    "pdf.fonttype": 42,
})

A = np.array([67.465, 73.176, 69.200])
B = np.array([64.516, 69.387, 69.543])
C = np.array([78.457, 72.237, 70.352])
means = [A.mean(), B.mean(), C.mean()]
sds = [A.std(ddof=1), B.std(ddof=1), C.std(ddof=1)]

fig, ax = plt.subplots(figsize=(3.6, 3.2))
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
ax.set_ylabel("Fabric thickness (µm)")
ax.set_ylim(0, 90)
ax.set_xlim(-0.55, 2.55)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for i, (m, s) in enumerate(zip(means, sds)):
    ax.text(i, m + s + 2.2, f"{m:.1f} ± {s:.1f}", ha="center", va="bottom", fontsize=8)

fig.savefig(HERE / "Figure_thickness_journal.png")
fig.savefig(HERE / "Figure_thickness_journal.pdf")
allv = np.concatenate([A, B, C])
print(f"combined {allv.mean():.1f} ± {allv.std(ddof=1):.1f} µm  n={len(allv)}")
