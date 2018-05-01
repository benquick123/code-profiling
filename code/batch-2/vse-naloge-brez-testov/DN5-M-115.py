def unikati(s):
    nov = []
    for a in s:
        if a not in nov:
            nov.append(a)
    return nov

def avtor(tvit):
    x = tvit.split(":")
    return x[0]

def vsi_avtorji(tviti):
    nov = []
    for x in tviti:
        y = avtor(x)
        if y not in nov:
            nov.append(y)
    return nov

def izloci_besedo(beseda):
    for i in range(2):
        for a in beseda:
            if a.isalnum() == False:
                beseda = beseda[1:len(beseda)]
            else:
                break
        beseda = beseda[::-1]
    return beseda

def se_zacne_z(tvit, c):
    izpis=[]
    n = tvit.split(" ")
    for x in n:
        if c in x:
            x=izloci_besedo(x)
            izpis.append(x)
    return izpis

def zberi_se_zacne_z(tviti, c):
    izpis = []
    for a in tviti:
        if c in a:
            x = se_zacne_z(a, c)
            izpis.extend(x)
    izpis = unikati(izpis)
    return izpis

def vse_afne(tviti):
    izpis=[]
    for y in tviti:
        n = y.split(" ")
        for x in n:
            if "@" in x:
                x = izloci_besedo(x)
                if x not in izpis:
                    izpis.append(x)
    return izpis

def vsi_hashtagi(tviti):
    izpis = []
    for y in tviti:
        n = y.split(" ")
        for x in n:
            if "#" in x:
                x = izloci_besedo(x)
                if x not in izpis:
                    izpis.append(x)
    return izpis

def vse_osebe(tviti):
    izpis=[]
    x = vse_afne(tviti)
    x.extend(vsi_avtorji(tviti))
    izpis = unikati(x)
    izpis.sort()
    return izpis

def custva(tviti, hashtagi):
    izpis = []
    for i in hashtagi:
        for tvit in tviti:
            if i in tvit:
                izpis.append(avtor(tvit))
    izpis = unikati(izpis)
    izpis.sort()
    return izpis

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        x = (avtor(tvit))
        if x == oseba1:
            if oseba2 in tvit and oseba2 in vse_osebe(tviti):
                return True
            else:
                return False


