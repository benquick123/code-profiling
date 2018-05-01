
def unikati(s):
    t=[]
    for e in s:
        if e in t:
            continue
        t.append(e)
    return t


def avtor(tvit):
    t1=tvit.split()
    return t1[0][:-1]


def vsi_avtorji(tviti):
    z=[]
    for e in tviti:
        a = avtor(e)
        z.append(a)
    return unikati(z)


def izloci_besedo(beseda):
    t=""
    for e in beseda:
        if e.isalnum() or e == "-":
            t+=e
    return t


def se_zacne_z(tvit,c):
    z=[]
    t=tvit.split()
    for e in t:
        if e[0]==c:
            z.append(izloci_besedo(e[1:]))
    return z


def zberi_se_zacne_z(tviti,c):
    u=[]
    for tvit in tviti:
        z=se_zacne_z(tvit,c)
        for e in z:
            u.append(e)
    return unikati(u)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")


def vse_osebe(tviti):
    u=vsi_avtorji(tviti)
    t=vse_afne(tviti)
    z=u+t
    o=unikati(z)
    r=o.sort()
    return o


def custva(tviti, hashtagi):
    t=[]
    for tvit in tviti:
        for e in hashtagi:
            if e in tvit:
                z=avtor(tvit)
                t.append(z)
    t=unikati(t)
    t.sort()
    return t


def se_poznata(tviti,oseba1,oseba2):
    if oseba1 and oseba2 not in vsi_avtorji(tviti):
        return False
    for tvit in tviti:
        if oseba1 in tvit:
            if oseba2 in tvit:
                return True
    else:
        return False





