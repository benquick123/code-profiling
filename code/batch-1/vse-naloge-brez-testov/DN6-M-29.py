import collections


def unikati(s):
    rez = []
    for i in s:
        if i in rez:
            pass
        else:
            rez.append(i)
    return rez

def avtor(tvit):
    novi = tvit.split(":")
    return novi[0]

def vsi_avtorji(tviti):
    p = []
    for tvit in tviti:
        a = avtor(tvit)
        p.append(a)
    p = unikati(p)
    return p

def izloci_besedo(beseda):
    s = ""
    for c in beseda:
        if c.isalnum() or c == "-":
            s += c
    return s

def se_zacne_z(tvit, c):
    rez = []
    for beseda in tvit.split(" "):
        if beseda.startswith(c):
            rez.append(izloci_besedo(beseda))
    return rez

def zberi_se_zacne_z(tviti, c):
    rez = []
    for tvit in tviti:
        for beseda in tvit.split(" "):
            if beseda.startswith(c):
                rez.append(izloci_besedo(beseda))
                rez = unikati(rez)
    return rez

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    rez = []
    a = vse_afne(tviti)
    b = vsi_avtorji(tviti)
    for c in a:
        rez.append(c)
    for c in b:
        rez.append(c)
    rez = unikati(rez)
    return sorted(rez)

def besedilo(tvit):
    a = avtor(tvit)
    od = a + ": "
    tv = tvit.lstrip(od)
    return tv

def zadnji_tvit(tviti):
    slovar = collections.defaultdict(int)
    a = vsi_avtorji(tviti)
    for ime in a:
        for tvit in tviti:
            if avtor(tvit) == ime:
                slovar[ime] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = collections.defaultdict(int)
    a = vsi_avtorji(tviti)
    for ime in a:
        for tvit in tviti:
            if avtor(tvit) == ime:
                slovar[ime] = besedilo(tvit)
                break
    return slovar

def prestej_tvite(tviti):
    slovar = collections.defaultdict(int)
    a = vsi_avtorji(tviti)
    b = 1
    for ime in a:
        for tvit in tviti:
            if avtor(tvit) == ime:
                slovar[ime] = b
                b += 1
        b = 1
    return slovar

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = []
        omenjeni = se_zacne_z(besedilo(tvit), "@")
        if avtor(tvit) not in omenjeni:
            slovar[avtor(tvit)] += omenjeni
    return slovar

def neomembe(ime, omembe):
    rez = []
    for imena, drugo in omembe.items():
        if imena == ime:
            for im in omembe:
                if im not in drugo and im != ime:
                    rez.append(im)
    return rez






