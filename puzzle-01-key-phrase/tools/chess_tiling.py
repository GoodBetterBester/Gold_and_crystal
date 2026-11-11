import sys
S={
'A':{(0,0):'',(0,1):'',(0,2):'',(0,3):'',(1,0):'',(2,0):'',(3,0):'',(1,2):''},
'B':{(0,2):'',(0,3):'',(1,0):'',(1,2):'',(2,0):'',(2,1):'N',(2,2):'K',(2,3):''},
'C':{(0,3):'',(1,0):'',(1,2):'',(1,3):'R',(2,0):'',(2,1):'',(2,2):'',(2,3):''},
'D':{(0,0):'',(0,1):'',(0,2):'P',(0,3):'',(0,4):'',(1,3):'P',(2,2):'',(2,3):''},
'E':{(0,2):'',(1,1):'',(1,2):'',(2,1):'P',(2,2):'Q',(3,0):'',(3,1):'',(3,2):''},
'F':{(0,0):'',(0,1):'',(1,0):'',(1,1):'',(2,0):'',(3,0):'',(3,1):'',(4,1):''},
'G':{(0,0):'',(0,1):'',(0,2):'',(1,0):'',(1,1):'',(1,2):'',(2,2):'',(3,2):''},
'H':{(0,0):'',(0,1):'P',(0,2):'',(0,3):'',(1,3):'',(2,3):'',(3,3):'',(4,3):''},
}
rot=len(sys.argv)>1
def norm(d):
    mr=min(r for r,c in d);mc=min(c for r,c in d)
    return tuple(sorted(((r-mr,c-mc),v) for (r,c),v in d.items()))
def orients(d):
    out={norm(d)}
    if rot:
        cur=d
        for _ in range(3):
            cur={(c,-r):v for (r,c),v in cur.items()}; out.add(norm(cur))
        m={(r,-c):v for (r,c),v in d.items()}; cur=m; out.add(norm(cur))
        for _ in range(3):
            cur={(c,-r):v for (r,c),v in cur.items()}; out.add(norm(cur))
    return list(out)
O={k:orients(v) for k,v in S.items()}
board={}
sols=[]
def first():
    for r in range(8):
        for c in range(8):
            if (r,c) not in board: return r,c
def solve(rem):
    if not rem: sols.append(dict(board)); return
    r0,c0=first()
    for k in list(rem):
        for o in O[k]:
            # anchor: first cell of o (min row, then min col) at r0,c0
            (ar,ac),_=o[0]
            cells=[((r-ar+r0),(c-ac+c0),v) for (r,c),v in o]
            if all(0<=r<8 and 0<=c<8 and (r,c) not in board for r,c,v in cells):
                for r,c,v in cells: board[(r,c)]=(k,v)
                solve(rem-{k})
                for r,c,v in cells: del board[(r,c)]
solve(set(S))
print(len(sols))
for s in sols[:20]:
    for r in range(8):
        print(8-r,' '.join(s[(r,c)][0]+(s[(r,c)][1] or '.') for c in range(8)))
    print('  '+'  '.join('abcdefgh'))
    print([(v[1],'abcdefgh'[c]+str(8-r)) for (r,c),v in s.items() if v[1]])
