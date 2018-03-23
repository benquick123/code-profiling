import math
# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for kraj in kraji:
        if kraj[0] == ime:
            return (kraj[1], kraj[2])
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 +(y2-y1)**2 )

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    kraji_domet = []
    for kraj in kraji:
        ime_tarc = kraj[0]
        if ime_tarc != ime and razdalja(ime, ime_tarc, kraji) <= domet:
            kraji_domet.append(ime_tarc)
    return kraji_domet

def najbolj_oddaljeni(ime, imena, kraji):
    nabor_razdalj = []
    for kraj1 in imena:
        nabor_razdalj.append((kraj1, razdalja(ime, kraj1, kraji)))
    return max(nabor_razdalj, key = lambda x: x[1])[0]

def zalijemo(ime, domet, kraji):
    nabor_krajev = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, nabor_krajev, kraji)

def presek(s1, s2):
    s3 = set(s1) & set(s2)
    return list(s3)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    domet1 = v_dometu(ime1, domet, kraji)
    domet2 = v_dometu(ime2, domet, kraji)
    return presek(domet1, domet2)

