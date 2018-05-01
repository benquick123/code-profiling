# Tu pišite svoje funkcije:
import math

max_domet = 30

def koordinate(kraj, kraji):
    for seznam_kraji in kraji:
        if kraj == seznam_kraji[0]:
            x1 = seznam_kraji[1]
            y1 = seznam_kraji[2]
            return x1, y1
    
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = math.sqrt((math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2)))
    return razdalja

def razdalja(ime1, ime2, kraji):
    kraj_1 = koordinate(ime1, kraji)
    kraj_2 = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj_1[0], kraj_1[1], kraj_2[0], kraj_2[1]) 

def v_dometu(ime1, domet, kraji):
    kraji_v_dometu = []
    for seznam_kraji in kraji:
        if razdalja(ime1, seznam_kraji[0], kraji) <= domet and  ime1 != seznam_kraji[0]:
            kraji_v_dometu.append(seznam_kraji[0] )
        else:
            pass
    return kraji_v_dometu

def najbolj_oddaljeni(ime1, imena, kraji):
    x1, y1 = koordinate(ime1, kraji)
    najbolj_oddaljen_kraj = ""
    najdaljsa_razdalja = 0
    for seznam_kraji in kraji:
        if seznam_kraji[0] in imena:
            razdalja = razdalja_koordinat(x1, y1, seznam_kraji[1], seznam_kraji[2])
            if najdaljsa_razdalja <= razdalja:
                najdaljsa_razdalja = razdalja
                najbolj_oddaljen_kraj = seznam_kraji[0]
    return najbolj_oddaljen_kraj

def zalijemo(ime1, domet, kraji):
    return najbolj_oddaljeni(ime1, v_dometu(ime1, domet, kraji), kraji)

def presek(s1, s2):
    presek = []
    for i in range(0, len(s1)):
        if s1[i] in s2: 
            presek.append(s1[i])
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))

