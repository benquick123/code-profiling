def unikati(s):
    u = []
    for e in s:
        if u.count(e) < 1:
            u.append(e)
    return u

def avtor(tvit):
    tvit = tvit.split()
    for e in tvit:
        if e[0]:
            e = e.rstrip(":")
            return e

def vsi_avtorji(tviti):
    b = []
    a = []
    for tvit in tviti:
        o = avtor(tvit)
        a.append(o)
    return unikati(a)

def izloci_besedo(beseda):
    for znak in beseda:
        if znak.isalnum():
            break
        else:
            beseda = beseda.lstrip(znak[0])
    for znak in beseda[::-1]:
        if znak.isalnum():
            break
        else:
            beseda = beseda.rstrip(znak[-1])
    return beseda

def se_zacne_z(tvit, c):
    vrni = []
    tvit = tvit.split()
    for beseda in tvit:
        for znak in beseda:
            if znak[0] == c:
                beseda = izloci_besedo(beseda)
                vrni.append(beseda)
    return vrni


def zberi_se_zacne_z(tviti, c):
    vrni = []
    a = []
    for tvit in tviti:
        tvit = tvit.split()
        for beseda in tvit:
            for znak in beseda:
                if znak[0] == c:
                    beseda = izloci_besedo(beseda)
                    vrni.append(beseda)
                    a = unikati(vrni)
    return a

def vse_afne(tviti):
    c = "@"
    b = zberi_se_zacne_z(tviti,c)
    return b

def vsi_hashtagi(tviti):
    c = "#"
    b = zberi_se_zacne_z(tviti, c)
    return b

def vse_osebe(tviti):
    b = []
    for tvit in tviti:
        tvit = tvit.split(":")
        avtor = tvit[0]
        b.append(avtor)
        tekst = tvit[1]
        tekst = tekst.split()
        for beseda in tekst:
            if beseda[0] == "@":
                beseda = izloci_besedo(beseda)
                b.append(beseda)
                c = unikati(b)
    c.sort()
    return c

























