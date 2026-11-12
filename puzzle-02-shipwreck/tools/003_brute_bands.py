import itertools
L=[8,15,7,3,17,5,12,19,13,9,16,18,0,11,4]
R=[16,11,9,8,2,4,18,10,6,12,14,17,15,7,0]
T1=[6,4,1,10];T2=[5,14,13,2];B1=[6,3,1,9];B2=[13,2,17,7]
G={}  # (col,row) col0..5,row0..14
for r in range(15): G[(0,r)]=L[r]; G[(5,r)]=R[r]
for c in range(4): G[(c+1,0)]=T1[c];G[(c+1,1)]=T2[c];G[(c+1,13)]=B1[c];G[(c+1,14)]=B2[c]
codes=[('e',2),('b',3),('d',1),('d',3),('a',4),('d',1)]
words=open('t.txt').read().split()
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
results={}
def add(desc,nums):
    results.setdefault(tuple(nums),[]).append(desc)
# rows sets: any 4 rows (ordered increasing) from 15 -> too many; use consecutive + band sets
rowsets=[tuple(range(s,s+4)) for s in range(12)]+[(0,1,13,14)]
colsets=[tuple(range(s,s+5)) for s in range(2)]
for rs in rowsets:
  for cs in colsets:
    for rr in (rs,rs[::-1]):
      for cc in (cs,cs[::-1]):
        try: nums=[G[(cc['abcde'.index(l)],rr[n-1])] for l,n in codes]
        except KeyError: continue
        add(f'cols{cc} rows{rr}',nums)
# transposed: letters = rows (5 consecutive rows), numbers = cols (4 consecutive of 6)
for s in range(11):
  rs=tuple(range(s,s+5))
  for cs in [tuple(range(c,c+4)) for c in range(3)]:
    for rr in (rs,rs[::-1]):
      for cc in (cs,cs[::-1]):
        try: nums=[G[(cc[n-1],rr['abcde'.index(l)])] for l,n in codes]
        except KeyError: continue
        add(f'T rows{rr} cols{cc}',nums)
print(len(results),'distinct number sets')
for nums,d in results.items():
    s1=''.join(A[n-1] if n>0 else '_' for n in nums); s0=''.join(A[n] for n in nums)
    w=' '.join(words[n-1] if n>0 else '-' for n in nums)
    print(nums,s1,s0,'|',w,'|',d[0])
