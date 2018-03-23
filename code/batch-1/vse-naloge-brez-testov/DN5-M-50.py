def unikati(s):
    u = []
    for i in s:
        if i not in u:
            u.append(i)
    return u


def avtor(tvit):
    t = tvit.split(":")
    for i in t:
        return i


def vsi_avtorji(tviti):
    avtorji = []
    t = ":".join(tviti)
    u = t.split(":")
    i = u[0]
    for i in u[::2]:
        if i not in avtorji:
            avtorji.append(i)
    return avtorji

def izloci_besedo(beseda):
    b = beseda
    while b:
        if b[0].isalnum():
            break
        b = b[1:]
    while True:
            if not b[-1].isalnum():
                b = b[:-1]
            else:
                break
    return b

def se_zacne_z(tvit, c):
    l = []
    tvit_c = tvit.split()
    for i in tvit_c:
        if c == i[0]:
            niz = izloci_besedo(i)
            l.append(niz)
    return l

def zberi_se_zacne_z(tviti, c):
    l = []
    tvit_1 = " ".join(tviti)
    tvit_c = tvit_1.split()
    for i in tvit_c:
        if c in i[0]:
            niz = izloci_besedo(i)
            if niz not in l:
                l.append(niz)
    return l

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    c = "#"
    return zberi_se_zacne_z(tviti, c)

def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti)
    afna = vse_afne(tviti)
    seznam_nov = unikati(avtorji + afna)
    seznam_nov.sort()
    return seznam_nov

