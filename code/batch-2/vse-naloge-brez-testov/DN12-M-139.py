import collections


def preberi(ime_datoteke):
    vrstice = open(ime_datoteke).read()
    vrstice = vrstice.strip()
    vrstice = vrstice.split("\n")
    slovar = dict.fromkeys(range(1, len(vrstice) + 1))
    krizisce = 1

    for vrstica in vrstice:
        vrstica_stevilke = vrstica.split()
        vrednosti = []

        for povezava in vrstica_stevilke:
            vrednosti.append(int(povezava))

        while True:
            if vrednosti[0] == min(vrednosti):
                break
            else:
                vrednosti.append(vrednosti[0])
                vrednosti.remove(vrednosti[0])

        slovar[krizisce] = vrednosti
        krizisce += 1

    return slovar


def mozna_pot(pot, zemljevid):
    if not len(zemljevid[pot[0]]) == 1 or not len(zemljevid[pot[-1]]) == 1:
        return False

    for krozisce in range(1, len(pot) - 1):

        if len(zemljevid[pot[krozisce]]) == 1:
            return False

    for korak in range(len(pot) - 1):
        if pot[korak] == pot[korak + 1]:
            return False

        if pot[korak] not in zemljevid[pot[korak + 1]]:
            return False

    return True


def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False

    koraki = pot[1:-1]
    krozisca = []

    for krozisce in zemljevid:
        if len(zemljevid[krozisce]) != 1:
            krozisca.append(krozisce)

    for korak in koraki:
        if korak in krozisca:
            krozisca.remove(korak)

        else:
            return False

    if len(krozisca) == 0:
        return True

    else:
        return False


def navodila(pot, zemljevid):
    navodila_sez = []
    for korak in range(1, len(pot) - 1):
        izvoz = 0
        prisel_iz = pot[korak - 1]
        trenutno_v = pot[korak]
        zemljevid_trenutni = zemljevid[trenutno_v]
        grem_v = pot[korak + 1]

        izvoz_trenutni = zemljevid_trenutni.index(prisel_iz)

        while zemljevid_trenutni[izvoz_trenutni] != grem_v:
            zemljevid_trenutni.append(zemljevid_trenutni[0])
            zemljevid_trenutni.remove(zemljevid_trenutni[0])
            izvoz += 1

        navodila_sez.append(izvoz)

    return navodila_sez


def prevozi(zacetek, navodila, zemljevid):
    prevozi_sez = [zacetek]
    slovar_zacetkov = {1: 3, 2: 4, 12: 13, 15: 16}

    prisel_iz = zacetek
    trenutno_v = slovar_zacetkov[zacetek]

    prevozi_sez.append(trenutno_v)

    for navodilo in navodila:
        zemljevid_trenutni = zemljevid[trenutno_v]

        while zemljevid_trenutni[0] != prisel_iz:
            zemljevid_trenutni.append(zemljevid_trenutni[0])
            zemljevid_trenutni.remove(zemljevid_trenutni[0])

        grem_v = zemljevid_trenutni[navodilo]

        prevozi_sez.append(grem_v)
        prisel_iz = trenutno_v
        trenutno_v = grem_v

    return prevozi_sez


def sosedi(doslej, zemljevid):
    vrni = set()
    for element in doslej:
        povezave = zemljevid[element]

        for povezava in povezave:
            vrni.add(povezava)

    for element in doslej:
        if element in vrni:
            vrni.remove(element)

    return vrni


def razdalja(x, y, zemljevid):
    razdalja_med_krozisci = 0
    mnozica = {x}

    while True:
        if y in mnozica:
            return razdalja_med_krozisci

        else:
            mnozica = sosedi(mnozica, zemljevid)
            razdalja_med_krozisci += 1


def najkrajsa_navodila(x, y, zemljevid):
    # Slovar z povezavami med krozisci, ki se ne povezujejo na krizisca, ki smo jih ze obiskali

    lahko_obiscemo = set()
    lahko_obiscemo.add(x)
    poti = collections.defaultdict(list)

    poti[x] = zemljevid[x]

    while y not in lahko_obiscemo:
        for pot in poti:
            for element in zemljevid[pot]:
                lahko_obiscemo.add(element)

        for pot in lahko_obiscemo:
            for element in zemljevid[pot]:
                if element not in lahko_obiscemo:
                    poti[pot].append(element)

    # Iskanje najkrajse poti z pomočjo oddaljenosti med krozisci

    najkrajsa_pot = [x]
    koraki = poti[x]
    razdalja_med_xy = razdalja(x, y, zemljevid)

    while y not in koraki:
        for element in koraki:
            if razdalja(element, y, zemljevid) < razdalja_med_xy:
                korak_naslednji = element
                razdalja_med_xy = razdalja(element, y, zemljevid)

        koraki = poti[korak_naslednji]
        najkrajsa_pot.append(korak_naslednji)

    najkrajsa_pot.append(y)

    return navodila(najkrajsa_pot, zemljevid)


