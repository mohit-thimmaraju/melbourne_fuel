\# Should a Melbourne driver fill up this week?



\*\*As of 30 Oct 2026:\*\* Fill if the tank is low. Melbourne wholesale ULP is \*\*225.0 cpl\*\*, \*\*+3.6 cpl\*\* this week, \*\*1.5 cpl below Sydney\*\*.



| | |

| --- | --- |

| Question | Fill this week, or wait? Is Melbourne cheaper than Sydney at the gate? |

| Data | AIP Terminal Gate Prices (official weekday wholesale, GST in, cpl) |

| Tools | Python, pandas, Excel-ready CSV |

| Caveat | Wholesale is not the pump |



\## How to reproduce



```powershell

cd melbourne-fuel

.\\.venv\\Scripts\\Activate.ps1

python src\\pull\_aip.py

python src\\clean\_aip.py







```



Then open `data/processed/aip\_ulp.csv` and `outputs/findings.md`.



\## Files



| File | Why |

| --- | --- |

| `src/pull\_aip.py` | Downloads the official AIP page |

| `src/clean\_aip.py` | Turns the ULP table into a CSV |

| `data/processed/aip\_ulp.csv` | Excel source |

| `outputs/findings.md` | The call and the caveat |

