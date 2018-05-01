def unikati(s):
    nov = []
    for e in s:
        if e not in nov:
            nov.append(e)
    return nov

def avtor(tvit):
    s = tvit.split(':')
    return s[0]

def vsi_avtorji(tviti):
    avtorji = []
    for vrstica in tviti:
        avtorji.append(avtor(vrstica))
    return unikati(avtorji)

def nazaj(beseda):
    return beseda[::-1]

def izloci_besedo(beseda):
    while True:
        for znak in beseda:
            while znak.isalnum() == False:
                beseda = beseda[1:]
                break
            if znak.isalnum() == True:
                beseda = beseda[:]
                break
        for znak in nazaj(beseda):
            while znak.isalnum() == False:
                beseda = beseda[:-1]
                break
            if znak.isalnum() == True:
                beseda = beseda[:]
                break
        return beseda

def se_zacne_z(tvit, c):
    s = []
    for beseda in tvit.split():
        if beseda[0] == c:
            f = izloci_besedo(beseda)
            s.append(f)
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    sez = []
    for tvit in tviti:
        s.append(se_zacne_z(tvit, c))
    for podsez in s:
        for e in podsez:
            sez.append(e)
    return unikati(sez)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    s = vsi_avtorji(tviti) + vse_afne(tviti)
    return unikati(sorted(s))

def custva(tviti,hashtagi):
    s = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                s.append(avtor(tvit))
    return unikati(sorted(s))


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        avt = avtor(tvit)
        afne = se_zacne_z(tvit, '@')
        if avt == oseba1 or avt == oseba2:
            for afna in afne:
                if afna == oseba1 or afna == oseba2:
                    return True
    return False


