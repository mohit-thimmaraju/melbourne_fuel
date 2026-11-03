from io import StringIO
from pathlib import Path
import pandas as pd

html = Path("data/raw/aip_tgp.html").read_text(encoding="utf-8")
ulp = pd.read_html(StringIO(html))[0]
ulp.to_csv("data/processed/aip_ulp.csv", index=False)

print("Saved data/processed/aip_ulp.csv")
print()
print(ulp.to_string(index=False))
