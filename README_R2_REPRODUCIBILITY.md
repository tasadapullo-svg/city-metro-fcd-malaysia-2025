# CSTP R2: deterministic verification of the seven-city City–Metro comparisons

This read-only workflow reproduces the *descriptive* outputs used in the manuscript from the validated 2025 City–Metro master workbook. It does not create new experiments or change the observed TomTom records. The script can also create a **de-identified reviewer archive** that contains only the indicator fields and selected source-index fields needed to verify the paper.

## Input

The public repository already contains the original, unchanged processed workbook:

`data__processed__TomTom_Malaysia_7Cities_City_Metro_2025_Master.xlsx`

The script reads the following sheets without modifying the workbook:

| Worksheet | Used for | Expected records |
|---|---|---:|
| `01_annual_overview` | Four indicator differences, composite scores, Top-2/Top-3 | 14 |
| `02_monthly_congestion` | 2025 paired monthly TAS and signed gap | 336 including 2024 |
| `03_rush_hour_clean` | AM/PM 10-km travel time and PAI | 28 |
| `04_heatmap_long` | 7 cities × 2 units × 3 indicators × 168 day–hour cells | 7,056 |
| `09_source_audit` | Traceability/index only | 70 |
| `11_validation` | Confirmed presence, not used as a substitute for recomputation | existing |

The original `data__processed__TomTom_7Cities_rush_hour_long_2025.xlsx` includes legacy/mixed records; do **not** use it in place of the cleaned 28-record worksheet for PAI.

## 1. Run reproducibility checks on the unchanged master workbook

Install Python 3.9 or newer and `openpyxl`:

```bash
python -m pip install openpyxl
python scripts__05_reproduce_cstp_r2.py --check --output-dir r2_reproduction
```

If the workbook is stored elsewhere:

```bash
python scripts__05_reproduce_cstp_r2.py --master "C:/path/to/TomTom_Malaysia_7Cities_City_Metro_2025_Master.xlsx" --check --output-dir r2_reproduction
```

**Important:** `--check` is required for a rounded-result PASS. Without it, the script only computes outputs and does not certify correspondence with the published numerical targets. For its `--check` mode the script verifies four annual summary metrics, the six M0–M5 Top-2 groups, six Top-k overlaps, seven PAI differences, 21 TAS entries, seven signed monthly gaps, and Johor Bahru's unrounded TAS–annual contrast. A nonzero exit status indicates failure. The summary JSON captures input SHA-256, counts and validation outcomes.

The outputs are:

- `annual_sensitivity.csv`
- `robustness_M0_M5.csv`
- `screening_top2_top3.csv`
- `peak_asymmetry_PAI.csv`
- `temporal_absolute_sensitivity_TAS.csv`
- `monthly_congestion_2025.csv`
- `reproduction_summary.json`

## 2. Prepare an author-free supplementary archive for double-anonymized review

```bash
python scripts__05_reproduce_cstp_r2.py --check --output-dir r2_reproduction --build-review-package CSTP_R2_Reviewer_Verification.zip
```

This creates a separate archive containing the above outputs, the executable script, compact data CSVs, a non-identifying 70-record source-audit index and an instruction file. The archive **does not** include a link to the author-identified GitHub account, the unfiltered master workbook, the identity-related `extracted_by` metadata, source screenshots or proprietary polygons/algorithms. Review every generated file before submitting it. Upload the *generated archive* via the journal's reviewer-facing supplementary-files route; do **not** upload this GitHub update ZIP instead.

Reviewer command after extracting that archive:

```bash
python -m pip install openpyxl
python reproduce_review_results.py --data-dir data --check --output-dir rerun
```

## Sharing and scientific boundaries

- The GitHub repository README currently includes author-identifying information; **do not use this repository URL as an anonymized reviewer link**.
- Do not upload screenshots from TomTom or proprietary raw/platform materials without confirming redistribution permission.
- The package offers numerical reproducibility from previously extracted provider-reported values. It does **not** validate either geographic reporting unit against detector observations, nor infer causal effects of unpublished TomTom boundaries, probes or weighting rules.
- Annual, monthly and 168-slot summaries are descriptive. The cross-city sample remains seven urban areas.
- The legacy `scripts__02_build_tomtom_long_tables.py` is a template, and the legacy `scripts__03_validate_dataset_package.py` uses pre-flattening directory paths. The new script is a self-contained entry point for the manuscript's reported numerical outputs, without overwriting either older file.
- The accepted manuscript should include the correct public repository URL and a **verified** permanent archive DOI only after the journal's anonymization requirements permit identification. Do not invent a Zenodo record identifier.

**Submission gate:** the response to Reviewer 1, Comment 1 can state that the supplementary verification materials *have been provided* only after the generated reviewer archive has been attached and checked in the editorial system.
