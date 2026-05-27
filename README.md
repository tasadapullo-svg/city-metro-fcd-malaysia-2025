# Malaysia 7 Cities Traffic Performance Dataset Package (TomTom + OSM + Population/Vehicle)

Prepared for: Sun Wenjie, Faculty of Built Environment and Surveying, Universiti Teknologi Malaysia.  
Package version: 2026-05-07 recalibrated monthly coverage.

## Purpose

This package supports an exploratory urban traffic-performance manuscript using platform-reported TomTom Traffic Index indicators, OpenStreetMap road-network indicators, and population/vehicle background proxies for seven Malaysian cities.

## City coverage

1. George Town
2. Kota Bharu
3. Kuala Lumpur
4. Seberang Perai
5. Johor Bahru
6. Ipoh
7. Kajang

## Directory structure

```text
Malaysia_7Cities_Traffic_Dataset_Package/
├─ data/
│  ├─ raw/
│  │  ├─ tomtom_screenshots/
│  │  ├─ tomtom_city_workbooks/
│  │  ├─ osm_boundaries/
│  │  ├─ osm_road_edges/
│  │  └─ population_vehicle/
│  └─ processed/
│     ├─ TomTom_source_log.xlsx
│     ├─ TomTom_7Cities_heatmap_long_2025.xlsx
│     ├─ TomTom_7Cities_monthly_congestion_long_2025.xlsx
│     ├─ TomTom_7Cities_rush_hour_long_2025.xlsx
│     ├─ Malaysia_7Cities_master_dataset.xlsx
│     ├─ OSM_road_network_indicators_7_cities_recalibrated.xlsx
│     └─ population_vehicle_indicators_7_cities.xlsx
├─ scripts/
├─ validation/
└─ docs/
```

## Key processed files

| File | Description | Coverage |
|---|---|---:|
| `TomTom_source_log.xlsx` | Screenshot-level traceability log | 70 screenshot records |
| `TomTom_7Cities_heatmap_long_2025.xlsx` | 24 × 7 driving-pattern data for travel time, congestion and speed | 7056 records |
| `TomTom_7Cities_monthly_congestion_long_2025.xlsx` | Monthly congestion values for City/Metro, 2024/2025, Jan-Dec | 336 records |
| `TomTom_7Cities_rush_hour_long_2025.xlsx` | Morning/evening rush-hour summaries | 38 records |
| `Malaysia_7Cities_master_dataset.xlsx` | Merged TomTom + OSM + population/vehicle city-level master file | 7 cities |

## Monthly congestion recalibration

The monthly congestion table has been updated to full January–December coverage:

```text
7 cities × 2 scales × 2 years × 12 months = 336 monthly records
```

For the six recalibrated cities, the values were transcribed from the latest uploaded `20260507图片.zip` overview screenshots. City monthly values come from `1.png`; Metro monthly values come from `2.png`. George Town already had full Jan-Dec coverage in the original extraction workbook.

## Methodological caveat

TomTom indicators are treated as platform-reported comparative indicators. They are not interpreted as ground-truth detector observations. OSM boundaries are used as contextual spatial units and are not assumed to reproduce proprietary TomTom reporting boundaries.

## Recommended citation statement for data availability

The processed indicator tables, source logs, screenshots, spatial boundary files, OSM road-edge files, and analysis scripts are provided in this replication package. Raw platform algorithms and proprietary TomTom reporting boundaries are not redistributed or reconstructed.
