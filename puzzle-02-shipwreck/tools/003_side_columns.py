import re,unicodedata
L=[8,15,7,3,17,5,12,19,13,9,16,18,0,11,4]
R=[16,11,9,8,2,4,18,10,6,12,14,17,15,7,0]
def clean(s): s=unicodedata.normalize('NFD',s); return re.sub(r'[^A-Za-z]','',s).upper()
txt=open('t.txt').read()
words=txt.split()
paras=[p for p in txt.split('\n\n') if p.strip()]
src={'JUANPONCEDELEON':'JUANPONCEDELEON',
 '002 plaintext':'RECORDADAJPDLELHOMBREQUEBUSCOLAVIDAETERNA',
 'maya letters':clean(txt),
 'maya first letters':''.join(clean(w)[0] for w in words if clean(w)),
 'last sentence':clean(paras[-1]),
 'ESCUALO':'ESCUALO'}
cols={'left':L,'right':R,'left rev':L[::-1],'right rev':R[::-1]}
for cn,c in cols.items():
  print('==',cn,c)
  print('  A=1:',''.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[v-1] if v else '_' for v in c),' A=0:',''.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[v] for v in c))
  for sn,s in src.items():
    idx1=''.join(s[v-1] if 0<v<=len(s) else '_' for v in c)   # value = position (1-based)
    idx0=''.join(s[v] if v<len(s) else '_' for v in c)
    order=''.join(s[i] for i in sorted(range(15),key=lambda i:c[i]) if i<len(s))  # read boxes in order of value
    print(f'  {sn:20s} pos1:{idx1}  pos0:{idx0}  order:{order}')
# words: value = word index
for cn,c in cols.items():
  print(cn,'words:',' '.join(words[v-1] if v else '-' for v in c))
# combined: left value & right value pairs as (paragraph? word?)
print('pairs', list(zip(L,R)))
