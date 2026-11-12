import sys, numpy as np
from PIL import Image
from scipy import ndimage as ndi
S='/mnt/user-data/uploads/Downloads/'; k=1241/990
THR=115
def mask(f,box,thr=None,close=7,keep=1,out=None):
    im=np.asarray(Image.open(S+f).convert('RGB').crop(tuple(int(v*k) for v in box))).astype(float)
    r,g,b=im[...,0],im[...,1],im[...,2]
    L=0.3*r+0.59*g+0.11*b; ink=(L<THR)&((r-g)>25)
    ink=ndi.binary_closing(ink,structure=np.ones((close,close)))
    filled=ndi.binary_fill_holes(ink)
    lab,n=ndi.label(filled); s=ndi.sum(filled,lab,range(1,n+1)); order=np.argsort(s)[::-1][:keep]
    m=np.isin(lab,order+1)
    if out: Image.fromarray((m*255).astype(np.uint8)).save(out)
    return m
if __name__=='__main__':
    mask('2b.jpeg',(40,60,950,1280),close=9,keep=4,out='m002.png')
    mask('6.jpeg',(240,270,800,1210),close=9,keep=1,out='m006.png')
    mask('4 (1).jpeg',(260,320,710,520),close=7,keep=2,out='m004.png')
