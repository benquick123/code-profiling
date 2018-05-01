def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    avtorji = []
    for zapis in tviti:
        avtorji.append(avtor(zapis))
    return unikati(avtorji)

def izloci_besedo(beseda):
    return "".join(i for i in beseda if i.isalnum() or i == "-")

def se_zacne_z(tvit, c):
    return [izloci_besedo(i) for i in tvit.split() if i.startswith(c)]

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)

def vse_afne(tviti):
    seznam = []
    for i in tviti:
        for j in i.split():
            if j.startswith("@"):
                seznam.append(izloci_besedo(j))
    return unikati(seznam)

def vsi_hashtagi(tviti):
    seznam = []
    for i in tviti:
        for j in i.split():
            if j.startswith("#"):
                seznam.append(izloci_besedo(j))
    return unikati(seznam)

def vse_osebe(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    seznam += vse_afne(tviti)
    return unikati(sorted(seznam))

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        for hash in hashtagi:
            if hash in tvit:
                seznam.append(avtor(tvit))
    return unikati(sorted(seznam))

def se_poznata(tviti, oseba1, oseba2):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = [izloci_besedo(i) for i in tvit.split() if i.startswith("@")]
    try:
        if oseba1 in slovar[oseba2] or oseba2 in slovar[oseba1]:
            return True
    except KeyError:
        return False




