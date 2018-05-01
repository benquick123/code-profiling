
from math import sqrt

##############################OGREVALNI DEL#############################

def koordinate(ime, kraji):
    ret = None
    for ime1, x, y in kraji:
        if ime1 == ime:
            ret = (x, y)
            return ret

def razdalja_koordinat(x1, y1, x2, y2):
    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    distance = razdalja_koordinat(x1, y1, x2, y2)
    return distance

##############################OBVEZNI DEL################################

def v_dometu(ime, domet, kraji):
    x = []
    for name1, x1, y1 in kraji:
        if name1 == ime:
            for name2, x2, y2 in kraji:
                distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if 0 < distance <= domet:
                    x.append(name2)
    return x

def najbolj_oddaljeni(ime, imena, kraji):
    distancemax = 0
    distancemaxtown = ""
    for kraj1, x1, y1 in kraji:
        if ime == kraj1:
            for x in imena:
                for kraj2, x2, y2 in kraji:
                    if x == kraj2:
                        distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        if distance > distancemax:
                            distancemax = distance
                            distancemaxtown = kraj2
    return distancemaxtown

def zalijemo(ime, domet, kraji):
    maxdistance = 0
    maxkraj = ""
    for ime1, x1, y1 in kraji:
        if ime == ime1:
            for ime2, x2, y2 in kraji:
                distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if domet > distance > maxdistance:
                    maxdistance = distance
                    maxkraj = ime2
    return maxkraj

##############################DODATNI DEL################################

def presek(s1, s2):
    presek = []
    for x in s1:
        for y in s2:
            if x == y:
                presek.append(x)
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    x = []
    y = []
    skupaj = []
    for kraj1, x1, y1 in kraji:
        if kraj1 == ime1:
            for kraj2, x2, y2 in kraji:
                distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if domet > distance > 0:
                    x.append(kraj2)
            break
    for kraj1, x1, y1 in kraji:
        if kraj1 == ime2:
            for kraj2, x2, y2 in kraji:
                distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if domet > distance > 0:
                    y.append(kraj2)
            break
    for element in x:
        for element2 in y:
            if element == element2:
                skupaj.append(element)
    return skupaj

