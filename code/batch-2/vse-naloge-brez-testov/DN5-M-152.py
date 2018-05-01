# Obvezni del 1:
def unikati(s):
    nov_unikati = []
    for stevilka in s:
        if stevilka not in nov_unikati:
            nov_unikati.append(stevilka)
    return nov_unikati

# Obvezni del 2:
def avtor(tvit):
    ime = tvit.split(":")
    return ime[0]

# Obvezni del 3:
def vsi_avtorji(tviti):
    avtorji = []
    for ime in tviti:
        avtorji.append(avtor(ime))
    unikat_avtorji = unikati(avtorji)
    return unikat_avtorji

# Obvezni del 4:
def izloci_besedo(beseda):
    if beseda.isalnum():
        return beseda
    else:
        while beseda[0].isalnum() == False:
            beseda = beseda[1:]
        while beseda[-1].isalnum() == False:
            beseda = beseda[:-1]
    return beseda

# Obvezni del 5:
def se_zacne_z(tvit, c):
    besede = []
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            besede.append(beseda)
    return besede

# Obvezni del 6:
def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit, c))
        unikat_besede = unikati(besede)
    return unikat_besede

# Obvezni del 7:
def vse_afne(tviti):
    return(zberi_se_zacne_z(tviti, "@"))

# Obvezni del 8:
def vsi_hashtagi(tviti):
    return(zberi_se_zacne_z(tviti, "#"))

# Obvezni del 9:
def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti)
    osebe.extend(vse_afne(tviti))
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

# Dodatni del 1:
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for a in hashtagi:
            if "#"+a in tvit:
                avtorji.append(avtor(tvit))
            avtorji = unikati(avtorji)
            avtorji.sort()
    return avtorji

# Dodatni del 2:
def se_poznata(tviti, oseba1, oseba2):
    i = 0
    for tvit in tviti:
        if oseba1+":" in tvit and "@"+oseba2 in tvit:
            i += 1
    if i >= 1:
        return True
    else:
        return False

