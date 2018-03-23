def unikati(s):
    unikati = []
    for element in s:
        if element not in unikati:
            unikati.append(element)
    return unikati

def avtor(tvit):
    return tvit[:tvit.find(":")]

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    while(not beseda[0].isalnum()):
        beseda = beseda[1:]
    while(not beseda[-1].isalnum()):
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    vse_besede = tvit.split()
    rezultati = []
    for beseda in vse_besede:
        if beseda[0] == c:
            rezultati.append(izloci_besedo(beseda))
    return rezultati

def zberi_se_zacne_z(tviti, c):
    rezultati = []
    for tvit in tviti:
        rezultati += se_zacne_z(tvit, c)
    return unikati(rezultati)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(osebe)

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        hashtagi_tvita = se_zacne_z(tvit, '#')
        for hashtag in hashtagi:
            if hashtag in hashtagi_tvita:
                avtorji.append(avtor(tvit))
    avtorji = sorted(avtorji)
    return unikati(avtorji)

def tviti_avtorja(tviti, ime):
    rezultati = []
    for tvit in tviti:
        if avtor(tvit) == ime:
            rezultati.append(tvit)
    return rezultati

def se_poznata(tviti, oseba1, oseba2):
    tviti_osebe1 = tviti_avtorja(tviti, oseba1)
    tviti_osebe2 = tviti_avtorja(tviti, oseba2)
    if oseba2 in vse_afne(tviti_osebe1):
        return True
    elif oseba1 in vse_afne(tviti_osebe2):
        return True
    return False



