# -*- coding: utf-8 -*-

def unikati(s):
    urejen = []
    for i in s:
        if i not in urejen:
            urejen.append(i)
    return urejen

def avtor(tvit):
    return tvit.split(':')[0]

def vsi_avtorji(tviti):
    seznam = []
    for t in tviti:
        seznam.append(avtor(t))
    return unikati(seznam)

import re
def izloci_besedo(beseda):
    return re.sub('[^A-Za-z0-9-]+', '', beseda).lstrip()

def se_zacne_z(tvit, c):
    seznam = []
    for b in tvit.split():
        if b.startswith(c):
            seznam.append(izloci_besedo(b))
    return seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for t in tviti:
        for tt in t.split():
            if tt.startswith(c):
                seznam.append(izloci_besedo(tt))
    return unikati(seznam)

def vse_afne(tviti):
    c = '@'
    return zberi_se_zacne_z(tviti, c)

def vsi_hashtagi(tviti):
    c = '#'
    return zberi_se_zacne_z(tviti, c)

def vse_osebe(tviti):
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    '''
    osebe = []
    for t in tviti:
        for h in hashtagi:
            htg = t.split('#')[1]
            if h == htg:
                osebe.append(avtor(t))
    osebe.sort()
    return unikati(osebe)
    '''
    return unikati(sorted(avtor(tvit) for tvit in tviti if set(hashtagi) & set(se_zacne_z(tvit, "#"))))

def se_poznata(tviti, oseba1, oseba2):
    for t in tviti:
        a = avtor(t)
        o = se_zacne_z(t, "@")
        if oseba1 == a and oseba2 in o or \
                oseba2 == a and oseba1 in o:
            return True
    return False

def besedilo(tvit):
    bes = tvit[tvit.find(":")+2:]
    return bes

def zadnji_tvit(tviti):
    slovar = {}
    for t in tviti:
        slovar[avtor(t)] = besedilo(t)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for t in tviti:
        if avtor(t) not in slovar:
            slovar[avtor(t)] = besedilo(t)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    avtorji = []
    for t in tviti:
        avtorji.append(avtor(t))
    for a in avtorji:
        if a not in slovar:
            slovar[a] = 0
        slovar[a] += 1
    return slovar

def omembe(tviti):
    slovar = {}
    for t in tviti:
        auth = t.split(": ")[0]
        omemba = re.findall("@([aA-zZ]*)", t)
        slovar[auth] = slovar.get(auth, []) + omemba
    return slovar

def neomembe(ime, omembe):
    self_omembe = omembe.get(ime, []) + [ime]
    return list(set(omembe.keys()) - set(self_omembe))


