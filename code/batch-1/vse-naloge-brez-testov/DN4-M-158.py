# Tu pišite svoje funkcije:
from math import *
def koordinate(ime,kraji):
    for ime2,kor1,kor2 in kraji:
        if ime2 == ime:
            return kor1,kor2
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznam=[]
    for imeK, kor1, kor2 in kraji:
        if imeK == ime:
            kord1 = kor1
            kord2 = kor2
            break
    for imeK, kor1, kor2 in kraji:
        raz = sqrt((kor1 - kord1) ** 2 + (kor2 - kord2) ** 2)
        if raz <= domet and ime != imeK:
            seznam.append(imeK)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    maxraz = 0
    maxime=""
    for imeK, kor1, kor2 in kraji:
        if imeK == ime:
            kor1_1= kor1
            kor1_2 = kor2
    for imeK in imena:
        for imeK2,kor2_1,kor2_2 in kraji:
            if imeK2 == imeK:
                raz = sqrt((kor2_1 - kor1_1) ** 2 + (kor2_2 - kor1_2) ** 2)
                if maxraz < raz:
                    maxraz = raz
                    maxime = imeK2
    return maxime

def zalijemo(ime, domet, kraji):
    for imeK, kor1, kor2 in kraji:
        if imeK == ime:
            kord1 = kor1
            kord2 = kor2
            break
    maxraz = 0
    for ime, kor1, kor2 in kraji:
        raz = sqrt((kor1 - kord1) ** 2 + (kor2 - kord2) ** 2)
        if maxraz < raz and raz <= domet:
            maxraz = raz
            maxime = ime
    return maxime

def presek(s1, s2):
    seznam=[]
    for ime1 in s1:
        for ime2 in s2:
            if ime1==ime2:
                seznam.append(ime1)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam=[]
    for imeK, kor1, kor2 in kraji:
        if imeK == ime1:
            korKraj1_1 = kor1
            korKraj1_2 = kor2
            break

    for imeK, kor1, kor2 in kraji:
        if imeK == ime2:
            korKraj2_1 = kor1
            korKraj2_2 = kor2
            break

    for ime, kor1, kor2 in kraji:
        razKraj1 = sqrt((kor1 - korKraj1_1) ** 2 + (kor2 - korKraj1_2) ** 2)
        razKraj2 = sqrt((kor1 - korKraj2_1) ** 2 + (kor2 - korKraj2_2) ** 2)
        if razKraj1 <= domet and razKraj2 <= domet:
            seznam.append(ime)

    return seznam
