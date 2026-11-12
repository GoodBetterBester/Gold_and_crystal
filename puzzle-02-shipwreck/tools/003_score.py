import io,contextlib,itertools
from wordfreq import top_n_list
D=set()
for lang in ('en','es','pt','fr','la' ):
    try: D|={w.upper() for w in top_n_list(lang,40000) if w.isalpha() and len(w)>=3}
    except Exception: pass
D|={'BIMINI','TULUM','CUBA','HAVANA','HABANA','MAYA','LEON','PONCE','JUAN','ISLA','CAYO','COBA'}
f=io.StringIO()
with contextlib.redirect_stdout(f): exec(open('brute.py').read())
sets=set(results)
with contextlib.redirect_stdout(io.StringIO()): exec(open('brute2.py').read())
sets|=set(seen)
print('total sets',len(sets))
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def dec(nums,off):
    out=''
    for n in nums:
        i=n-off
        if not 0<=i<26: return None
        out+=A[i]
    return out
hits=[]
for nums in sets:
  for off,lab in ((1,'A=1'),(0,'A=0')):
    s=dec(nums,off)
    if not s: continue
    sc=0;why=''
    if s in D: sc=10;why=s
    for k in range(3,4):
        if s[:k] in D and s[k:] in D: sc=max(sc,6);why=s[:k]+' '+s[k:]
    for k in (2,4):
        if s[:k] in D and s[k:] in D: sc=max(sc,4);why=s[:k]+' '+s[k:]
    # reversed
    r=s[::-1]
    if r in D: sc=max(sc,8);why='rev '+r
    if sc: hits.append((sc,s,lab,nums,why))
hits.sort(reverse=True)
for h in hits[:40]: print(h)
print(len(hits))
