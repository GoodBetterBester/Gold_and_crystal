"""Shallow-water (reef and bank) map from public terrain tiles with sea-floor depth.

  python3 seabed.py ZOOM LAT_MIN LAT_MAX LON_MIN LON_MAX out.png [LAT,LON ...]

Light blue = shallower than 40 m, pale = shallower than 10 m, tan = land. Extra LAT,LON pairs are marked with a red X.
Tiles: elevation-tiles-prod.s3.amazonaws.com (terrarium). Cached in the current folder.
"""
import math, os, sys, urllib.request, numpy as np, concurrent.futures as cf
from PIL import Image, ImageDraw
Z=int(sys.argv[1]); lat0,lat1,lon0,lon1=map(float,sys.argv[2:6]); out=sys.argv[6]
def xy(lat,lon,z):
    n=2**z; return (lon+180)/360*n,(1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n
x0,y1=xy(lat0,lon0,Z); x1,y0=xy(lat1,lon1,Z)
X=range(int(x0),int(x1)+1); Y=range(int(y0),int(y1)+1)
def get(t):
    x,y=t; f=f'{Z}_{x}_{y}.png'
    if not os.path.exists(f): urllib.request.urlretrieve(f'https://elevation-tiles-prod.s3.amazonaws.com/terrarium/{Z}/{x}/{y}.png',f)
with cf.ThreadPoolExecutor(16) as ex: list(ex.map(get,[(x,y) for x in X for y in Y]))
E=np.zeros((256*len(Y),256*len(X)),np.float32)
for i,x in enumerate(X):
  for j,y in enumerate(Y):
    a=np.asarray(Image.open(f'{Z}_{x}_{y}.png').convert('RGB')).astype(np.float32)
    E[j*256:(j+1)*256,i*256:(i+1)*256]=a[...,0]*256+a[...,1]+a[...,2]/256-32768
px=lambda lat,lon:((xy(lat,lon,Z)[0]-X.start)*256,(xy(lat,lon,Z)[1]-Y.start)*256)
img=np.zeros(E.shape+(3,),np.uint8); img[:]=(20,40,90)
img[E>-200]=(60,120,170); img[E>-40]=(120,210,220); img[E>-10]=(170,235,235); img[E>0]=(200,180,120)
im=Image.fromarray(img); d=ImageDraw.Draw(im)
# graticule
for la in range(int(lat0),int(lat1)+1):
    _,y=px(la,lon0); d.line([(0,y),(im.width,y)],fill=(255,255,255)); d.text((3,y+2),f'{la}N',fill='white')
for lo in range(int(lon0),int(lon1)+1):
    x,_=px(lat0,lo); d.line([(x,0),(x,im.height)],fill=(255,255,255)); d.text((x+2,3),f'{-lo}W',fill='white')
for p in sys.argv[7:]:
    la,lo=map(float,p.split(',')); x,y=px(la,lo); d.line([(x-8,y-8),(x+8,y+8)],fill='red',width=3); d.line([(x-8,y+8),(x+8,y-8)],fill='red',width=3)
(xa,ya),(xb,yb)=px(lat1,lon0),px(lat0,lon1)
im.crop((int(xa),int(ya),int(xb),int(yb))).save(out); print(out)
