#!/usr/bin/env python3
"""
Fiber diameter figure (mean ± SD + histogram).
Reads FIJI Results CSVs from Lab2Figi/diameter/.
Writes figures/python/Figure_diameter_journal.png and .pdf.
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA = HERE / "Lab2Figi" / "diameter"
OUT = HERE / "figures" / "python"
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    "A": DATA / "a-Results-1000x.csv",
    "B": DATA / "b-Results-1000x.csv",
    "C": DATA / "c-Results-1000x.csv",
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
    "savefig.pad_inches": 0.04,
    "savefig.facecolor": "white",
    "pdf.fonttype": 42,
})


def load_length(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run this script from the repo root.")
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    header = [h.strip() for h in rows[0]]
    col = header.index("Length")
    return np.array([float(r[col]) for r in rows[1:] if r and r[col].strip()])


A = load_length(FILES["A"])
B = load_length(FILES["B"])
C = load_length(FILES["C"])
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

fig.savefig(OUT / "Figure_diameter_journal.png")
fig.savefig(OUT / "Figure_diameter_journal.pdf")
print("wrote", OUT / "Figure_diameter_journal.png")
print(f"combined mean ± SD = {allv.mean():.2f} ± {allv.std(ddof=1):.2f} µm  n={len(allv)}")
