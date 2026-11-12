import json, math, os, sys, numpy as np, rasterio
from concurrent.futures import ThreadPoolExecutor
from rasterio.warp import reproject, Resampling
from rasterio.transform import from_bounds as tfb
from PIL import Image
os.environ['GDAL_DISABLE_READDIR_ON_OPEN']='EMPTY_DIR'
WC='https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_{}_Map.tif'
M=np.load('land.npy'); LAT1,LON0,R=33,-90,0.002
isl=json.load(open('islands.json')); PX=260
def box(d):
    la0,la1,lo0,lo1=d['bbox']; k=math.cos(math.radians((la0+la1)/2))
    h=la1-la0; w=(lo1-lo0)*k; s=max(h,w)*1.12+0.004
    cy,cx=(la0+la1)/2,(lo0+lo1)/2
    return cy-s/2,cy+s/2,cx-s/2/k,cx+s/2/k
def colour(land):
    img=np.zeros(land.shape+(3,),np.uint8); img[:]=(207,227,234); img[land]=(226,211,173); return img
def one(d):
    fn=f"thumbs/{d['id']}.png"
    if os.path.exists(fn): return
    la0,la1,lo0,lo1=box(d)
    if d['km2']>400:
        y0=int((LAT1-la1)/R); y1=int((LAT1-la0)/R); x0=int((lo0-LON0)/R); x1=int((lo1-LON0)/R)
        land=M[max(y0,0):y1,max(x0,0):x1].astype(bool)
        im=Image.fromarray(colour(land)).resize((PX,PX),Image.NEAREST)
    else:
        T=tfb(lo0,la0,lo1,la1,PX*2,PX*2); out=np.zeros((PX*2,PX*2),np.uint8)
        for la in range(int(la0//3*3),int(la1)+1,3):
            for lo in range(int(lo0//3*3),int(lo1)+1,3):
                t=f'N{la:02d}W{-lo:03d}'
                try:
                    with rasterio.open(WC.format(t)) as r:
                        reproject(rasterio.band(r,1),out,dst_transform=T,dst_crs='EPSG:4326',resampling=Resampling.mode,init_dest_nodata=False)
                except Exception: pass
        land=(out!=80)&(out!=0)
        im=Image.fromarray(colour(land)).resize((PX,PX),Image.LANCZOS)
    im.save(fn)
with ThreadPoolExecutor(16) as ex:
    for i,_ in enumerate(ex.map(one,isl)):
        if i%50==0: print(i,flush=True)
print('done')
