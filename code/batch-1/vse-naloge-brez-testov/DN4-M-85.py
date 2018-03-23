# Tu pišite svoje funkcije:

def koordinate(ime, kraji):
    for ime_k, x, y in kraji:
        if ime_k == ime:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)


def razdalja(ime1, ime2, kraji):
   x1, y1 = koordinate(ime1, kraji)
   x2, y2 = koordinate(ime2, kraji)
   return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    xk, yk = koordinate(ime, kraji)
    tmp = []
    for ime_k, x, y in kraji:
        if ime_k == ime: continue
        elif razdalja_koordinat(x,  y, xk, yk) - domet <= 0:
            tmp.append(ime_k)
    return tmp

def najbolj_oddaljeni(ime, imena, kraji):
    max = 0
    najbolj_oddaljen = ""
    for ime2 in imena:
        if max < razdalja(ime, ime2, kraji):
            max = razdalja(ime, ime2, kraji)
            najbolj_oddaljen = ime2
    return najbolj_oddaljen

def zalijemo(ime, domet, kraji):
    max_razdalja = 0
    ime_max = ""
    for imek, x, y in kraji:
        if (razdalja(ime, imek, kraji) - domet <= 0) and (max_razdalja < razdalja(ime, imek, kraji)):
            max_razdalja = razdalja(ime, imek, kraji)
            ime_max = imek
    return ime_max

def skupno_zalivanje(ime1,ime2, domet, kraji):
    tmp = []
    for ime_k, x, y in kraji:
        if (razdalja(ime1, ime_k, kraji ) - domet <=0) and (razdalja(ime2, ime_k, kraji ) - domet <=0):
            tmp.append(ime_k)
    return tmp


def presek(s1, s2):
    skupno = []
    for element_s1 in s1:
        for element_s2 in s2:
            if element_s1 == element_s2:
                skupno.append(element_s2)
    return skupno


