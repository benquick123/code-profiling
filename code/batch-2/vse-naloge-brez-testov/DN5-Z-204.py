def unikati(s):
    nov = []
    for x in s:
        if x not in nov:
            nov.append(x)
    return nov

def avtor(tvit):
    for beseda in tvit.split():
        if ":" in beseda:
            return beseda[:-1]

def vsi_avtorji(tviti):
    sez = []
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in sez:
            sez.append(ime)
    return sez

def izloci_besedo(beseda):
    spredaj = False
    zadaj = False
    while spredaj == False:
        if not beseda[0].isalnum():
            beseda = beseda[1:]
        else:
            spredaj = True
            break
    while zadaj == False:
        if not beseda[-1].isalnum():
            beseda = beseda[:-1]
        else:
            zadaj = True
            break
    return beseda

def se_zacne_z(tvit, c):
    sez = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            beseda = izloci_besedo(beseda)
            sez.append(beseda)
    return sez

def zberi_se_zacne_z(tviti, c):
    sez = []
    vse = " ".join(tviti)
    sez += se_zacne_z(vse,c)
    return unikati(sez)

def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, "@")
    return afne

def vsi_hashtagi(tviti):
    hash = zberi_se_zacne_z(tviti, "#")
    return hash

#Vrne po abecedi urejen seznam vseh oseb, ki nastopajo v tvitih - bodisi kot avtorji, ali omenjene v tvitih. Vsaka oseba naj se pojavi le enkrat.
def vse_osebe(tviti):
    sez = []
    sez += vsi_avtorji(tviti)
    sez += vse_afne(tviti)
    sez = unikati(sez)
    return sorted(sez)

def custva(tviti, hashtagi):
    sez = []
    for tvit in tviti:
        for hash in hashtagi:
            if hash in tvit:
                sez.append(avtor(tvit))
    return sorted(unikati(sez))

def se_poznata(tviti, oseba1, oseba2):
    poznanstvo = False
    tviti1 = []
    tviti2 = []
    for x in tviti:
        if oseba1 == avtor(x):
            tviti1.append(x)
            if oseba2  in vse_afne(tviti1):
                poznanstvo = True
    for y in tviti:
        if oseba2 == avtor(y):
            tviti2.append(y)
            if oseba1 in vse_afne(tviti2):
                poznanstvo = True
    return poznanstvo




