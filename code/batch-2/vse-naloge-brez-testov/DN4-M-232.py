# Tu pišite svoje funkcije:
import math
def koordinate(ime, kraji): #vrne koordinate kraja
    for mesto,x,y in kraji:
        if ime == mesto:
            return x,y

def razdalja_koordinat(x1,y1,x2,y2): # vrne razdaljo med točkama
    r = math.sqrt(((x2-x1)**2)+(y2-y1)**2)
    return r

def razdalja(ime1, ime2, kraji): #vrne razdaljo med krajema (z uporabo privih dveh funkcij)
    x1, y1 =koordinate(ime1,kraji) #pokliče funkcijo ter pridobi koordinate,
    x2, y2= koordinate(ime2,kraji) #ki se shranijo v x1,y1 in x2,y2.
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji): #vrne kraje, ki so v dometu(brez samega sebe)
    s = []
    novo = 0
    for mesto, x, y in kraji:
        if razdalja(ime, mesto, kraji) <= domet and razdalja(ime, mesto, kraji) > 0:
            novo = mesto #v "novo" shrani imena mest, ki so v dometu
            s.append(novo) #dodajanje prej shranjenih mest v seznam s
    return s               #vrne seznam mest

def najbolj_oddaljeni(ime, imena, kraji): #vrne najbolj oddaljen kraj iz seznama "imena"
    raz2 = 0
    for mesto, x, y in kraji: #sprehod skozi seznam "kraji"
        for name in imena: #sprehod skozi PODAN seznam "imena"
            if mesto == name:
                raz = razdalja(ime, name, kraji) #če se ujemata zračuna razdaljo
                if raz > raz2: #pogleda katero je največjo
                    name2 = name   #ime najbolj oddaljenega mesta shrani v "name2"
                    raz2 = raz #prav tako razdaljo v "raz2"
    return name2

def zalijemo(ime, domet, kraji):
    dom = v_dometu(ime, domet, kraji)
    naj = najbolj_oddaljeni(ime, dom, kraji)
    return naj
    #raz2 = 0
    #for mesto,x,y in kraji: #sprehod skos vse kraje is seznama
        #raz = razdalja(ime, mesto, kraji) #izračun razdalj vseh krajev od "ime"
        #if raz < domet: #pogoj da je razdalja manjša od dometa
            #if raz > raz2: #preverimo kateri je najbolj oddaljen vendar v dometu
                #mesto2 = mesto #"mesto2" priredimo ime najbolj odddaljenega mesta v dometu
                #raz2 = raz #ko dobimo največjo razdaljo jo priredimo "raz2"
    #return mesto2

def presek(s1,s2): #vrne elemente, ki se nahajajo v obeh seznamih,
    return list(set(s1).intersection(set(s2))) #vrstni red ni pomemben, velikost je lahko različna

