def besedilo(tvit):
    a = tvit.split(" ")
    stavek = " ".join(a[1:])

    return stavek

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:

        avtor = tvit.split(":")[0]
        slovar[avtor] = besedilo(tvit)


    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        if avtor not in slovar:
            slovar[avtor] = besedilo(tvit)

    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        if avtor not in slovar:
            slovar[avtor] = 1
        else:
            slovar[avtor] += 1

    return slovar


def isal(beseda):

    while beseda[len(beseda) - 1].isalnum() == False:
        beseda = beseda[:-1]

    while beseda[0].isalnum() == False:
        beseda = beseda[1:]

    return beseda

from collections import defaultdict

def omembe(tviti):
    slovar = defaultdict(list)

    for tvit in tviti:
        avtor = tvit.split(":")[0]
        seznam = slovar[avtor]
        for beseda in tvit.split(" "):
            if beseda[0] == "@":
                seznam.append(isal(beseda))
        slovar[avtor] = seznam

    print(slovar)
    return slovar


def neomembe(ime, omembe):
    seznam = []
    for x in omembe:  #gres cez vse kljuce
        if x not in omembe[ime] and x != ime:  #ce kljuc ni v seznamu omembe[ime] in ce kljuc ni enako imenu
            seznam.append(x)                   # ga dodas na seznam

    return seznam

def se_poznata(ime1, ime2, omembe):
    se_poznata = False
    for kljuc in omembe:

        if kljuc == ime1 and ime2 in omembe[ime1] or kljuc == ime2 and ime1 in omembe[ime2]:
            se_poznata = True
            break

    return se_poznata


def hashtagi(tviti):
    slovar = defaultdict(list)
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        besede = tvit.split(" ")
        for beseda in besede:
            if beseda[0] == "#":
                seznam = slovar[isal(beseda)]
                seznam.append(avtor)
                slovar[isal(beseda)] = sorted(seznam)

    return slovar



