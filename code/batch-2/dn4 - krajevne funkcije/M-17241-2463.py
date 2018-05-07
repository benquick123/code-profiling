from math import *

def koordinate(ime, kraji):
    a = 0
    b = 0
    for c in kraji:
        mesta, koordinata_a ,koordinata_b = c
        if ime == mesta:
            a = koordinata_a
            b = koordinata_b
            return a, b
        elif ime == None:
            return None

def razdalja_koordinat(a1, b1, a2, b2):
    oddaljenost = sqrt(pow(a2 - a1, 2) + pow(b2 - b1, 2))
    return oddaljenost

def razdalja(kraj_a, kraj_b, kraji):
    a1, b1 = koordinate(kraj_a, kraji)
    a2, b2 = koordinate(kraj_b, kraji)
    return razdalja_koordinat(a1, b1, a2, b2)

def v_dometu(ime, domet, kraji):
    kraj1, kraj2 = koordinate(ime, kraji)
    zadeni_mesto = []
    for x in kraji:
        kraj, a2, b2 = x
        razdalja = razdalja_koordinat(kraj1, kraj2, a2, b2)
        if domet >= razdalja and kraj != ime:
            zadeni_mesto.append(kraj)
    return zadeni_mesto

def najbolj_oddaljeni(ime, vasi, kraji):
    dolzina = []
    a1, b1 = koordinate(ime, kraji)
    razdalja = 0
    for e in kraji:
        ime_kraja, x_koordinata, y_koordinata = e
        if ime == ime_kraja:
            x = x_koordinata
            y = y_koordinata

    daljava = 0
    for o in vasi:
        for y in kraji:
            mesto_b = o
            ime_kraja, a, b = y
            if ime_kraja == mesto_b:
                ime_a = a
                ime_b = b
                razdalja = sqrt(pow(ime_a - a1, 2) + pow(ime_b - b1, 2))
                dolzina.append([(razdalja), (mesto_b)])

    vrni = 0
    for g in dolzina:
        razdalja, mesto_b = g
        if razdalja > daljava:
            daljava = razdalja
            vrni = mesto_b
    return vrni

def zalijemo(ime, doseg, kraji):
    dolzina = 0
    naj_dolzina = 0
    zadeto_mesto = ""
    ime_a, ime_b = koordinate(ime, kraji)
    for kraj, a, b in kraji:
        dolzina = razdalja_koordinat(ime_a, ime_b, a, b)
        if doseg > dolzina > naj_dolzina:
            naj_dolzina = dolzina
            zadeto_mesto = kraj
    return zadeto_mesto

