import collections

def unikati(s):
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u

def avtor(tvit):
   colon = tvit.index(":")
   name = tvit[0 : colon]
   return name

def vsi_avtorji(tviti):
    vsi = []
    for x in tviti:
        y = avtor(x)
        if y not in vsi:
            vsi.append(y)
    return vsi

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    elementi = tvit.split()
    okrnjeno = []
    for x in elementi:
        if x[0] == c:
            okrnjeno.append(izloci_besedo(x))
    return okrnjeno

def zberi_se_zacne_z(tviti, c):
    trending = []
    tviti = " ".join(tviti)
    trending += se_zacne_z(tviti, c)
    return unikati(trending)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    nabor = []
    nabor += vsi_avtorji(tviti)
    nabor += vse_afne(tviti)
    nabor = unikati(nabor)
    return sorted(nabor)

def custva(tviti, hashtagi):
    hasharji = []
    for x in tviti:
        for kljucnik in hashtagi:
            if kljucnik in x:
                hasharji.append(avtor(x))
    return sorted(unikati(hasharji))


def besedilo(tvit):
    colon = tvit.index(":")
    tekst = tvit[colon + 2 : ]
    return tekst

def zadnji_tvit(tviti):
    zadnji = {}
    for x in tviti:
        zadnji[avtor(x)] = besedilo(x)
    return zadnji

def prvi_tvit(tviti):
    prvi = {}
    for x in tviti:
        if avtor(x) not in prvi:
            prvi[avtor(x)] = besedilo(x)
    return prvi

def prestej_tvite(tviti):
    civki = []
    civkasi = {}
    for x in tviti:
        civki.append(avtor(x))
    civkasi = collections.Counter(civki)
    return civkasi

def omembe(tviti):
    omenjanja = collections.defaultdict(list)
    for tvit in tviti:
        civkar = avtor(tvit)
        omenjanja[civkar]
        civk = besedilo(tvit)
        afne = se_zacne_z(civk, "@")
        for x in afne:
            omenjanja[civkar].append(x)
    return omenjanja

def neomembe(ime, omembe):
    prezrti = []
    for civkar, afne in omembe.items():
        if civkar != ime and civkar not in omembe[ime]:
            prezrti.append(civkar)
    return prezrti



def se_poznata(ime1, ime2, omembe):
    poznanstvo = False
    for civkar, afne in omembe.items():
        if ime1 == civkar and ime2 in afne:
            poznanstvo = True
        if ime2 == civkar and ime1 in afne:
            poznanstvo = True
    return poznanstvo

def hashtagi(tviti):
    lojtrisce = collections.defaultdict(list)
    for tvit in tviti:
        civkar, kljucniki = avtor(tvit), se_zacne_z(tvit, "#")
        for x in kljucniki:
            lojtrisce[x].append(civkar)
            lojtrisce[x] = sorted(lojtrisce[x])
    return lojtrisce
























