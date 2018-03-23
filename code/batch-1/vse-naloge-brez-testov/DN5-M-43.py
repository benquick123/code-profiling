def unikati(s):
    nov_seznam = []
    for stevilo in s:
        if stevilo not in nov_seznam:
            nov_seznam.append(stevilo)

    return nov_seznam

def avtor(tvit):
    seznam = tvit.split(" ")
    return seznam[0][:-1]

def vsi_avtorji(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    return unikati(seznam)

def izloci_besedo(beseda):
    n = 0

    for crka in beseda:
        if crka.isalnum() == False:
            n = n + 1
        if crka.isalnum() == True:
            break

    beseda1 = beseda[n:]
    beseda2 = beseda1[::-1]
    n = 0

    for crka in beseda2:
        if crka.isalnum() == False:
            n = n + 1
        if crka.isalnum() == True:
            break
    beseda1 = beseda2[n:]

    return(beseda1[::-1])

def se_zacne_z(tvit, c):
    seznam = tvit.split(" ")
    seznam1 = []
    for a in seznam:
        if a[0] == c:
            seznam1.append(izloci_besedo(a))

    return seznam1

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam.extend(se_zacne_z(tvit,c))

    return unikati(seznam)

def vse_afne(tviti):
    return  zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    osebe = []
    osebe.extend(vsi_avtorji(tviti))
    osebe.extend(vse_afne(tviti))
    return sorted(unikati(osebe))

