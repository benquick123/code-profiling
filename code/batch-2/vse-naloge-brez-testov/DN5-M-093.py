def unikati(s):
    s1 = []
    for e in s:
        if e in s1:
            continue
        else:
            s1.append(e)
    return s1

def avtor(tvit):
    return tvit.split(":") [0]

def vsi_avtorji(tviti):
    vsi = []
    for tvit in tviti:
        vsi.append(avtor(tvit))
    return unikati(vsi)

def izloci_besedo(beseda):
    beseda = list(beseda)
    while not beseda[0].isalnum():
            beseda.remove(beseda[0])
    while not beseda[-1].isalnum():
            beseda.remove(beseda[-1])
    return "".join(beseda)

def se_zacne_z(tvit, c):
    nov = []
    for beseda in tvit.split(" "):
        if beseda[0] == c:
            nov.append(izloci_besedo(beseda))
        else:
            continue
    return nov

def zberi_se_zacne_z(tviti, c):
    nov = []
    for tvit in tviti:
        nov += se_zacne_z(tvit, c)
    return unikati(nov)

def vse_afne(tviti):
     return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    nov = []
    for hash in hashtagi:
        for tvit in tviti:
            if hash in vsi_hashtagi(tvit.split(" ")):
                nov.append(avtor(tvit))
    return sorted(unikati(nov))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            if oseba2 in se_zacne_z(tvit, "@"):
                return True
        if avtor(tvit) == oseba2:
            if oseba1 in se_zacne_z(tvit, "@"):
                return True
    return False



# TESTI!

