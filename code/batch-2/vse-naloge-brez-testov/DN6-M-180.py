
def unikati(s):
    nov_sez = []
    for stevilo in s:
        if stevilo not in nov_sez:
            nov_sez.append(stevilo)
    return nov_sez

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
    znak = []
    for a in tvit.split():
        if a.startswith(c):
            znak.append(izloci_besedo(a))
    return znak

def zberi_se_zacne_z(tvit, c):
    afne = []
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

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        if neprazen_presek(se_zacne_z(tvit, "#"), hashtagi):
            avtorji.append(avtor(tvit))
    avtorji.sort()
    return unikati(avtorji)

def neprazen_presek(s, t):
    for e in s:
        if e in t:
            return True
    return False

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if oseba1 == pisec and oseba2 in omenjeni or \
                oseba2 == pisec and oseba1 in omenjeni:
            return True
    return False






from collections import *

def besedilo(tvit):
    poved = tvit[tvit.index(":")+1:]
    return poved.strip()

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    stevec = []
    for tvit in tviti:
        stevec.append(avtor(tvit))
    return Counter(stevec)

def omembe(tviti):
    slovar = defaultdict(list)
    for tvit in tviti:
        slovar[avtor(tvit)] += se_zacne_z(tvit,"@")
    return slovar

def neomembe(ime, omembe):
    a = []
    for kljuci in omembe:
        a.append(kljuci)
    for izlocenec in omembe.get(ime,):
        if izlocenec in a:
            a.remove(izlocenec)
    a.remove(ime)
    return a

def se_poznata(ime1, ime2, omembe):
    for oseba in omembe:
        if ime1 == oseba and ime2 in omembe[ime1] or \
                ime2 == oseba and ime1 in omembe[ime2]:
            return True
    return False

def hashtagi(tviti):
    slovar = defaultdict(list)
    for tvit in tviti:
        kljuc = izloci_besedo(vsi_hashtagi(tvit))
        slovar[kljuc[0]] = []
    for hashi in slovar:
        slovar[hashi] += custva(tviti, hashi)
    return slovar


