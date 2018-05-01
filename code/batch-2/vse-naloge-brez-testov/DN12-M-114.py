import collections

def preberi(ime_datoteke):
    slovar = collections.defaultdict(int)
    v = 1
    for vrstica in open(ime_datoteke, 'r', encoding='UTF8').read().splitlines():
        s1 = [int(x) for x in vrstica.split()]
        i = s1.index(min(s1))
        slovar[v] = s1[i:] + s1[:i]
        v += 1
    return slovar

def mozna_pot(pot, zemljevid):
    konec = {kljuc for kljuc, vrednost in zemljevid.items() if len(vrednost) == 1}
    return {pot[0], pot[-1]} <= konec and not set(pot[1:-1]) & konec and\
           all(a in zemljevid[b] for a, b in zip(pot,pot[1:]))

def hamiltonova(pot, zemljevid):
    return mozna_pot(pot, zemljevid) and len(pot) == len(set(pot)) ==\
           sum(len(zemljevid[x]) > 1 for x in zemljevid) + 2

def navodila(pot, zemljevid):
    return [(zemljevid[b].index(c) - zemljevid[b].index(a)) % len(zemljevid[b])
            for a,b,c in zip(pot, pot[1:], pot[2:])]

def prevozi(zacetek, navodila, zemljevid):
    izvoz = zemljevid[zacetek][0]
    s = [zacetek, izvoz]
    for x in navodila:
        g = zemljevid[izvoz]
        a = izvoz
        izvoz = g[(g.index(zacetek) + x) % len(g)]
        s.append(izvoz)
        zacetek = a
    return s


def sosedi(doslej, zemljevid):
    return {x for y in doslej for x in zemljevid[y] if x not in doslej}

# 1 opcija
'''def pot(x,y, zemljevid):
    s, s1 = [x], [x]
    slovar = collections.defaultdict(int)
    for korak in s:
        for x in zemljevid[korak]:
            if x == y:
                slovar[x] = korak
                return slovar
            if x not in s1:
                s.append(x)
                s1.append(x)
                slovar[x] = korak
    return slovar

def preberi_pot(x,y,slovar):
    return slovar[y] == x and [x,y] or preberi_pot(x, slovar[y], slovar) + [y]

def razdalja(x,y,zemljevid):
    return len(preberi_pot(x,y,pot(x,y,zemljevid))) - 1

def najkrajsa_navodila(x, y, zemljevid):
    return navodila(preberi_pot(x,y,pot(x,y,zemljevid)), zemljevid)'''

# 2 opcija
def razdalja(x, y, zemljevid):
    x = {x} if type(x) is int else x
    if y in x:
        return 0
    return 1 + razdalja(sosedi(x, zemljevid), y, zemljevid)

def sosedi_slovar(slovar, zemljevid):
    return {x: slovar[y] + [y] for y in slovar for x in zemljevid[y] if x not in slovar}

def najkrajsa_navodila(x, y, zemljevid):
    if type(x) is int:
        x = {y: [x] for y in zemljevid[x]}
    if y in x:
        return navodila(x[y] + [y], zemljevid)
    return najkrajsa_navodila(sosedi_slovar(x, zemljevid), y, zemljevid)



