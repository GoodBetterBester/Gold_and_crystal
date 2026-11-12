from match import *
s=1/0.375
beata=[(75,70),(110,75),(130,95),(150,130),(160,150),(140,165),(110,180),(70,195),(30,195),(15,180),(20,150),(45,110),(60,85)]
gt=[(380,45),(385,60),(385,100),(385,150),(380,190),(385,230),(380,250),(365,245),(345,250),(335,255),(325,245),(320,225),(330,200),(340,180),(345,140),(355,100),(370,60)]
gt=[((x-265),y) for x,y in gt]
for name,pts,sc,truth in [('Beata',beata,s,'Beata'),('GrandTurk',gt,1/0.319,'Grand Turk')]:
    m=poly_mask(pts,sc); r,allsc,up=rank(m)
    print('==',name)
    for row in r[:10]: print(row)
    # rank of truth by lat/lon
import numpy as np
for name,pts,sc,tid in [('Beata',beata,s,93),('GrandTurk',gt,1/0.319,164)]:
    m=poly_mask(pts,sc); r,allsc,up=rank(m)
    print(name,'any-rot rank',int((allsc>allsc[tid]).sum())+1,'northup rank',int((up>up[tid]).sum())+1, 'of',len(allsc))
    big=np.array([d['km2']>=3 for d in ISL])
    print('  northup rank among >=3km2', int(((up>up[tid])&big).sum())+1,'of',big.sum())
