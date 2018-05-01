import collections

def preberi(ime_datoteke):

    slovar = collections.defaultdict(list)
    kljuc = 1


    for vrstica in open(ime_datoteke):
        seznam = []
        for y in vrstica.split(" "):
            seznam.append(int(y.strip()))



        for x in range(len(seznam)):

            if seznam[0] != min(seznam):  #če prvi element ni minimum seznama ga dodaš na konec in ga zbrišeš iz začetka
                seznam.append(seznam[0])
                seznam.remove(seznam[0])
            else:
                break

        slovar[kljuc] = seznam
        kljuc += 1

    return slovar


def mozna_pot(pot, zemljevid):
    slovar = zemljevid

    pari = list(zip(pot, pot[1:]))

    kljuc, vrednost = pari[0]

    if len(slovar[kljuc]) != 1:         #prvo krožišče ni začetek, vrni false.
        return False

    if len(pari) == 1:
        return False

    if vrednost in slovar[kljuc]:

        for kljuc, vrednost in pari[1:]:
            if vrednost not in slovar[kljuc] or len(slovar[kljuc]) == 1:       #če vrednosti ni v seznamu (ne moremo priti do krozisca)
                return False                                                # ali če je katerikoli seznam vmes dolg 1 element (smo sli na izhod)
                                                                            #vrni False

        if len(slovar[vrednost]) != 1:      #ko končamo pogledamo dolžino seznama na zadnjem ključu,
            return False                    # če ni 1 pomeni da nismo prišli na izhod (vrni False)

        return True

    else:
        return False

def hamiltonova(pot, zemljevid):

    mozna = mozna_pot(pot, zemljevid)

    mnozica = set()
    mnozica1 = set()

    if mozna:
        for kljuc in zemljevid:              #sestavi mnozico vseh krozisc razen izhodov/vhodov
            if len(zemljevid[kljuc]) > 1:
                mnozica.add(kljuc)


        for krizisce in pot:                    #sestavi mnozico vseh krozisc cez katere "gre" pot
            if krizisce in mnozica1:            #ce je krizisce ze v mnozici pomeni, da gremo v 2. cez krizisce
                return False                    # in zato vrnemo false

            if len(zemljevid[krizisce]) > 1:
                mnozica1.add(krizisce)

        return mnozica == mnozica1



    else:               #ce pot ni mozna (ni povezave, ne zacnemo/koncamo na vhodu/izhodu) vrnemo false
        return False

def obrni_seznam(uvoz, seznam):
    for x in range(len(seznam)):
        if seznam[0] != uvoz:
            seznam.append(seznam[0])
            seznam.remove(seznam[0])
        else:
            return seznam


def navodila(pot, zemljevid):

    pari = list(zip(pot[1:], pot[2:]))
    seznam = []

    uvoz = pot[0]           #zapomnemo si iz katerega krožišča pridemo v naslednje


    for kljuc, vrednost in pari:
        obrnjen_seznam = obrni_seznam(uvoz, zemljevid[kljuc])
        seznam.append(obrnjen_seznam.index(vrednost))
        uvoz = kljuc

    return seznam

def prevozi(zacetek, navodila, zemljevid):

    seznam = [zacetek]          #v seznam dodas 1. vrednost

    krozisce = zemljevid[zacetek][0]      #v seznam dodamo 2. vrednost (krozisce, kamor pridemo iz zacetka)
    seznam.append(krozisce)

    uvoz = zacetek

    for x in navodila:

        obrnjen_seznam = obrni_seznam(uvoz, zemljevid[krozisce])

        uvoz = krozisce         #zapomnimo si iz katerega uvoza bomo prišli v naslednje krožišče

        krozisce = obrnjen_seznam[x]
        seznam.append(krozisce)


    return seznam

def sosedi(doslej, zemljevid):

    mnozica = set()

    for krozisce in doslej:
        for x in zemljevid[krozisce]:
            if x not in doslej:
                mnozica.add(x)

    return mnozica


def razdalja(x, y, zemljevid):
    mnozica = {x}
    stevec = 0
    mnozica2 = set()
    mnozica3 = set()
    mnozica4 = set()
    mnozica5 = set()

    stevec += 1
    for a in zemljevid[x]:

        mnozica.add(a)
        mnozica2.add(a)
        if y in mnozica:
            return stevec

    stevec += 1
    for a in mnozica2:
        for b in zemljevid[a]:
            mnozica.add(b)
            mnozica3.add(b)
            if y in mnozica:
                return stevec

    stevec += 1
    for a in mnozica3:
        for b in zemljevid[a]:
            mnozica.add(b)
            mnozica4.add(b)
            if y in mnozica:
                return stevec

    stevec += 1
    for a in mnozica4:
        for b in zemljevid[a]:
            mnozica5.add(b)
            mnozica.add(b)
            if y in mnozica:
                return stevec

    stevec += 1
    for a in mnozica5:
        for b in zemljevid[a]:
            mnozica.add(b)
            if y in mnozica:
                return stevec

import collections







