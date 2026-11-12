"""ELDORIA-004: find the X from the triangle.

Side marks are Maya base-20 numbers (bar = 5, dot = 1, shell = 0, two places):
base = 100, Bimini side = 105, Tulum side = 101. The base is Shark Mound -> Tulum.
Needs: pip install pyproj
"""
import math
from pyproj import Geod

g = Geod(ellps="WGS84")
SHARK_MOUND = (25.7491, -79.24753)
TULUM = (20.216, -87.428)

def solve(a, b, ra, rb, R=6371000.0):
    """Points ra metres from a and rb metres from b (both solutions)."""
    az, _, d = g.inv(a[1], a[0], b[1], b[0])
    cos_a = (math.cos(rb / R) - math.cos(ra / R) * math.cos(d / R)) / (math.sin(ra / R) * math.sin(d / R))
    ang = math.degrees(math.acos(cos_a))
    out = []
    for s in (1, -1):
        lon, lat, _ = g.fwd(a[1], a[0], az + s * ang, ra)
        out.append((round(lat, 4), round(lon, 4)))
    return out

if __name__ == "__main__":
    base = g.inv(SHARK_MOUND[1], SHARK_MOUND[0], TULUM[1], TULUM[0])[2]
    unit = base / 100
    print(f"base {base/1000:.0f} km, unit {unit/1000:.2f} km")
    for p in solve(SHARK_MOUND, TULUM, 105 * unit, 101 * unit):
        print(p)   # southern one = Bajo Nuevo Bank
