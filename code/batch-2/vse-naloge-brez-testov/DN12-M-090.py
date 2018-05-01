########################
# Za oceno 6

def preberi(ime_datoteke): #vrne slovar {krožišče: [sosednja krožišča]}
    slovar = {}
    datoteka = open(ime_datoteke)
    i = 1
    for vrstica in datoteka:
        slovar[i] = [] #ustvari ključ s številko krožišča
        vrstica = vrstica.split(' ')
        for x in vrstica:
            slovar[i].append(int(x)) #in kot vrednost shrani sosednja krožišča
        for x in zip(slovar[i], slovar[i][1:]): #uredi vrednosti tako, da se vedno začne z najmanjšo številko
            if slovar[i][0] > slovar[i][1]:
                slovar[i] += [slovar[i].pop(0)]
        i += 1
    return slovar

def mozna_pot(pot, zemljevid): #vrne True, če je pot možno prevoziti
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1: #preveri, če sta začetna in končna točka ustrezni (imata le eno povezavo)
        return False
    i = 0
    prejsnji = pot[0]
    for ukaz in pot[1:]: #če je celotna pot pravilna
        if ukaz not in zemljevid[pot[i]]: #ali obstaja povezava med krožišči
            return False
        if ukaz == prejsnji: #če se nobeno krožišče ne ponovi
            return False
        if len(zemljevid[ukaz]) == 1 and ukaz != pot[-1]: #če je vmes kakšno končno krožišče (ne upoštevamo zadnjega)
            return False
        i += 1
        prejsnji = ukaz
    return True

def hamiltonova(pot, zemljevid): #vrne True, če je pot Hamiltonova (čez vsa krožišča natančno enkrat)
    if not mozna_pot(pot, zemljevid): #preveri, če je pot možna
        return False
    obiskani = []
    for ukaz in pot:
        if ukaz in obiskani: #če se krožišče ponovi
            return False
        if ukaz not in obiskani:
            obiskani.append(ukaz)
    st_krozisc = 2 #vhod/izhod
    for kljuc in zemljevid: #prešteje koliko krožišč je treba obiskati
        if len(zemljevid[kljuc]) != 1:
            st_krozisc += 1
    if len(obiskani) != st_krozisc: #in preveri, če jih res obišče toliko
        return False
    return True


########################
# Za oceno 7

def navodila(pot, zemljevid): #vrne navodila, kako prevoziti pot (izvozi)
    '''izvozi = []
    for prejsnji, trenutni, naslednji in zip(pot, pot[1:], pot[2:]): #glede na prejšnje in naslednje krožišče izračuna na kateri izvoz moramo na trenutnem krožišču
        izvozi.append((zemljevid[trenutni].index(naslednji) - zemljevid[trenutni].index(prejsnji)) % len(zemljevid[trenutni]))
    return izvozi'''
    return [(zemljevid[trenutni].index(naslednji) - zemljevid[trenutni].index(prejsnji)) % len(zemljevid[trenutni])
            for prejsnji, trenutni, naslednji in zip(pot, pot[1:], pot[2:])]


########################
# Za oceno 8

def prevozi(zacetek, navodila, zemljevid): #vrne zaporedje prevoženih krožišč (obratno od 7)
    pot = [zacetek]
    trenutno = zemljevid[zacetek][0]
    pot.append(trenutno) #pripnemo začetek in drugo krožišče
    for x in navodila:
        naslednje = (zemljevid[trenutno].index(zacetek) + x) % len(zemljevid[trenutno]) #izračunamo indeks naslednjega krožišča
        pot.append(zemljevid[trenutno][naslednje]) #in zabeležimo njegovo dejansko številko
        zacetek = trenutno
        trenutno = zemljevid[trenutno][naslednje]
    return pot


########################
# Za oceno 9

def sosedi(doslej, zemljevid): #vrne množico vseh sosednjih krožišč (razen njih samih)
    sosednja_krozisca = set()
    for x in doslej: #za vsako krožišče v doslej
        for krozisce in zemljevid[x]: #pogleda sosede
            if krozisce not in doslej: #če niso med doslej
                sosednja_krozisca.add(krozisce) #jih doda v množico
    return sosednja_krozisca

def razdalja(x, y, zemljevid): #vrne razdaljo med dvema krožiščema
    krozisca = {x}
    dolzina = 0
    while y not in krozisca: #dokler ne najdemo iskanega krožišča
        krozisca = sosedi(krozisca, zemljevid) #gledamo sosede od trenutnih (najprej samo sosede od x, potem sosede sosedov od x, itd.)
        dolzina += 1 #in večamo razdaljo do iskanega
    return dolzina


########################
# Za oceno 10

def najkrajsa_navodila(x, y, zemljevid): #vrne najkrajša navodila od x do y (izvozi)
    seznam = [] #seznam poti
    seznam.append([x]) #dodaj začetek
    while seznam:
        pot = seznam.pop(0) #poglej prvo pot iz seznama
        krozisce = pot[-1] #poglej zadnje krožišče iz poti
        if krozisce == y: #če je enako iskanemu, smo našli pravo pot
            #print(pot)
            return navodila(pot, zemljevid)
        for sosed in zemljevid.get(krozisce, []): #za vsako sosednje krožišče ustvari novo pot in jo pripne v seznam
            nova_pot = list(pot)
            nova_pot.append(sosed)
            seznam.append(nova_pot)
    #rešeno z algoritmom BFS (Breadth-First Search)


########################
#Testi (ne spreminjaj)

