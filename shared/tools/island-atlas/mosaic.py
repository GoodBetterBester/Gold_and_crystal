import os, numpy as np, rasterio
from concurrent.futures import ThreadPoolExecutor
from rasterio.enums import Resampling
os.environ['GDAL_DISABLE_READDIR_ON_OPEN']='EMPTY_DIR'
WC='https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_{}_Map.tif'
LAT0,LAT1,LON0,LON1=9,33,-90,-57; R=0.002; N=int(3/R)
H=int((LAT1-LAT0)/R); W=int((LON1-LON0)/R)
M=np.zeros((H,W),np.uint8)
def job(la,lo):
    t=f'N{la:02d}W{-lo:03d}'
    try:
        with rasterio.open(WC.format(t)) as r:
            a=r.read(1,out_shape=(N,N),resampling=Resampling.nearest)
    except Exception: return t,None
    return (la,lo),a
jobs=[(la,lo) for la in range(LAT0,LAT1,3) for lo in range(LON0,LON1,3)]
with ThreadPoolExecutor(12) as ex:
    for k,a in ex.map(lambda x: job(*x), jobs):
        if a is None: continue
        la,lo=k; y0=int((LAT1-(la+3))/R); x0=int((lo-LON0)/R)
        M[y0:y0+N,x0:x0+N]=((a!=80)&(a!=0)).astype(np.uint8)
        print('ok',k,flush=True)
np.save('land.npy',M); print(M.shape, M.mean())
