"""Run the ELDORIA-005 log legs from a start point (plane sailing, nautical miles).

Usage: python3 dead_reckoning.py LAT LON   (west longitudes negative)
"""
import math, sys

LEGS = [("Day 21", "E", 200), ("Day 23", "N", 175), ("Day 26", "NE", 150),
        ("Day 28", "E", 250), ("Day 30", "N", 114), ("Day 32", "W", 230)]
BEARING = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}

def run(lat, lon, legs=LEGS, compass_offset=0):
    for day, h, nm in legs:
        b = math.radians(BEARING[h] + compass_offset)
        dlat = nm * math.cos(b) / 60
        mid = math.radians(lat + dlat / 2)
        lon += nm * math.sin(b) / 60 / math.cos(mid)
        lat += dlat
        print(f"{day}: {h:>2} {nm:>3} nm -> {lat:7.3f} N, {lon:8.3f}")
    return lat, lon

if __name__ == "__main__":
    run(float(sys.argv[1]), float(sys.argv[2]))
