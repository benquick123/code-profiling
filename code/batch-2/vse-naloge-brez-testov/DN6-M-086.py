#Funkcije prejsnje naloge:

def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    ime = tvit.split(":")
    return ime[0]

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        a = avtor(i)
        if a not in seznam:
            seznam.append(a)
    return seznam

def izloci_besedo(beseda):
    for i in range(len(beseda) -1):
        if beseda[i].isalnum() == True:
            zacetek = i
            break
    for j in range(len(beseda)-1, 0, -1):
        if beseda[j].isalnum() == True:
            konec = j
            break
    ime = beseda[zacetek:konec +1]
    return ime

def se_zacne_z(tvit, c):
    seznam = []
    a = tvit.split()
    for i in a:
        if i[0] == c:
            b = izloci_besedo(i)
            seznam.append(b)
    return seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for i in tviti:
        a = se_zacne_z(i, c)
        for beseda in a:
            if beseda != [] and beseda not in seznam:
                seznam.append(beseda)
    return seznam

def vse_afne(tviti):
    afna = zberi_se_zacne_z(tviti, "@")
    return afna

def vsi_hashtagi(tviti):
    hashtag = zberi_se_zacne_z(tviti, "#")
    return hashtag

def vse_osebe(tviti):
    seznam = vsi_avtorji(tviti) + vse_afne(tviti)
    urejen = sorted(unikati(seznam))
    return urejen


#Obvezna naloga:

def besedilo(tvit):
    besedilo1 = tvit.split(": ")
    return ": ".join(besedilo1[1:])


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

import collections
def prestej_tvite(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    seznam2 = collections.Counter(seznam)
    return seznam2

def omembe(tviti):
    seznam = collections.defaultdict(list)
    for tvit in tviti:
        seznam[avtor(tvit)] += se_zacne_z(tvit, "@")
    return seznam

def neomembe(ime, omembe):
    seznam = []
    for avtor in omembe:
        if avtor == ime:
            for oseba in omembe:
                if oseba not in avtor and oseba != ime and oseba not in omembe[avtor]:
                    seznam.append(oseba)
            break
    return seznam

#Dodatna naloga: ///

