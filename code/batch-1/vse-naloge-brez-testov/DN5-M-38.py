import re
"""
def unikati(s):
    izbrani = []
    for x in s:
        if x not in izbrani:
            izbrani.append(x)
    return izbrani

def unikati(s):
    izbrani = []
    return [x for x in s if not(x in izbrani or izbrani.append(x))]

def izloci_besedo(beseda):
    for y,i in enumerate(beseda):
        if i.isalnum():
            z = y
            break
    for x,j in enumerate(beseda):
        if j.isalnum():
            k = x    
    return beseda[z:k+1]
"""

def unikati(s):
    return [x for i , x in enumerate(s) if i == s.index(x)]

def avtor(tvit):
    return tvit.split()[0][:-1]

def vsi_avtorji(tviti):
    return unikati([avtor(i) for i in tviti])

def izloci_besedo(beseda):
    return re.search(r"([a-zA-Z\d]+.*[a-zA-Z\d])|([a-zA-Z\d])", beseda)[1]
    
def se_zacne_z(tvit, c):
    return [izloci_besedo(x) for x in tvit.split() if x[0]==c]

def zberi_se_zacne_z(tviti, c):
    return unikati([elementi for lista in (se_zacne_z(x, c) for x in tviti) for elementi in lista])

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    return sorted(unikati([avtor(tvit) for tvit in tviti for hashtag in hashtagi if "#"+hashtag in tvit]))   

def se_poznata(tviti, oseba1, oseba2):
    return [True for tvit in tviti if oseba1 == avtor(tvit) and oseba2 in se_zacne_z(tvit, "@") or oseba2 == avtor(tvit) and oseba1 in se_zacne_z(tvit, "@")]
        
            
