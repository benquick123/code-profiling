def unikati(s):
    s1=[]
    for x in s:
        if x not in s1:
            s1.append(x)
    return s1

def avtor(tvit):
    return tvit.split()[0][:-1]

def vsi_avtorji(tviti):
    return unikati([avtor(x) for x in tviti])

def izloci_besedo(beseda):
   while not beseda[0].isalnum():
       beseda = beseda[1:]
   while not beseda[-1].isalnum():
       beseda = beseda[:-1]
   return beseda

def se_zacne_z(tvit, c):
    return [izloci_besedo(x) for x in tvit.split() if x[0] == c]

def zberi_se_zacne_z(tviti, c):
    s=[]
    for niz in tviti:
        s.extend(se_zacne_z(niz,c))
    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    return sorted(unikati(vse_afne(tviti) + vsi_avtorji(tviti)))

def custva(tviti, hashtagi):
    s=[]
    for ime, tagi in [(avtor(x), se_zacne_z(x, '#')) for x in tviti]:
        for tag in tagi:
            if tag in hashtagi:
                s.append(ime)
    return sorted(unikati(s))

def se_poznata(tviti, oseba1, oseba2):
    for ime, imena in [(avtor(x), se_zacne_z(x, '@')) for x in tviti]:
        if oseba1 == ime and oseba2 in imena or oseba2 == ime and oseba1 in imena :
            return True
    return False



















