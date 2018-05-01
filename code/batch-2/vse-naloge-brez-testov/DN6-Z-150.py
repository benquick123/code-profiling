def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == c:
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    osebe.sort()
    return osebe

def neprazen_presek(s, t):
    for e in s:
        if e in t:
            return True
    return False

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        if neprazen_presek(se_zacne_z(tvit, "#"), hashtagi):
            avtorji.append(avtor(tvit))
    avtorji.sort()
    return unikati(avtorji)

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if oseba1 == pisec and oseba2 in omenjeni or \
                oseba2 == pisec and oseba1 in omenjeni:
            return True
    return False

def besedilo(tvit):
    dvopicje = 0
    for crka in tvit:
        dvopicje += 1
        if crka == ":":
            break
    stuff = tvit[dvopicje+1:]
    return stuff


def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)]=besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)]=besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = 0
        slovar[avtor(tvit)] += 1
    return slovar


def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = []
        slovar[avtor(tvit)] += se_zacne_z(tvit,"@")
    return slovar


def neomembe (ime, omembe):
    seznam =[]
    for kljuc in omembe:
        enakost = False
        for ime2 in omembe[ime]:
            if kljuc == ime2:
                enakost = True
        if ime == kljuc:
            enakost = True
        if not enakost:
            seznam.append(kljuc)

    return seznam


