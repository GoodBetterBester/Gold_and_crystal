import json, numpy as np, sys
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
G=96
def norm(m):
    ys,xs=np.nonzero(m); cy,cx=ys.mean(),xs.mean(); a=len(ys)
    s=np.sqrt(a)/ (G*0.28)   # island area -> ~ (0.28G)^2 px
    yy,xx=np.mgrid[0:G,0:G]; sy=(yy-G/2)*s+cy; sx=(xx-G/2)*s+cx
    return ndi.map_coordinates(m.astype(float),[sy,sx],order=1,cval=0)>0.5
def poly_mask(pts,scale=1.0):
    pts=[(x*scale,y*scale) for x,y in pts]; xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    W=int(max(xs))+5; H=int(max(ys))+5; im=Image.new('L',(W,H),0); ImageDraw.Draw(im).polygon(pts,fill=255)
    return np.asarray(im)>0
def island_mask(i):
    a=np.asarray(Image.open(f'thumbs/{i}.png').convert('L'))<215
    lab,n=ndi.label(a); 
    if n==0: return None
    c=lab.shape[0]//2; best=None;bd=1e9
    for k in range(1,n+1):
        ys,xs=np.nonzero(lab==k)
        if len(ys)<30: continue
        d=np.min((ys-c)**2+(xs-c)**2)
        if d<bd: bd=d;best=k
    return lab==best if best else None
ISL=json.load(open('islands.json'))
CACHE='cand.npy'
try: C=np.load(CACHE)
except Exception:
    C=np.zeros((len(ISL),G,G),bool)
    for d in ISL:
        m=island_mask(d['id'])
        if m is not None: C[d['id']]=norm(m)
    np.save(CACHE,C)
def rank(skmask,angles=range(0,360,5),mirror=True,top=15):
    base=norm(skmask); res=[]
    variants=[]
    for mir in ([False,True] if mirror else [False]):
        b=base[:,::-1] if mir else base
        for ang in angles:
            r=ndi.rotate(b.astype(float),ang,reshape=False,order=1)>0.5   # rotate sketch CCW by ang
            variants.append((mir,ang,r))
    V=np.stack([v[2] for v in variants]).reshape(len(variants),-1).astype(np.float32)
    Cf=C.reshape(len(C),-1).astype(np.float32)
    inter=Cf@V.T; union=Cf.sum(1)[:,None]+V.sum(1)[None,:]-inter
    iou=inter/np.maximum(union,1)
    best=iou.argmax(1); sc=iou.max(1)
    nu=[k for k,v in enumerate(variants) if not v[0] and (v[1]<=15 or v[1]>=345)]
    up=iou[:,nu].max(1)
    order=np.argsort(-sc)[:top]
    return [(int(i),ISL[i]['name'],ISL[i]['km2'],round(float(sc[i]),3),round(float(up[i]),3),variants[best[i]][:2]) for i in order], sc, up
