def preberi (ime_datoteke):
    dat = open(ime_datoteke).read().split("\n")
    d = {}
    i = 1
    for vrstica in dat:
        if vrstica == "":
            break
        d[i]=[]
        i+=1

    j = 1
    for vrstica in dat:
        if vrstica == " ":
            break
        cifra = vrstica.split(" ")
        for c in cifra:
            if c == '':
                break
            d[j].append(int(c))
        j+=1
    for indeks in d:
       d[indeks]=sortiraj(d[indeks])
    return d

def sortiraj(seznam):
    if len(seznam)==1:
        return seznam
    i = 0
    min = seznam[0]
    while i<len(seznam):
        if min > seznam[i]:
            min = seznam[i]
        i+=1

    zbrisano = []
    j = 0
    while True:
        if seznam[j] == min:
            break
        zbrisano.append(seznam[j])
        seznam.pop(j)
    seznam.extend(zbrisano)
    return seznam


def mozna_pot(pot, zemljevid):
    mozni_izhodi_vhodi = preveri_vhod_izhod(zemljevid)
    if pot[0] not in mozni_izhodi_vhodi or pot[-1] not in mozni_izhodi_vhodi:
        return False
    i = 0
    j = 1

    while j < len(pot):
        if pot[i] not in zemljevid[pot[j]] or (pot[i] in mozni_izhodi_vhodi and i>0) or pot[i]==pot[j]:
            return False
        i += 1
        j += 1

    return True

def preveri_vhod_izhod(zemljevid):
    seznam=[]
    for indeks in zemljevid:
        if len(zemljevid[indeks])==1:
            seznam.append(indeks)
    return seznam


def hamiltonova(pot,zemljevid):
    stKrozisc = 0
    if mozna_pot(pot,zemljevid):

        dolzinaUnikat = unikati(pot)

        if len(pot) == len(dolzinaUnikat):

            for st, krozisce in zemljevid.items():
                if len(krozisce) > 1:
                    stKrozisc = stKrozisc + 1

            if len(pot) - 2 == stKrozisc:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def unikati(s):
    seznam=[]
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def navodila(pot, zemljevid):
    gps = []
    j = 0
    premik = 0

    while j < len(pot)-2:
        prejsnji = pot[j]
        trenutni = pot[j+1]
        naslednji = pot[j+2]
        izvozi = zemljevid[trenutni]
        izhodisce = izvozi.index(prejsnji)
        izvozi.extend(izvozi)
        while True:
            if izvozi[izhodisce] == naslednji:
                break
            izhodisce += 1
            premik += 1
        gps.append(premik)
        premik = 0
        j+=1

    return gps

def prevozi(zacetek, navodila, zemljevid):
    prevozeno = []
    prevozeno.append(zacetek)
    krozisce = zemljevid[zacetek][0]
    prevozeno.append(krozisce)
    izhodisce = zacetek
    indeks = 0

    for cifra in navodila:
        krozisca = zemljevid[krozisce]
        i = 0
        while i<len(krozisca):
            if krozisca[i] == izhodisce:
                indeks = i
                break
            i+=1
        indeks += cifra
        krozisca.extend(krozisca)
        izhodisce = krozisce
        krozisce = krozisca[indeks]
        prevozeno.append(krozisce)

    return prevozeno




