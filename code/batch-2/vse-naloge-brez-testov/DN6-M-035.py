import re
def besedilo(tvit):
    return(tvit.partition(" ")[2])


def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        besedil = tvit.split(":",1)[1]
        slovar.update({avtor:besedil.lstrip()})
    return(slovar)


def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        besedil = tvit.split(":",1)[1]
        if avtor in slovar:
            continue
        else:
            slovar.update({avtor:besedil.lstrip()})
    return(slovar)

def prestej_tvite(tviti):
    slovar = {}
    vrednost=1
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        if avtor in slovar:
            stevec = slovar[avtor]
            stevec = stevec + 1
            slovar.update({avtor:stevec})
        else:
            slovar.update({avtor:vrednost})
    return(slovar)

from collections import defaultdict

def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t
def se_zacne_z(tvit, c):
    return [izloci_besedo(beseda) for beseda in tvit.split() if beseda[0] == c]

def izloci_besedo(beseda):
    for prva in range(len(beseda)):
        if beseda[prva].isalnum():
            break
    for zadnja in range(len(beseda), 0, -1):
        if beseda[zadnja-1].isalnum():
            break
    return beseda[prva:zadnja]

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def omembe(tviti):
    slovar = {}
    osebe = []
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        if avtor not in slovar:
            slovar[avtor] = []
    seznam_besed = vse_afne(tviti)
    for tvit_besedilo in tviti:
        avtor = tvit_besedilo.split(":")[0]
        besedil = tvit_besedilo.split(":", 1)[1]
        for avtor_dict in seznam_besed:
            if avtor_dict in besedil:
                slovar[avtor].append(avtor_dict)
    return (slovar)


def neomembe(ime,omembe):
    seznam_oseb = []
    vracilo = []
    for tvit in omembe:
        seznam_oseb.append(tvit)
    for oseba in seznam_oseb:
        if oseba != ime:
            if oseba not in omembe[ime]:
                vracilo.append(oseba)
    return(vracilo)

