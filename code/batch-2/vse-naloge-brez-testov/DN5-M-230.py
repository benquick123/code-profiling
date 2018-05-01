def unikati(s):
    s1=[]
    for i in s:
        if i not in s1:
            s1.append(i)
    return s1

def avtor(tvit):
    tvit=tvit.split()
    return tvit[0].strip(":")

def vsi_avtorji(tviti):
    avtorji=[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    while beseda[0].isalnum() == 0:
        beseda=beseda.strip(beseda[0])
    while beseda[-1].isalnum() == 0:
        beseda=beseda.strip(beseda[-1])
    return beseda

def se_zacne_z(tvit, c):
    list = []
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == str(c):
            list.append(izloci_besedo(beseda))
    return list

def zberi_se_zacne_z(tviti, c):
    s=[]
    for tvit in tviti:
         s+=(se_zacne_z(tvit,c))
    return unikati(s)

def vse_afne(tviti):
    s = []
    for tvit in tviti:
        s += (se_zacne_z(tvit, "@"))
    return unikati(s)

def vsi_hashtagi(tviti):
    s = []
    for tvit in tviti:
        s += (se_zacne_z(tvit, "#"))
    return unikati(s)

def vse_osebe(tviti):
    osebe=[]
    osebe += vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    return sorted(unikati(osebe))

def custva(tviti,hashtagi):
    custvene_osebe=[]
    s=[]
    for tvit in tviti:
        tvit=tvit.split()
        for beseda in tvit:
            for hashtag in hashtagi:
                if beseda == "#"+hashtag:
                    custvene_osebe.append(tvit[0])
    for custvena_oseba in custvene_osebe:
        s.append(izloci_besedo(custvena_oseba))
    return sorted(unikati(s))

def se_poznata(tviti,oseba1,oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            for beseda in se_zacne_z(tvit,"@"):
                if beseda == oseba2:
                    return True
        elif avtor(tvit) == oseba2:
            for beseda in se_zacne_z(tvit,"@"):
                if beseda == oseba1:
                    return True

