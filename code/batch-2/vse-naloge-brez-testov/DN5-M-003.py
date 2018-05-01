def unikati(s):
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u

def avtor(tvit):
   colon = tvit.index(":")
   name = tvit[0 : colon]
   return name

def vsi_avtorji(tviti):
    vsi = []
    for x in tviti:
        y = avtor(x)
        if y not in vsi:
            vsi.append(y)
    return vsi

def izloci_besedo(beseda):
    forward = False
    backward = False
    while forward == False:
            if beseda[0].isalnum() is False:
                beseda = beseda[1 : ]
            else:
                forward = True
                break
    while backward == False:
        if beseda[-1].isalnum() is False:
            beseda = beseda[ : -1]
        else:
            backward = True
            break
    return beseda

def se_zacne_z(tvit, c):
    elementi = tvit.split()
    okrnjeno = []
    for x in elementi:
        if x[0] == c:
            okrnjeno.append(izloci_besedo(x))
    return okrnjeno

def zberi_se_zacne_z(tviti, c):
    trending = []
    tviti = " ".join(tviti)
    trending += se_zacne_z(tviti, c)
    return unikati(trending)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    nabor = []
    nabor += vsi_avtorji(tviti)
    nabor += vse_afne(tviti)
    nabor = unikati(nabor)
    return sorted(nabor)


def custva(tviti, hashtagi):
    hasharji = []
    for x in tviti:
        for kljucnik in hashtagi:
            if kljucnik in x:
                hasharji.append(avtor(x))
    return sorted(unikati(hasharji))

def se_poznata(tviti, oseba1, oseba2):
    poznanstvo = False
    oseba1_tviti = []
    oseba2_tviti = []
    for x in tviti:
        if oseba1 == avtor(x):
            oseba1_tviti.append(x)
            if oseba2 in vse_afne(oseba1_tviti):
                poznanstvo = True
    for y in tviti:
        if oseba2 == avtor(y):
            oseba2_tviti.append(y)
            if oseba1 in vse_afne(oseba2_tviti):
                poznanstvo = True
    return poznanstvo
















