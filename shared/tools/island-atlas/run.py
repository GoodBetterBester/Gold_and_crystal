from match import *
import numpy as np
from PIL import Image, ImageDraw
t006=[(510,290),(560,320),(640,370),(720,385),(700,400),(670,400),(650,430),(680,480),(690,520),(660,560),(620,600),(600,660),(610,700),(620,740),(580,760),(560,800),(545,850),(520,900),(490,960),(460,1000),(430,1040),(400,1100),(390,1150),(380,1195),(330,1180),(290,1150),(260,1080),(300,1050),(330,1010),(380,950),(420,880),(440,820),(460,760),(470,720),(460,700),(490,640),(480,600),(440,560),(420,510),(460,490),(500,420),(520,360)]
m4=np.asarray(Image.open('m004.png'))>0
lab,n=ndi.label(m4); s=ndi.sum(m4,lab,range(1,n+1)); o=np.argsort(s)[::-1]
comps={'004 big (right)':lab==o[0]+1,'004 small (left crescent)':lab==o[1]+1,'006':poly_mask(t006)}
big=np.array([d['km2']>=3 for d in ISL])
sheet=[];out={}
for name,m in comps.items():
    r,sc,up=rank(m)
    score=np.where(big,up,0)
    top=np.argsort(-score)[:12]; out[name]=[(int(i),ISL[i]['name'],ISL[i]['km2'],round(float(up[i]),3)) for i in top]
    row=Image.new('RGB',(13*130,150),'white'); d=ImageDraw.Draw(row)
    sk=Image.fromarray((norm(m)*255).astype(np.uint8)).resize((120,120)); row.paste(sk.convert('RGB'),(5,5)); d.text((5,130),name[:22],fill='black')
    for k,i in enumerate(top):
        im=Image.open(f'thumbs/{i}.png').resize((120,120)); row.paste(im,(130*(k+1)+5,5)); d.text((130*(k+1)+5,128),f"#{i} {ISL[i]['name'][:18]}",fill='black'); d.text((130*(k+1)+5,139),f"{ISL[i]['km2']}km2 s={up[i]:.2f}",fill='black')
    sheet.append(row)
S=Image.new('RGB',(13*130,150*len(sheet)),'white')
for k,r in enumerate(sheet): S.paste(r,(0,150*k))
S.save('shortlist.png')
import json; print(json.dumps(out,indent=0))
