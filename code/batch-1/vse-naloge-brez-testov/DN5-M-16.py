import re
def unikati(s):
    a = []
    for x in s:
        if x not in a:
            a.append(x)
    return a

def avtor(tvit):
    prostor = tvit.index(":")
    return tvit[0:prostor]

def vsi_avtorji(tviti):
    a = []
    for x in tviti:
        a.append(avtor(x))
    a = unikati(a)
    return a

def izloci_besedo(beseda):
   a=re.sub('^[^\s\w]*|[^\s\w]*$','',beseda)
   return a

def se_zacne_z(tvit, c):
    a=[]
    seznam = [t for t in tvit.split() if t.startswith(c)]
    for x in seznam:
        a.append(izloci_besedo(x))
    return a

def zberi_se_zacne_z(tviti, c):
    seznam=[]
    for x in tviti:
        a=se_zacne_z(x,c)
        seznam += a
    seznam=unikati(seznam)
    return seznam

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    seznam = vse_afne(tviti) + vsi_avtorji(tviti)
    seznam = unikati(seznam)
    seznam = sorted(seznam)
    return seznam

def custva(tviti, hashtagi):
    b=[]
    for y in tviti:
        for x in hashtagi:
            if x in y:
                b.append(avtor(y))
    b=unikati(b)
    b=sorted(b)
    return b

def se_poznata(tviti, oseba1, oseba2):

    if oseba1 in vsi_avtorji(tviti) and oseba2 in vsi_avtorji(tviti):
        for y in tviti:
            if oseba2 == avtor(y):
                if oseba1 in y:
                    return True
            if oseba1 == avtor(y):
                if oseba2 in y:
                    return True
    return False



#____________________________________testi_________________________________________
