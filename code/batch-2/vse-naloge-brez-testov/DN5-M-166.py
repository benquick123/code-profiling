def unikati(s):
    nov_seznam = []
    for x in s:
        if x in nov_seznam:
            pass
        else:
            nov_seznam.append(x)
    return nov_seznam


def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    seznam2 = []
    for kos in tviti:
        seznam2.append(avtor(kos))
    return unikati(seznam2)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
            beseda = beseda[1:]
    while not beseda[-1].isalnum():
           beseda = beseda[:-1]
    return beseda


def se_zacne_z(tvit, c):
    seznam3 = tvit.split(" ")
    seznam4 = []
    for beseda in seznam3:
        if beseda[0] == c:
            seznam4.append(izloci_besedo(beseda))
    return seznam4


def zberi_se_zacne_z(tviti, c):
    seznam3 =[]
    for x in tviti:
        seznam3 += x.split(" ")
    seznam4 = []
    for beseda in seznam3:
        if beseda[0] == c:
            if izloci_besedo(beseda) in seznam4:
                pass
            else:
                seznam4.append(izloci_besedo(beseda))
    return seznam4


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    seznam_oseb.sort()
    return seznam_oseb


def custva(tviti, hashtagi):
    seznam1 =[]
    seznam_avtorjev = []
    for x in tviti:
        seznam1 = x.split(" ")
        for beseda in seznam1:
            if beseda[0] == "#":
                if izloci_besedo(beseda) in hashtagi:
                     seznam_avtorjev.append(avtor(x))
    seznam_avtorjev = unikati(seznam_avtorjev)
    seznam_avtorjev.sort()
    return seznam_avtorjev


def se_poznata(tviti, oseba1, oseba2):
    seznam1 =[]
    velja = 0
    for x in tviti:
        seznam1 = x.split(" ")
        for beseda in seznam1:
            if beseda[0] == "@":
                if izloci_besedo(beseda) == oseba1 and oseba2 == avtor(x):
                     velja += 1
    seznam2 =[]
    for x in tviti:
        seznam2 = x.split(" ")
        for beseda in seznam2:
            if beseda[0] == "@":
                if izloci_besedo(beseda) == oseba2 and oseba1 == avtor(x):
                     velja += 1
    if velja:
        return True
    else:
        return False



