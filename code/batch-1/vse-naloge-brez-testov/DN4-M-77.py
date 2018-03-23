from math import *


# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y
    return None


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdaljaMedKraji = razdalja_koordinat(x1, y1, x2, y2)
    return razdaljaMedKraji


def v_dometu(ime, domet, kraji):
    krajiVDometu = []
    for kraj, x, y in kraji:
        if kraj != ime:
            razdaljaDometa = razdalja(ime, kraj, kraji)
            if razdaljaDometa <= domet:
                krajiVDometu.append(kraj)
    return krajiVDometu

def najbolj_oddaljeni(ime, imena, kraji):
    najboljOddaljen = ime
    for kraj in imena:
        if razdalja(ime, kraj, kraji) > razdalja(ime, najboljOddaljen, kraji):
            najboljOddaljen = kraj
    return najboljOddaljen

def zalijemo(ime, domet, kraji):
    imena = v_dometu(ime, domet, kraji)
    najOddaljenDomet = najbolj_oddaljeni(ime, imena, kraji)
    return najOddaljenDomet

def presek(s1, s2):
    skupno = [skupenPodatek for skupenPodatek in s1 if skupenPodatek in s2]
    return skupno

def skupno_zalivanje(ime1, ime2, domet, kraji):
    ime1Kraji = v_dometu(ime1, domet, kraji)
    ime2Kraji = v_dometu(ime2, domet, kraji)
    skupniKraji = presek(ime1Kraji, ime2Kraji)
    return skupniKraji

