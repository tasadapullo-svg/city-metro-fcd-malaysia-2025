"""Monthly congestion recalibration values for six Malaysian cities.

The values below were transcribed from the latest 20260507 TomTom overview screenshots:
- 1.png = City overview/monthly congestion
- 2.png = Metro overview/monthly congestion

The table has complete Jan-Dec coverage for City/Metro and 2024/2025.
"""

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

MONTHLY_VALUES = {'Kota Bharu': {'City': {2025: [51, 49, 51, 51, 43, 46, 42, 45, 50, 49, 48, 51], 2024: [47, 50, 51, 54, 45, 45, 44, 43, 49, 45, 47, 51]}, 'Metro': {2025: [37, 35, 38, 42, 32, 35, 32, 32, 37, 35, 36, 37], 2024: [35, 37, 36, 42, 34, 36, 33, 34, 36, 33, 35, 37]}}, 'Kuala Lumpur': {'City': {2025: [43, 45, 42, 43, 40, 39, 44, 47, 42, 42, 47, 46], 2024: [42, 40, 44, 40, 44, 40, 41, 45, 40, 44, 45, 43]}, 'Metro': {2025: [39, 40, 38, 41, 37, 36, 40, 41, 37, 39, 42, 39], 2024: [39, 37, 40, 39, 41, 36, 38, 40, 38, 41, 42, 38]}}, 'Seberang Perai': {'City': {2025: [40, 40, 38, 44, 41, 42, 39, 41, 46, 47, 47, 43], 2024: [37, 40, 39, 40, 45, 42, 36, 42, 42, 40, 43, 43]}, 'Metro': {2025: [35, 35, 35, 37, 36, 36, 36, 36, 38, 40, 40, 39], 2024: [34, 36, 36, 37, 39, 37, 35, 37, 39, 37, 38, 39]}}, 'Johor Bahru': {'City': {2025: [38, 36, 40, 38, 39, 40, 40, 41, 39, 39, 39, 42], 2024: [38, 32, 39, 35, 36, 38, 37, 38, 39, 35, 36, 38]}, 'Metro': {2025: [39, 35, 41, 39, 38, 36, 39, 40, 38, 39, 40, 40], 2024: [40, 32, 38, 35, 37, 37, 37, 37, 36, 36, 38, 37]}}, 'Ipoh': {'City': {2025: [34, 35, 33, 32, 33, 32, 33, 36, 33, 36, 36, 38], 2024: [35, 34, 32, 32, 35, 35, 33, 35, 34, 36, 35, 37]}, 'Metro': {2025: [31, 30, 30, 29, 29, 28, 29, 30, 29, 32, 31, 33], 2024: [30, 31, 29, 29, 31, 30, 30, 30, 30, 31, 31, 31]}}, 'Kajang': {'City': {2025: [27, 30, 31, 33, 28, 26, 28, 29, 27, 30, 33, 30], 2024: [30, 29, 35, 33, 34, 28, 30, 31, 32, 31, 34, 31]}, 'Metro': {2025: [29, 31, 30, 35, 30, 28, 30, 30, 27, 29, 33, 30], 2024: [29, 29, 32, 32, 33, 29, 30, 31, 32, 31, 35, 33]}}}

EXPECTED_RECORDS = 6 * 2 * 2 * 12
actual = sum(len(MONTHLY_VALUES[city][scale][year]) for city in MONTHLY_VALUES for scale in MONTHLY_VALUES[city] for year in MONTHLY_VALUES[city][scale])
assert actual == EXPECTED_RECORDS, (actual, EXPECTED_RECORDS)
print(f"PASS: {actual} monthly recalibration values for six cities.")
