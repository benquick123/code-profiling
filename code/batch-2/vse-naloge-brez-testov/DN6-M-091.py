#Stare funkcije

def unikati(s):
    t = []
    for e in s:
        if e not in t:
            t.append(e)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    s = []
    for tvit in tviti:
        s.append(avtor(tvit))
    return unikati(s)

def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    return [izloci_besedo(beseda) for beseda in tvit.split() if beseda[0] == c]

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        s += se_zacne_z(tvit, c)
    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

#Obvezne

def besedilo(tvit):
        return tvit.replace(avtor(tvit) + ": ", "")

def zadnji_tvit(tviti):
    zadnji = {}
    for tvit in tviti:
        zadnji[avtor(tvit)] = besedilo(tvit)
    return zadnji

def prvi_tvit(tviti):
    prvi = {}
    for tvit in tviti:
        if avtor(tvit) not in prvi:
            prvi[avtor(tvit)] = besedilo(tvit)
    return prvi

def prestej_tvite(tviti):
    s = []
    for tvit in tviti:
        s.append(avtor(tvit))
    import collections
    return collections.Counter(s)

def omembe(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d[avtor(tvit)] = se_zacne_z(tvit, "@")
        else:
            d[avtor(tvit)] += se_zacne_z(tvit, "@")
    return d

def neomembe(ime, omembe):
    vsi = list(omembe.keys())
    vsi.remove(ime)
    omenjeni = omembe.get(ime, "")
    neomenjeni = set(vsi) - set(omenjeni)
    return list(neomenjeni)

#Dodatne

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.get(ime2, []) or ime2 in omembe.get(ime1, []):
        return True

def hashtagi(tviti):
    d = {}
    hashtagi = vsi_hashtagi(tviti)
    for hashtag in hashtagi:
        d[hashtag] = []
    for tvit in tviti:
        hashtagi = se_zacne_z(tvit, "#")
        for hashtag in hashtagi:
            d[hashtag].append(avtor(tvit))
            d[hashtag] = sorted(d[hashtag])
    return d

#Testi

