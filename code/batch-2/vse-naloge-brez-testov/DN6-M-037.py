def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    return unikati(avtor(tvit) for tvit in tviti)

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    return [izloci_besedo(beseda) for beseda in tvit.split() if beseda[0] == c]

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
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    return unikati(sorted(avtor(tvit) for tvit in tviti if set(hashtagi) & set(se_zacne_z(tvit, "#"))))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if oseba1 == pisec and oseba2 in omenjeni or oseba2 == pisec and oseba1 in omenjeni:
            return True
    return False

"""----------------------------------------------------------------------------------------------------"""
import collections

def besedilo(tvit):
    return tvit[tvit.index(":") + 2:]

def zadnji_tvit(tviti):
    pokupckano = {}
    for tvit in tviti:
        pokupckano[avtor(tvit)] = besedilo(tvit)
    return pokupckano

def prvi_tvit(tviti):
    zbrano = {}
    for tvit in tviti:
        if avtor(tvit) not in zbrano:
            zbrano[avtor(tvit)] = besedilo(tvit)
    return zbrano


def prestej_tvite(tviti):
    vsi_pisatelji = [avtor(tvit) for tvit in tviti]
    return collections.Counter(vsi_pisatelji)


def omembe(tviti):
    opravljanje = collections.defaultdict(list)
    for tvit in tviti:
            opravljanje[avtor(tvit)]
            if se_zacne_z(tvit, "@") != []:
                opravljanje[avtor(tvit)] += (se_zacne_z(tvit, "@"))
    return opravljanje

        
def neomembe(ime, omembe):
    neomenjeni_ljudje = []
    for name in omembe:
        if name not in omembe[ime] and name != ime:
            neomenjeni_ljudje.append(name)
    return neomenjeni_ljudje

"""-----------------------------------------------------------------"""

def se_poznata(ime1, ime2, omembe):
    if ime2 in omembe.get(ime1, []) or ime1 in omembe.get(ime2, []):
        return True
    return False

def hashtagi(tviti):
    slovar_hastagov = collections.defaultdict(list)
    vsi_hashtagi_zbrani = vsi_hashtagi(tviti)
    for tvit in tviti:
        for hashtag in vsi_hashtagi_zbrani:
            if hashtag in tvit:
                slovar_hastagov[hashtag].append(avtor(tvit))
                slovar_hastagov[hashtag] = sorted(slovar_hastagov[hashtag])
    return slovar_hastagov




