import re

def unikati(s):
    if s == []:
        return []
    seznam = [s[0]]
    for e in s:
        if e in seznam:
            continue
        else:
            seznam.append(e)
    return seznam


def avtor(tvit):
    a = tvit.split(":")
    return a[0]


def vsi_avtorji(tviti):
    avto = ""
    avtorji = []
    unikatno = []
    for tvit in tviti:
        avto = avtor(tvit)
        avtorji.append(avto)
    unikatno = unikati(avtorji)
    return unikatno


def izloci_besedo(beseda):
    beseda = re.sub('[^0-9a-zA-Z--]+','', beseda)
    return beseda


def se_zacne_z(tvit, c):
    seznam = tvit.split(" ")
    nov_seznam = []
    for beseda in seznam:
        if beseda[0] == c:
            nov_seznam.append(izloci_besedo(beseda))
        else:
            continue
    return nov_seznam


def zberi_se_zacne_z(tviti, c):
    seznam = []
    for twit in tviti:
        twit = twit.split()
        for beseda in twit:
            if beseda[0] == c:
                beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)
                if beseda not in seznam:
                    seznam.append(beseda)
    return seznam


def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, '@')
    return afne


def vsi_hashtagi(tviti):
    hastag = zberi_se_zacne_z(tviti, '#')
    return hastag


def vse_osebe(tviti):
    seznam_vseh = vse_afne(tviti)
    avtorji = vsi_avtorji(tviti)
    for ljudi in seznam_vseh:
        if ljudi not in avtorji:
            avtorji.append(ljudi)
    avtorji.sort()
    return avtorji


