"""Basic package validation checks."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
required = [
    "data/processed/TomTom_source_log.xlsx",
    "data/processed/TomTom_7Cities_heatmap_long_2025.xlsx",
    "data/processed/TomTom_7Cities_monthly_congestion_long_2025.xlsx",
    "data/processed/TomTom_7Cities_rush_hour_long_2025.xlsx",
    "data/processed/Malaysia_7Cities_master_dataset.xlsx",
    "data/raw/tomtom_screenshots",
    "data/raw/osm_boundaries",
    "data/raw/osm_road_edges",
]
missing = [p for p in required if not (ROOT/p).exists()]
print("Missing files/folders:" if missing else "All required files/folders found.")
for p in missing:
    print(" -", p)
# Count screenshot PNGs
shots=list((ROOT/"data/raw/tomtom_screenshots").glob("**/*.png"))
print(f"TomTom screenshots: {len(shots)} PNG files")
