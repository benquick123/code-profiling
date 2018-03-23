def unikati(s):
    seznam=[]
    for neki in s:
        if neki not in seznam:
            seznam.append(neki)
    return seznam

def avtor(tvit):
    ime=tvit.split()
    imeNovo=ime[0].replace(":","")
    return imeNovo

def vsi_avtorji(tviti):
    seznam=[]
    for neki in tviti:
        ime=avtor(neki)
        if ime not in seznam:
            seznam.append(ime)
    return seznam

def izloci_besedo(beseda):
    beseda = list(beseda)
    while (ord(beseda[0]) < 48 or ord(beseda[0]) > 57) and (ord(beseda[0]) < 65 or ord(beseda[0]) > 90) and (ord(beseda[0]) < 97 or ord(beseda[0]) > 122):
        del (beseda[0])
    i = len(beseda) - 1
    while (ord(beseda[i]) < 48 or ord(beseda[i]) > 57) and (ord(beseda[i]) < 65 or ord(beseda[i]) > 90) and (ord(beseda[i]) < 97 or ord(beseda[i]) > 122):
        del (beseda[i])
        i = i - 1
    beseda = "".join(beseda)
    return beseda

def se_zacne_z(tvit, c):
    tvit=tvit.split()
    seznam=[]
    for neki in tvit:
        if neki[0] == c:
            novaBes=izloci_besedo(neki)
            seznam.append(novaBes)
    return seznam

def zberi_se_zacne_z(tviti,c):
    sez=[]
    for neki in tviti:
        neki=neki.split()
        for neki2 in neki:
            if neki2[0] == c:
                novaBes = izloci_besedo(neki2)
                sez.append(novaBes)
    return unikati(sez)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    novSeznam=[]
    novSeznam=vse_afne(tviti)+vsi_avtorji(tviti)
    novSeznam=unikati(novSeznam)
    novSeznam.sort()
    return novSeznam

def custva(tviti,hashtagi):
    seznam=[]
    for neki in tviti:
        neki = neki.split()
        for neki2 in hashtagi:
            if "#"+neki2 in neki:
                seznam.append(avtor(neki[0]))
    seznam=unikati(seznam)
    seznam.sort()
    return seznam

def se_poznata(tviti,oseba1,oseba2):
    for neki in tviti:
        if avtor(neki) == oseba1:
            if "@"+oseba2 in neki:
                return True
    for neki in tviti:
        if avtor(neki) == oseba2:
            if "@"+oseba1 in neki:
                return True
    return False


