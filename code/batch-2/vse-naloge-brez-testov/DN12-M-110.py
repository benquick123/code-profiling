import collections

def preobrni_iz_prejsnjega(s, preobrni_v):
    seznam = s
    stevec = 0
    while seznam[0] != preobrni_v:
        trenutni = seznam[0]
        if trenutni == preobrni_v:
            break
        else:
            del seznam[0]
            seznam.append(trenutni)
            stevec += 1
    return seznam, stevec

def preobrni_od_do(s, start, end):
    seznam = preobrni_iz_prejsnjega(s, start)[0]
    return preobrni_iz_prejsnjega(seznam, end)

def preobrni_n_krat(s, kolikokrat):
    seznam1 = s
    stevec = 0
    while stevec != kolikokrat:
        trenutni = seznam1[0]
        del seznam1[0]
        seznam1.append(trenutni)
        stevec += 1
    return seznam1

def preobrni_min(s):
    return preobrni_iz_prejsnjega(s, min(s))[0]
    """seznam = s
    najmanjsa = min(s)
    while seznam[0] != najmanjsa:
        trenutni = seznam[0]
        if trenutni == najmanjsa:
            break
        else:
            del seznam[0]
            seznam.append(trenutni)
    return seznam"""

def preberi(ime_datoteke):
    file = open(ime_datoteke)
    datoteka = file.read()
    vrstice = datoteka.splitlines()
    zemljevid = collections.defaultdict(list)
    for i, vrstica in enumerate(vrstice):
        seznam_stevilk = vrstica.split()
        for e in seznam_stevilk:
            zemljevid[i+1].append(int(e))
        zemljevid[i+1] = preobrni_min(zemljevid[i + 1])
    return zemljevid

def koncna(del_poti, zemljevid):
    if len(zemljevid[del_poti]) < 2:
        return True
    return False

def mozna_pot(pot, zemljevid):
    if koncna(pot[0], zemljevid) and koncna(pot[-1], zemljevid):
        for index, (prvi, drugi) in enumerate(zip(pot, pot[1:])):
            if index != 0 and index != len(pot) - 1 and koncna(prvi, zemljevid):  # če ni prvi ali pa zadnji element v seznamu, potem preveri, če je pot končna
                return False
            if drugi not in zemljevid[prvi]:
                return False
        return True
    return False

def unikati(s):
    uni = []
    for i in s:
        if i not in uni:
            uni.append(i)
    return uni

def krozisca(zemljevid):
    s = []
    for krizisce in zemljevid:
        if len(zemljevid[krizisce]) > 1:
            s.append(krizisce)
    return s

def vsa_krozisca(pot, zemljevid):
    s = krozisca(zemljevid)
    for krizisce in s:
        if krizisce not in pot:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if pot == unikati(pot) and mozna_pot(pot, zemljevid) and vsa_krozisca(pot, zemljevid):
        return True
    return False

def navodila(pot, zemljevid):
    seznam_izhodov = []
    for prvi, drugi, tretji in zip(pot, pot[1:], pot[2:]):
        preobrnitev = preobrni_od_do(zemljevid[drugi], prvi, tretji)
        seznam_izhodov.append(preobrnitev[1])
    return seznam_izhodov

def prevozi(zacetek, navodila, zemljevid):
    seznam = [zacetek]
    prejsnje_krozisce = zacetek
    krozisce = zemljevid[zacetek][0]
    seznam.append(krozisce)
    for e in navodila:
        seznam_tega_krozisca = zemljevid[krozisce]
        seznam_tega_krozisca = preobrni_iz_prejsnjega(seznam_tega_krozisca, prejsnje_krozisce)[0]
        prejsnje_krozisce = krozisce
        krozisce = preobrni_n_krat(seznam_tega_krozisca, e)[0]
        seznam.append(krozisce)
    return seznam

def sosedi(doslej, zemljevid):
    mnozica = set()
    for krozisce in doslej:
        for sosedje in zemljevid[krozisce]:
            if sosedje not in doslej:
                mnozica.add(sosedje)
    return mnozica

def razdalja(x, y, zemljevid):
    mnozica = {x}
    i = 0
    while y not in mnozica:
        mnozica = sosedi(mnozica, zemljevid)
        i=i+1
    return i
"""
def sosedi_2(krizisce, zemljevid):
    mnozica = set()
    for sosedje in zemljevid[krizisce]:
            mnozica.add(sosedje)
    return mnozica

def najkrajsa_navodila_1(x, y, dolzina, seznam, zemljevid):
    mnozica = {x}
    if y == x:
        return seznam
    while y not in mnozica:
        mnozica = sosedi(mnozica, zemljevid)
    for krizisce in mnozica:
        if y in zemljevid[krizisce]:
            seznam.extend(krizisce)
            y = krizisce
    return najkrajsa_navodila_1(x, y, dolzina-1, seznam, zemljevid)

def najkrajsa_navodila(x, y, zemljevid):
    dolzina = razdalja(x, y, zemljevid)
    seznam = [y]
    return najkrajsa_navodila_1(x, y, dolzina, seznam, zemljevid)

def najkrajsa_navodila(x, y, zemljevid):
    mnozica = {x}
    slovar = dict()
    while y not in mnozica:
        for krizisce in mnozica:
            mnozica = sosedi_2(krizisce, zemljevid)
            for e in slovar:
                k = slovar[e]
                if k in mnozica:
                    mnozica.remove(k)
            print(mnozica)
            for sosed in mnozica:
                slovar[sosed] = krizisce
            if y in mnozica:
                break
    print(slovar)
    zadnji = y
    seznam = list()
    while zadnji != x:
        for trenutni in slovar:
            if trenutni == zadnji:
                seznam.append(trenutni)
                zadnji = slovar[trenutni]
                break
        if zadnji == x:
            seznam.append(x)
            break
        print(seznam)
    seznam = seznam[::-1]
    navigacija = navodila(seznam, zemljevid)
    return navigacija"""

def sosedi_2(slovar, zemljevid):
    nov_slovar = dict(slovar)
    for krozisce in slovar:
        for sosedje in zemljevid[krozisce]:
            if sosedje not in slovar:
                nov_slovar[sosedje] = krozisce
    #print(nov_slovar)
    return nov_slovar

def najkrajsa_navodila(x, y, zemljevid):
    zaceten = {x: sosedi({x}, zemljevid).pop()}
    while y not in zaceten:
        zaceten = sosedi_2(zaceten, zemljevid)
    #print(zaceten)
    zadnji = y
    seznam = list()
    while zadnji != x:
        for trenutni in zaceten:
            if trenutni == zadnji:
                seznam.append(trenutni)
                zadnji = zaceten[trenutni]
                break
        if zadnji == x:
            seznam.append(x)
            break
        #print(seznam)
    seznam = seznam[::-1]
    navigacija = navodila(seznam, zemljevid)
    return navigacija



