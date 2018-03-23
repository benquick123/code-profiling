__author__ = 'Dolores'
# Tu pišite svoje funkcije:

def koordinate(ime, kraji):
    koordinata = None
    for i in kraji:
        if i[0]==ime:
            koordinata=(i[1],i[2])
    return koordinata

def razdalja_koordinat(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5 #**0.5 je isto kot koren

def razdalja(ime1, ime2, kraji):
    koord1 = koordinate(ime1, kraji)
    koord2 = koordinate(ime2, kraji)
    return razdalja_koordinat(koord1[0], koord1[1], koord2[0], koord2[1])

def v_dometu(ime, domet, kraji):
    seznam=[]
    for i in kraji:
        if (razdalja(ime, i[0], kraji) <= domet) & (ime != i[0]): #Pogoj (ime != i[0]) preveri, da kraj ne meri razdalje do sebe
            seznam.append(i[0])
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    kraj = ""
    maxrazdalja = 0
    for i in imena:
        if razdalja(ime, i, kraji) > maxrazdalja:
            maxrazdalja = razdalja(ime, i, kraji)
            kraj = i
    return kraj

def zalijemo(ime, domet, kraji):
    vdometu = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, vdometu, kraji)

def presek(s1, s2):
    presek=[]
    for i in s1:
        if i in s2:
            presek.append(i)
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1 = v_dometu(ime1, domet, kraji)
    seznam2 = v_dometu(ime2, domet, kraji)
    return presek(seznam1, seznam2)







