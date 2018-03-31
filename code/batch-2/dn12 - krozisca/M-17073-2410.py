def preberi(ime_datoteke):
    zemljevid={}
    stevilo=1
    for vrstica in open(ime_datoteke):
        vrstica=vrstica.strip().split()
        vrstica1=[]
        for a in vrstica:
            vrstica1.append(int(a))
        if len(vrstica1)>1:
            for a in vrstica1:
                c=0
                if vrstica1[0]>vrstica1[1]:
                    c=vrstica1[0]
                    del vrstica1[0]
                    vrstica1.append(c)
        zemljevid[stevilo]=vrstica1
        stevilo+=1
    return zemljevid

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]])>1:
        return False
    if len(zemljevid[pot[-1]])>1:
        return False
    pot=pot[::-1]
    for i in range(len(pot)-1):
        if len(zemljevid[pot[i]])==1:
            if 0<i<len(pot)+1:
                return False
        if pot[i]==pot[i+1]:
            return False
        if pot[i] in zemljevid[pot[i+1]]:
            continue
        else:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    a=[]
    k=[]
    for b in pot:
        if b not in a:
            a.append(b)
    if a!=pot:
        return False
    for ime in zemljevid:
        if len(zemljevid[ime])>1:
            k.append(ime)
    if len(k)+2==len(a):
        return True
    return False

def navodila(pot, zemljevid):
    izvozi=[]
    for i in range(len(pot)-2):
        a=zemljevid[pot[i+1]].index(pot[i+2])-zemljevid[pot[i+1]].index(pot[i])%len(zemljevid[pot[i+1]])
        if a<0:
            b=len(zemljevid[pot[i+1]])+a
            izvozi.append(b)
        else:
            izvozi.append(a)
    return izvozi

def prevozi(zacetek, navodila, zemljevid):
    z=zemljevid
    a=zacetek
    c=z[zacetek][0]
    prevozi=[zacetek, c]
    for i in range(len(navodila)-1):
        if z[c].index(a)+navodila[i]>=len(z[c]):
            b=z[c][z[c].index(a)+(navodila[i]-len(z[c]))]
            prevozi.append(b)
            c=b
        else:
            b = z[c][z[c].index(a) + navodila[i]]
            prevozi.append(b)
            c=b
        a = prevozi[i + 1]
    for m in z[prevozi[-1]]:
        if len(z[m])==1:
            prevozi.append(m)
    return prevozi

def sosedi(doslej, zemljevid):
    vozlisca=set()
    v=[]
    for a in doslej:
        v+=zemljevid[a]
    for b in v:
        vozlisca.add(b)
    return vozlisca-doslej

def razdalja(x, y, zemljevid):
    if y in zemljevid[x]:
        return 0
    for k in zemljevid[x]:
        r = razdalja(k, y, zemljevid)
        if r is not None:
            return r + 1