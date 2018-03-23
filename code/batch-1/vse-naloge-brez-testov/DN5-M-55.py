def unikati(s):
    list = []
    for a in s:
        if a not in list:
            list.append(a)
    return list

def avtor(tvit):
    a = tvit.split()
    return a[0][:-1]

def vsi_avtorji(tviti):
    list = []
    for a in tviti:
        list.append(avtor(a))
    list = unikati(list)
    return list

def izloci_besedo(beseda):
    nekaj = ""
    for a in beseda:
        if a.isalnum():
            nekaj += a
        if a == "-":
            nekaj += a
    return nekaj

def se_zacne_z(tvit, c):
    list = []
    for a in tvit.split():
        if a[0] == c:
            list.append(izloci_besedo(a))
    return list

def zberi_se_zacne_z(tviti,c):
    list = []
    for a in tviti:
        for beseda in a.split():
            if beseda[0] == c:
                list.append(izloci_besedo(beseda))
    list = unikati(list)
    return list

def vse_afne(tviti):
    list = []
    for a in tviti:
        for beseda in a.split():
            if beseda[0] == "@":
                list.append(izloci_besedo(beseda))
    list = unikati(list)
    return list

def vsi_hashtagi(tviti):
    list = zberi_se_zacne_z(tviti, "#")
    return unikati(list)

def vse_osebe(tviti):
    list = vsi_avtorji(tviti)
    list += zberi_se_zacne_z(tviti, "@")
    return sorted(unikati(list))


