def unikati(s):
    r = []
    for i in s:
        if i not in r:
            r.append(i)
    return r


def avtor(tviti):
    tviti = tviti.split()
    return tviti[0][:-1]


def vsi_avtorji(tviti):
    s = []
    for i in tviti:
        s.append(avtor(i))
    return unikati(s)


def izloci_besedo(bes):
    f = True
    while f:
        if (not bes[0].isalnum()):
            bes = bes[1:]
        else:
            f = False
    b = True
    while b:
        if (not bes[-1].isalnum()):
            bes = bes[:-1]
        else:
            b = False
    return bes

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    re = []
    for i in tvit:
        if i[0] == c:
            re.append(izloci_besedo(i))
    return re

def zberi_se_zacne_z(tviti, c):
    s = []
    for i in tviti:
        s+=se_zacne_z(i,c)
    return unikati(s)
