from math import *
#KOORDINATE:
def koordinate(ime, kraji):
    kraj = ime
    for ime, x, y in kraji:
        if kraj == ime:
            return (x, y)
    else:
        return None



#RAZDALJA KOORDINAT:
def razdalja_koordinat(x1, y1, x2, y2):
    r = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return (r)



#RAZDALJA:
def razdalja(ime1, ime2, kraji):
    k1 = koordinate (ime1, kraji)
    k2 = koordinate(ime2, kraji)
    r = razdalja_koordinat(k1[0], k1[1],  k2[0], k2[1])
    return (r)
    print (r)



#V DOMETU:
def v_dometu(ime, domet, kraji):
    sez = []
    kraj = ime
    for ime, x, y in kraji:
        if ime == kraj:
            ime1 = ime
            x1 = x
            y1 = y

    for ime, x, y in kraji:
        dlon = y - y1
        dlat = x - x1
        d= sqrt((dlat**2)+(dlon**2))
        if d <= domet and ime1 != ime:
            sez.append(ime)
    return (sez)



#NAJBOLJ_ODDALJENI:
def najbolj_oddaljeni(ime, imena, kraji):
    kraj = ime
    d1 = 0
    for ime, x, y in kraji:
        if ime == kraj:
            ime1 = ime
            x1 = x
            y1 = y

    for ime4 in imena:
        for ime, x, y in kraji:
            if ime4 == ime:
                dlon = y - y1
                dlat = x - x1
                d= sqrt((dlat**2)+(dlon**2))
                if d > d1:
                    ime2 = ime
                    x2 = x
                    y2 = y
                    d1 = d
    return (ime2)



#ZALIJEMO:
def zalijemo (ime, domet, kraji):
    kraj = ime
    d1 = 0
    for ime, x, y in kraji:
        if ime == kraj:
            ime1 = ime
            x1 = x
            y1 = y

    for ime, x, y in kraji:
        dlon = y - y1
        dlat = x - x1
        d= sqrt((dlat**2)+(dlon**2))
        if d1 < d and d < domet:
            ime2 = ime
            x2 = x
            y2 = y
            d1 = d
    return (ime2)


#TESTI:


