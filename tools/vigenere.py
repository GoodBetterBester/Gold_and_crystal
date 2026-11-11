import itertools
C="Ey yxjh nov fpalhkfml nch ilzo sq aujgnluetw."
def dec(c,k,beau=False):
    out=[];i=0
    for ch in c:
        if ch.isalpha():
            a=ord(ch.lower())-97;b=ord(k[i%len(k)].lower())-97
            v=(b-a)%26 if beau else (a-b)%26
            out.append(chr(v+97));i+=1
        else: out.append(ch)
    return ''.join(out)
cands="FORTSANFELIPEDELMORRO SANFELIPEDELMORRO CASTILLODELMORRO FORTSANCRISTOBAL FORTSANLORENZO SANLORENZOELREAL FORTCHARLOTTE FORTSANSALVADOR CASTILLODESANMARCOS FORTFREDERIK FORTNASSAU FORTMONTAGU FORTCHRISTIANSVAERN SANJUANDEULUA CASTILLOSANFELIPE BRIMSTONEHILL FORTSANJERONIMO".split()
for k in cands:
    print(len(k),k,dec(C,k),'|',dec(C,k,True))
# crib: key fragment for guessed plaintext starts
letters=''.join(c for c in C.lower() if c.isalpha())
for p in ["inyour","toread","ifyour","onlythe","beyond","tofind","inthe","atthe","inorder","whoever","asthe","bythe","ofall","nowthe","heresits"]:
    k=''.join(chr((ord(a)-ord(b))%26+97) for a,b in zip(letters,p))
    print(p,k)
