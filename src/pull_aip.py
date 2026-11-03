from pathlib import Path
import requests

URL = "https://www.aip.com.au/pricing/terminal-gate-prices"
OUT = Path("data/raw/aip_tgp.html")

headers = {"User-Agent": "MohitFuelProject/0.1 (RMIT student)"}

print("Downloading AIP terminal gate prices...")
response = requests.get(URL, headers=headers, timeout=60)
print("Status code:", response.status_code)
response.raise_for_status()

OUT.write_text(response.text, encoding="utf-8")
print("Saved", OUT)
print("Bytes:", OUT.stat().st_size)