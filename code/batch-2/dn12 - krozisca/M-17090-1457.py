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

import unittest
from random import randint
import os

class Test06(unittest.TestCase):
    maxDiff = 100000

    def test_01_preberi(self):
        self.assertEqual(
            preberi("zemljevid.txt"),
            {1: [3],
             2: [4],
             3: [1, 8, 7, 6, 4],
             4: [2, 3, 6, 5],
             5: [4, 11, 10],
             6: [3, 11, 4],
             7: [3, 8, 11],
             8: [3, 16, 9, 7],
             9: [8, 16, 14, 11],
             10: [5, 11, 13],
             11: [5, 6, 7, 9, 14, 10],
             12: [13],
             13: [10, 14, 12],
             14: [9, 16, 13, 11],
             15: [16],
             16: [8, 15, 14, 9]})

        fname = "z{:05}.bla".format(randint(10000, 99999))
        with open(fname, "w") as f:
            f.write("2\n3 1\n2")
        try:
            self.assertEqual(preberi(fname), {1:[2], 2: [1, 3], 3: [2]})
        finally:
            try:
                os.remove(fname)
            except:
                print("Ne morem pobrisati {}. (Je na Dropboxu?) Briši sam(a).".format(fname))

    def test_02_mozna_pot(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 2], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 2][::-1], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 5, 4, 3, 1], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 5, 4, 3, 1][::-1], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 8, 16, 15], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 8, 16, 15][::-1], zemljevid))
        self.assertTrue(mozna_pot([15, 16, 15], zemljevid))

        # Ne začne/konča se na vhodih/izhodih
        self.assertFalse(mozna_pot([1, 3, 7, 11, 14, 16], zemljevid))
        self.assertFalse(mozna_pot([3, 7, 11, 14, 16, 15], zemljevid))

        # Vmes gre ven
        self.assertFalse(mozna_pot([1, 3, 6, 4, 2, 4, 5, 11, 14, 13, 12], zemljevid))
        self.assertFalse(mozna_pot([1, 3, 6, 4, 2, 2, 4, 5, 11, 14, 13, 12], zemljevid))

        # Ponovi eno križišče
        self.assertFalse(mozna_pot([1, 3, 8, 8, 16, 15], zemljevid))

        # Ni povezave
        self.assertFalse(mozna_pot([1, 3, 16, 15], zemljevid))
        self.assertFalse(mozna_pot([1, 15], zemljevid))

        zemljevid2 = {1: [2], 2: [1, 3], 3: [2]}
        self.assertTrue(mozna_pot([1, 2, 3], zemljevid2))
        self.assertFalse(mozna_pot([1, 3], zemljevid2))

        zemljevid2 = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        self.assertTrue(mozna_pot([1, 2, 3, 4], zemljevid2))
        self.assertTrue(mozna_pot([4, 3, 2, 1], zemljevid2))
        self.assertFalse(mozna_pot([1, 3, 4], zemljevid2))
        self.assertFalse(mozna_pot([1, 4], zemljevid2))

    def test_03_hamiltonova(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertTrue(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))
        self.assertTrue(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12][::-1], zemljevid))

        # Ena manjka
        self.assertFalse(hamiltonova([1, 3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))

        # Ni začetka/konca
        self.assertFalse(hamiltonova([3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))
        self.assertFalse(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13], zemljevid))

        # Ponavljenje
        self.assertFalse(hamiltonova([1, 3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 11, 14, 13, 12], zemljevid))
        self.assertFalse(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 3, 4, 5, 10, 13, 12], zemljevid))

        zemljevid2 = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        self.assertTrue(hamiltonova([1, 2, 3, 4], zemljevid2))
        self.assertTrue(hamiltonova([4, 3, 2, 1], zemljevid2))
        self.assertFalse(hamiltonova([1, 2, 4], zemljevid2))


class Test07(unittest.TestCase):
    maxDiff = 100000

    def test_01_navodila(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(navodila([1, 3, 8, 16, 15], zemljevid), [1, 1, 1])
        self.assertEqual(navodila([1, 3, 6, 4, 2], zemljevid), [3, 2, 2])
        self.assertEqual(navodila([1, 3, 6, 11, 14, 16, 15], zemljevid), [3, 1, 3, 2, 3])
        self.assertEqual(navodila([12, 13, 14, 11, 9, 8, 7, 3, 4, 2], zemljevid), [2, 1, 5, 1, 1, 2, 2, 3])
        self.assertEqual(navodila([2, 4, 2], zemljevid), [0])
        self.assertEqual(navodila([15, 16, 14, 11, 9, 16, 14, 11, 9, 16, 15], zemljevid), [1, 2, 5, 2, 3, 2, 5, 2, 2])


class Test08(unittest.TestCase):
    maxDiff = 100000

    def test_01_prevozi(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(prevozi(1, [1, 1, 1], zemljevid), [1, 3, 8, 16, 15])
        self.assertEqual(prevozi(1, [3, 2, 2], zemljevid), [1, 3, 6, 4, 2])
        self.assertEqual(prevozi(1, [3, 1, 3, 2, 3], zemljevid), [1, 3, 6, 11, 14, 16, 15])
        self.assertEqual(prevozi(12, [2, 1, 5, 1, 1, 2, 2, 3], zemljevid), [12, 13, 14, 11, 9, 8, 7, 3, 4, 2])
        self.assertEqual(prevozi(2, [0], zemljevid), [2, 4, 2])
        self.assertEqual(prevozi(15, [1, 2, 5, 2, 3, 2, 5, 2, 2], zemljevid), [15, 16, 14, 11, 9, 16, 14, 11, 9, 16, 15])

class Test09(unittest.TestCase):
    maxDiff = 100000

    def test_01_sosedi(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(sosedi({15}, zemljevid), {16})
        self.assertEqual(sosedi({15, 16}, zemljevid), {14, 9, 8})
        self.assertEqual(sosedi({15, 16, 14, 9, 8}, zemljevid), {3, 7, 11, 13})
        self.assertEqual(sosedi({15, 16, 14, 9, 8, 3, 7, 11, 13}, zemljevid), {1, 4, 6, 5, 10, 12})
        self.assertEqual(sosedi({15, 16, 14, 9, 8, 3, 7, 11, 13, 1, 4, 6, 5, 10, 12}, zemljevid), {2})
        self.assertEqual(sosedi({15, 16, 14, 9, 8, 3, 7, 11, 13, 1, 4, 6, 5, 10, 12, 2}, zemljevid), set())

        self.assertEqual(sosedi({6}, zemljevid), {4, 3, 11})
        self.assertEqual(sosedi({6, 4, 3, 11}, zemljevid), {2, 5, 1, 7, 8, 9, 14, 10})

    def test_02_razdalja(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(razdalja(15, 16, zemljevid), 1)

        self.assertEqual(razdalja(15, 14, zemljevid), 2)
        self.assertEqual(razdalja(15, 9, zemljevid), 2)
        self.assertEqual(razdalja(15, 8, zemljevid), 2)

        self.assertEqual(razdalja(15, 7, zemljevid), 3)
        self.assertEqual(razdalja(15, 13, zemljevid), 3)

        self.assertEqual(razdalja(15, 5, zemljevid), 4)
        self.assertEqual(razdalja(15, 10, zemljevid), 4)

        self.assertEqual(razdalja(15, 2, zemljevid), 5)

        self.assertEqual(razdalja(6, 4, zemljevid), 1)
        self.assertEqual(razdalja(6, 5, zemljevid), 2)
        self.assertEqual(razdalja(6, 10, zemljevid), 2)
        self.assertEqual(razdalja(6, 13, zemljevid), 3)
        self.assertEqual(razdalja(6, 12, zemljevid), 4)


class Test10(unittest.TestCase):
    maxDiff = 100000

    def test_01_najkrajsa_pot(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(najkrajsa_navodila(1, 15, zemljevid), [1, 1, 1])
        self.assertEqual(najkrajsa_navodila(1, 2, zemljevid), [4, 3])
        self.assertEqual(najkrajsa_navodila(2, 15, zemljevid), [1, 2, 1, 1])
        self.assertEqual(najkrajsa_navodila(2, 12, zemljevid), [3, 2, 2, 2])
        self.assertEqual(najkrajsa_navodila(15, 12, zemljevid), [1, 1, 1])

        self.assertEqual(najkrajsa_navodila(15, 1, zemljevid), [3, 3, 4])
        self.assertEqual(najkrajsa_navodila(2, 1, zemljevid), [1, 1])
        self.assertEqual(najkrajsa_navodila(15, 2, zemljevid), [3, 3, 3, 3])
        self.assertEqual(najkrajsa_navodila(12, 2, zemljevid), [1, 1, 1, 1])
        self.assertEqual(najkrajsa_navodila(12, 15, zemljevid), [2, 3, 3])

        navodila = najkrajsa_navodila(1, 12, zemljevid)
        self.assertEqual(len(navodila), 5)
        self.assertEqual(prevozi(1, navodila, zemljevid)[-1], 12)

        navodila = najkrajsa_navodila(12, 1, zemljevid)
        self.assertEqual(len(navodila), 5)
        self.assertEqual(prevozi(12, navodila, zemljevid)[-1], 1)


if __name__ == "__main__":
    unittest.main()
