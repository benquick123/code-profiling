def izloci_besedo(beseda):
    n = 0

    for crka in beseda:
        if crka.isalnum() == False:
            n = n + 1
        if crka.isalnum() == True:
            break

    beseda1 = beseda[n:]
    beseda2 = beseda1[::-1]
    n = 0

    for crka in beseda2:
        if crka.isalnum() == False:
            n = n + 1
        if crka.isalnum() == True:
            break
    beseda1 = beseda2[n:]

    return(beseda1[::-1])

"""------------------------------------------------"""

from collections import defaultdict

def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        ime = tvit.split(":")[0]
        slovar[ime] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        ime = tvit.split(":")[0]
        if ime not in slovar:
            slovar[ime] = besedilo(tvit)
        else:
            pass

    return slovar

def prestej_tvite(tviti):
    seznam = []
    slovar = defaultdict(list)
    for tvit in tviti:
        seznam.append(tvit.split((": "), 1)[0])
        slovar = defaultdict(int)
        for ime in seznam:
            slovar[ime] += 1

    return slovar

def omembe(tviti):
    seznam = []
    slovar = defaultdict(list)
    for tvit in tviti:
        seznam.append(tvit.split(": ", 1))
        for ime, tvit1 in seznam:
            seznam1 = tvit1.split()
        for beseda in seznam1:
            seznam1 = slovar[ime]
            if beseda[0] == "@" not in seznam1:
                seznam1.append(izloci_besedo(beseda[1:]))
                slovar[ime] = seznam1
    return slovar

def neomembe(ime, omembe):
    seznam = []
    for kljuc in omembe:
        if kljuc != ime and kljuc not in omembe[ime]:
            seznam.append(kljuc)

    return seznam

