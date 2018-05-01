from math import *
import math

def unikati(seznam):
    novi_seznam = []
    for element_a in seznam:
        if(element_a in novi_seznam):
            continue
        else:
            novi_seznam.append(element_a)

    return novi_seznam

def avtor(tvit):
    seznam = tvit.split()
    prvi_element = seznam[0]
    odgovor = prvi_element[0:len(prvi_element)-1]

    return odgovor

def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        nov_uporabnik = avtor(tvit)
        seznam_avtorjev.append(nov_uporabnik)

    return(unikati(seznam_avtorjev))

def izloci_besedo(beseda):
    stevec_d = 0
    stevec_l = 0
    for i in range(0, len(beseda)):
        if (beseda[i].isalnum() == False):
            stevec_l = stevec_l + 1
        else:
            break

    for i in range(len(beseda) - 1, 0, -1):
        if (beseda[i].isalnum() == False):
            stevec_d = stevec_d + 1
        else:
            break

    return beseda[stevec_l:len(beseda) - stevec_d]

def se_zacne_z(tvit, c):
    seznam_besed = []
    seznam_tvit = tvit.split()
    for beseda in seznam_tvit:
        if(beseda[0] == c):
            if(len(beseda) > 1):
                skrajsana_beseda = izloci_besedo(beseda)
                seznam_besed.append(skrajsana_beseda)
            else:
                continue
        else:
            continue

    return unikati(seznam_besed)

def zberi_se_zacne_z(tviti, c):
    koncni_seznam = []
    for tvit in tviti:
        koncni_seznam.extend(se_zacne_z(tvit, c))

    return unikati(koncni_seznam)

def vse_afne(tviti):
    odgovor = zberi_se_zacne_z(tviti, "@")

    return  odgovor

def vsi_hashtagi(tviti):
    odgovor = zberi_se_zacne_z(tviti, "#")

    return odgovor

def vse_osebe(tviti):
    seznam1 = vsi_avtorji(tviti)
    seznam2 = vse_afne(tviti)

    return  sorted(unikati(seznam1+seznam2))

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        oseba = avtor(tvit)
        primerjava = se_zacne_z(tvit, "#")
        for prvi in primerjava:
            if(prvi in hashtagi):
                seznam.append(oseba)
            else:
                continue

    return sorted(unikati(seznam))

def se_poznata(tviti, oseba1, oseba2):
    tabela = []
    for tvit in tviti:
        pisec = avtor(tvit)
        poznavalec = se_zacne_z(tvit, "@")

        if(pisec == oseba1 and oseba2 in poznavalec) or (pisec == oseba2 and oseba1 in poznavalec):
            tabela.append(pisec)
            tabela.append(poznavalec)

    return tabela








