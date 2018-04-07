def preberi(ime_datoteke):
    d = {}
    n = 1
    for e in open(ime_datoteke, encoding="utf - 8"):
        d[n] = []
        if len(e.rstrip()) > 1:
            s = []
            for x in e.rstrip().split():
                s.append(int(x))
            if s[0] != min(s):
                s.extend(s[:s.index(min(s))])
                del s[:s.index(min(s))]
            d[n].extend(s)
        else:
            d[n].append(int(e.rstrip()))
        n += 1
    return d

def mozna_pot(pot, zemljevid):
    s = []
    for x,y in list(zip(pot, pot[1:])):
        if y in zemljevid[x] and len(zemljevid[pot[-1]]) == len(zemljevid[pot[0]]) == 1 \
                and all(len(zemljevid[e]) > 1 for e in pot[1:-1]):
            s.append(True)
        else:
            s.append(False)
    return all(s)


def hamiltonova(pot, zemljevid):
    vsakrozisca = set()
    for e in zemljevid:
        if len(zemljevid[e]) > 1:
            vsakrozisca.add(e)
    return mozna_pot(pot, zemljevid) and \
         len(vsakrozisca - set(pot[1:-1])) == 0 and \
             len(pot) == len(set(pot))

def navodila(pot, zemljevid):
    return [(zemljevid[x].index(pot[i + 1]) - zemljevid[x].index(pot[i - 1])) % len(zemljevid[x])
            for i, x in list(enumerate(pot)) if len(zemljevid[x]) > 1]

def prevozi(zacetek, navodila, zemljevid):
    n = 0
    pot = [zacetek, zemljevid[zacetek][0]]
    for x in navodila:
        pot.append(zemljevid[pot[-1]][(zemljevid[pot[-1]].index(zemljevid[pot[-1]][x])
         + zemljevid[pot[-1]].index(pot[n])) % len(zemljevid[pot[-1]])])
        n += 1
    return pot

def sosedi(doslej, zemljevid):
    v = set()
    for x in doslej:
        for y in zemljevid[x]:
            v.add(y)
    return v - doslej