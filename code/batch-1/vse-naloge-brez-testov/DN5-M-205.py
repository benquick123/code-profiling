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
    s1 = vse_afne(tviti)
    s2 = vsi_avtorji(tviti)
    s = s1 + s2
    return list(set(s))

