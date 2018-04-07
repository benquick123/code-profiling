import unittest
from random import randint
import os
from collections import Counter

# ********** POMOŽNE FUNKCIJE **********

def uredi(seznam):
    vrni = []
    indeks = seznam.index(min(seznam))
    for element in seznam[indeks:]:
        vrni.append(element)
    for element in seznam[:indeks]:
        vrni.append(element)
    return vrni

def aligreven(seznam, zemljevid):
    nov = []
    for element in seznam[1:-1]:
        if len(zemljevid[element]) == 1:
            nov.append('FAIL')
        else: nov.append ('OK')
    if 'FAIL' in nov:
        return False
    else:
        return True

def opravljenapot(pot, zemljevid):
    zdej = pot[0]
    cmp = []
    for next in pot[1:]:
        for moznost in zemljevid[zdej]:
            if moznost == next:
                cmp.append(zdej)
                break
        zdej = next
    cmp.append(next)
    return cmp

# ********** ZA OCENO 6 **********

def preberi(ime_datoteke):
    stevilo_krozisca = 1
    zemljevid = {}
    for vrstica in open(ime_datoteke):
        zemljevid[stevilo_krozisca] = []
        if len(vrstica.strip()) == 1:
            zemljevid[stevilo_krozisca].append(int(vrstica.strip()))
            stevilo_krozisca += 1
        if len(vrstica.strip()) > 1:
            for znak in vrstica.strip().split():
                if znak.isalnum():
                    zemljevid[stevilo_krozisca].append(int(znak))
            stevilo_krozisca += 1
    for vrednost in zemljevid.items():
        zemljevid[vrednost[0]] = uredi(vrednost[1])
    return zemljevid

def mozna_pot(pot, zemljevid):
    zdej, pogoj_zacetek = pot[0], pot[0]
    cmp = []
    for next in pot[1:]:
        for moznost in zemljevid[zdej]:
            if moznost == next:
                cmp.append(zdej)
                break
        zdej = next
    cmp.append(next)
    if not aligreven(cmp, zemljevid): return False
    if cmp == pot and len(zemljevid[pogoj_zacetek]) == 1 and len(zemljevid[next]) == 1:
        return True

def hamiltonova(pot, zemljevid):
    vsa = []
    for vsako in list(zemljevid.keys()):
        if len(zemljevid[vsako]) > 1:
            vsa.append(vsako)
    if mozna_pot(pot, zemljevid):
        for krozisce in pot[1:-1]:
            if zemljevid[krozisce] == 1:
                return False
        for posamezno in vsa:
            if posamezno not in pot[1:-1]:
                return False
        for ponovitev in Counter(pot).values():
            if ponovitev > 1:
                return False
        return True
    else: return False

# ********** TESTI **********

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

if __name__ == "__main__":
    unittest.main()
