
def st_krozisc(zemljevid):
    st = 0
    for k in zemljevid:
        if len(zemljevid[k]) > 1:
            st += 1
    return st

def unvisited_sosedi(curr, unvisited, zemljevid):
    ret = set()
    for i in zemljevid[curr]:
        if i in unvisited:
            ret = ret.union({i})
    return ret
# Ocena 6.
############################################################
def preberi(ime_datoteke):
    zemljevid = open(ime_datoteke)
    zemljevid_list = zemljevid.read()
    zemljevid_list = zemljevid_list.split('\n')
    zemljevid_dict = dict()
    for i in range(len(zemljevid_list)):
        if(len(zemljevid_list[i]) > 0):
            zemljevid_dict[i + 1] = zemljevid_list[i]
            zemljevid_dict[i + 1] = zemljevid_dict[i + 1].split()
            for j in zemljevid_dict[i + 1]:
                zemljevid_dict[i + 1][zemljevid_dict[i + 1].index(j)] = int(zemljevid_dict[i + 1][zemljevid_dict[i + 1].index(j)])

    for i in zemljevid_dict:
        while zemljevid_dict[i][0] != min(zemljevid_dict[i]):
            tmp = zemljevid_dict[i][0]
            zemljevid_dict[i].pop(0)
            zemljevid_dict[i].append(tmp)

    return zemljevid_dict

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False

    for k in range(len(pot) - 1) :
        if pot[k] not in zemljevid[pot[k + 1]]:
            return False
        if k != 0 and k != len(pot) - 1:
            if len(zemljevid[pot[k]]) <= 1:
                return False
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    krozisc = st_krozisc(zemljevid)
    pot_med_izhodisci = pot[1:-1]
    if krozisc != len(set(pot_med_izhodisci)):
        return False
    if len(pot_med_izhodisci) > len(set(pot_med_izhodisci)):
        return False
    return True
###################################################################


# Ocena 7
###################################################################
def navodila(pot, zemljevid):
    izvozi = []
    for i in range(1,len(pot) - 1):
        razdalja = zemljevid[pot[i]].index(pot[i - 1]) - zemljevid[pot[i]].index(pot[i + 1])
        razdalja =len(zemljevid[pot[i]]) -  razdalja % len(zemljevid[pot[i]])
        if pot[i - 1] == pot[i + 1]:
            razdalja = 0
        izvozi.append(razdalja)
    return izvozi
###################################################################

# Ocena 8
###################################################################
def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek]
    prejsnje_krozisce = pot[-1]
    pot.append(zemljevid[pot[-1]][0])
    for izvoz in navodila:
        zdajsnje_krozisce = pot[-1]
        if zemljevid[zdajsnje_krozisce].index(prejsnje_krozisce) + izvoz > len(zemljevid[zdajsnje_krozisce]) - 1:
            premik = zemljevid[zdajsnje_krozisce].index(prejsnje_krozisce) - (len(zemljevid[zdajsnje_krozisce]) - izvoz)
        else:
            premik = zemljevid[zdajsnje_krozisce].index(prejsnje_krozisce) + izvoz
        prejsnje_krozisce = pot[-1]
        pot.append(zemljevid[zdajsnje_krozisce][premik])
    return pot
##################################################################

# Ocena 9
#################################################################

#1.
def sosedi(doslej, zemljevid):
    ret = set()
    for uvoz in doslej:
        for izvoz in zemljevid[uvoz]:
            if (izvoz not in ret) and (izvoz not in doslej):
                ret = ret.union({izvoz})
    return ret

#2.
def razdalja(x, y, zemljevid):
    prevozeno = {x}
    pot = 0
    while y not in prevozeno:
        for i in prevozeno:
            prevozeno = prevozeno.union(zemljevid[i])
        pot+= 1
    return pot
#################################################################

# Ocena 10
#################################################################
def najkrajsa_navodila(x,y, zemljevid):
    node_values = {i:0 for i in zemljevid}
    node_values[x] = 1
    unvisited = {i for i in zemljevid if i != x}

    curr_node = x
    while(y != curr_node):
        for i in unvisited_sosedi(curr_node, unvisited, zemljevid):
            if node_values[i] == 0:
                node_values[i] = node_values[curr_node] + 1
            if node_values[i] > node_values[curr_node] + 1:
                node_values[i] = node_values[curr_node] + 1
        a = [i for i in unvisited if node_values[i] != 0 and i != curr_node]
        min = a[0]
        for i in a:
            if node_values[i] < node_values[min]:
                min = i
        unvisited = unvisited.difference({curr_node})
        curr_node = min
    counter = node_values[y]
    najkrajse = [y]
    for i in range(counter, 0, -1):
        for krozisce in zemljevid[najkrajse[-1]]:
            if node_values[krozisce] == i - 1:
                najkrajse.append(krozisce)
                break
    najkrajse = najkrajse[::-1]
    return navodila(najkrajse, zemljevid)

#################################################################

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
