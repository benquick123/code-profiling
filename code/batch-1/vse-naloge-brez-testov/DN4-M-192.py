# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):
    for name, x, y in kraji:
        if name == ime:
            return x, y

    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def razdalja(ime1, ime2, kraji):
    coords1 = koordinate(ime1, kraji)
    coords2 = koordinate(ime2, kraji)

    if coords1 is None or coords2 is None:
        return None

    return razdalja_koordinat(coords1[0], coords1[1], coords2[0], coords2[1])

def v_dometu(ime, domet, kraji):
    coords = koordinate(ime, kraji)

    places_in_range = []
    for name, x, y in kraji:
        if name == ime:
            continue
        range = razdalja_koordinat(coords[0], coords[1], x, y)
        if range <= domet:
            places_in_range.append(name)

    return places_in_range

def najbolj_oddaljeni(ime, imena, kraji):
    biggest_distance = -1
    furthest_place = ""
    for name in imena:
        distance = razdalja(ime, name, kraji)
        if distance > biggest_distance:
            biggest_distance = distance
            furthest_place = name

    return furthest_place

def zalijemo(ime, domet, kraji):
    coords = koordinate(ime, kraji)

    biggest_distance = -1
    furthest_place = ""
    for name, x, y in kraji:
        distance = razdalja_koordinat(coords[0], coords[1], x, y)
        if distance <= domet and distance >= biggest_distance:
            biggest_distance = distance
            furthest_place = name

    return furthest_place

def presek(s1, s2):
    intersect = []

    for value1 in s1:
        found = False
        i = 0
        while i < len(s2) and not found:
            if value1 == s2[i]:
                intersect.append(value1)
                found = True
            i += 1

    return intersect

def skupno_zalivanje(ime1, ime2, domet, kraji):
    places1 = v_dometu(ime1, domet, kraji)
    places2 = v_dometu(ime2, domet, kraji)

    return presek(places1, places2)

