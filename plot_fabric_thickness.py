#!/usr/bin/env python3
"""Fabric thickness figure (mean ± SD).
Reads FIJI Results CSVs from Lab2Figi/thickness/.
Writes figures/python/Figure_thickness_journal.png and .pdf.
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA = HERE / "Lab2Figi" / "thickness"
OUT = HERE / "figures" / "python"
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    "A": DATA / "a-Results-x100.csv",
    "B": DATA / "b-Results-x100.csv",
    "C": DATA / "c-Results-x100.csv",
}

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

fig.savefig(OUT / "Figure_thickness_journal.png")
fig.savefig(OUT / "Figure_thickness_journal.pdf")
allv = np.concatenate([A, B, C])
print(f"combined {allv.mean():.1f} ± {allv.std(ddof=1):.1f} µm  n={len(allv)}")
print("wrote", OUT / "Figure_thickness_journal.png")
