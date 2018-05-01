# Tu pišite svoje funkcije:

import math

def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if ime_kraja == ime:
            return (x, y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def razdalja(ime1, ime2, kraji):
    koordinate1 = koordinate(ime1, kraji)
    koordinate2 = koordinate(ime2, kraji)
    return razdalja_koordinat(koordinate1[0], koordinate1[1], koordinate2[0], koordinate2[1])

def v_dometu(ime, domet, kraji):
    koordinate_kraja = koordinate(ime, kraji)
    seznam = []
    for kraj in kraji:
        ime_kraja, x, y = kraj
        if ime_kraja == ime:
            continue # Kraj ne zaliva sebe.
        if razdalja(ime, ime_kraja, kraji) <= domet:
            seznam.append(ime_kraja)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    if not imena:
        return None
    najbolj_oddaljeni_ime = None
    najbolj_oddaljeni_razdalja = 0
    for ime_kraja in imena:
        razdalja_med_krajema = razdalja(ime, ime_kraja, kraji)
        if razdalja_med_krajema > najbolj_oddaljeni_razdalja:
            najbolj_oddaljeni_razdalja = razdalja_med_krajema
            najbolj_oddaljeni_ime = ime_kraja
    return najbolj_oddaljeni_ime

def zalijemo(ime, domet, kraji):
    najbolj_oddaljeni_ime = None
    najbolj_oddaljeni_razdalja = 0
    for ime_kraja, x, y in kraji:
        razdalja_med_krajema = razdalja(ime, ime_kraja, kraji)
        if razdalja_med_krajema <= domet and razdalja_med_krajema > najbolj_oddaljeni_razdalja:
            najbolj_oddaljeni_razdalja = razdalja_med_krajema
            najbolj_oddaljeni_ime = ime_kraja
    return najbolj_oddaljeni_ime

def presek(s1, s2):
    s3 = []
    for s in s1:
        if s in s2:
            s3.append(s)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))


