from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ulp = pd.read_csv("data/processed/aip_ulp.csv", index_col=0)

def short_label(col):
    cleaned = (
        col.replace("st ", " ").replace("nd ", " ").replace("rd ", " ").replace("th ", " ")
    )
    parsed = pd.to_datetime(cleaned, dayfirst=True)
    return f"{parsed.day} {parsed.strftime('%b')}"

labels = [short_label(col) for col in ulp.columns]
melbourne = ulp.loc["Melbourne"].astype(float)
sydney = ulp.loc["Sydney"].astype(float)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(labels, melbourne, marker="o", label="Melbourne")
ax.plot(labels, sydney, marker="o", label="Sydney")
ax.set_ylabel("ULP, cpl (GST in)")
ax.set_title("AIP terminal-gate ULP")
ax.legend()
ax.grid(True, axis="y", alpha=0.3)
fig.tight_layout()

out = Path("outputs/melbourne_vs_sydney.png")
fig.savefig(out, dpi=140)
print("Saved", out)
