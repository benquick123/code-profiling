

import unittest
from random import randint
import os

def preberi(ime_datoteke):
    '''Reads file ime_datoteke, extracts and sorts (lowest number first)
    each list in dictionary then returns it

    :param ime_datoteke:
    :return containerdict:
    '''
    with open(ime_datoteke, "r") as f:
        file = f.read().splitlines()
    containerdict = {}
    for num, item in enumerate(file):
        ctn = item.split(" ")
        containerdict[num+1] = []
        for i in ctn:
            containerdict[num+1].append(int(i))
        c = containerdict[num + 1]
        m = min(c)
        while c[0] != m:
            c.append(c.pop(0))
        containerdict[num+1] = c
    return containerdict

def mozna_pot(pot, zemljevid):
    '''Takes pot and zemljevid, pot is a path, and zemljevid is a dictionary of connections.
    function returns True if connections exist.

    :param pot:
    :param zemljevid:
    :return bool:
    '''
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1 \
            and pot[0] in zemljevid[pot[1]] and pot[-1] in zemljevid[pot[-2]]:
        pot = pot[1:-1]
        if not pot:
            return False
        for num, item in enumerate(pot):
            if num+1 < len(pot):
                if pot[num + 1] not in zemljevid[pot[num]] or len(zemljevid[pot[num]]) == 1:
                    return False
        else:
            return True
    else:
        return False

def hamiltonova(pot, zemljevid):
    '''Extends previous function. Only returns true if path exists and each node is passed only once.

    :param pot:
    :param zemljevid:
    :return bool:
    '''
    if mozna_pot(pot, zemljevid):
        for item in zemljevid:
            if pot.count(item) != 1 and len(zemljevid[item]) > 1:
                return False
        return True
    else:
        return False

def navodila(pot, zemljevid):
    '''Given an existing path, this function returns the jumps for each node, that the path takes.

    #examples assume zemljevid.txt is used.
    path: [6, 11, 10], return: [2, 4]
    path: [1, 3, 8, 16, 15], return: [1, 1, 1]
    path: [1, 3, 6, 4, 2], return: [3, 2, 2])


    :param pot:
    :param zemljevid:
    :return list generator:
    '''
    return [(zemljevid[premik].index(pot[num+1]) - zemljevid[premik].index(pot[num-1]))% len(zemljevid[premik])
            for num, premik in enumerate(pot) if num != 0 and num != len(pot)-1]



def prevozi(zacetek, navodila, zemljevid):
    '''Given starting point, a list of jump for each node in the path it takes
    Function returns a list of keys in dictionaries that describe that path.

    #examples assume zemljevid.txt is used.
    start: 1, navodila: [1, 1, 1], returns: [1, 3, 8, 16, 15]
    start: 1, navodila: [3, 2, 2], returns: [1, 3, 6, 4, 2]
    start: 15, navodila: [1, 2, 5, 2, 3, 2, 5, 2, 2], zemljevid)
    returns: [15, 16, 14, 11, 9, 16, 14, 11, 9, 16, 15]

    :param zacetek:
    :param navodila:
    :param zemljevid:
    :return container:
    '''
    container = [zacetek, zemljevid[zacetek][0]]
    for n in navodila:
        index1 = zemljevid[container[-1]].index(container[-2])
        nav = index1+n
        if nav >= len(zemljevid[container[-1]]):
            nav = nav-len(zemljevid[container[-1]])
        container.append(zemljevid[container[-1]][nav])
    return container


def sosedi(doslej, zemljevid):
    '''Function takes a set of nodes, and returns a set of all nodes connected to those nodes, without the nodes
    themselves.

    #examples assume that zemljevid.txt is used.
    doslej: {15, 16, 14, 9, 8}, returns: {3, 7, 11, 13}
    doslej: {15, 16}, returns: {14, 9, 8}


    :param doslej:
    :param zemljevid:
    :return container:
    '''
    container = set()
    for item in doslej:
        for i in zemljevid[item]:
            if i not in container and i not in doslej:
                container.add(i)
    return container


def razdalja(x, y, zemljevid):
    '''Takes x (starting point), y (ending point) and dict of connections (zemljevid) and returns the length of path
    between starting and ending node.

    #examples assume that zemljevid.txt is used.
    x: 15, y: 16 returns: 1
    x: 15, y: 14, returns: 2
    x: 15, y: 13, returns: 3
    x: 6, y: 12, returns: 4

    :param x:
    :param y:
    :param zemljevid:
    :return counter - int:
    '''
    mnozica = {x}
    counter = 0
    for item in range(1, len(zemljevid)):
        if y not in mnozica:
            mnozica = sosedi(mnozica, zemljevid)
            counter += 1
    return counter



def najkrajsa_navodila(x, y, zemljevid):
    '''Gets a starting point (x), ending point(y) and graph and finds the shortest route between points x and y,
    using a breadth first algorithm.

    #examples assume that zemljevid.txt is used.
    x: 2, y: 15, returns: [1, 2, 1, 1]
    x: 15, y: 1, returns: [3, 3, 4]
    x: 15, y: 2, returns: [3, 3, 3, 3]

    :param x:
    :param y:
    :param zemljevid:
    :return:
    '''
    obiskano = []
    vrsta = [[x]]
    while vrsta:
        trenutno = vrsta.pop(0)
        zadnji = trenutno[-1]
        if zadnji not in obiskano:
            for i in zemljevid[zadnji]:
                nova_pot = list(trenutno)
                nova_pot.append(i)
                vrsta.append(nova_pot)
                if i == y:
                    return navodila(nova_pot, zemljevid)
            obiskano.append(zadnji)




najkrajsa_navodila(1, 15, preberi("zemljevid.txt"))

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
