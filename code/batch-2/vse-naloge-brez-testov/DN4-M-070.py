# Tu pišite svoje funkcije:
from math import *

def v_dometu(ime, domet, kraji):
    seznam_krajev = []

    for kraj, koordinata1, koordinata2 in kraji:
        if ime == kraj:
            izbrana_koordinata1 = koordinata1;
            izbrana_koordinata2 = koordinata2;

    for kraj, koordinata1, koordinata2 in kraji:
        razdalja = sqrt((izbrana_koordinata1 - koordinata1) ** 2 + (izbrana_koordinata2 - koordinata2) ** 2)
        if razdalja <= domet and kraj != ime:
            seznam_krajev.append(str(kraj));

    return seznam_krajev

def najbolj_oddaljeni(ime, imena, kraji):
    najvecja_razdalja = 0
    izbrana_koordinata1 = 0
    izbrana_koordinata2 = 0
    najbolj_oddaljen_kraj_v_seznamu = ""

    for kraj, koordinata1, koordinata2 in kraji:
        if kraj == ime:
            izbrana_koordinata1 = koordinata1
            izbrana_koordinata2 = koordinata2

    for kraj, koordinata1, koordinata2 in kraji:
        for ime_v_seznamu in imena:
            if ime_v_seznamu == kraj:
                razdalja = sqrt((izbrana_koordinata1 - koordinata1) ** 2 + (izbrana_koordinata2 - koordinata2) ** 2)
                if razdalja > najvecja_razdalja:
                    najvecja_razdalja = razdalja
                    najbolj_oddaljen_kraj_v_seznamu = kraj

    return najbolj_oddaljen_kraj_v_seznamu

def zalijemo(ime, domet, kraji):
    najvecja_razdalja=0
    izbrana_koordinata1=0
    izbrana_koordinata2=0
    najbolj_oddaljen_kraj="Vsi kraji so oddaljeni dalje, kot je domet topa."

    for kraj, koordinata1, koordinata2 in kraji:
        if kraj == ime:
            izbrana_koordinata1 = koordinata1
            izbrana_koordinata2 = koordinata2

    for kraj, koordinata1, koordinata2 in kraji:
        razdalja = sqrt((izbrana_koordinata1 - koordinata1) ** 2 + (izbrana_koordinata2 - koordinata2) ** 2)
        if razdalja > najvecja_razdalja and razdalja <= domet:
            najvecja_razdalja = razdalja
            najbolj_oddaljen_kraj = kraj

    return najbolj_oddaljen_kraj

def presek(s1, s2):
    s3 = []

    for ime1 in s1:
        for ime2 in s2:
            if ime1 == ime2:
                s3.append(ime1)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraji_ki_jih_dosezeta_oba_kraja = []

    for kraj, koordinata1, koordinata2 in kraji:
        if ime1 == kraj:
            izbrana_koordinata1_kraja1 = koordinata1
            izbrana_koordinata2_kraja1 = koordinata2

        if ime2 == kraj:
            izbrana_koordinata1_kraja2 = koordinata1
            izbrana_koordinata2_kraja2 = koordinata2

    for kraj, koordinata1, koordinata2 in kraji:
        razdalja1 = sqrt(
            (izbrana_koordinata1_kraja1 - koordinata1) ** 2 + (izbrana_koordinata2_kraja1 - koordinata2) ** 2)
        razdalja2 = sqrt(
            (izbrana_koordinata1_kraja2 - koordinata1) ** 2 + (izbrana_koordinata2_kraja2 - koordinata2) ** 2)

        if razdalja1 <= domet and razdalja2 <= domet:
            kraji_ki_jih_dosezeta_oba_kraja.append(str(kraj))
    return kraji_ki_jih_dosezeta_oba_kraja

def koordinate(ime, kraji):
    z = 0

    for kraj, koordinata1, koordinata2 in kraji:
        if ime == kraj:
            x = koordinata1
            y = koordinata2
            z = 1
    if z == 1:
        return x, y


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    for kraj, koordinata1, koordinata2 in kraji:
        if ime1 == kraj:
            x1, y1 = koordinate(kraj, kraji)

        if ime2 == kraj:
            x2, y2 = koordinate(kraj, kraji)

    razdalja = razdalja_koordinat(x1,y1,x2,y2)
    return razdalja


