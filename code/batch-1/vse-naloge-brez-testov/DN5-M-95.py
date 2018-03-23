def unikati(s):
    nov = []
    for el in s:
        if el not in nov:
            nov += [el]
    return nov


def avtor(tvit):
    x = tvit.split(":")
    return x[0]


def vsi_avtorji(tviti):
    x = []
    for el in tviti:
        x += [avtor(el)]
    return unikati(x)


def izloci_besedo(beseda):
    i = 0
    while beseda[i].isalnum() == False:
        beseda = beseda[1:]
    i = len(beseda)-1
    while i >= 0 and beseda[i].isalnum() == False:
        beseda = beseda[:-1]
        i -= 1
    return beseda


def se_zacne_z(tvit, c):
    x = []
    y = tvit.split(" ")
    for el in y:
        if el[0] == c:
            x += [izloci_besedo(el)]
    return x


def zberi_se_zacne_z(tviti, c):
    x = []
    for el in tviti:
        temp = se_zacne_z(el, c)
        for e in temp:
            if e != []:
                x += [e]
    return unikati(x)


def vse_afne(tviti):
    x = []
    for el in tviti:
        t = el.split(" ")
        for e in t:
            if se_zacne_z(e, "@"):
                x += [izloci_besedo(e)]
    return unikati(x)


def vsi_hashtagi(tviti):
    x = []
    for el in tviti:
        t = el.split(" ")
        for e in t:
            if se_zacne_z(e, "#"):
                x += [izloci_besedo(e)]
    return unikati(x)


def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti)+vse_afne(tviti)))

def custva(tviti, hashtagi):
    x = []
    for el in tviti:
        t = el.split(" ")
        j = 1
        while j<len(t):
            if t[j][1:] in hashtagi:
                x.append(t[0][:-1])
            j += 1
    return sorted(unikati(x))


def se_poznata(tviti, oseba1, oseba2):
    if oseba1 in vsi_avtorji(tviti) and oseba2 in vsi_avtorji(tviti):
        for tvit in tviti:
            a = avtor(tvit)
            besede = tvit.split(" ")
            for beseda in besede:
                if izloci_besedo(beseda) == oseba2 and oseba1 == a:
                    return True
                if izloci_besedo(beseda) == oseba1 and oseba2 == a:
                    return True
    return False










