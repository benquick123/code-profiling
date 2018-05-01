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

####################Domaca naloga###############
import ast

def besedilo(tvit):
    t = tvit.split(":",1)[1]
    return t.lstrip()


def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s

def prvi_tvit(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s[avtor(tvit)] = besedilo(tvit)
    return s

import collections

def prestej_tvite(tviti):
    s = collections.defaultdict(int)
    for tvit in tviti:
        s[avtor(tvit)] += 1
    return s

def omembe(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) in s:
            s[avtor(tvit)] += unikati(se_zacne_z(tvit, "@"))
        elif avtor(tvit) not in s:
            s[avtor(tvit)] = unikati(se_zacne_z(tvit, "@"))
    return s

def neomembe(ime,omembe):
    s = []
    t = []
    for avtor, omenjeni in omembe.items():
        if avtor == ime:
            t += omenjeni
    for avtor, omenjeni in omembe.items():
        if avtor not in t:
            if avtor != ime:
                s.append(avtor)
    return s

def se_poznata(ime1, ime2, omembe):
    for ime,omenjeni in omembe.items():
        if ime1==ime and ime2 in omenjeni or ime2==ime and ime1 in omenjeni:
            return True
    return False

def hashtagi(tviti):
    s = {}
    for hashtag in vsi_hashtagi(tviti):
        s[hashtag]= []
    for tvit in tviti:
        for t in tvit.split():
            if izloci_besedo(t) in s:
                s[izloci_besedo(t)].append(avtor(tvit))
                s[izloci_besedo(t)].sort()
    return s







