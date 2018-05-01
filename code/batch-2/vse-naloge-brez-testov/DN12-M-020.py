
def preberi(ime_datoteke):
    slovar = {}
    i = 1
    for vrstica in open(ime_datoteke, encoding="utf8"):
        vrstica = vrstica.strip()
        seznam = vrstica.split()
        seznam = [int(i) for i in seznam]
        najmanjsa = min(seznam)
        seznam = seznam[seznam.index(najmanjsa):] + seznam[:seznam.index(najmanjsa)]
        slovar[i] = seznam
        i += 1
    return slovar


def mozna_pot(pot, zemljevid):
    seznam = []
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        seznam.append(True)
        if all(seznam):
            for element in pot[1:-1]:
                if len(zemljevid[element]) != 1:
                    seznam.append(True)
                else:
                    seznam.append(False)
        if all(seznam):
            for k1, k2 in zip(pot[:], pot[1:]):
                if k1 != k2:
                    seznam.append(True)
                else:
                    seznam.append(False)
        if all(seznam):
            for p1, p2 in zip(pot[:], pot[1:]):
                if p1 in zemljevid[p2] and p2 in zemljevid[p1]:
                    seznam.append(True)
                else:
                    seznam.append(False)
        return all(seznam)
    return False


def hamiltonova(pot, zemljevid):
    xs = []
    seznam = []
    stevilo_krozisc = 0
    if mozna_pot(pot, zemljevid):
        for krozisce in zemljevid:
            if len(zemljevid[krozisce]) > 1:
                stevilo_krozisc += 1
        if len(pot[1:-1]) == stevilo_krozisc:
            seznam.append(True)
        else:
            seznam.append(False)
        for element in pot[1:-1]:
            if element not in xs:
                xs.append(element)
            else:
                seznam.append(False)
        return all(seznam)
    return False


def navodila(pot, zemljevid):
    seznam = []
    for p1, p2, p3 in zip(pot[:], pot[1:], pot[2:]):
        s = zemljevid[p2]
        razlika = s.index(p3) - s.index(p1)
        seznam.append(razlika % len(zemljevid[p2]))
    return seznam


def navodila(pot, zemljevid):
    return [(zemljevid[p2].index(p3) - zemljevid[p2].index(p1)) % len(zemljevid[p2]) for p1, p2, p3 in zip(pot[:], pot[1:], pot[2:])]


def prevozi(zacetek, navodila, zemljevid):
    seznam = [zacetek, zemljevid[zacetek][0]]
    i = 1
    for navodilo in navodila:
        s = 2 * zemljevid[seznam[i]]
        indeks = s.index(seznam[i - 1]) + navodilo
        seznam.append(s[indeks])
        i += 1
    return seznam


def sosedi(doslej, zemljevid):
    s = set()
    for element in doslej:
        s |= set(zemljevid[element])
    return s - doslej


def razdalja(x, y, zemljevid):
    if isinstance(x, int):
        s = set()
        s.add(x)
    else:
        s = x
    s |= sosedi(s, zemljevid)
    if y in s:
        return 1
    return 1 + razdalja(s, y, zemljevid)


def sosedi2(slovar, zemljevid):
    nov_slovar = slovar.copy()
    for kljuc in slovar:
        seznam = zemljevid[kljuc]
        for element in seznam:
            if element not in nov_slovar:
                nov_slovar[element] = kljuc
    return nov_slovar


def najkrajsa_navodila(x, y, zemljevid):
    seznam = [y]
    slovar = {x: None}
    while y not in slovar:
        slovar = sosedi2(slovar, zemljevid)
    dodan = slovar[y]
    seznam.append(slovar[y])
    while x not in seznam:
        dodaj = slovar[dodan]
        seznam.append(dodaj)
        dodan = dodaj
    return navodila(seznam[::-1], zemljevid)


