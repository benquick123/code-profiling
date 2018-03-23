#1.
def unikati(s):
    xs = []
    for e in s:
        if e not in xs:
            xs.append(e)
    return xs

#2.
def avtor(tvit):
    ime = tvit.split(":")[0]
    return ime

#3.
def vsi_avtorji(tviti):
    xs = []
    for tvit in tviti:
        ime = tvit.split(":")[0]
        if ime not in xs:
            xs.append(ime)
    return xs

#4.
def izloci_besedo(beseda):
    izl_beseda = ""
    for x in beseda:
        if x.isalnum() or x == "-":
            izl_beseda += x
    return izl_beseda


#5.
def se_zacne_z(tvit, c):
    xs = []
    for x in tvit.split():
        if x[0] == c:
            xs.append(izloci_besedo(x))
    return xs

#6.
def zberi_se_zacne_z(tviti, c):
    xs = []
    for x in tviti:
        for y in x.split():
            if y[0] == c:
                beseda_c = izloci_besedo (y)
                if beseda_c not in xs:
                    xs.append(beseda_c)
    return xs

#7.
def vse_afne(tviti):
    xs = []
    for x in tviti:
        for y in x.split():
            if y[0] == "@":
                beseda_afna = izloci_besedo(y)
                if beseda_afna not in xs:
                    xs.append(beseda_afna)
    return xs

#8.
def vsi_hashtagi(tviti):
    xs = []
    for i in range(len(tviti)):
        x = tviti[i].split()
        for j in range(len(x)):
            if ("#" in x[j]) == True:
                beseda_hash = izloci_besedo(x[j])
                if beseda_hash not in xs:
                    xs.append(beseda_hash)
    return xs

#9.
def vse_osebe(tviti):
    osebe_v_tvitih = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(osebe_v_tvitih)
