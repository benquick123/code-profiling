#Unikati v seznamu:
def unikati(s):
    sez = []
    for i in s:
        if i not in sez:
            sez.append(i)
    return (sez)


#Avtor tvita:
def avtor (tvit):
    deli = tvit.split(":")
    return (deli[0])

#Vsi avotrji tvitov:
def vsi_avtorji(tvit):
    sez = []
    for i in tvit:
        deli = i.split(":")
        d = deli[0]
        if d not in sez:
            sez.append(d)
    return (sez)


#Izloči vse na začetku in kocu razen črk:
def izloci_besedo(beseda):
    for start, s in enumerate(beseda):
        if s.isalnum():
            break
    for end, s in enumerate(beseda[::-1]):
        if s.isalnum():
            break
    return (beseda[start:len(beseda) - end])


#Beseda se začne z:
def se_zacne_z(tvit, c):
    sez = []
    w = tvit.split()
    for i in w:
        if i[0] in c:
            n = izloci_besedo(i)
            sez.append(n)
    return (sez)


#Beseda se začne z:
def zberi_se_zacne_z(tviti, c):
    sez = []
    for i in tviti:
        w = i.split()
        for i in w:
            if i[0] in c:
                n = izloci_besedo(i)
                sez.append(n)
    u =unikati(sez)
    return (u)


#Beseda se začne z "@":
def vse_afne(tviti):
    o = zberi_se_zacne_z(tviti, "@")
    return (o)


#Beseda se začne z "#":
def vsi_hashtagi(tviti):
    o = zberi_se_zacne_z(tviti, "#")
    return (o)


#Vse osebe v tvitih:
def vse_osebe(tviti):
    a = vsi_avtorji(tviti) + vse_afne(tviti)
    u = unikati(a)
    s = sorted(u)
    return (s)


