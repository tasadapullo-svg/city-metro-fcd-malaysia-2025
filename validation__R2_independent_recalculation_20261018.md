# Frozen R2 numerical audit (2026-10-18)

Source: public GitHub `tasadapullo-svg/city-metro-fcd-malaysia-2025`, default branch `main`, processed paired master workbook `data__processed__TomTom_Malaysia_7Cities_City_Metro_2025_Master.xlsx`, Git blob SHA `05b749ff148b5bc74011c820a2a4d8b872a19765`.

## Independently checked against the actual GitHub workbook

- Annual independent city cases: 7; matched City/Metro annual records: 14.
- Mean absolute symmetric indicator sensitivity, %: congestion **11.3738823**, TT10 **19.1600531**, rush-hour speed burden **18.3077004**, 15-minute distance burden **19.0287348**. These reproduce 11.37, 19.16, 18.31, and 19.03 in the R1 manuscript (or 11.4, 19.2, 18.3, 19.0 at one decimal place).
- Composite M0–M5: the two highest-sensitivity cases are **Kota Bharu and Ipoh** in all six tested specifications. Rank order within that pair is not necessarily identical.
- Identical Top-2/Top-3 screening rules for congestion, TT10, speed: Jaccard overlaps **1/3, 1/2, 1, 3/4, 1/3, 1/2** respectively, with **5 of 6** non-identical shortlists; tie-inclusive Top-3 may contain four Metropolitan Area cases for TT10.
- PAI Equation (9): 28 cleaned AM/PM records, seven city-level signed contrasts. Compared to Figure 5(c), **7/7** agree to three displayed decimals.
- Temporal Absolute Sensitivity Equation (7): 7,056 hourly-profile entries corresponding to 3,528 City/Metro pairs. **21/21** city–indicator TAS values agree to two displayed decimals; no missing/duplicate day-hour pairs.
- Monthly congestion Equation (8): 336 records overall (2024–2025), **12 matched 2025 months per city**, and **7/7** reported 2025 mean signed monthly gaps agree.
- Johor Bahru: City annual congestion 39.5, Metro 38.8; annual absolute normalized gap **1.78799489%**, 24×7 congestion TAS **15.49363210%**, and unrounded difference **13.70563721 percentage points**, reported correctly as **13.71**.

### Seven signed PAI contrasts (unrounded)

| Urban case | ΔPAI (City − Metropolitan Area) |
|---|---:|
| George Town | −0.03245153 |
| Kota Bharu | +0.04470277 |
| Kuala Lumpur | +0.04946912 |
| Seberang Perai | −0.13494710 |
| Johor Bahru | −0.03815760 |
| Ipoh | +0.02701286 |
| Kajang | −0.00530282 |

### 24×7 TAS percentages, independently recomputed

| Urban case | Congestion | TT10 | Speed |
|---|---:|---:|---:|
| George Town | 13.63 | 20.17 | 19.43 |
| Kota Bharu | 28.68 | 26.44 | 25.11 |
| Kuala Lumpur | 14.46 | 16.56 | 16.53 |
| Seberang Perai | 17.99 | 4.00 | 3.78 |
| Johor Bahru | 15.49 | 27.69 | 28.73 |
| Ipoh | 15.04 | 33.68 | 35.47 |
| Kajang | 7.26 | 10.11 | 10.42 |

## Execution and scope statement

The published-target recomputations above used a separate read-only numerical extraction from the actual GitHub workbook, rather than trusting saved outputs or the old workbook validation report. The newly packaged Python verification tool was separately syntax-checked and its XLSX → anonymous CSV → rerun path was tested for equality of all six output tables on a **synthetic structure-compatible fixture**. The Python tool's `--check` path must still be run on the authentic GitHub workbook by the author before the reviewer-facing archive is attached and submission completion is claimed. Synthetic fixture numerical outputs are **not** research evidence and are not included in this GitHub update.

No source data, figures, original equations or reported results were edited.
