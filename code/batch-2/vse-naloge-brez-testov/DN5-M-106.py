# -*- coding: utf-8 -*-
def unikati(s):
    niz=[]
    for i in s:
        if i not in niz:
            niz.append(i)
    return niz

def avtor(tvit):
    niz = tvit.split(":")
    return niz[0]

def vsi_avtorji(tviti):
    niz=[]
    for i in tviti:
        niz.append(avtor(i))
    return unikati(niz)

def izloci_besedo(beseda):
    for i in beseda:
        if i.isalnum()==False:
            beseda=beseda[:0]+beseda[1:]
        elif i.isalnum()==True:
            for i in beseda[::-1]:
                if i.isalnum()==False:
                    beseda = beseda[:-1]
                else:
                    break
            break
    return beseda

def se_zacne_z(tvit,c):
    niz=[]
    str=tvit.split(" ")
    for i in str:
        if i[0]==c:
            niz.append(izloci_besedo(i))
    return niz

def zberi_se_zacne_z(tviti, c):
    niz=[]
    for i in tviti:
        niz=niz+se_zacne_z(i,c)
    return unikati(niz)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    niz = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(niz)

def custva(tviti,hashtagi):
    imena=[]
    for i in tviti:
        for j in hashtagi:
            tag=se_zacne_z(i,"#")
        for z in tag:
            if j == z:
                imena.append(avtor(i))
    return sorted(imena)

def se_poznata(tviti, oseba1, oseba2):
    omemba=[]
    bool = False
    for i in tviti:
        ime=avtor(i)
        if(ime==oseba1):
            omemba=se_zacne_z(i,"@")
            for j in omemba:
                if j==oseba2:
                    bool=True
                    return bool
        elif(ime==oseba2):
            omemba=se_zacne_z(i,"@")
            for j in omemba:
                if j==oseba1:
                    bool=True
                    return bool

