def unikati(s):
    seznamNov = []
    for e in s:
        if e not in seznamNov:
            seznamNov.append(e)
    return seznamNov

def avtor(tvit):
    return tvit.split(':')[0]

def vsi_avtorji(tviti):
    seznam=[]
    for e in range(len(tviti)):
       seznam.append(avtor(tviti[e]))
    return unikati(seznam)

def izloci_besedo(beseda):
    for i in range(len(beseda)):
        if beseda[i].isalnum():
            start = i
            break
    for i in range(len(beseda)):
        if beseda[(len(beseda)-1)-i].isalnum():
            end = i
            break
    if end == 0:
        return beseda[start:]
    else:
        return beseda[start:-end]

def se_zacne_z(tvit, c):
    novSeznam = []
    for rijec in tvit.split(' '):
        if rijec[0] == c:
            novSeznam.append(izloci_besedo(rijec))
    return novSeznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        rijec = se_zacne_z(tvit, c)
        seznam.extend(rijec)
    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    noviSeznam = vse_afne(tviti) + seznam
    noviSeznam.sort(key=str.lower)
    return(unikati(noviSeznam))

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        hash1 = se_zacne_z(tvit, '#')
        if list(set(hash1) & set(hashtagi)):
            seznam.append(avtor(tvit))
    noviSeznam = unikati(seznam)
    noviSeznam.sort(key=str.lower)
    return noviSeznam

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            osebe = se_zacne_z(tvit, '@')
    if oseba2 in osebe:
        return True













