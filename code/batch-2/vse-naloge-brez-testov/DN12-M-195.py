def preberi(ime_datoteke):
    s = {}
    i = 1
    for vrstica in open(ime_datoteke).read().splitlines():
        vrstica = [int(a) for a in vrstica.split()]
        while vrstica[0]!=min(vrstica):
            vrstica.insert(0, vrstica.pop())
        s[i]=vrstica
        i +=1
    return s

def mozna_pot(pot, zemljevid):
    for i in range(1,len(pot)-1):
        if len(zemljevid[pot[i]])== 1:
            return False
    for i in range(0,len(pot)-1):
        if pot[i+1] not in zemljevid[pot[i]]:
            return False
        elif pot[i]==pot[i+1]:
            return False
    if len(zemljevid[pot[0]]) != 1:
        return False
    elif len(zemljevid[pot[-1]]) != 1:
        return False
    else:
        return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot,zemljevid):
        return False
    elif len(pot)!=len(set(pot)):
        return False
    else:
        s = set()
        for key,value in zemljevid.items():
            if len(value)>1:
                s.add(key)
    t = set(pot[1:-1])
    return t == s


def navodila(pot, zemljevid):
    s = []
    for i in range(1, len(pot)-1):
        prej,tren,nasl = pot[i-1],pot[i],pot[i+1]
        izvozi = zemljevid[tren]
        ind_izvoza = izvozi.index(nasl)
        ind_privoza = izvozi.index(prej)
        s.append((ind_izvoza-ind_privoza)%len(izvozi))
    return s

def prevozi(zacetek, navodila, zemljevid):
    s = [zacetek,zemljevid[zacetek][0]]
    for i in navodila:
        tren,prej = s[-1],s[-2]
        izvozi = zemljevid[tren]
        ind_privoza = izvozi.index(prej)
        ind_izvoza = (ind_privoza + i)%len(izvozi)
        s.append(izvozi[ind_izvoza])
    return s


def sosedi(doslej, zemljevid):
    s = []
    for e in doslej:
        s.extend(zemljevid[e])
    for i in s:
        if i in doslej:
            s.remove(i)
    return set(s)











