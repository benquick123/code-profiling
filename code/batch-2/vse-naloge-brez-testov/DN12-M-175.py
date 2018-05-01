from collections import defaultdict

def preberi(ime_datoteke):
    zemljevid = defaultdict(list)

    st_vozlisca = 1
    datoteka = open(ime_datoteke, "r")
    vrstica = datoteka.readline()

    while vrstica:
        vozlisca = [int(beseda) for beseda in vrstica.split()]
        for vozlisce in vozlisca:
            zemljevid[st_vozlisca].append(vozlisce)
        min_indeks = zemljevid[st_vozlisca].index(min(zemljevid[st_vozlisca]))
        zemljevid[st_vozlisca] = zemljevid[st_vozlisca][min_indeks:] + zemljevid[st_vozlisca][:min_indeks]
        vrstica = datoteka.readline()
        st_vozlisca += 1

    datoteka.close()
    return dict(zemljevid)

def mozna_pot(pot, zemljevid):
    vhodi_izhodi = [vozlisce for vozlisce in zemljevid if len(zemljevid[vozlisce]) ==  1]
    if pot[0] not in vhodi_izhodi or pot[-1] not in vhodi_izhodi:
        return False
    for vozlisce in pot[1:-1]:
        if vozlisce in vhodi_izhodi:
            return False
    for v1, v2 in zip(pot, pot[1:]):
        if v1 == v2:
            return False
    for v1, v2 in zip(pot, pot[1:]):
        if v2 not in zemljevid[v1]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    pot_unikati = list(set(pot))
    krozisca = [vozlisce for vozlisce in zemljevid if len(zemljevid[vozlisce]) > 1]
    for krozisce in krozisca:
        if krozisce not in pot_unikati or pot.count(krozisce) > 1:
            return False
    return mozna_pot(pot, zemljevid)

def navodila(pot, zemljevid):
    navodila_ = []
    prejsnji = pot[0]
    for v1, v2 in zip(pot[1:], pot[2:]):
        prejsnji_indeks = zemljevid[v1].index(prejsnji)
        krozisca = zemljevid[v1][prejsnji_indeks:] + zemljevid[v1][:prejsnji_indeks]
        navodila_.append(krozisca.index(v2))
        prejsnji = v1
    return navodila_

def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek, zemljevid[zacetek][0]]
    trenutni = zemljevid[zacetek][0]
    prejsnji = pot[0]
    prejsnji_indeks = zemljevid[trenutni].index(prejsnji)


    for navodilo in navodila:
        krozisca = zemljevid[trenutni][prejsnji_indeks:] + zemljevid[trenutni][:prejsnji_indeks]

        trenutni = krozisca[navodilo]
        pot.append(trenutni)
        prejsnji = pot[len(pot) - 2]
        prejsnji_indeks = zemljevid[trenutni].index(prejsnji)

    return pot


def sosedi(doslej, zemljevid):
    mnozica = set()
    for v in doslej:
        for st in zemljevid[v]:
            if st not in doslej and st not in mnozica:
                mnozica.add(st)
    return mnozica


def razdalja(x, y, zemljevid):
    doslej = set()
    doslej.add(x)

    razdalja_ = 1

    sosedi_ = sosedi(doslej, zemljevid)
    while y not in sosedi_:
        doslej.clear()
        for val in sosedi_:
            doslej.add(val)
        sosedi_ = sosedi(doslej, zemljevid)
        razdalja_ += 1
    return razdalja_

def najkrajsa_navodila(x, y, zemljevid):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    vozlisca = set(zemljevid.keys())
    razdalje = {vozlisce: float("inf") for vozlisce in zemljevid}
    prejsnji = {vozlisce: None for vozlisce in zemljevid}

    razdalje[x] = 0

    while vozlisca:
        min_razdalja = min([razdalje[v] for v in zemljevid if v in vozlisca])
        for vozlisce in vozlisca:
            if razdalje[vozlisce] == min_razdalja:
                break

        if vozlisce == y:
            break

        vozlisca.remove(vozlisce)

        for sosed in sosedi((vozlisce,), zemljevid):
            razdalja_ = razdalje[vozlisce] + razdalja(vozlisce, sosed, zemljevid)
            if razdalja_ < razdalje[sosed]:
                razdalje[sosed] = razdalja_
                prejsnji[sosed] = vozlisce

    pot = [y]
    while pot[-1] != x:
        pot.append(prejsnji[pot[-1]])
    pot.reverse()

    return navodila(pot, zemljevid)


