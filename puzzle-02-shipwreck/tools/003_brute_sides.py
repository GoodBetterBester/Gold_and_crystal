exec(open('brute.py').read().split("results={}")[0])
results={}
top_in=[L[0]]+T1+[R[0]]; bot_in=[L[-1]]+B2+[R[-1]]
top_mid=T1; bot_mid=B2
sides_opts={
 'top(incl corners)':top_in,'top mid':T1,'top row2':T2,
 'bottom(incl corners)':bot_in,'bottom mid':B2,'bottom row1':B1,
 'left':L,'right':R}
import itertools
names=list(sides_opts)
seen={}
for perm in itertools.permutations(names,4):
  for revs in itertools.product([0,1],repeat=4):
    seqs=[sides_opts[p][::-1] if r else sides_opts[p] for p,r in zip(perm,revs)]
    try: nums=tuple(seqs[n-1]['abcde'.index(l)] for l,n in codes)
    except IndexError: continue
    seen.setdefault(nums,(perm,revs))
print(len(seen))
import re
words=open('t.txt').read().split()
# score: letters A=1 forming dictionary-ish? print those where letters A1 contain vowels pattern
for nums,(p,r) in seen.items():
    s1=''.join(A[n-1] if n>0 else '_' for n in nums)
    print(s1, nums, p, r)
