def unikati(s):
    a = []
    for x in s:
        if x not in a:
            a.append(x)
    return a

def avtor(s):
    a = s.split()
    for b in a:
        if b.count(":") > 0:
            return b[:-1]

def vsi_avtorji(s):
    x = []
    for a in s:
        b = avtor(a)
        if b not in x:
            x.append(b)
    return x

def izloci_besedo(beseda):
    beseda = list(beseda)
    while not beseda[0].isalnum():
        beseda.pop(0)
    while not beseda[-1].isalnum():
        beseda.pop(-1)
    return "".join(beseda)

def se_zacne_z(tvit,c):
    x = []
    tvit = tvit.split()
    for z in tvit:
        if c in z:
            x.append(izloci_besedo(z))
    return x

def zberi_se_zacne_z(tviti,c):
    z = []
    for x in tviti:
        y = se_zacne_z(x,c)
        z.extend(y)
    q = unikati(z)
    return q

def vse_afne(tviti):
    z = []
    for x in tviti:
        y = se_zacne_z(x,"@")
        z.extend(y)
    q = unikati(z)
    return q

def vsi_hashtagi(tviti):
    z = []
    for x in tviti:
        y = se_zacne_z(x,"#")
        z.extend(y)
    q = unikati(z)
    return q

def vse_osebe(tviti):
    x = []
    a = vse_afne(tviti)
    b = vsi_avtorji(tviti)
    x.extend(a)
    x.extend(b)
    x = unikati(x)
    while None in x:
        x.remove(none)
    x.sort()
    return x






