#Prva
def unikati(s):
    seznam = []
    for vsak in s:
        if vsak not in seznam:
            seznam.append(vsak)
    return seznam

#Druga
def avtor(tvit):
    seznam = tvit.split(":")
    return seznam[0]

#Tretja
def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        seznam1 = tvit.split(":")
        if seznam1[0] not in avtorji:
            avtorji.append(seznam1[0])
    return avtorji

#Četrta
def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return(beseda)

#Peta
def se_zacne_z(tvit, c):
    seznam = []
    tvit = tvit.split()
    for vsak in tvit:
        if vsak[0] == c:
            seznam.append(izloci_besedo(vsak))
    return seznam

#Šesta
def zberi_se_zacne_z(tviti, c):
    resitev = []
    for i in tviti:
        seznam1 = i.split()
        for j in seznam1:
            if j[0] == c and izloci_besedo(j) not in resitev:
                resitev.append(izloci_besedo(j))
    return resitev

#Sedma
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

#Osma
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

#Deveta
def vse_osebe(tviti):
    rezultat = []
    for k in tviti:
        seznam = k.split(":")
        if seznam[0] not in rezultat:
            rezultat.append(seznam[0])
    for i in tviti:
        seznam1 = i.split()
        for j in seznam1:
            if j[0] == "@" and izloci_besedo(j) not in rezultat:
                rezultat.append(izloci_besedo(j))
    rezultat.sort()
    return(rezultat)

#Dodatna prva
def custva(tviti, hashtagi):
    izpis = []
    for i in tviti:
        seznam = i.split()
        for j in seznam:
            if j[1:] in (vsi_hashtagi(tviti)) and j[1:] in hashtagi:
                if (avtor(i)) not in izpis:
                    izpis.append(avtor(i))
    izpis.sort()
    return izpis

#Dodatna druga
def se_poznata(tviti, oseba1, oseba2):
    for i in tviti:
        if avtor(i) == oseba1:
            for j in se_zacne_z(i, "@"):
                if j == oseba2:
                    return True
    return False

"""========================================================================="""

