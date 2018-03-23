# DN4

from math import *

# ogrevalna naloga: koordinate

def koordinate(ime, kraji):
    for kraj ,x, y in kraji:
        if kraj == ime:
            return x, y

# ogrevalna naloga: razdalja_koordinat

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt ((x1 - x2) ** 2 + (y1 - y2) ** 2)

# ogrevalna naloga: razdalja_krajev

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate (ime1, kraji)
    x2, y2 = koordinate (ime2, kraji)
    return razdalja_koordinat (x1, y1, x2, y2)

# obvezna naloga: v_dometu

def v_dometu(ime, domet, kraji):
    seznam_krajev = []
    for kraj, x, y in kraji:
        if kraj == ime:
            x1, y1 = x, y
            for tarce, x2, y2 in kraji:
                razdalja = sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if razdalja <= domet and razdalja != 0:
                    seznam_krajev.append(tarce)
            return seznam_krajev

# obvezna naloga: najbolj_oddaljeni

def najbolj_oddaljeni(ime, imena, kraji):
    naj_oddaljen = 0
    for kraj, x, y in kraji:
        if kraj == ime:
            x1, y1 = x, y
            for tarce, x2, y2 in kraji:
                for mesto in imena:
                    if mesto == tarce:
                        razdalja = sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)
                        if razdalja > naj_oddaljen:
                            naj_oddaljen = razdalja
                            oddaljen_kraj = mesto
    return oddaljen_kraj

# obvezna naloga: zalijemo

def zalijemo(ime, domet, kraji):
    naj_oddaljen = 0
    for kraj, x, y in kraji:
        if kraj == ime:
            x1, y1 = x, y
            for tarce, x2, y2 in kraji:
                razdalja = sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if domet >= razdalja and naj_oddaljen <= razdalja:
                    naj_oddaljen = razdalja
                    oddaljen_kraj = tarce
    return oddaljen_kraj

# dodatna naloga: presek

def presek(s1, s2):
    presek = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                presek.append(e1)

    return presek

# dodatna naloga: skupno_zalivanje

def skupno_zalivanje(ime1, ime2, domet, kraji):
    tarce_ime1 = []
    tarce_ime2 = []
    presek = []
    for kraj, x, y in kraji:
        if kraj == ime1:
            x1, y1 = x, y
            for tarce, x2, y2 in kraji:
                razdalja = sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if domet >= razdalja:
                    tarce_ime1.append (tarce)
        if kraj == ime2:
            x1, y1 = x, y
            for tarce, x2, y2 in kraji:
                razdalja = sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if domet >= razdalja:
                    tarce_ime2.append (tarce)
    for e1 in tarce_ime1:
        for e2 in tarce_ime2:
            if e1 == e2:
                presek.append(e1)
    return presek








