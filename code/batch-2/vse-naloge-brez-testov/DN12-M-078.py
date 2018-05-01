#za oceno 6


def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    i = 1
    tab = {}
    for vrstica in datoteka:
        tmp = [int(n) for n in vrstica.strip('\n').split()]
        najmanjse = min(tmp)
        while tmp[0] != najmanjse:
            last = tmp[0]
            tmp = tmp[1:]
            tmp.append(last)
        tab[i] = tmp
        i += 1
    return tab


def mozna_pot(pot, zemljevid):
    for indeks, korak in enumerate(pot[:-1]):
        if pot[indeks + 1] not in zemljevid[korak] or len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1 \
                or (len(zemljevid[korak]) == 1 and 0 < indeks < len(pot) - 1):
            return False
    return True


def hamiltonova(pot, zemljevid):
    krozisca = [n for n in zemljevid if len(zemljevid[n]) > 1]
    tmp = pot[1:-1]
    tmp.sort()
    if mozna_pot(pot, zemljevid) and tmp == krozisca:
        return True
    return False


#za oceno 7


def navodila(pot, zemljevid):
    tab = []
    for indeks, korak in enumerate(pot):
        if 0 < indeks < len(pot) - 1:
            prejsnji = zemljevid[korak].index(pot[indeks - 1])
            naslednji = zemljevid[korak].index(pot[indeks + 1])
            tab.append((naslednji - prejsnji) % len(zemljevid[korak]))
    return tab


#za oceno 8


def prevozi(zacetek, navodila, zemljevid):
    tab = [zacetek, zemljevid[zacetek][0]]
    for navodilo in navodila:
        current = max([i for i, x in enumerate(zemljevid[tab[-1]]) if x == tab[-2]])
        tab.append(zemljevid[tab[-1]][(current + navodilo) % len(zemljevid[tab[-1]])])
    return tab


#za oceno 9


def sosedi(doslej, zemljevid):
    tab = []
    for stevilka in doslej:
        for smer in zemljevid[stevilka]:
           if smer not in doslej:
                tab.append(smer)
    return set(tab)


def razdalja(x, y, zemljevid):
    mno = {x}
    i = 1
    while y not in sosedi(mno, zemljevid):
        i += 1
        mno.update(sosedi(mno, zemljevid))
    return i


#za oceno 10


def najkrajsa_navodila(x, y, zemljevid):
    tab = [x]
    raz = razdalja(x, y, zemljevid)
    mno = x
    while True:
        minimum = [0, raz]
        for sosed in sosedi({mno}, zemljevid):
            if (sosed != x and sosed == tab[-1] and minimum[0] == 0) or sosed == y:
                tab.append(y)
                return navodila(tab, zemljevid)
            tmp = razdalja(sosed, y, zemljevid)
            if tmp < minimum[1]:
                minimum[0] = sosed
                minimum[1] = tmp
        tab.append(minimum[0])
        mno = minimum[0]


