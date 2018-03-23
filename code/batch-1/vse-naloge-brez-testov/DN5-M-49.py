def unikati(s):
    unikati = []
    for element in s:
        if element not in unikati:
            unikati.append(element)
    return unikati

def avtor(tvit):
    razdeljen = tvit.split(":")
    return razdeljen[0]

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        if avtor(tvit) not in avtorji:
            avtorji.append(avtor(tvit))
    return avtorji

def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    se_zacne = []
    for beseda in tvit.split():
        if beseda[0] == c:
            se_zacne.append(izloci_besedo(beseda))
    return se_zacne

def zberi_se_zacne_z(tviti, c):
    besede_tviti = []
    for tvit in tviti:
        besede_tvit = se_zacne_z(tvit, c)
        besede_tviti.extend(besede_tvit)
        enkrat_besede_tviti = unikati(besede_tviti)
    return enkrat_besede_tviti

def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, "@")
    return afne

def vsi_hashtagi(tviti):
    hashtagi = zberi_se_zacne_z(tviti, "#")
    return hashtagi

def vse_osebe(tviti):
    vse_osebe = []
    avtorji = vsi_avtorji(tviti)
    vse_osebe.extend(avtorji)
    osebe = vse_afne(tviti)
    vse_osebe.extend(osebe)
    vse_osebe = unikati(vse_osebe)
    vse_osebe.sort()
    return vse_osebe

def custva(tviti, hashtagi):
    osebe = []
    for tvit in tviti:
        razdeljen = tvit.split(":")
        razdeljen_tvit = razdeljen[1].split()
        razdeljen_besede = []
        for beseda in razdeljen_tvit:
            razdeljen_besede.append(izloci_besedo(beseda))
        for hashtag in hashtagi:
            if hashtag in razdeljen_besede:
                osebe.append(razdeljen[0])
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        razdeljen = tvit.split()
        razdeljen_besede = []
        razdeljen_besede_ciste = []
        for beseda in razdeljen:
            if beseda[0] == "@" or beseda[-1] == ":":
                razdeljen_besede.append(beseda)
        for beseda in razdeljen_besede:
            razdeljen_besede_ciste.append(izloci_besedo(beseda))
        if oseba1 in razdeljen_besede_ciste and oseba2 in razdeljen_besede_ciste:
            return True
    return False

