# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for mesto, x, y in kraji:
        if ime == mesto:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + ( y1 - y2)**2)

def razdalja(ime1, ime2, kraji): #brez presledka po menu
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja_ab = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja_ab


def v_dometu(ime, domet, kraji):
    seznam_krajev = [] #vnesti je potrebno navodilo za izpis seznama-prazen...zaenkrat
    for mesto, x, y in kraji:
        razdalja12 = razdalja(ime, mesto, kraji)
        if 0 < razdalja12 <= domet:
            seznam_krajev.append(mesto)
    return seznam_krajev

def najbolj_oddaljeni(ime, imena, kraji):
    najvecja_razdalja = 0
    daleko_mesto = ""
    for kraj in imena:
        r = razdalja(ime, kraj, kraji)
        if r > najvecja_razdalja:
            najvecja_razdalja = r
            daleko_mesto = kraj
    return daleko_mesto
def zalijemo (ime, domet, kraji):
    najdaljsi_domet = 0
    oddaljeno_mesto = ""
    for mestokraj in kraji:
        r= razdalja (ime, mestokraj, kraji)
        if r > najdaljsi_domet > domet:
            najdaljsi_domet= domet
            oddaljeno_mesto = mestokraj
    return oddaljeno_mesto


