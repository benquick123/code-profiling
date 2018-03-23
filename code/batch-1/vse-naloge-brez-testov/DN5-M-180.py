def unikati(s):
    nov_s = []
    for i in s:
        if i not in nov_s:
            nov_s.append(i)
    return nov_s

def avtor(tvit):
    list = tvit.split()
    for s in list:
        if ':' == s[len(s) - 1]:
            s = s.replace(':', '')
            return s


def vsi_avtorji(tviti):
    sez_avtorjev = []
    for s in tviti:
        if avtor(s) not in sez_avtorjev:
            sez_avtorjev.append(avtor(s))
    return sez_avtorjev


import re
def izloci_besedo(beseda):
    return re.sub('[^0-9a-zA-Z-]+', '', beseda)

def se_zacne_z(tvit, c):
    c_zacne = []
    sz = tvit.split()
    for i in sz:
        if i.startswith(c):
            c_zacne.append(izloci_besedo(i))
    return c_zacne


def zberi_se_zacne_z(tviti, c):
    se_zacne = []
    for i in tviti:
        se_zacne.extend(se_zacne_z(i, c))
        nov_s = unikati(se_zacne)
    return nov_s


def vse_afne(tviti):
    c = '@'
    return zberi_se_zacne_z(tviti, c)


def vsi_hashtagi(tviti):
    c = '#'
    return zberi_se_zacne_z(tviti, c)


def vse_osebe(tviti):
    abc = []
    abc.extend(vsi_avtorji(tviti))
    abc.extend(vse_afne(tviti))
    i = unikati(abc)
    i.sort()
    return i
















