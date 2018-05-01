def preberi(ime_datoteke):
    ključ = 1
    zemljevid = {}
    for obrati in open(ime_datoteke):
        o = []
        for e in obrati.split():
            o.append(int(e))
        while o[0] != min(o):
            o.append(o[0])
            o.remove(o[0])
        zemljevid[ključ] = o
        ključ += 1
    return zemljevid

def mozna_pot(pot, zemljevid):
    prejsna = zemljevid[pot[0]]
    prej = pot[0]
    for p in pot[1:-1]:
        if len(zemljevid[p]) > 1 and p in prejsna and p != prej:
            prejsna = zemljevid[p]
            prej = p
        else:
            return False
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1 and len(pot[1:-1]) >= 1:
        return True
    return False


def hamiltonova(pot, zemljevid):
    krožišča = []
    for k in zemljevid.keys():
        if len(zemljevid[k]) > 1:
            krožišča.append(k)
    for p in pot:
        if p in krožišča:
            krožišča.remove(p)
    if mozna_pot(pot, zemljevid) and len(pot) == len(set(pot)) and len(krožišča) == 0:
        return True
    return False


def navodila(pot, zemljevid):
    return [(zemljevid[t].index(n) - zemljevid[t].index(p)) % (len(zemljevid[t])) for p, t, n in list(zip(pot, pot[1:], pot[2:]))]

def prevozi(zacetek, navodila, zemljevid):
    krožišča = [zacetek, zemljevid[zacetek][0]]
    t = zemljevid[zacetek][0]
    vh = zacetek
    for n in navodila:
        iz = zemljevid[t][(zemljevid[t].index(vh) + n) % len(zemljevid[t])]
        krožišča.append(iz)
        vh = t
        t = iz
        print(n, zemljevid[t].index(vh) + n)
    print(krožišča)
    return krožišča

def sosedi(doslej, zemljevid):
    a = set()
    for d in doslej:
        a = a | set(zemljevid[d])
    return a - doslej

def razdalja(x, y, zemljevid):
    a = sosedi({x}, zemljevid)
    stevec = 1
    while y not in a:
        stevec += 1
        a = a | sosedi(a, zemljevid)
    return stevec

def najkrajsa_navodila(x, y, zemljevid):
    slovar = {}
    p = []
    for e in zemljevid[x]:
        slovar[e] = x
    while y not in slovar:
        sosedni_slovar(slovar, zemljevid)
    for e in slovar:
        p.append(slovar[e])
    print (p)
    return


def sosedni_slovar(slovar, zemljevid):
    for e in slovar:
        for s in zemljevid[e]:
            slovar[s] = e
    return slovar











