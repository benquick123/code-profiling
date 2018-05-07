import collections

def preobrni_iz_prejsnjega(s, preobrni_v):
    seznam = s
    stevec = 0
    while seznam[0] != preobrni_v:
        trenutni = seznam[0]
        if trenutni == preobrni_v:
            break
        else:
            del seznam[0]
            seznam.append(trenutni)
            stevec += 1
    return seznam, stevec

def preobrni_od_do(s, start, end):
    seznam = preobrni_iz_prejsnjega(s, start)[0]
    return preobrni_iz_prejsnjega(seznam, end)

def preobrni_n_krat(s, kolikokrat):
    seznam1 = s
    stevec = 0
    while stevec != kolikokrat:
        trenutni = seznam1[0]
        del seznam1[0]
        seznam1.append(trenutni)
        stevec += 1
    return seznam1

def preobrni_min(s):
    return preobrni_iz_prejsnjega(s, min(s))[0]
    """seznam = s
    najmanjsa = min(s)
    while seznam[0] != najmanjsa:
        trenutni = seznam[0]
        if trenutni == najmanjsa:
            break
        else:
            del seznam[0]
            seznam.append(trenutni)
    return seznam"""

def preberi(ime_datoteke):
    file = open(ime_datoteke)
    datoteka = file.read()
    vrstice = datoteka.splitlines()
    zemljevid = collections.defaultdict(list)
    for i, vrstica in enumerate(vrstice):
        seznam_stevilk = vrstica.split()
        for e in seznam_stevilk:
            zemljevid[i+1].append(int(e))
        zemljevid[i+1] = preobrni_min(zemljevid[i + 1])
    return zemljevid

def koncna(del_poti, zemljevid):
    if len(zemljevid[del_poti]) < 2:
        return True
    return False

def mozna_pot(pot, zemljevid):
    if koncna(pot[0], zemljevid) and koncna(pot[-1], zemljevid):
        for index, (prvi, drugi) in enumerate(zip(pot, pot[1:])):
            if index != 0 and index != len(pot) - 1 and koncna(prvi, zemljevid):  # če ni prvi ali pa zadnji element v seznamu, potem preveri, če je pot končna
                return False
            if drugi not in zemljevid[prvi]:
                return False
        return True
    return False

def unikati(s):
    uni = []
    for i in s:
        if i not in uni:
            uni.append(i)
    return uni

def krozisca(zemljevid):
    s = []
    for krizisce in zemljevid:
        if len(zemljevid[krizisce]) > 1:
            s.append(krizisce)
    return s

def vsa_krozisca(pot, zemljevid):
    s = krozisca(zemljevid)
    for krizisce in s:
        if krizisce not in pot:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if pot == unikati(pot) and mozna_pot(pot, zemljevid) and vsa_krozisca(pot, zemljevid):
        return True
    return False

def navodila(pot, zemljevid):
    seznam_izhodov = []
    for prvi, drugi, tretji in zip(pot, pot[1:], pot[2:]):
        preobrnitev = preobrni_od_do(zemljevid[drugi], prvi, tretji)
        seznam_izhodov.append(preobrnitev[1])
    return seznam_izhodov

def prevozi(zacetek, navodila, zemljevid):
    seznam = [zacetek]
    prejsnje_krozisce = zacetek
    krozisce = zemljevid[zacetek][0]
    seznam.append(krozisce)
    for e in navodila:
        seznam_tega_krozisca = zemljevid[krozisce]
        seznam_tega_krozisca = preobrni_iz_prejsnjega(seznam_tega_krozisca, prejsnje_krozisce)[0]
        prejsnje_krozisce = krozisce
        krozisce = preobrni_n_krat(seznam_tega_krozisca, e)[0]
        seznam.append(krozisce)
    return seznam

def sosedi(doslej, zemljevid):
    mnozica = set()
    for krozisce in doslej:
        for sosedje in zemljevid[krozisce]:
            if sosedje not in doslej:
                mnozica.add(sosedje)
    return mnozica

def razdalja(x, y, zemljevid):
    mnozica = {x}
    i = 0
    while y not in mnozica:
        mnozica = sosedi(mnozica, zemljevid)
        i=i+1
    return i
"""
def sosedi_2(krizisce, zemljevid):
    mnozica = set()
    for sosedje in zemljevid[krizisce]:
            mnozica.add(sosedje)
    return mnozica

def najkrajsa_navodila_1(x, y, dolzina, seznam, zemljevid):
    mnozica = {x}
    if y == x:
        return seznam
    while y not in mnozica:
        mnozica = sosedi(mnozica, zemljevid)
    for krizisce in mnozica:
        if y in zemljevid[krizisce]:
            seznam.extend(krizisce)
            y = krizisce
    return najkrajsa_navodila_1(x, y, dolzina-1, seznam, zemljevid)

def najkrajsa_navodila(x, y, zemljevid):
    dolzina = razdalja(x, y, zemljevid)
    seznam = [y]
    return najkrajsa_navodila_1(x, y, dolzina, seznam, zemljevid)

def najkrajsa_navodila(x, y, zemljevid):
    mnozica = {x}
    slovar = dict()
    while y not in mnozica:
        for krizisce in mnozica:
            mnozica = sosedi_2(krizisce, zemljevid)
            for e in slovar:
                k = slovar[e]
                if k in mnozica:
                    mnozica.remove(k)
            print(mnozica)
            for sosed in mnozica:
                slovar[sosed] = krizisce
            if y in mnozica:
                break
    print(slovar)
    zadnji = y
    seznam = list()
    while zadnji != x:
        for trenutni in slovar:
            if trenutni == zadnji:
                seznam.append(trenutni)
                zadnji = slovar[trenutni]
                break
        if zadnji == x:
            seznam.append(x)
            break
        print(seznam)
    seznam = seznam[::-1]
    navigacija = navodila(seznam, zemljevid)
    return navigacija"""

def sosedi_2(slovar, zemljevid):
    nov_slovar = dict(slovar)
    for krozisce in slovar:
        for sosedje in zemljevid[krozisce]:
            if sosedje not in slovar:
                nov_slovar[sosedje] = krozisce
    #print(nov_slovar)
    return nov_slovar

def najkrajsa_navodila(x, y, zemljevid):
    zaceten = {x: sosedi({x}, zemljevid).pop()}
    while y not in zaceten:
        zaceten = sosedi_2(zaceten, zemljevid)
    #print(zaceten)
    zadnji = y
    seznam = list()
    while zadnji != x:
        for trenutni in zaceten:
            if trenutni == zadnji:
                seznam.append(trenutni)
                zadnji = zaceten[trenutni]
                break
        if zadnji == x:
            seznam.append(x)
            break
        #print(seznam)
    seznam = seznam[::-1]
    navigacija = navodila(seznam, zemljevid)
    return navigacija



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
