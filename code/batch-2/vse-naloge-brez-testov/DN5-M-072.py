def unikati(s):
    s2 = []
    for e in s:
        if e not in s2:
            s2.append(e)
    return s2

def avtor(tvit):
    x = tvit.split(":")
    return x [0]

def vsi_avtorji(tviti):
    seznam_a = []
    for tvit in tviti:
        y = avtor(tvit)
        seznam_a.append(y)
    z = unikati(seznam_a)
    return z

def izloci_besedo(beseda):
    while str.isalnum(beseda [0]) == False:
     beseda = beseda[1:]
    while str.isalnum(beseda [-1]) == False:
     beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    s = tvit.split()
    z = []
    for e in s:
        if e [0] == c:
            z.append(e)
    a = []
    for i in z:
        b = izloci_besedo(i)
        a.append(b)
    return a

def zberi_se_zacne_z (tviti,c):
    a =". ".join(tviti)
    b = se_zacne_z(a,c)
    return unikati(b)

def vse_afne(tviti):
    return zberi_se_zacne_z (tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z (tviti, "#")

def vse_osebe(tviti):
    s = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(s))

def custva (tviti, hashtagi):
    b = []
    for e in hashtagi:
        b.append(izloci_besedo(e))
    c = []
    for tvit in tviti:
        a = se_zacne_z(tvit,"#")
        if len (set(b).intersection(a)) > 0:
            c.append(avtor(tvit))
    return sorted(unikati(c))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        b = oseba2 in se_zacne_z(tvit, "@")
        if oseba1 == avtor(tvit) and b:
            return True









        







