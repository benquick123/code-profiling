def unikati(s):
    """Vrne vse elemente seznama po 1x"""
    sez = []
    for a in s:
        if a not in sez:
            sez.append(a)
    return sez

def avtor(tvit):
    """Vrne ime avtorja (vse pred :)"""
    ime = tvit.split(":")
    return ime[0]

def vsi_avtorji(tvit):
    """Vrne vse avtorje po 1x"""
    sez = []
    for vrsta in tvit:
        ime = avtor(vrsta)
        sez.append(ime)
    vsi = unikati(sez)
    return vsi

def izloci_besedo(beseda):
    """Vrne besedo brez vseh čudnih znakov"""
    for znak in beseda:
        if str.isalnum(znak):
            break
        beseda = beseda.replace(znak, "")
    for znak in beseda[::-1]:
        if str.isalnum(znak):
            break
        beseda = beseda.replace(znak, "")
    return beseda

def se_zacne_z(tvit, c):
    """Vrne besedo, ki se začne z določenim znakom"""
    tvit = tvit.split()
    sez = []
    for beseda in tvit:
        if beseda[0] == c:
            nova = izloci_besedo(beseda)
            sez.append(nova)
    return sez

def zberi_se_zacne_z(tviti, c):
    """Vrne vse besede, ki se začnejo z določenim znakom po 1x"""
    sez = []
    for niz in tviti:
        besede = se_zacne_z(niz, c)
        if besede != []:
            sez.append(besede)
    sezn = []
    for listi in sez:
        skupaj = sezn + listi
        sezn = skupaj
    return vsi_avtorji(sezn)

def vse_afne(tviti):
    """"Vrne vse besede, ki se začnejo z @ po 1x"""
    afna = "@"
    afne = zberi_se_zacne_z(tviti, afna)
    return afne

def vsi_hashtagi(tviti):
    """Vrne vse besede, ki se začnejo s # po 1x"""
    hash = "#"
    hashtag = zberi_se_zacne_z(tviti, hash)
    return hashtag

def vse_osebe(tviti):
    """Vrne vse besede, ki se pojavijo kot avtorji ali so emenjene po 1x"""
    afna = "@"
    afne = zberi_se_zacne_z(tviti, afna)
    avtorji = vsi_avtorji(tviti)
    sez = sorted(unikati(afne + avtorji))
    return sez

#Dodatna naloga
def custva(tviti, hashtagi):
    """Vrne seznam imen, ki so uporabljala določene hashtage"""
    sez = []
    for deli in tviti:
        for hash in hashtagi:
            if "#"+hash in deli:
                sez.append(avtor(deli))
    sez = sorted(unikati(sez))
    return sez

def se_poznata(tviti,oseba1,oseba2):
    """Vrne TRUE. če se osebi poznatas"""
    for part in tviti:
        if oseba1 == avtor(part):
            c = "@"
            sez = se_zacne_z(part,c)
            if oseba2 in sez:
                return True
    return  False





