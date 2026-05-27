"""Build a TomTom screenshot source log.
Edit CAPTURE_DATE and SOURCE_URLS if screenshots are recollected.
"""
from pathlib import Path
import csv
CITIES = ["George Town", "Kota Bharu", "Kuala Lumpur", "Seberang Perai", "Johor Bahru", "Ipoh", "Kajang"]
SOURCE_URLS = {
    "George Town":"https://www.tomtom.com/traffic-index/city/george-town",
    "Kota Bharu":"https://www.tomtom.com/traffic-index/city/kota-bharu",
    "Kuala Lumpur":"https://www.tomtom.com/traffic-index/city/kuala-lumpur",
    "Seberang Perai":"https://www.tomtom.com/traffic-index/seberang-perai-traffic",
    "Johor Bahru":"https://www.tomtom.com/traffic-index/city/johor-bahru",
    "Ipoh":"https://www.tomtom.com/traffic-index/city/ipoh",
    "Kajang":"https://www.tomtom.com/traffic-index/city/kajang",
}
IMAGE_CODEBOOK = {
    1:("overview_monthly","City"), 2:("overview_monthly","Metro"),
    3:("rush_hour","City"), 4:("rush_hour","Metro"),
    5:("heatmap_travel_time","City"), 6:("heatmap_travel_time","Metro"),
    7:("heatmap_congestion","City"), 8:("heatmap_congestion","Metro"),
    9:("heatmap_speed","City"), 10:("heatmap_speed","Metro"),
}
CAPTURE_DATE = "2026-05-07"
rows=[]
for city in CITIES:
    for image_no,(module,scale) in IMAGE_CODEBOOK.items():
        rows.append({
            "city":city,
            "data_year":2025,
            "scale":scale,
            "indicator_module":module,
            "screenshot_file":f"{image_no}.png",
            "source_platform":"TomTom Traffic Index",
            "source_url":SOURCE_URLS[city],
            "capture_date":CAPTURE_DATE,
            "extraction_method":"manual extraction from TomTom screenshots",
            "limitation":"platform-reported indicators; not ground-truth detector observations"
        })
with open("TomTom_source_log.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    writer.writeheader(); writer.writerows(rows)
print("Wrote TomTom_source_log.csv")
