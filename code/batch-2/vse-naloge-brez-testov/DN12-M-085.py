def minimum(seznam): # dodatna funkcija
    vrednost=min(seznam) # potrebujemo najmanjso vrednost v seznami
    prazen_seznam=[] # potrebujemo prazen seznam za shranjevanje
    index=seznam.index(vrednost) # potrebujemo index tistega minimuma da izpišemo use kar je po in pred
    prazen_seznam.append(vrednost) # na prvo mesto v serznam pripnemo minimum
    for element in seznam[index+1:]: # potem izpišemo vse kar je po njemu, vendar prištejemo 1 ker minimum smo že izpisali
        prazen_seznam.append(element)
    for element in seznam[:index]:# izpišemo še vse pred minimumom
        prazen_seznam.append(element)
    return prazen_seznam # returnamo seznam


import collections # potrebujemo defaultdict!!!!!!


def preberi(ime_datoteke):
    stevilo= 1 #stevilo mi bo sluzilo kot ključ v seznamu
    datoteka=open(ime_datoteke) # najprej zmeraj odpri datoteko!
    slovar = collections.defaultdict(list) # delno prazen slovar za shranjevanje
    for vrstica in datoteka: # za vsako vrsto v datoteko
        seznam=list() # prazen slovar
        for element in vrstica.split(): # vsako vrstico še splitam za posamezen element
            seznam.append(int(element))
        slovar[stevilo]=minimum(seznam) # kličemo funkcijo minimuma za preureditev seznama
        stevilo=stevilo +1  # stevilo povecamo za 1 torej naslednje krizisce
    datoteka.close() # datoteko zapri zmeraj na konci!!!!!!!!
    print(datoteka) # testen print
    return slovar #izpišemo slovar


def mozna_pot(pot, zemljevid):
    prvi_element=pot[0] # če ni prvi ali zadnji element v poti končna povezava potem pot ni mozna
    zadnji_element= pot[-1]
    for element in zemljevid: # za vsak element v zemljevidu
        if element==prvi_element: #če je element enak prvemu
            dolzina=len(zemljevid[element]) # najdemo dolžino tega krožišča (število povezav)
            if dolzina> 1: # če je 1 potem je končna povezava
                return False
        if element== zadnji_element: # enako storimo še za zadnji element
            dolzina=len(zemljevid[element])
            if dolzina>1:  # če je 1 potem je končna povezava
                return False

    pot_brez_prvega_in_zadnjega=[] # sem  bom kopiral seznam pot
    for element in pot:
        pot_brez_prvega_in_zadnjega.append(element) #nov seznam pot

    del pot_brez_prvega_in_zadnjega[0] # zbrišemo prvi in zadnji element da nam ne preverja začetne in končne povezave
    del pot_brez_prvega_in_zadnjega[-1]
    for povezava in pot_brez_prvega_in_zadnjega: #za vsako povezavo v novem seznamu poti
        for krozisce in zemljevid: #za vsako krozisce v zemljevidu
            if povezava==krozisce: # preverimo če je element poti enak kroziscu
                dolzina=len(zemljevid[krozisce]) #izracunamo dolzino krizisca
                if dolzina==1: # če je končna povezava(dolzina enaka 1) potem ni mozna pot
                    return False

    for element in pot: #preverimo če je naslednji element enak naslednjemu
        if element != pot[-1]: # nesme it preko seznamoa
            tocka=pot.index(element) # dobimo index prve točke
            naslednja_tocka=tocka+1 # in indeks naslednje točke
            if pot[tocka]==pot[naslednja_tocka]: # če sta enaki, vrne false
                return False

    dolzina= len(pot) -1 # ker števec gre od 1 dalje, index pa od 0

    for stevec in range(dolzina): # za vsak števec v range od 0 dalje
        if pot[stevec+1] not in zemljevid[pot[stevec]]: # če je naslednji element potem je pravilno zato števec + 1
            return False
    return True # če prej ne vrne false, potem je pravilno.

def hamiltonova(pot,zemljevid):
    vrednost=0 # vrednosti, koliko je krajišč oz križišč z eno povezavo
    if mozna_pot(pot, zemljevid)==True: #če je pot možna gremo naprej
        dolzina_poti=len(pot) # izračunam dolžino poti
        dolzina_zemljevida=len(zemljevid) # izračunam dolžino zemljevida
        for element in zemljevid: #za vsak element v zemljevidu
            dolzina=len(zemljevid[element]) #izračunamo dolžino tega korzisca, če je enaka ena, saj iščemo začetek
            if dolzina==1: # če je enak ena
                vrednost=vrednost +1 #prištejemo vrednosti
        nova_vrednost= vrednost - 2 #odštejemo dva, ker potrebujemo začetek in konec
        if dolzina_poti== dolzina_zemljevida - nova_vrednost: #ostanek  odštejemo od dolžine zemljevida
            return True
    else:
        return False
