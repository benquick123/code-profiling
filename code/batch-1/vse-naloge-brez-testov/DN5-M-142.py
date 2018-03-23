def unikati(s):
    nov =[]

    for el in s:
        if el not in nov:
            nov.append(el)
    return nov

def avtor(tvit):
    vrni = tvit.split(" ")
    ime = vrni[0]
    return ime.replace(":","")

def vsi_avtorji(tviti):
    seznam =[]
    for el in tviti:
        seznam.append(avtor(el))
    return unikati(seznam)

def izloci_besedo(beseda):
    nova=""
    for crka in beseda:
        if crka.isalnum() or crka == '-':
            nova+=crka
    return nova

def se_zacne_z(tvit,c):
    razcleni = tvit.split(" ")
    nov=[]
    for raz in razcleni:
        if raz[0] == c:
            nov.append(izloci_besedo(raz))
    return nov

def zberi_se_zacne_z(tviti,c):
    nov=[]
    for tvit in tviti:
        nov.extend(se_zacne_z(tvit,c))
    return unikati(nov)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    nov=[]
    nov.extend(vsi_avtorji(tviti))
    nov.extend(vse_afne(tviti))
    nov = unikati(nov)
    nov.sort()
    return nov

def custva(tviti,hashtagi):
    nov=[]
    for has in hashtagi:
        for tvit in tviti:
            if has in se_zacne_z(tvit,"#"):
                nov.append(avtor(tvit))

    nov = unikati(nov)
    nov.sort()
    return nov

def se_poznata(tviti,oseba1,oseba2):
    for tvit in tviti:
        if avtor(tvit)==oseba1:
            if oseba2 in se_zacne_z(tvit,"@"):
                return True
        if avtor(tvit)==oseba2:
            if oseba1 in se_zacne_z(tvit,"@"):
                return False

