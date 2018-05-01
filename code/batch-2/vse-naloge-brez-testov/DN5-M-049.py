def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    author, x = tvit.split(":", 1)
    return author

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        x = avtor(i)
        if x not in seznam:
            seznam.append(x)
    return seznam

def izloci_besedo(beseda):
    if not beseda.isalnum():
        for znak in beseda:
            if znak.isalnum():
                break
            else:
                beseda = beseda.replace(znak, '')

        for znak2 in reversed(beseda):
            if znak2.isalnum():
                break
            else:
                beseda = beseda.replace(znak2, '')
    return beseda

def se_zacne_z(tvit, c):
    s = []
    tvit = izloci_besedo(tvit)

    spliti = tvit.split(" ")
    for i in spliti:
        if i.startswith(c):
            s.append(i.replace(c, '').replace(",", '').replace("?", ''))

    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for i in tviti:
        i = se_zacne_z(i, c)
        if i not in s:
            s.append(i)
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        tvit = se_zacne_z(tvit, c)          #dobim nazaj seznam besed iz funkcije se_zacne_z(tvit, c)
        for beseda in tvit:                 #grem cez ta seznam da dobim ven vse besede
            if beseda not in s:             #ce posamezna beseda ni v MAIN seznamu, jo dodam
                s.append(beseda)
    return s

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    s = []
    for i in vsi_avtorji(tviti):
        s.append(i)
    for i in vse_afne(tviti):
        if i not in s:
            s.append(i)

    return sorted(s)

