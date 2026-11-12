"""Sharp shapes and satellite photos for any place, from free open data on AWS.

  python3 satview.py shape  "Bimini" 25.66 25.78 -79.32 -79.22 out.png
  python3 satview.py photo  "Bimini" 25.66 25.78 -79.32 -79.22 out.png

shape = ESA WorldCover 2021 (10 m land/water map): crisp coastlines, lakes, lagoons.
photo = Sentinel-2 true colour (10 m), least-cloudy recent scene.
Bounds are lat_min lat_max lon_min lon_max (west negative). North is up.
Needs: pip install rasterio mgrs pillow numpy
"""
import json, math, os, sys, urllib.request, re
import numpy as np, rasterio, mgrs
from rasterio.windows import from_bounds
from rasterio.warp import transform_bounds, reproject, Resampling
from rasterio.transform import from_bounds as tfb
from PIL import Image, ImageDraw

os.environ.setdefault('GDAL_DISABLE_READDIR_ON_OPEN', 'EMPTY_DIR')
WC = 'https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_{}_Map.tif'
S2 = 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/'

def grid(lat0, lat1, lon0, lon1, px=900):
    k = math.cos(math.radians((lat0 + lat1) / 2))
    w, h = (lon1 - lon0) * k, lat1 - lat0
    W, H = (px, max(1, int(px * h / w))) if w >= h else (max(1, int(px * w / h)), px)
    return W, H, tfb(lon0, lat0, lon1, lat1, W, H)

def wc_tiles(lat0, lat1, lon0, lon1):
    for la in range(int(math.floor(lat0 / 3) * 3), int(lat1) + 1, 3):
        for lo in range(int(math.floor(lon0 / 3) * 3), int(lon1) + 1, 3):
            yield ('N' if la >= 0 else 'S') + f'{abs(la):02d}' + ('E' if lo >= 0 else 'W') + f'{abs(lo):03d}'

def shape(lat0, lat1, lon0, lon1, px=900):
    W, H, T = grid(lat0, lat1, lon0, lon1, px)
    out = np.zeros((H, W), np.uint8)
    for t in wc_tiles(lat0, lat1, lon0, lon1):
        try:
            with rasterio.open(WC.format(t)) as r:
                reproject(rasterio.band(r, 1), out, dst_transform=T, dst_crs='EPSG:4326',
                          resampling=Resampling.mode, init_dest_nodata=False)
        except Exception as e:
            print('skip', t, e)
    land = (out != 80) & (out != 0)
    img = np.zeros((H, W, 3), np.uint8); img[:] = (207, 227, 234); img[land] = (226, 211, 173)
    img[out == 95] = (150, 190, 140)  # mangroves
    return Image.fromarray(img)

def scenes(lat, lon, months):
    tile = mgrs.MGRS().toMGRS(lat, lon, MGRSPrecision=0)
    m = re.match(r'(\d+)([A-Z])([A-Z]{2})', tile); z, b, sq = m.groups()
    for y, mo in months:
        p = f'sentinel-s2-l2a-cogs/{int(z)}/{b}/{sq}/{y}/{mo}/'
        xml = urllib.request.urlopen(S2 + f'?list-type=2&delimiter=/&prefix={p}', timeout=30).read().decode()
        for pre in re.findall(r'<Prefix>(' + re.escape(p) + r'[^<]+/)</Prefix>', xml):
            sid = pre.rstrip('/').split('/')[-1]
            try:
                meta = json.load(urllib.request.urlopen(S2 + pre + sid + '.json', timeout=30))
                yield meta['properties'].get('eo:cloud_cover', 100), S2 + pre + 'TCI.tif'
            except Exception:
                pass

def photo(lat0, lat1, lon0, lon1, px=900):
    W, H, T = grid(lat0, lat1, lon0, lon1, px)
    months = [(2025, m) for m in (4, 3, 2, 1)] + [(2024, m) for m in (12, 11, 5, 4, 3)]
    best = sorted(scenes((lat0 + lat1) / 2, (lon0 + lon1) / 2, months))[:3]
    out = np.zeros((3, H, W), np.uint8)
    for cc, url in best:
        tmp = np.zeros((3, H, W), np.uint8)
        with rasterio.open(url) as r:
            for i in range(3):
                reproject(rasterio.band(r, i + 1), tmp[i], dst_transform=T, dst_crs='EPSG:4326',
                          resampling=Resampling.bilinear)
        hole = out.sum(0) == 0
        out[:, hole] = tmp[:, hole]
        print(f'used scene cloud {cc:.0f}%')
        if (out.sum(0) == 0).mean() < 0.01: break
    return Image.fromarray(out.transpose(1, 2, 0))

def label(img, text):
    o = Image.new('RGB', (img.width, img.height + 26), 'white'); o.paste(img, (0, 0))
    ImageDraw.Draw(o).text((6, img.height + 6), text, fill='black'); return o

if __name__ == '__main__':
    mode, name = sys.argv[1], sys.argv[2]
    lat0, lat1, lon0, lon1 = map(float, sys.argv[3:7])
    img = (shape if mode == 'shape' else photo)(lat0, lat1, lon0, lon1)
    label(img, f'{name}  {lat0:.3f}-{lat1:.3f}N {lon0:.3f}-{lon1:.3f}  (north up)').save(sys.argv[7])
