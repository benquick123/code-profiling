def unikati(s):
    nov_sez = []
    for stevilo in s:
        if stevilo not in nov_sez:
            nov_sez.append(stevilo)
    return nov_sez

def avtor(tvit):
    return tvit[0:tvit.index(":")]

def vsi_avtorji(tviti):
    s = []
    for a in tviti:
        if avtor(a) not in s:
            s.append(avtor(a))
    return s

def izloci_besedo(beseda):
    i, c = [0, len(beseda)]
    for a in beseda:
        if a.isalnum():
            z1 = i
            break
        i += 1
    for b in beseda[::-1]:
        if b.isalnum():
            zz = c
            break
        c -= 1
    return beseda[z1:zz]

def se_zacne_z(tvit, c):
    znak = []
    for a in tvit.split():
        if a.startswith(c):
            znak.append(izloci_besedo(a))
    return znak

def zberi_se_zacne_z(tviti, c):
    besede = []
    for a in tviti[0:]:
        for b in a.split():
            if b.startswith(c):
                if izloci_besedo(b) not in besede:
                    besede.append(izloci_besedo(b))
    return besede

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    s = []
    s += zberi_se_zacne_z(tviti, "@") + vsi_avtorji(tviti)
    s = unikati(s)
    s.sort()
    return s

def custva(tviti, hastagi):
    osebe = []
    for a in tviti:
        for b in hastagi:
            for c in a.split():
                if b in izloci_besedo(c):
                    if avtor(a) not in osebe:
                        osebe.append(avtor(a))
    osebe.sort()
    return osebe

def se_poznata(tviti, oseba1, oseba2):
    for a in tviti:
        s = a.split()
        if avtor(s[0]) == oseba1 or avtor(s[0]) == oseba2:
            if oseba2 in zberi_se_zacne_z(s, "@") or oseba1 in zberi_se_zacne_z(s, "@"):
                return True
    return False



