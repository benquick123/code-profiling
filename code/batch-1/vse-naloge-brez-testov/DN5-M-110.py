#-*- coding: utf-8 -*-
def unikati(s):
    tab=[]
    for x in s:
       if tab.count(x)==0:
           tab.append(x)
    return tab



    return tab

def avtor(tvit):
    return tvit.split(':')[0]

def vsi_avtorji(tviti):
    avtorji=[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    for crka in beseda:
        if not crka.isalnum():
            beseda=beseda[1:]
        else:
            break

    for crka in beseda[::-1]:
        if not crka.isalnum():
            beseda=beseda[:len(beseda)-1]

        else:
            break
    return beseda

def se_zacne_z(tvit, c):
    rez=[]
    tvit=tvit.split(' ')
    for beseda in tvit:
        if(beseda.startswith(c)):
            rez.append(izloci_besedo(beseda))
    return rez
def zberi_se_zacne_z(tviti, c):
    rez=[]
    for tvit in tviti:
        rez+=se_zacne_z(tvit,c)
    return unikati(rez)
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")
def vse_osebe(tviti):
    rez = vsi_avtorji(tviti)
    rez+=vse_afne(tviti)
    rez=unikati(rez)
    rez.sort()
    return  rez




