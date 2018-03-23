import math

def koordinate(ime, kraji):
    koord = None
    for imei, lon, lat in kraji:
        if imei == ime:
            koord = (lon, lat)
    return koord



def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja


def razdalja(ime1, ime2, kraji):
    ogLat, ogLon = koordinate(ime1, kraji)
    ogLat2, ogLon2 = koordinate(ime2, kraji)
    return razdalja_koordinat(ogLat, ogLon, ogLat2, ogLon2)


def v_dometu(ime, domet, kraji):
    mesta = []
    for a, b, c in kraji:
        z = razdalja(ime, a, kraji)
        if z <= domet and ime != a:
            mesta.append(a)
    return mesta


def najbolj_oddaljeni(ime, imena, kraji):
    maxR = 0
    maxI = ""
    for imei in imena:
        z = razdalja(ime, imei, kraji)
        if z >= maxR: maxR, maxI = z, imei
    return maxI


def zalijemo(ime, domet, kraji):
    maxR, maxI = 0, ""
    for imei in v_dometu(ime, domet, kraji):
        if maxR <= razdalja(ime, imei, kraji): maxR, maxI = razdalja(ime, imei, kraji), imei
    return maxI


def presek(s1, s2):
    return list(set(s1).intersection(s2))


def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))


# Tu pišite svoje funkcije:


