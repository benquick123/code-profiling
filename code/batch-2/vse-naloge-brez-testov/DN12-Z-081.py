def preobrni(stevila):
    index = stevila.index(min(stevila))
    stevila2 = stevila[index:] + stevila[:index]
    return stevila2

def preobrni2(stevila, stevilo): # preobrni pot glede na podano število
    index = stevila.index(stevilo)
    stevila2 = stevila[index:] + stevila[:index]
    return stevila2


def preberi(ime_datoteke):
    slovar = {}
    datoteka = open(ime_datoteke)

    i = 1
    for vrstica in datoteka:
        razdeljeno = vrstica.strip().split(" ")
        razdeljeno_stevila = [int(i) for i in razdeljeno]
        stevila_preobrnjeno = preobrni(razdeljeno_stevila)
        slovar[i] = stevila_preobrnjeno
        i += 1

    datoteka.close()

    return slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1: # prva ...
        return False
    if len(zemljevid[pot[-1]]) != 1: # ... in zadnja morata biti krajiš&#269;i (samo ena pot vodi iz te to&#269;ke)
        return False

    if len(pot) == 2: # vmes ni povezave
        return False

    for i in range(1, len(pot) - 1):
        krozisce = pot[i]
        zadnjo_krozisce = pot[i - 1]
        if krozisce not in zemljevid[zadnjo_krozisce]:
            return False
        if len(zemljevid[krozisce]) == 1: # vmes gre ven
            return False

    return True

def seznam_krozisc(zemljevid):
    seznam = []
    for krozisce in zemljevid:
        if len(zemljevid[krozisce]) > 1:
            seznam.append(krozisce)
    return seznam


def vsa_krozisca(pot, zemljevid):
    for i in zemljevid:
        if i not in pot:
            return False
    return True


def brez_ponovitev(seznam):
    return len(seznam) == len(set(seznam))


def hamiltonova(pot, zemljevid):
    return mozna_pot(pot, zemljevid) and vsa_krozisca(pot, seznam_krozisc(zemljevid)) and brez_ponovitev(pot)


def izvoz(iz, v, na, zemljevid):
    izvozi = preobrni2(zemljevid[v], iz)
    index_izvoza = izvozi.index(na)
    return index_izvoza


def navodila(pot, zemljevid):
    seznam_izvozov = []
    for i in range(1, len(pot) - 1):
        krozisce = pot[i]
        zadnjo_krozisce = pot[i - 1]
        naslednje_krozisce = pot[i + 1]
        seznam_izvozov.append(izvoz(zadnjo_krozisce, krozisce, naslednje_krozisce, zemljevid))
    return seznam_izvozov

def prevozi(zacetek, navodila2, zemljevid):
    seznam = [zacetek, zemljevid[zacetek][0]]
    krozisce = seznam[1]
    iz = seznam[0]

    for stevilka_izvoza in navodila2:
        seznam_izhodov = preobrni2(zemljevid[krozisce], iz)
        izhod = seznam_izhodov[stevilka_izvoza]
        seznam.append(izhod)

        iz = krozisce
        krozisce = izhod

    return seznam
