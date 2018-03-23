def unikati(s):
    unikatni = []
    for x in s:
        if x not in unikatni:
            unikatni.append(x)
    return unikatni

def avtor(tvit):
    a = tvit.split()
    ime = a.pop(0)
    b = list(ime)
    c = b.pop()
    e = "".join(b)
    return e

def vsi_avtorji(tviti):
    seznam = []
    for x in tviti:
        a = avtor(x)
        seznam.append(a)
    a = unikati(seznam)
    return a

def izloci_besedo(beseda):
    a = list(beseda)
    b = []
    for x in a:
        if x.isalnum() == True or x == ("-"):
            b.append(x)
    c = "".join(b)
    return c

def se_zacne_z(tvit, c):
    seznam = []
    seznam2 = []
    seznam3 = []
    a = tvit.split()
    for x in a:
        b = list(x)
        seznam.append(b)
    for y in seznam:
        for z in y:
            if c == z:
                seznam2.append(y)
    for g in seznam2:
        f =  "".join(g)
        h = izloci_besedo(f)
        seznam3.append(h)
    return seznam3

def zberi_se_zacne_z(tviti, c):
    prazen_seznam = []
    prazno = []
    for x in tviti:
        e = se_zacne_z(x,c)
        if e not in prazen_seznam and e != prazno:
            prazen_seznam.append(e)
    for z in prazen_seznam:
        for y in z:
            if y not in prazno:
                prazno.append(y)
    return prazno

def vse_afne(tviti):
    z = zberi_se_zacne_z(tviti,"@")
    return z

def vsi_hashtagi(tviti):
    e = zberi_se_zacne_z(tviti,"#")
    return e

def vse_osebe(tviti):
    osebe = []
    a1 = vse_afne(tviti)
    b1 = vsi_avtorji(tviti)
    for a in a1:
        if a not in osebe:
            osebe.append(a)
    for b in b1:
        if b not in osebe:
            osebe.append(b)
    e = sorted(osebe)
    return e


