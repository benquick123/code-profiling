def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam


def avtor(tvit):
    beseda = tvit.split()
    b = beseda[0]
    b = b.replace(":", "")
    return b


def vsi_avtorji(tviti):
    seznam = []
    nseznam = []
    for x in tviti:
        b = x.split(":")
        seznam.append(b)
    for y in seznam:
        c = y[0]
        c = c.replace(":", "")
        nseznam.append(c)
    return unikati(nseznam)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda


def se_zacne_z(tvit, c):
    seznam = []
    for znak in tvit.split():
        if c in znak:
            znak = izloci_besedo(znak)
            seznam.append(znak)
    return seznam


def zberi_se_zacne_z(tviti, c):
    seznam = []
    nseznam = []
    for x in tviti:
        beseda = x.split()
        seznam.extend(beseda)
    for a in seznam:
        nseznam.extend(se_zacne_z(a, c))
    return unikati(nseznam)


def vse_afne(tviti):
    seznam = []
    nseznam = []
    for x in tviti:
        beseda = x.split()
        seznam.extend(beseda)
    for a in seznam:
        nseznam.extend(se_zacne_z(a, "@"))
    return unikati(nseznam)

def vsi_hashtagi(tviti):
    seznam = []
    nseznam = []
    for x in tviti:
        beseda = x.split()
        seznam.extend(beseda)
    for a in seznam:
        nseznam.extend(se_zacne_z(a, "#"))
    return unikati(nseznam)

def vse_osebe(tviti):
    seznam = []
    a = vsi_avtorji(tviti)
    b = vse_afne(tviti)
    seznam = a + b
    seznam = sorted(seznam, key=str.lower)
    return unikati(seznam)

