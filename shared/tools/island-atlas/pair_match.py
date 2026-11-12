import json,numpy as np
from PIL import Image,ImageDraw
from scipy import ndimage as ndi
L=np.load('land.npy'); R=0.002; LAT1=33; LON0=-90
ISL=json.load(open('islands.json'))
big=[(555,480),(600,450),(660,440),(720,425),(800,415),(850,425),(860,450),(845,500),(790,555),(730,600),(680,630),(640,635),(590,610),(560,560),(550,520)]
small=[(355,535),(390,510),(440,500),(490,510),(525,540),(560,575),(585,600),(575,615),(530,605),(470,600),(410,590),(370,575),(352,555)]
im=Image.new('L',(1000,800),0);d=ImageDraw.Draw(im);d.polygon(big,fill=255);d.polygon(small,fill=255)
SK=np.asarray(im)>0
a_b=Image.new('L',(1000,800),0);ImageDraw.Draw(a_b).polygon(big,fill=255);ab=(np.asarray(a_b)>0).sum()
print('small/big area',round((SK.sum()-ab)/ab,2))
G=96
def norm(m):
    ys,xs=np.nonzero(m); cy,cx=ys.mean(),xs.mean(); s=np.sqrt(len(ys))/(G*0.22)
    yy,xx=np.mgrid[0:G,0:G]; return ndi.map_coordinates(m.astype(float),[(yy-G/2)*s+cy,(xx-G/2)*s+cx],order=1)>0.5
base=norm(SK)
V=[];meta=[]
for mir in (0,1):
  b=base[:,::-1] if mir else base
  for ang in range(0,360,5):
    V.append(ndi.rotate(b.astype(float),ang,reshape=False,order=1)>0.5);meta.append((mir,ang))
V=np.stack(V).reshape(len(V),-1).astype(np.float32)
def px(lat,lon): return int((LAT1-lat)/R),int((lon-LON0)/R)
cent={d['id']:((d['bbox'][0]+d['bbox'][1])/2,(d['bbox'][2]+d['bbox'][3])/2) for d in ISL}
res=[]
for d in ISL:
    if d['km2']<3: continue
    a,b,c,e=d['bbox']; span=max(b-a,(e-c)*0.93)
    nb=[x for x in ISL if x['id']!=d['id'] and 0.08<x['km2']/d['km2']<0.7 and np.hypot(cent[x['id']][0]-(a+b)/2,(cent[x['id']][1]-(c+e)/2)*0.93)<span*1.3]
    for x in nb:
        A=min(a,x['bbox'][0]);B=max(b,x['bbox'][1]);C=min(c,x['bbox'][2]);E=max(e,x['bbox'][3])
        y0,x0=px(B,C);y1,x1=px(A,E);pad=5
        crop=L[max(0,y0-pad):y1+pad,max(0,x0-pad):x1+pad].astype(bool)
        lab,n=ndi.label(crop); 
        if n<2: continue
        sz=ndi.sum(crop,lab,range(1,n+1)); keep=np.argsort(-sz)[:2]+1
        m=np.isin(lab,keep)
        c1=norm(m).reshape(-1).astype(np.float32)
        inter=V@c1; iou=inter/(V.sum(1)+c1.sum()-inter)
        k=int(iou.argmax()); res.append((float(iou[k]),d['id'],d['name'],d['km2'],x['id'],x['km2'],meta[k]))
res.sort(reverse=True)
seen=set()
for r in res:
    key=frozenset((r[1],r[4]))
    if key in seen: continue
    seen.add(key); print(round(r[0],3),r[1:])
    if len(seen)>=25: break
