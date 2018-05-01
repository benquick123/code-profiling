# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):

    # for i in range(len(kraji)):
    #     if kraji[i][0] == ime:
    #         return (kraji[i][1], kraji[i][2])
    # Ne razumem popolnoma, zakaj ta del kode faila v ko se požene drugi test za to funkcijo.
    # Je to zaradi tega, ker je array poslan v funkcijo znotraj objekta 'NoGetItem'

    for kraj in kraji:
        if(kraj[0] == ime):
            return (kraj[1], kraj[2])
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def razdalja(ime1, ime2, kraji):
    mesto1 = koordinate(ime1, kraji)
    mesto2 = koordinate(ime2, kraji)
    return razdalja_koordinat(mesto1[0], mesto1[1], mesto2[0], mesto2[1])

def v_dometu(ime, domet, kraji):
    for i in range(len(kraji)):
        if kraji[i][0] == ime:
            x1 = kraji[i][1]
            y1 = kraji[i][2]
            break

    kraji_v_dometu = []
    for i in range(len(kraji)):
        x2 = kraji[i][1]
        y2 = kraji[i][2]
        razdalja = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        if razdalja <= domet and razdalja != 0:
            kraji_v_dometu.append(kraji[i][0])

    return kraji_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    maxRazdalja = -1000
    maxKraj     = imena[0]

    for i in range(len(kraji)):
        if kraji[i][0] == ime:
            x1 = kraji[i][1]
            y1 = kraji[i][2]
            break

    for i in range(len(kraji)):
        if kraji[i][0] in imena:
            x2 = kraji[i][1]
            y2 = kraji[i][2]
            razdalja = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
            if razdalja > maxRazdalja:
                maxRazdalja = razdalja
                maxKraj     = kraji[i][0]
    return maxKraj

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

def presek(s1, s2):
    skupni = []

    if len(s1) > len(s2):
        for i in range(len(s1)):
            if s1[i] in s2:
                skupni.append(s1[i])
    else:
        for i in range(len(s2)):
            if s2[i] in s1:
                skupni.append(s2[i])

    return skupni

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)

