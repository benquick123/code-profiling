# Obvezni del

# 1.
def unikati(s):
    d = []
    for x in s:
        if (x in s) and (x not in d):
            d.append(x)
    return d

# 2.
def avtor(tvit):
    x = tvit.split(":")
    e = x[0]
    return e

# 3.
def vsi_avtorji(tviti):
    d = []
    for e in tviti:
        x = avtor(e)
        if x not in d:
            d.append(x)
    return d

# 4.
def izloci_besedo(beseda):
    for e in beseda[::1]:
        if not e.isalnum():
            beseda = beseda[1:]
        else:
            break
    for e in beseda[::-1]:
        if not e.isalnum():
            beseda = beseda[:-1]
        else:
            break
    return beseda

# 5.
def se_zacne_z(tvit, c):
    d = []
    for e in tvit.split():
        if c == e[0]:
            d.append(izloci_besedo(e))
    return d

#6.
def zberi_se_zacne_z(tviti, c):
    d = []
    for tvit in tviti:
        for beseda in tvit.split():
            if beseda[0] == c:
                x = izloci_besedo(beseda)
                if x not in d:
                    d.append(x)
    return d

# 7.
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

# 8.
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

# 9.
def vse_osebe(tviti):
    x = vsi_avtorji(tviti)
    y = vse_afne(tviti)
    for e in y:
        if e not in x:
            x.append(e)
    return sorted(x)




