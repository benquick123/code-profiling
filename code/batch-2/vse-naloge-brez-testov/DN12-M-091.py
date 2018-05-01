def preberi(ime_datoteke):
    d, k = {}, 1
    for vrstica in open(ime_datoteke):
        d[k] = [int(x) for x in vrstica.split()]
        i = d[k].index(min(d[k]))
        d[k] = d[k][i:] + d[k][:i]
        k += 1
    return d

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) > 1 or len(zemljevid[pot[-1]]) > 1:
        return False
    for e in pot[1:-2]:
        if len(zemljevid[e]) < 2:
            return False
    for i in range(len(pot) - 1):
        if pot[i+1] not in zemljevid[pot[i]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if sorted(pot) == list(set(zemljevid) - ({x for x in zemljevid if len(zemljevid[x]) == 1} - {pot[0], pot[-1]})) \
            and mozna_pot(pot, zemljevid):
        return True
    return False

def navodila(pot, zemljevid):
    return [(zemljevid[pot[i]].index(pot[i+1]) - zemljevid[pot[i]].index(pot[i-1]))
                % len(zemljevid[pot[i]]) for i in range(1, len(pot)-1)]

def prevozi(zacetek, navodila, zemljevid):
    s = [zacetek]
    krozisce = zemljevid[zacetek][0]
    for i in range(len(navodila)):
        izhod = (zemljevid[krozisce].index(s[-1]) + navodila[i]) % len(zemljevid[krozisce])
        s.append(krozisce)
        krozisce = zemljevid[krozisce][izhod]
    s.append(krozisce)
    return s

def sosedi(doslej, zemljevid):
    return {x for e in doslej for x in zemljevid[e]} - doslej

def razdalja(x, y, zemljevid):
    razdalja = 1
    doslej = sosedi({x}, zemljevid)
    while y not in doslej:
        doslej |= sosedi(doslej, zemljevid)
        razdalja += 1
    return razdalja

def najkrajsa_navodila(x, y, zemljevid):
    from random import randint
    min_razdalja = razdalja(x, y, zemljevid) - 1
    navodila = []
    while not (len(navodila) == min_razdalja
               and mozna_pot(prevozi(x, navodila, zemljevid), zemljevid)
               and prevozi(x, navodila, zemljevid)[-1] == y):
        navodila = []
        for i in range(min_razdalja):
            navodila.append(randint(1, 4))
    pot = prevozi(x, navodila, zemljevid)
    for i in range(len(navodila)):
        navodila[i] = navodila[i] % len(zemljevid[pot[i+1]])
    return navodila

