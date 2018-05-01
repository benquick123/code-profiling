def preberi(ime_datoteke):
    slovar = {}
    i = 1
    for vrstica in open(ime_datoteke):
        krozisce = vrstica.strip()
        slovar[i] = []
        for cifra in krozisce.split():
            slovar[i].append(int(cifra))
        while slovar[i][0] != min(slovar[i]):
            slovar[i].append(slovar[i][0])
            del slovar[i][0]
        i += 1
    return slovar


def mozna_pot(pot, zemljevid):
    return True if len(zemljevid[pot[0]]) == len(zemljevid[pot[-1]]) == 1 and \
                   all([len(zemljevid[i]) > 1 for i in pot[1:-1]]) and \
                   all([i != j for i, j in zip(pot, pot[1:])]) and \
                   all([i in zemljevid[j] for i, j in zip(pot, pot[1:])]) else False

def hamiltonova(pot, zemljevid):
    return True if mozna_pot(pot, zemljevid) \
                   and all([kljuc in pot or len(zemljevid[kljuc]) == 1 for kljuc in zemljevid]) \
                   and all(pot.count(tocka)==1 for tocka in pot) else False


def navodila(pot, zemljevid):
    return [(zemljevid[j].index(k) - zemljevid[j].index(i)) % len(zemljevid[j]) for i, j, k in zip(pot, pot[1:], pot[2:])]

def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek, zemljevid[zacetek][0]]
    for zavoj in navodila:
        pot.append(zemljevid[pot[-1]][(zemljevid[pot[-1]].index(pot[-2]) + zavoj) % len(zemljevid[pot[-1]])])
    return pot


def sosedi(doslej, zemljevid):
    mnozica = set()
    for tocka in doslej:
        mnozica = mnozica | set(zemljevid[tocka])
    mnozica = mnozica - doslej
    return mnozica


def razdalja(x, y, zemljevid):
    mnozica = {x}
    i = 0
    while y not in mnozica:
        mnozica = mnozica | sosedi(mnozica, zemljevid)
        i = i + 1
    return i


def kljucsosedi(doslej, zemljevid):
    slovar = doslej.copy()
    for kljuc in doslej:
        for sosed in zemljevid[kljuc]:
            if sosed not in slovar:
                slovar[sosed] = kljuc
    return slovar

def najkrajsa_navodila(x, y, zemljevid):
    slovar = {zemljevid[x][0]: x}
    while y not in slovar:
        slovar = kljucsosedi(slovar, zemljevid)
    # print(slovar[y])

    najdeno = y
    pot = []
    while najdeno != x:
        pot.append(najdeno)
        najdeno = slovar[najdeno]
    return navodila([x] + pot[::-1], zemljevid)

# def najkrajsa_navodila(x, y, zemljevid):
#     slovar = {x: zemljevid[x][0]}
#     pot = [x]
#     tpot = {x}
#     zadnjaplast = [x]
#     while y not in tpot:
#
#         for e in zadnjaplast:
#             for sosed in zemljevid[e]:
#                 if sosed not in tpot:
#                     slovar[sosed] = e
#                     tzadnjaplast.append(sosed)
#         zadnjaplast = sosedi(tpot, zemljevid) - tpot
#
#         tpot = tpot | sosedi(tpot, zemljevid)
#
#     najdeno = y
#     while najdeno != x:
#         najdeno = slovar[najdeno]
#         pot.append(najdeno)
#
#     return navodila(najdeno[:-1:], zemljevid)

