def unikati(s):
    nov_seznam=[]
    for x in s:
        if x not in nov_seznam:
            nov_seznam.append(x)
    return nov_seznam

def avtor(tvit):
    return tvit[0:tvit.find(":")]

def vsi_avtorji(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    return unikati(seznam)

def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda.strip(beseda[0])
    while beseda[-1].isalnum() == False:
        beseda = beseda.rstrip(beseda[-1])
    return beseda

def se_zacne_z(tvit, c):
    nov_seznam = []
    seznam = tvit.split()
    for x in seznam:
        if x[0] == c:
            nov_seznam.append(izloci_besedo(x))
    return nov_seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) +
                  vse_afne(tviti)),
                  key=str.lower)

def custva(tviti, hashtagi):
    imena = []
    seznam = list(zip(vsi_avtorji(tviti),vsi_hashtagi(tviti)))
    for x in seznam:
        for hash in hashtagi:
            if x[1] == hash:
                imena.append(x[0])
    return sorted(unikati(imena), key=str.lower)

