"""Template script for rebuilding TomTom long-format tables from city extraction workbooks.
This package already includes the built XLSX outputs. Use this file as an auditable processing template.
Recommended dependencies for local rebuild: pandas, openpyxl.
"""
from pathlib import Path
import pandas as pd

CITY_FILES = {
    "George Town":"George_Town_2025_TomTom_extracted_data.xlsx",
    "Kota Bharu":"Kota_Bharu_traffic_2025_extracted.xlsx",
    "Kuala Lumpur":"Kuala_Lumpur_2025_TomTom_extracted_data.xlsx",
    "Seberang Perai":"Seberang_Perai_traffic_2025_from_images.xlsx",
    "Johor Bahru":"Johor_Bahru_TomTom_2025_extracted_data.xlsx",
    "Ipoh":"Ipoh_TomTom_2025_extracted.xlsx",
    "Kajang":"Kajang_TomTom_2025_extracted_data.xlsx",
}

# This template intentionally avoids fabricating missing values.
# Example rule: if a workbook lacks Monthly_Congestion, write a coverage note rather than imputing values.

def main():
    print("Use the processed XLSX files included in data/processed as the controlled version.")
    print("For full rebuild, implement city-specific sheet mappings documented in README.md.")

if __name__ == "__main__":
    main()
