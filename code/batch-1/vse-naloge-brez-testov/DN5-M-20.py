#### OBVEZNI DEL ####

def unikati(s):
    seznam = []

    for x in s:
        if x not in seznam:
            seznam += [x]

    return seznam

import re
def avtor(tvit):

    beseda = []
    ime = []

    beseda = tvit.split()

    ime = re.sub(r'\W+', '', beseda[0])

    return ime

def vsi_avtorji(tviti):

    avtorji = []

    for x in tviti:
        avtorji += [avtor(x)]

    avtorji = unikati(avtorji)

    return avtorji

from string import punctuation
def izloci_besedo(beseda):

    beseda = beseda.lstrip(punctuation)
    beseda = beseda.rstrip(punctuation)

    return beseda

def se_zacne_z(tvit, c):
    besede = []
    kljucne_besede = []

    besede = tvit.split()

    for x in besede:
        if c in x:
            kljucne_besede += [izloci_besedo(x)]

    return kljucne_besede

def zberi_se_zacne_z(tviti, c):

    kljucne_besede = []

    for tvit in tviti:
        kljucne_besede += se_zacne_z(tvit, c)

    kljucne_besede = unikati(kljucne_besede)

    return kljucne_besede

def vse_afne(tviti):

    kljucne_besede = []
    c = '@'

    kljucne_besede = zberi_se_zacne_z(tviti, c)

    return kljucne_besede

def vsi_hashtagi(tviti):
    kljucne_besede = []
    c = '#'

    kljucne_besede = zberi_se_zacne_z(tviti, c)

    return kljucne_besede

def vse_osebe(tviti):

    osebe = []

    osebe = vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort(key=str.lower)

    return osebe

#### DODATNI DEL ####

def custva(tviti, hashtagi):

    besede = []
    puste_besede = []
    avtorji = []

    for tvit in tviti:
        besede = tvit.split()
        for x in besede:
            puste_besede = [izloci_besedo(x)]
            for y in hashtagi:
                if y in puste_besede:
                    avtorji += [avtor(tvit)]

    avtorji = unikati(avtorji)
    avtorji.sort(key=str.lower)

    return avtorji

def se_poznata(tviti, oseba1, oseba2):

    besede = []

    for tvit in tviti:
        besede = tvit.split()

        if oseba1 == avtor(tvit):
            for x in besede:
                if izloci_besedo(x) == oseba2 and '@' in x:
                    return True
            else:
                return False
















#####################################
