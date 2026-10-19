# Malaysia Seven-City City–Metro FCD Reproducibility Package

Prepared for: Sun Wenjie, Faculty of Built Environment and Surveying, Universiti Teknologi Malaysia.  
Package version: 2026-10-19 CSTP R2 reproducibility update.

## Purpose

This package supports an exploratory urban traffic-performance manuscript using platform-reported TomTom Traffic Index indicators, OpenStreetMap road-network indicators, and population/vehicle background proxies for seven Malaysian cities.

## CSTP R2 reproducibility

The R2 verification workflow independently recomputes the manuscript's annual sensitivity, M0–M5 robustness, Top-2/Top-3 screening, peak asymmetry (PAI), 24×7 temporal absolute sensitivity (TAS), and monthly congestion results from the frozen processed master workbook.

```bash
python -m pip install "openpyxl>=3.1"
python scripts__05_reproduce_cstp_r2.py --check --output-dir r2_reproduction
```

To also generate the self-contained, de-identified reviewer archive:

```bash
python scripts__05_reproduce_cstp_r2.py --check --output-dir r2_reproduction --build-review-package CSTP_R2_Reviewer_Verification.zip
```

See [`README_R2_REPRODUCIBILITY.md`](README_R2_REPRODUCIBILITY.md) for inputs, outputs, reviewer instructions, and scientific boundaries. The generated output directory and reviewer ZIP are verification artifacts and are not committed to this repository.

## City coverage

1. George Town
2. Kota Bharu
3. Kuala Lumpur
4. Seberang Perai
5. Johor Bahru
6. Ipoh
7. Kajang

## Repository structure

```text
city-metro-fcd-malaysia-2025/
├─ data__processed__*.xlsx
├─ data__raw__*.xlsx / *.parquet / *.geojson
├─ scripts__*.py
├─ validation__*
├─ docs__*.docx
├─ README_R2_REPRODUCIBILITY.md
├─ README_FLAT_PACKAGE.md
└─ FILE_MANIFEST.csv
```

The public GitHub package is intentionally flat. Double underscores in filenames preserve the original directory roles. Raw TomTom screenshots are excluded because redistribution rights are restricted.

## Key processed files

| File | Description | Coverage |
|---|---|---:|
| `data__processed__TomTom_Malaysia_7Cities_City_Metro_2025_Master.xlsx` | Frozen City–Metro master workbook used by the R2 verification script | 7 cities; 13 worksheets |
| `data__processed__TomTom_source_log.xlsx` | Screenshot-level traceability log | 70 source records |
| `data__processed__TomTom_7Cities_heatmap_long_2025.xlsx` | 24 × 7 driving-pattern data for travel time, congestion and speed | 7,056 records |
| `data__processed__TomTom_7Cities_monthly_congestion_long_2025.xlsx` | Monthly congestion values for City/Metro, 2024–2025, January–December | 336 records |
| `data__processed__TomTom_7Cities_rush_hour_long_2025.xlsx` | Legacy/mixed rush-hour export; not the PAI verification input | 38 records |

For PAI, the R2 workflow uses the cleaned 28-record `03_rush_hour_clean` worksheet in the frozen master workbook.

## Monthly congestion recalibration

The monthly congestion table has been updated to full January–December coverage:

```text
7 cities × 2 scales × 2 years × 12 months = 336 monthly records
```

For the six recalibrated cities, the values were transcribed from the latest uploaded `20260507图片.zip` overview screenshots. City monthly values come from `1.png`; Metro monthly values come from `2.png`. George Town already had full Jan-Dec coverage in the original extraction workbook.

## Methodological caveat

TomTom indicators are treated as platform-reported comparative indicators. They are not interpreted as ground-truth detector observations. OSM boundaries are used as contextual spatial units and are not assumed to reproduce proprietary TomTom reporting boundaries.

## Recommended citation statement for data availability

The processed indicator tables, source logs, permitted spatial boundary files, OSM road-edge files, and analysis scripts are provided in this replication package. Raw TomTom screenshots, platform algorithms, and proprietary TomTom reporting boundaries are not redistributed or reconstructed.
