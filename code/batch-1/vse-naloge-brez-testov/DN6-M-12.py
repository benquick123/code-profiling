def unikati(s):
    s1 = []
    for e in s:
        if e in s1:
            continue
        else:
            s1.append(e)
    return s1


def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    vsi = []
    for tvit in tviti:
        vsi.append(avtor(tvit))
    return unikati(vsi)


def izloci_besedo(beseda):
    beseda = list(beseda)
    while not beseda[0].isalnum():
        beseda.remove(beseda[0])
    while not beseda[-1].isalnum():
        beseda.remove(beseda[-1])
    return "".join(beseda)


def se_zacne_z(tvit, c):
    nov = []
    for beseda in tvit.split(" "):
        if beseda[0] == c:
            nov.append(izloci_besedo(beseda))
        else:
            continue
    return nov


def zberi_se_zacne_z(tviti, c):
    nov = []
    for tvit in tviti:
        nov += se_zacne_z(tvit, c)
    return unikati(nov)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))


def custva(tviti, hashtagi):
    nov = []
    for hash in hashtagi:
        for tvit in tviti:
            if hash in vsi_hashtagi(tvit.split(" ")):
                nov.append(avtor(tvit))
    return sorted(unikati(nov))


def se_poznata1(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            if oseba2 in se_zacne_z(tvit, "@"):
                return True
        if avtor(tvit) == oseba2:
            if oseba1 in se_zacne_z(tvit, "@"):
                return True
    return False


# ====================== (Novi tviti) ===========================================================

def besedilo(tvit):
    return tvit.split(avtor(tvit) + ": ")[1]


def zadnji_tvit(tviti):
    slovar_t = {}
    for tvit in tviti:
        slovar_t[avtor(tvit)] = besedilo(tvit)
    return  slovar_t

def prvi_tvit(tviti):
    slovar_t = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar_t:
            slovar_t[avtor(tvit)] = besedilo(tvit)
    return slovar_t

import collections

def prestej_tvite(tviti):
    pogostost = collections.defaultdict(int)
    for tvit in tviti:
        pogostost[avtor(tvit)] += 1
    return pogostost

def omembe(tviti):
    omembe = {}
    for tvit in tviti:
        if avtor(tvit) not in omembe:
            omembe[avtor(tvit)] = se_zacne_z(tvit, "@")
        omembe[avtor(tvit)] = unikati(omembe[avtor(tvit)] + se_zacne_z(tvit, "@"))
    return omembe

def neomembe(ime, omembe):
    ne = []
    for neomenjen in omembe:
        if neomenjen not in omembe[ime] and neomenjen is not ime:
            ne.append(neomenjen)
    return ne

def se_poznata(ime1, ime2, omembe):
    if ime2 in (omembe or omembe[ime1]) and ime1 in (omembe or omembe[ime2]):
        if ime1 in omembe[ime2] or ime2 in omembe[ime1]:
            return True
    else:
        return False

def hashtagi(tviti):
    s = {}
    for tvit in tviti:
        for hash in se_zacne_z(tvit, "#"):
            if hash not in s:
                s[hash] = [avtor(tvit)]
            else:
                s[hash] = sorted(s[hash] + [avtor(tvit)])
    return s








# TESTI!


