def preberi(ime_datoteke):
    slovar = {}
    kljuc = 1
    for line in open(ime_datoteke):
        vrstica = [int(stevilo) for stevilo in line.strip().split(" ")]
        min_index = vrstica.index(min(vrstica))
        slovar[kljuc] = vrstica[min_index:] + vrstica[:min_index]
        kljuc += 1
    return slovar


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False
    for povezava in pot[1:-1]:
        if len(zemljevid[povezava]) == 1:
            return False
    for p1, p2 in zip(pot, pot[1:]):
        if p1 == p2:
            return False
        if p2 not in zemljevid[p1]:
            return False
    return True


def hamiltonova(pot, zemljevid):
    krozisca = [key for key in zemljevid.keys() if len(zemljevid[key]) > 1]
    pot_krozisca = [k for k in pot if k in krozisca]
    if mozna_pot(pot, zemljevid) \
            and len(pot_krozisca) == len(krozisca) \
            and len(pot_krozisca) == len(set(pot_krozisca)):
        return True
    return False


def navodila(pot, zemljevid):
    seznam = []
    for prej, zdaj, naprej in zip(pot, pot[1:], pot[2:]):
        prisel = zemljevid[zdaj].index(prej) + 1
        gres = zemljevid[zdaj].index(naprej) + 1
        if gres < prisel:
            seznam.append((len(zemljevid[zdaj]) - prisel) + gres)
        else:
            seznam.append(gres - prisel)
    return seznam


def prevozi(zacetek, navodila, zemljevid):
    vozlisca = [zacetek, zemljevid[zacetek][0]]
    for navodilo in navodila:
        kje = zemljevid[vozlisca[-1]].index(vozlisca[-2])
        kam = (kje + navodilo) % len(zemljevid[vozlisca[-1]])
        vozlisca.append(zemljevid[vozlisca[-1]][kam])
    return vozlisca


def sosedi(doslej, zemljevid):
    return {k1 for krozisce in doslej for k1 in zemljevid[krozisce] if k1 not in doslej}


def razdalja(x, y, zemljevid):
    r = 0
    s = {x}
    while True:
        r += 1
        for sosed in sosedi(s, zemljevid):
            s.add(sosed)
            if sosed == y:
                return r


def najkrajsa_navodila(start, cilj, zemljevid):
    poti = [(start, )]
    for pot in poti:
        zadnje_krozisce = pot[-1]
        for krozisce in zemljevid[zadnje_krozisce]:
            if krozisce not in pot:
                nova_pot = pot + (krozisce, )
                if krozisce == cilj:
                    return navodila(nova_pot, zemljevid)
                else:
                    poti.append(nova_pot)


