from math import *
# Tu pišite svoje funkcije:

# Ogrevalna funkcija 1

def koordinate(ime, kraji):
    for mesto, x, y in kraji:
        if mesto == ime:
            t = (x,y)
            break
    else:
        t = None
    return t

# Ogrevalna funkcija 2:

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return razdalja

# Ogrevalna funkcija 3:

def razdalja(ime1,ime2,kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    razdalja_kraji = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja_kraji

# Obvezni del 1:

def v_dometu(ime, domet, kraji):
    seznam_krajev = []
    for kraj, x, y in kraji:
        razdalja_krajev = razdalja(ime,kraj, kraji)
        if razdalja_krajev <= domet and kraj != ime:
            seznam_krajev.append(kraj)
    return seznam_krajev

# Obvezni del 2:
'''
najbolj_oddaljeni(ime, imena, kraji) prejme ime nekega kraja, seznam imen nekih krajev (imena) in
že običajni seznam terk z imeni in koordinatami krajev.
Med kraji v seznamu imena (ne med vsemi kraji, temveč samo med temi!) mora vrniti ime tistega, ki je najbolj oddaljen od kraja ime. 
Če recimo, pokličemo najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji), 
kjer so kraji vsi kraji iz prejšnje naloge, vrne "Maribor", saj je Maribor med temi štirimi kraji najdalj od Ljubljane
'''
def najbolj_oddaljeni(ime, imena, kraji):
    naj_oddaljen = 0
    naj_kraj = ""
    for kraj in imena:
        naj_razdalja = razdalja(ime, kraj, kraji)
        if naj_razdalja > naj_oddaljen:
            naj_oddaljen = naj_razdalja
            naj_kraj = kraj
    return naj_kraj

# Obvezni del 3:

def zalijemo(ime, domet, kraji):
    naj_oddaljen = 0
    for kraj, x, y in kraji:
        razdalja_med = razdalja(ime, kraj, kraji)
        if razdalja_med <= domet and razdalja_med > naj_oddaljen:
            naj_kraj = kraj
            naj_oddaljen = razdalja_med
    return naj_kraj



