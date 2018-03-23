def unikati(s):
    nov = []
    for i in s:
        if i not in nov:
            nov.append(i)
    return nov

def avtor(tvit):
    tvit = tvit.split(":")
    return tvit[0]

def vsi_avtorji(tviti):
    seznam = []
    for niz in tviti:
        ime = avtor(niz)
        seznam.append(ime)
    return unikati(seznam)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    s = []
    for niz in tvit.split():
        if niz[0] == c:
            s.append(izloci_besedo(niz))
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        s += se_zacne_z(tvit, c)
    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    s = vse_afne(tviti)
    for tvit in tviti:
        s.append(avtor(tvit))
    s.sort()
    s = unikati(s)
    return s


