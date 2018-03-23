def unikati(s):
    sez = []
    for x in s:
        if x not in sez:
            sez.append(x)
    return sez

def avtor(tvit):
    spl = tvit.split(" ")
    ime = spl[0]

    return ime[:-1]

def vsi_avtorji(tviti):
    i = 0
    sez = []
    for x in tviti:
        novi = tviti[i].split(" ")
        ime1 = novi[0]
        ime2 = ime1[:-1]

        if ime2 not in sez:
            sez.append(ime2)
        i += 1
    return sez

def izloci_besedo(beseda):
    for x in beseda:
        if not x.isalnum():
            beseda = beseda.replace(x, "")
        else:
            break

    ime_rev = beseda[::-1]

    for x in ime_rev:
        if not x.isalnum():
            ime_rev = ime_rev.replace(x, "")
        else:
            break

    imeF = ime_rev[::-1]
    return imeF

def se_zacne_z(tvit, c):
    i = 0
    sez = []

    for y in tvit.split(" "):
        if y.startswith(c):
            koš = "!@#$=:?,."

            for smet in koš:
                y = y.replace(smet, "")
            if y not in sez:
                sez.append(y)
        i += 1
    return sez

def zberi_se_zacne_z(tviti, c):
    i = 0
    sez = []
    for x in tviti:
        for y in x.split(" "):
            if y.startswith(c):
                koš = "!@#$=:?,."

                for smet in koš:
                    y = y.replace(smet, "")
                if y not in sez:
                    sez.append(y)
            i += 1
    return sez

def vse_afne(tviti):
    i = 0
    sez = []
    for x in tviti:
        for y in x.split(" "):
            if y.startswith("@"):
                koš = "!@#$=:?,."

                for smet in koš:
                    y = y.replace(smet, "")
                if y not in sez:
                    sez.append(y)
            i += 1
    return sez

def vsi_hashtagi(tviti):
    i = 0
    sez = []
    for x in tviti:
        for y in x.split(" "):
            if y.startswith("#"):
                koš = "!@#$=:?,."

                for smet in koš:
                    y = y.replace(smet, "")
                if y not in sez:
                    sez.append(y)
            i += 1
    return sez

def vse_osebe(tviti):

    sez = []

    for x in vsi_avtorji(tviti):
        sez.append(x)

    for y in vse_afne(tviti):
        if y not in sez:
            sez.append(y)

    sez.sort()

    return sez

