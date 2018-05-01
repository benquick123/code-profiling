def preberi(ime_datoteke):
    rezultat = {}
    with open(ime_datoteke) as file:
        for ln, line in enumerate(file):
            sosedi = [int(x) for x in line.split()]
            najm_element = sosedi.index(min(sosedi))
            urejeni_sosedi = sosedi[najm_element:] + sosedi[:najm_element]
            rezultat[ln + 1] = urejeni_sosedi
    return rezultat

def mozna_pot(pot, zemljevid):
    return mozna_pot_impl(pot, zemljevid, 0)

def mozna_pot_impl(pot, zemljevid, lvl):
    a, b = pot[0], pot[1]
    mozen_prehod = b in zemljevid[a]
    a_izhod = len(zemljevid[a]) == 1
    b_izhod = len(zemljevid[b]) == 1
    if a == b: return False
    if lvl == 0 and not a_izhod: return False
    if len(pot) == 2: return mozen_prehod and b_izhod
    if mozen_prehod and mozna_pot_impl(pot[1:], zemljevid, lvl + 1) and not b_izhod:
        return True
    else:
        return False

from collections import Counter
def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        vsa_krozisca = Counter({krozisce for krozisce in zemljevid if len(zemljevid[krozisce]) > 1})
        for krozisce in pot:
            if krozisce in vsa_krozisca:
                vsa_krozisca[krozisce] += 1
        if all(prehodi == 2 for prehodi in vsa_krozisca.values()):
            return True
    return False

def navodila(pot, zemljevid):
    navodilo = []
    for i, prestop in enumerate(pot):
        a, b = pot[i], pot[i+1]
        if len(zemljevid[a]) == 1:
            continue
        prejsnji = pot[i-1]
        vhod_v_a = zemljevid[a].index(prejsnji)
        izhod_do_b = zemljevid[a].index(b)
        razlika = izhod_do_b - vhod_v_a
        navodilo.append(razlika % (len(zemljevid[a])))
        if len(zemljevid[b]) == 1:
            break;
    return navodilo

def prevozi(zacetek, navodila, zemljevid):
    prevoz = []
    prevoz.append(zacetek)
    prevoz.append(zemljevid[zacetek][0])
    for ukaz in navodila:
        prisel_iz = prevoz[-2]
        trenutna_lokacija = zemljevid[prevoz[-1]]
        destinacija = trenutna_lokacija[(trenutna_lokacija.index(prisel_iz) + ukaz) % len(trenutna_lokacija)]
        prevoz.append(destinacija)
    return prevoz

def sosedi(doslej, zemljevid):
    mnozica_sosedov = set()
    for vozlišče in doslej:
        sosedi_vozlisca = zemljevid[vozlišče]
        for sosed in sosedi_vozlisca:
            mnozica_sosedov.add(sosed)
    for krozisce in doslej:
        if krozisce in mnozica_sosedov:
            mnozica_sosedov.remove(krozisce)
    return mnozica_sosedov

def razdalja(x, y, zemljevid):
    mnozica = sosedi(set([x]), zemljevid)
    st_korakov = 1
    while y not in mnozica:
        st_korakov += 1
        iteracija_sosedov = sosedi(mnozica, zemljevid)
        for sosed in iteracija_sosedov: mnozica.add(sosed)
    return st_korakov

def slovarifikacija(slovar, zemljevid):
    rezultat = slovar.copy()
    for kljuc in list(rezultat):
        sosedi_kljuca = zemljevid[kljuc]
        for sosed in sosedi_kljuca:
            if sosed not in rezultat:
                rezultat[sosed] = kljuc
    return rezultat

def slovar_to_pot(x, y, slovar):
    pot = [y]
    while x != pot[-1]:
        pot.append(slovar[pot[-1]])
    return pot

def najkrajsa_navodila(x, y, zemljevid):
    slovar = {zemljevid[x][0]: x}
    while y not in slovar:
        slovar = slovarifikacija(slovar, zemljevid)
    pot = slovar_to_pot(x, y, slovar)
    navodilo = navodila(pot[::-1], zemljevid)
    return navodilo



