def unikati(s):
    unikati = []
    for element in s:
        if element not in unikati:
            unikati.append(element)
    return unikati

def avtor(tvit):
    razdeljen = tvit.split(":")
    return razdeljen[0]

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

def vsi_hashtagi(tviti):
    hashtagi = zberi_se_zacne_z(tviti, "#")
    return hashtagi


def besedilo(tvit):
    razdeljen = tvit.split()
    vsebina = ""
    del razdeljen[0]
    for beseda in razdeljen:
        vsebina += beseda
        vsebina += " "
    vsebina = vsebina[:-1]
    return vsebina

def zadnji_tvit(tviti):
    zadnji_tviti = {}
    for tvit in tviti:
        zadnji_tviti[avtor(tvit)] = besedilo(tvit)
    return zadnji_tviti

def prvi_tvit(tviti):
    prvi_tviti = {}
    for tvit in tviti:
        if avtor(tvit) not in prvi_tviti:
            prvi_tviti[avtor(tvit)] = besedilo(tvit)
    return prvi_tviti

def prestej_tvite(tviti):
    vsi_tviti = {}
    for tvit in tviti:
        if avtor(tvit) not in vsi_tviti:
            vsi_tviti[avtor(tvit)] = 1
        elif avtor(tvit) in vsi_tviti:
            vsi_tviti[avtor(tvit)] += 1
    return vsi_tviti

def omembe(tviti):
    omembe_tviti = {}
    for tvit in tviti:
        if avtor(tvit) not in omembe_tviti:
            omembe_tviti[avtor(tvit)] = se_zacne_z(tvit, "@")
        elif avtor(tvit) in omembe_tviti:
            omembe_tviti[avtor(tvit)] += se_zacne_z(tvit, "@")
    for oseba in omembe_tviti:
        omembe_tviti[oseba] = unikati(omembe_tviti[oseba])
    return omembe_tviti

def neomembe(ime, omembe):
    imena = []
    neomenjeni = []
    for avtor in omembe:
        imena.append(avtor)
    for avtor in omembe:
        if avtor == ime:
            for avtor1 in imena:
                if avtor1 != ime and avtor1 not in omembe[ime]:
                    neomenjeni.append(avtor1)
    return neomenjeni

def se_poznata(ime1, ime2, omembe):
    for ime in omembe:
        if ime1 == ime and ime2 in omembe[ime]:
            return True
        elif ime2 == ime and ime1 in omembe[ime]:
            return True
    return False

def hashtagi(tviti):
    slovar_hashtagi = {}
    zbrani_hashtagi = vsi_hashtagi(tviti)
    for tvit in tviti:
        razdeljen = tvit.split(":")
        razdeljen_tvit = razdeljen[1].split()
        razdeljen_besede = []
        for beseda in razdeljen_tvit:
            razdeljen_besede.append(izloci_besedo(beseda))
        for hashtag in zbrani_hashtagi:
            if hashtag not in slovar_hashtagi:
                if hashtag in razdeljen_besede:
                    slovar_hashtagi[hashtag] = [razdeljen[0]]
            elif hashtag in slovar_hashtagi:
                if hashtag in razdeljen_besede:
                    slovar_hashtagi[hashtag].append(razdeljen[0])
    for hashtag in slovar_hashtagi:
        slovar_hashtagi[hashtag].sort()
    return slovar_hashtagi



