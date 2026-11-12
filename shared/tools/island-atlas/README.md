# Island atlas

Live page: https://claude.ai/artifact/5y2NW6RhDr3aAx2w8oaKm9 (private)

880 islands (> 1 km²) between Florida and Barbados, from ESA WorldCover 2021 (10 m).
Rebuild: `python3 mosaic.py && python3 islands.py && python3 render.py` (needs rasterio, scipy, geonamescache, pillow).
`islands.json` has id, nearby-town name, area and bounding box for each island.
