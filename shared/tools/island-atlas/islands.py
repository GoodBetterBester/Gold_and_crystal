import numpy as np, json, math
from scipy import ndimage
import geonamescache
M=np.load('land.npy'); LAT1,LON0,R=33,-90,0.002
lab,n=ndimage.label(M,structure=np.ones((3,3)))
objs=ndimage.find_objects(lab); sizes=ndimage.sum(M,lab,range(1,n+1))
gc=geonamescache.GeonamesCache(min_city_population=500) if 'min_city_population' in geonamescache.GeonamesCache.__init__.__code__.co_varnames else geonamescache.GeonamesCache()
cities=[c for c in gc.get_cities().values() if 8<c['latitude']<34 and -91<c['longitude']<-56]
print('cities',len(cities))
out=[]
for i,(sl,s) in enumerate(zip(objs,sizes)):
    ys,xs=sl
    lat0=LAT1-ys.stop*R; lat1=LAT1-ys.start*R; lon0=LON0+xs.start*R; lon1=LON0+xs.stop*R
    km2=s*(R*111.32)**2*math.cos(math.radians((lat0+lat1)/2))
    if km2<1 or km2>150000: continue
    if ys.start==0 or xs.start==0 or ys.stop==M.shape[0] or xs.stop==M.shape[1]: continue
    inside=[c for c in cities if lat0<=c['latitude']<=lat1 and lon0<=c['longitude']<=lon1 and lab[int((LAT1-c['latitude'])/R),int((c['longitude']-LON0)/R)]==i+1]
    if inside:
        c=max(inside,key=lambda c:c['population']); name=f"{c['name']} ({c['countrycode']})"
    else:
        cy,cx=(lat0+lat1)/2,(lon0+lon1)/2
        c=min(cities,key=lambda c:(c['latitude']-cy)**2+((c['longitude']-cx)*math.cos(math.radians(cy)))**2)
        d=math.hypot(c['latitude']-cy,(c['longitude']-cx)*math.cos(math.radians(cy)))*111
        name=f"near {c['name']} ({c['countrycode']}, {d:.0f} km)"
    out.append(dict(id=len(out),name=name,km2=round(km2,1),bbox=[round(lat0,4),round(lat1,4),round(lon0,4),round(lon1,4)]))
out.sort(key=lambda d:-d['km2'])
for k,d in enumerate(out): d['id']=k
json.dump(out,open('islands.json','w'),indent=0)
print(len(out)); print(out[:5]); print(sum(d['km2']<5 for d in out))
