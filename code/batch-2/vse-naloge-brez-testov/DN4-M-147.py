# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return None

def razdalja(ime1, ime2, kraji):
    return None

def presek(s1, s2):
	return None
	
def skupno_zalivanje(ime1, ime2, domet, kraji):
	return ["Ljubljana", "Murska Sobota"]


def v_dometu(ime, domet, kraji):
    x_kraja_1=0
    y_kraja_1=0
    for terka in kraji:
        if(terka[0]==ime):
            x_kraja_1=terka[1]
            y_kraja_1=terka[2]

    seznam_krajev = []
    for terka in kraji:
        x_kraja_2 = terka[1]
        y_kraja_2 = terka[2]
        razdalja = sqrt((x_kraja_1 - x_kraja_2)**2+(y_kraja_1-y_kraja_2)**2)
        if(razdalja <= domet and terka[0]!=ime):
            seznam_krajev.append(terka[0])

    return seznam_krajev


def najbolj_oddaljeni(ime, imena, kraji):
    x_kraja_1 = 0
    y_kraja_1 = 0
    for terka in kraji:
        if (terka[0] == ime):
            x_kraja_1 = terka[1]
            y_kraja_1 = terka[2]

    najbolj_oddaljen=""
    razdalja_najbolj_oddaljenega=-1

    for terka in kraji:

        if(terka[0] in imena):
            x_kraja_2 = terka[1]
            y_kraja_2 = terka[2]

            razdalja = sqrt((x_kraja_1 - x_kraja_2)**2+(y_kraja_1-y_kraja_2)**2)

            if(razdalja > razdalja_najbolj_oddaljenega ):

                najbolj_oddaljen = terka[0]
                razdalja_najbolj_oddaljenega = razdalja

    return najbolj_oddaljen



def zalijemo(ime, domet, kraji):

    x_kraja_1 = 0
    y_kraja_1 = 0

    for terka in kraji:
        if (terka[0] == ime):
            x_kraja_1 = terka[1]
            y_kraja_1 = terka[2]

    najbolj_oddaljen=""
    razdalja_najbolj_oddaljenega=-1

    for terka in kraji:

        x_kraja_2 = terka[1]
        y_kraja_2 = terka[2]

        razdalja = sqrt((x_kraja_1 - x_kraja_2)**2+(y_kraja_1-y_kraja_2)**2)

        if(razdalja > razdalja_najbolj_oddaljenega and razdalja <= domet and terka[0]!=ime):

            najbolj_oddaljen = terka[0]
            razdalja_najbolj_oddaljenega = razdalja

    return najbolj_oddaljen


