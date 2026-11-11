import chess,itertools
def mates(fen,depth):
    b=chess.Board(fen)
    if not b.is_valid(): return 'invalid '+str(b.status())
    def mate_in(b,n):
        for m in list(b.legal_moves):
            b.push(m)
            ok=False
            if b.is_checkmate(): ok=True
            elif n>1 and not b.is_game_over():
                ok=all(_r(b,m2,n) for m2 in list(b.legal_moves))
            b.pop()
            if ok: yield m
    def _r(b,m2,n):
        b.push(m2); r=any(True for _ in mate_in(b,n-1)); b.pop(); return r
    res=[]
    for n in range(1,depth+1):
        ms=[b.san(m) for m in mate_in(b,n)]
        if ms: return n,ms
    return None
base_white={'K':'c1','N':'b1','Q':'g2','R':'h7','P':['d4','e3','f2','f5']}
for rook in ['a7','a8','b8','a6']:
    w={'c1':'K','b1':'N','g2':'Q','h7':'R','d4':'P','e3':'P','f2':'P','f5':'P'}
    bl={'b3':'k','b4':'p','a4':'q','c6':'p','d7':'n','c7':'b',rook:'r'}
    b=chess.Board(None)
    for s,p in {**w,**bl}.items(): b.set_piece_at(chess.parse_square(s),chess.Piece.from_symbol(p))
    b.turn=chess.WHITE
    print(rook,b.fen(),mates(b.fen(),3))
