def unikati(s):
    sez = []
    for e in s:
        if e not in sez:
            sez.append(e)
    return sez


def avtor(tvit):
    sp = tvit.split(":")
    for m in sp:
        return m

def vsi_avtorji(tviti):
    sez = []
    for ime in tviti:
        sez.append(ime.split(":")[0])
    return unikati(sez)


def izloci_besedo(beseda):
    for crka in beseda:
        if crka.isalpha() != True:
            beseda = beseda[1:]
        elif crka[0].isalpha() == True:
            break
    for crka in beseda[::-1]:
        if crka.isalpha() != True:
            beseda = beseda[:-1]
        elif crka[0].isalpha() == True:
            break
    return beseda

def se_zacne_z(tvit, c):
    s =[]
    sp = tvit.split(" ")
    for znak in sp:
        if znak[0] == c:
            znak = znak[1:]
            if znak.isalnum() != True:
                znak = znak[:-1]
            s.append(znak)
    return s


def zberi_se_zacne_z(tviti, c):
    total =[]
    m = []
    for e in tviti:
        m.append(se_zacne_z(e, c))
    for i in m:
        total += i
    return unikati(total)


def vse_afne(tviti):
    m =[]
    sez = []
    for i in tviti:
        sez.append(se_zacne_z(i, "@"))
    for e in sez:
        m += e
    return unikati(m)

def vsi_hashtagi(tviti):
    m =[]
    sez = []
    for i in tviti:
        sez.append(se_zacne_z(i, "#"))
    for e in sez:
        m += e
    return unikati(m)

def vse_osebe(tviti):
    total = []
    s = []
    h = []
    h.append(vsi_avtorji(tviti))
    s.append(vse_afne(tviti))
    for i, m in zip(h,s):
        total = m + i
    return sorted(unikati(total))





