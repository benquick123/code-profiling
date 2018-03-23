
def unikati(s):
    s1 = []
    for e in s:
        if e not in s1:
            s1.append(e)
    return s1

def avtor(tvit):
    s =  tvit.split()
    return s[0][:-1]

def vsi_avtorji(tviti):
    s = []
    for tvit in tviti:
        s.append(avtor(tvit))
    return unikati(s)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda


def se_zacne_z(tvit, c):
    s = []
    for beseda in tvit.split():
        if beseda[0] == c:
            s.append(izloci_besedo(beseda))
    return s


def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        s += se_zacne_z(tvit, c)
    return unikati(s)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    s = vse_afne(tviti)
    for tvit in tviti:
        s.append(avtor(tvit))
    s = unikati(s)
    s.sort()
    return s

###

def besedilo(tvit):
    value = tvit.split()[1:]
    return " ".join(value)

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


def prestej_tvite(tviti):
    stevec = []
    slovar = {}
    for tvit in tviti:
        stevec.append(avtor(tvit))
    for pisec in stevec:
        if pisec not in slovar:
            slovar[pisec] = 0
        slovar[pisec] += 1
    return slovar


def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = se_zacne_z(tvit, "@")
        slovar[avtor(tvit)] += se_zacne_z(tvit, "@")
        slovar[avtor(tvit)] = unikati(slovar[avtor(tvit)])
    return slovar


def neomembe(ime, omembe):
    seznam = []
    for avtorji in omembe:
       seznam.append(avtorji)
    if ime in omembe:
        seznam.remove(ime)
    koncni = list(set(seznam) - set(omembe[ime]))
    return koncni




