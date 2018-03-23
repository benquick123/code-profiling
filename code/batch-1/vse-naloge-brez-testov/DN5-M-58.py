# UNIKATI -dela-
def unikati(s):
    sez = []
    for e in s:
        if e not in sez:
            sez.append(e)
    return sez

# AVTOR -dela-
def avtor(tvit):
    at = tvit.split()[0]
    ime = ""
    for l in at:
        if l.isalpha():
            ime += l
    return ime

# VSI AVTORJI -dela-
def vsi_avtorji(tviti):
    sez = []
    for a in tviti:
        tr_avtor = avtor(a)
        if tr_avtor not in sez:
            sez.append(tr_avtor)
    return sez

# IZLOCI BESEDO -dela-
def izloci_besedo(beseda):
    while len(beseda) > 0 and not beseda[0].isalnum():
        beseda = beseda[1:]
    while len(beseda) > 0 and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

# SE ZACNE -dela-
def se_zacne_z(tvit, c):
    sez = []
    for e in tvit.split():
        if e.startswith(c):
            sez.append(izloci_besedo(e))
    return sez

# ZBERI SE ZACNE Z -dela-
def zberi_se_zacne_z(tviti, c):
    sez = []
    new_sez = []
    for e in tviti:
        new_sez.append(se_zacne_z(e, c))
    for e in new_sez:
        for i in e:
            if i != None and i not in sez:
                sez.append(i)
    return sez

# VSE AFNE -dela-
def vse_afne(tviti):
    c = "@"
    seznam = zberi_se_zacne_z(tviti, c)
    return seznam

# VSI HASHTAGI -dela-
def vsi_hashtagi(tviti):
    c = "#"
    seznam = zberi_se_zacne_z(tviti, c)
    return seznam


# VSE OSEBE -dela-
def vse_osebe(tviti):
    sez_oseb = []
    sez1 = vsi_avtorji(tviti)
    sez2 = zberi_se_zacne_z(tviti, "@")
    for e in sez1:
        if e not in sez_oseb:
            sez_oseb.append(e)
    for i in sez2:
        if i not in sez_oseb:
            sez_oseb.append(i)
    sez_oseb = sorted(sez_oseb)
    return sez_oseb





