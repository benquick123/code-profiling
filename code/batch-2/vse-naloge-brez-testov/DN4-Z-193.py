# Tu pišite svoje funkcije:

def koordinate(kraj1,vsi_kraji):
    for ime1, x1, y1 in vsi_kraji:
        if ime1 == kraj1:
            return x1,y1

from math import sqrt
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja_k = sqrt((pow((x1 - x2), 2)) + (pow((y1 - y2), 2)))
    return razdalja_k

def razdalja(kraj1,kraj2,vsi_kraji):
    x1, y1 = koordinate(kraj1,vsi_kraji)
    x2, y2 = koordinate(kraj2,vsi_kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

##############

def v_dometu(kraj, domet, vsi_kraji):
    kraj1 = kraj
    s = []
    for kraj2, x2, y2 in vsi_kraji:
        if kraj2 is not kraj:
            if domet >= razdalja(kraj1,kraj2,vsi_kraji):
                s.append(kraj2)
    return s

def najbolj_oddaljeni(kraj, imena, vsi_kraji):
    najvisja = 0
    najodd = 0
    kraj1 = kraj
    for kraj2 in imena:
        if razdalja(kraj1, kraj2, vsi_kraji)> najvisja:
            najodd = kraj2
            najvisja = razdalja(kraj1, kraj2, vsi_kraji)
    return najodd

def zalijemo(kraj, domet, vsi_kraji):
    kraj1 = kraj
    najvisja = 0
    dosegljivi = v_dometu(kraj, domet, vsi_kraji)
    for kraj2 in dosegljivi:
        if razdalja(kraj1, kraj2, vsi_kraji) > najvisja:
            najodd = kraj2
            najvisja = razdalja(kraj1, kraj2, vsi_kraji)
    return najodd

######################################
def presek(s1,s2):
    p = []
    for e in s1:
        for e2 in s2:
            if e2 == e:
                p.append(e2)
    return p


def skupno_zalivanje(kraj1, kraj2, domet, vsi_kraji):
    p = []
    g = v_dometu(kraj1, domet, vsi_kraji)
    h = v_dometu(kraj2, domet, vsi_kraji)
    for e1 in g:
        for e2 in h:
            if e1 == e2:
                p.append(e2)
    return p









