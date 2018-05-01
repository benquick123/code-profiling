# Tu pišite svoje funkcije:
from math import *

def v_dometu(ime,domet,kraji):
    x1 = 0
    y1 = 0

    seznam_krajev = []

    for kra in kraji:
        ime, x, y = kra

        if ime == ime:    #dobi koordinate vpisanga mesta
            x1 = x
            y1 = y

    for Vsi_kraji in kraji:
        ime_kraja, x, y = Vsi_kraji


        razdalja = sqrt((x - x1) ** 2 + (y - y1) ** 2)   #računa razdaljo

        if (razdalja < int(domet)):     #primerja domet z razdaljo
            terka = (ime_kraja)
            seznam_krajev.append(terka)

    return(seznam_krajev)

def zalijemo(ime,domet,kraji):
    Najdaljsa_mozna_razdalja = 0
    ciljni_kraj = ""

    y1 = 0
    x1 = 0

    for kra in kraji:
        kraj, x, y = kra

        if ime == kraj:
            x1 = x
            y1 = y

    for racun in kraji:
        ime, x, y = racun
        razdalja = sqrt((x - x1) ** 2 + (y - y1) ** 2)

        if (razdalja < int(domet)):
            if (razdalja > Najdaljsa_mozna_razdalja):
                Najdaljsa_mozna_razdalja = razdalja
                ciljni_kraj = ime
    return (ciljni_kraj)

def najbolj_oddaljeni(ime, domet, kraji):
    x1 = 0
    y1 = 0
    razdalja = 0
    seznam_krajev = []
    Najdaljsa_razdalja = 0
    oddaljeno_mesto = ""

    for kra in kraji:
        ime, x, y = kra

        if ime == ime:          #dobi koordinate vpisanga mesta
            x1 = x
            y1 = y

    for kraji_domet in domet:      #gre čez seznam domet
        ime_kraja = kraji_domet

        for kraj in kraji:        #gre čez seznam kraji
            ime_kraj, x, y = kraj

            if ime_kraj == ime_kraja:        #primerja domet s kraji
                razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

                if razdalja > Najdaljsa_razdalja:     #primerja največje razdalje in shrani
                    Najdaljsa_razdalja = razdalja
                    oddaljeno_mesto = ime_kraj
    return (oddaljeno_mesto)



