def unikati(s):
    novi = []
    for element in s:
        if element not in novi:
            novi.append(element)
    return novi

def avtor(tvit):
    s = tvit.find(":")
    return tvit[:s]

def vsi_avtorji(tviti):
    seznam = []
    for s in tviti:
        seznam.append(avtor(s))
    return unikati(seznam)

def izloci_besedo(beseda):
    i = 0
    while beseda[i].isalnum() == False:
        i += 1
    j = -1
    while beseda[j].isalnum() == False:
        j -= 1
    if j == -1:
        j = len(beseda)
    else:
        j += 1
    return beseda[i:j]

def se_zacne_z(tvit, c):
    seznam = []
    s = tvit.split()
    for beseda in s:
        if beseda[0] == c:
            seznam.append(izloci_besedo(beseda))
    return seznam

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
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(osebe)

def custva(tviti, hastagi):
    seznam = []
    for hash in hastagi:
        for tvit in tviti:
            if hash == se_zacne_z(tvit, "#"):
                seznam.append(avtor(tvit))
    return sorted(unikati(seznam))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if se_zacne_z(tvit, "@") == oseba1 and avtor(tvit) == oseba2:
            return True
        if se_zacne_z(tvit, "@") == oseba2 and avtor(tvit) == oseba1:
            return True
    return False

