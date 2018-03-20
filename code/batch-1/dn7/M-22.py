# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    """
    Generiraj vse koordinate (x, y) za polje s podano širino in višino
    Args:
        s (int): širina
        v (int): višina

    Returns:
        generator parov polj
    """
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

import collections


def sosedov(x, y, mine):
    bomb = 0
    for a in mine:
        if a == (x + 1, y) or a == (x - 1, y) or a == (x, y + 1) or a == (x, y - 1) or a == (x + 1, y + 1) or a == (x + 1, y - 1) or a == (x - 1, y + 1) or a == (x - 1, y - 1):
            bomb += 1
    return bomb


def najvec_sosedov(mine, s, v):
    a, b = 0, 0
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) > sosedov(a, b, mine):
                a, b = x, y
    return a, b


def brez_sosedov(mine, s, v):
    prosta_pot = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                prosta_pot.add((x, y))
    return prosta_pot


def po_sosedih(mine, s, v):
    bojno_stanje = collections.defaultdict(set)
    for n in range(9):
        bojno_stanje[n] = set()
    for x in range(s):
        for y in range(v):
            bojno_stanje[sosedov(x, y, mine)].add((x, y))
    return bojno_stanje



########################
# Za oceno 7



def dolzina_poti(pot):
    koraki = 0
    pot_x, pot_y = [], []
    if pot:
        for x, y in pot:
            pot_x.append(x), pot_y.append(y)
        current_x, current_y = pot_x[0], pot_y[0]
        for x1 in pot_x:
            if x1 != current_x:
                koraki += abs(current_x - x1)
                current_x = x1
        for y1 in pot_y:
            if y1 != current_y:
                koraki += abs(current_y - y1)
                current_y = y1
    return koraki


def varnost(pot, mine):
    varnost = True
    for korak in pot:
        if korak in mine:
            varnost = False
            break
    return varnost

def premik(x0, y0, x1, y1):
    pot = [(x0, y0)]
    if x0 == x1:
        a = y0
        while a != y1:
            if y1 > y0:
                pot.append((x0, a + 1))
                a = a + 1
            else:
                pot.append((x0, a - 1))
                a = a - 1
    if y0 == y1:
        b = x0
        while b != x1:
            if x1 > x0:
                pot.append((b + 1, y0))
                b = b + 1
            else:
                pot.append((b - 1, y0))
                b = b - 1
    return pot

def varen_premik(x0, y0, x1, y1, mine):
    return varnost(premik(x0, y0, x1, y1), mine)

def varna_pot(pot, mine):
    varnost = True
    potovanje = list()
    if pot:
        if len(pot) > 1:
            while pot[-1] not in potovanje:
                for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
                    korak = premik(x0, y0, x1, y1)
                    for a in korak:
                        potovanje.append(a)
                    pot = pot[1 :]
            for step in potovanje:
                if step in mine:
                    varnost = False
                    break
        if len(pot) == 1:
            for z in pot:
                if z in mine:
                    varnost = False
    return varnost





########################
# Za oceno 8


def polje_v_mine(polje):
    if polje.endswith(" "):
        polje = polje[ : -1]
    polje = polje.split(" ")
    koordinate = set()
    s = 0
    v = len(polje)
    x = 0
    for jarek in polje:
        y = polje.index(jarek)
        s = len(jarek)
        valuex = 0
        for crka in jarek:
            if crka == ".":
                valuex += 1
            else:
                x = valuex
                valuex += 1
            koordinate.add((x, y))
    return koordinate, s, v



def sovrazne_koordinate(seznam):
    koordinate = set()
    for podatki in seznam:
        x, y, mina = podatki
        if mina == True:
            koordinate.add((x, y))
    return koordinate

def takticna_ocena(x, y, polje):
    polje1 = polje
    if polje.endswith(" "):
        polje1 = polje[: -1]
    polje1 = polje1.split(" ")
    jarek = polje1[y]
    znak = jarek[x]
    if znak == "X":
        return True
    else:
        return False

def strateski_seznam(polje):
    seznam = []
    polje1 = polje
    if polje.endswith(" "):
        polje1 = polje[ : -1]
    polje1 = polje1.split(" ")
    visina = len(polje1)
    for jarek in polje1:
        sirina = len(jarek)
    map = vsa_polja(sirina, visina)
    for x, y in map:
        pozicija = (x, y, takticna_ocena(x, y, polje))
        seznam.append(pozicija)
    return seznam

def polje_v_mine(polje):
    koordinate = set()
    karta = strateski_seznam(polje)
    karta1 = sovrazne_koordinate(karta)
    polje1 = polje
    if polje.endswith(" "):
        polje1 = polje[ : -1]
    polje1 = polje1.split(" ")
    visina = len(polje1)
    for jarek in polje1:
        sirina = len(jarek)
    return karta1, sirina, visina

########################
# Za oceno 9

def sosedov(x,y, mine):
    return len([a for a in mine if a == (x + 1, y) or a == (x - 1, y) or a == (x, y + 1) or a == (x, y - 1) or a == (x + 1, y + 1) or a == (x + 1, y - 1) or a == (x - 1, y + 1) or a == (x - 1, y - 1)])

def najvec_sosedov(mine, s, v):
    return max([(a, b) for a, b, c in [(x, y, sosedov(x, y, mine)) for x, y in vsa_polja(s, v)] if c == (max(c for a, b, c in [(x, y, sosedov(x, y, mine)) for x, y in vsa_polja(s, v)]))])

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {n :  {koordinate for koordinate, mine in [((x, y), z) for x, y, z in [koordinate for koordinate in[(x, y, sosedov(x, y, mine)) for x, y in vsa_polja(s, v)]]] if mine == n} for n in range(9)}

def dolzina_poti(pot):
    return sum([w + z for w, z in [(abs(a2 - a1), abs(b2 - b1)) for (a1, b1), (a2, b2) in [((x0, y0), (x1, y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1: ])]]])

def varen_premik(x0, y0, x1, y1, mine):
    return all([bomba not in mine for bomba in [[[(x0, z) for z in range(y0, y1 + 1)] if y0 < y1 else [(x0, z) for z in range(y0, y1 - 1, -1)]][0] if x0 == x1 else [[(z, y0) for z in range(x0, x1 + 1)] if x0 < x1 else [(z, y0) for z in range(x0, x1 - 1, -1)]][0]][0]])

def varna_pot(pot, mine):
    return all([all([all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in [((x0, y0), (x1, y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]]) if len(pot) > 1 else pot[0] not in mine]) if len(pot) > 0 else True])


########################
# Za oceno 10

def preberi_pot(ukaz):
    ukaz = ukaz.split("\n")
    pot, orientacija = [(0, 0)], "gor"
    usmeritve = ["gor", "desno", "dol", "levo"]
    x, y = 0, 0
    for command in ukaz:
        if command == "DESNO":
            orientacija = usmeritve[(usmeritve.index(orientacija) + 1)%4]
        elif command == "LEVO":
            orientacija = usmeritve[(usmeritve.index(orientacija) - 1)%4]
        else:
            command = int(command)
            if orientacija == "gor":
                x1, y1 = x, (y - command)
                x, y = x1, y1
                pot.append((x, y))
            elif orientacija == "dol":
                x1, y1 = x, (y + command)
                x, y = x1, y1
                pot.append((x, y))
            elif orientacija == "desno":
                x1, y1 = (x + command), y
                x, y = x1, y1
                pot.append((x, y))
            elif orientacija == "levo":
                x1, y1 = (x - command), y
                x, y = x1, y1
                pot.append((x, y))
    return pot



def zapisi_pot(ukazi):
    pot = ""
    ukazi1 = zip(ukazi, ukazi[1 :])
    usmeritve_desno = ["gor", "desno", "dol", "levo"]
    trenutna_orientacija = "gor"
    for (x0, y0), (x1, y1) in ukazi1:
        if x1 - x0 == 0:
            gibov = abs(y1 - y0)
            if y1 - y0 < 0:
                orientacija = "gor"
            if y1 - y0 > 0:
                orientacija = "dol"
        if y1 - y0 == 0:
            gibov = abs(x1 - x0)
            if x1 - x0 < 0:
                orientacija = "levo"
            if x1 - x0 > 0:
                orientacija = "desno"
        gibov_v_desno = 0
        while trenutna_orientacija != orientacija:
            trenutna_orientacija = usmeritve_desno[(usmeritve_desno.index(trenutna_orientacija) + 1)%4]
            gibov_v_desno += 1
        pot = pot + (gibov_v_desno * "\nDESNO") + "\n" + str(gibov)
    pot = pot.rstrip()
    pot = pot.lstrip()
    return pot


import unittest


"""
...X....
.X....X.
.XX.....
......X.
"""
mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
s1, v1 = 8, 4


"""
........
........
........
"""
mine2 = set()
s2, v2 = 8, 3


"""
...X...X.X....X.
"""
mine3 = {(3, 0), (7, 0), (9, 0), (14, 0)}
s3, v3 = 16, 1

"""
X
"""
mine4 = {(0, 0)}
s4, v4 = 1, 1

"""
X
.
.
X
.
X
.
"""
mine5 = {(0, 0), (0, 3), (0, 5)}
s5, v5 = 1, 7

class Test06(unittest.TestCase):
    def test_01_sosedov(self):
        self.assertEqual(sosedov(2, 1, mine1), 4)
        self.assertEqual(sosedov(0, 3, mine1), 1)
        self.assertEqual(sosedov(4, 3, mine1), 0)
        self.assertEqual(sosedov(4, 2, mine1), 0)
        self.assertEqual(sosedov(0, 0, mine1), 1)
        self.assertEqual(sosedov(7, 0, mine1), 1)
        self.assertEqual(sosedov(3, 0, mine1), 0)

        self.assertEqual(sosedov(2, 2, mine2), 0)
        self.assertEqual(sosedov(0, 0, mine2), 0)
        self.assertEqual(sosedov(0, 0, mine2), 0)

        self.assertEqual(sosedov(0, 0, mine3), 0)
        self.assertEqual(sosedov(2, 0, mine3), 1)
        self.assertEqual(sosedov(3, 0, mine3), 0)
        self.assertEqual(sosedov(8, 0, mine3), 2)

        self.assertEqual(sosedov(0, 0, mine4), 0)

        self.assertEqual(sosedov(0, 0, mine5), 0)
        self.assertEqual(sosedov(0, 1, mine5), 1)
        self.assertEqual(sosedov(0, 2, mine5), 1)
        self.assertEqual(sosedov(0, 3, mine5), 0)
        self.assertEqual(sosedov(0, 4, mine5), 2)
        self.assertEqual(sosedov(0, 5, mine5), 0)
        self.assertEqual(sosedov(0, 6, mine5), 1)

    def test_02_najvec_sosedov(self):
        self.assertEqual(najvec_sosedov(mine1, s1, v1), (2, 1))
        x, y = najvec_sosedov(mine2, s2, v2)
        self.assertTrue(0 <= x < s2)
        self.assertTrue(0 <= y < v2)
        self.assertEqual(najvec_sosedov(mine3, s3, v3), (8, 0))
        self.assertEqual(najvec_sosedov(mine4, s4, v4), (0, 0))
        self.assertEqual(najvec_sosedov(mine5, s5, v5), (0, 4))

    def test_03_brez_sosedov(self):
        self.assertEqual(brez_sosedov(mine1, s1, v1),
                         {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)})
        self.assertEqual(brez_sosedov(mine2, s2, v2),
                         {(x, y) for x in range(s2) for y in range(v2)})
        self.assertEqual(brez_sosedov(mine3, s3, v3),
                         {(x, 0) for x in (0, 1, 3, 5, 7, 9, 11, 12, 14)})
        self.assertEqual(brez_sosedov(mine4, s4, v4), {(0, 0)})
        self.assertEqual(brez_sosedov(mine5, s5, v5),
                         {(0, 0), (0, 3), (0, 5)})

    def test_04_po_sosedih(self):
        self.assertEqual(po_sosedih(mine1, s1, v1),
                         {0: {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)},
                          1: {(7, 3), (3, 2), (0, 0), (7, 0), (3, 3), (7, 1),
                              (4, 0), (6, 0), (5, 0), (5, 3), (5, 1), (1, 0),
                              (4, 1), (0, 3)},
                          2: {(0, 1), (1, 2), (1, 3), (0, 2), (3, 1), (2, 0),
                              (6, 2), (2, 3), (2, 2), (5, 2), (1, 1), (7, 2)},
                          3: set(),
                          4: {(2, 1)},
                          5: set(),
                          6: set(),
                          7: set(),
                          8: set()}
                         )

        prazen = dict.fromkeys(range(9), set())
        prazen[0] = {(x, y) for x in range(s2) for y in range(v2)}
        self.assertEqual(po_sosedih(mine2, s2, v2), prazen)

        s = dict.fromkeys(range(9), set())
        s.update({0: {(9, 0), (0, 0), (7, 0), (12, 0), (3, 0), (11, 0),
                      (14, 0), (5, 0), (1, 0)},
                  1: {(15, 0), (6, 0), (2, 0), (10, 0), (13, 0), (4, 0)},
                  2: {(8, 0)}})
        self.assertEqual(po_sosedih(mine3, s3, v3), s)

        s = dict.fromkeys(range(9), set())
        s.update({0: {(9, 0), (0, 0), (7, 0), (12, 0), (3, 0), (11, 0),
                      (14, 0), (5, 0), (1, 0)},
                  1: {(15, 0), (6, 0), (2, 0), (10, 0), (13, 0), (4, 0)},
                  2: {(8, 0)}})
        self.assertEqual(po_sosedih(mine3, s3, v3), s)

        s = dict.fromkeys(range(9), set())
        s[0] = {(0, 0)}
        self.assertEqual(po_sosedih(mine4, s4, v4), s)

        s = dict.fromkeys(range(9), set())
        s.update({0: {(0, 3), (0, 0), (0, 5)},
                  1: {(0, 1), (0, 6), (0, 2)},
                  2: {(0, 4)}})
        self.assertEqual(po_sosedih(mine5, s5, v5), s)


class Test07(unittest.TestCase):
    def test_01_dolzina_poti(self):
        self.assertEqual(dolzina_poti([(7, 2), (7, 5)]), 3)
        self.assertEqual(dolzina_poti([(7, 5), (7, 2)]), 3)
        self.assertEqual(dolzina_poti([(7, 5), (4, 5)]), 3)
        self.assertEqual(dolzina_poti([(1, 5), (4, 5)]), 3)
        self.assertEqual(
            dolzina_poti([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]),
            3 + 4 + 1 + 3 + 1)
        self.assertEqual(
            dolzina_poti([(0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]),
            4 + 1 + 3 + 1)
        self.assertEqual(
            dolzina_poti([(0, 0), (0, 1), (3, 1)]),
            1 + 3)
        self.assertEqual(dolzina_poti([(5, 3)]), 0)
        self.assertEqual(dolzina_poti([]), 0)

    """
    ...X....
    .X....X.
    .XX.....
    ......X.
    """
    def test_02_varen_premik(self):
        self.assertTrue(varen_premik(3, 1, 3, 3, mine1))
        self.assertTrue(varen_premik(3, 3, 3, 1, mine1))
        self.assertTrue(varen_premik(4, 0, 7, 0, mine1))
        self.assertTrue(varen_premik(7, 0, 4, 0, mine1))
        self.assertTrue(varen_premik(2, 1, 5, 1, mine1))
        self.assertTrue(varen_premik(5, 1, 2, 1, mine1))

        self.assertFalse(varen_premik(2, 1, 6, 1, mine1))
        self.assertFalse(varen_premik(6, 1, 2, 1, mine1))
        self.assertFalse(varen_premik(1, 1, 5, 1, mine1))
        self.assertFalse(varen_premik(5, 1, 1, 1, mine1))
        self.assertFalse(varen_premik(0, 1, 4, 1, mine1))
        self.assertFalse(varen_premik(4, 1, 0, 1, mine1))

        self.assertFalse(varen_premik(2, 1, 2, 3, mine1))
        self.assertFalse(varen_premik(2, 3, 2, 1, mine1))
        self.assertFalse(varen_premik(2, 1, 2, 2, mine1))
        self.assertFalse(varen_premik(2, 2, 2, 1, mine1))
        self.assertFalse(varen_premik(2, 2, 2, 0, mine1))
        self.assertFalse(varen_premik(2, 0, 2, 2, mine1))

        self.assertFalse(varen_premik(1, 1, 1, 1, mine1))

    """
    ...X....
    .X....X.
    .XX.....
    ......X.
    """
    def test_03_varna_pot(self):
        self.assertTrue(varna_pot([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)], mine1))
        self.assertTrue(varna_pot([(0, 3), (4, 3), (4, 2), (7, 2), (7, 3)], mine1))
        self.assertTrue(varna_pot([(2, 1)], mine1))
        self.assertTrue(varna_pot([], mine1))

        self.assertFalse(varna_pot([(0, 0), (0, 1), (3, 1)], mine1))
        self.assertFalse(varna_pot([(0, 0), (1, 0), (1, 3)], mine1))
        self.assertFalse(varna_pot([(0, 0), (1, 0), (0, 0), (1, 0), (1, 3), (3, 3)], mine1))
        self.assertFalse(varna_pot([(1, 1)], mine1))


class Test08(unittest.TestCase):
    def test_01_polje_v_mine(self):
        # Če si sledi več nizov, med katerimi ni ničesar, jih Python zlepi
        # ".X. "   "..X" je isto kot ".X. ...".
        self.assertEqual(polje_v_mine("...X.... "
                                      ".X....X. "
                                      ".XX..... "
                                      "......X."), (mine1, s1, v1))
        self.assertEqual(polje_v_mine("........ "
                                      "........ "
                                      "........"), (mine2, s2, v2))
        self.assertEqual(polje_v_mine("...X...X.X....X."), (mine3, s3, v3))
        self.assertEqual(polje_v_mine("X"), (mine4, s4, v4))
        self.assertEqual(polje_v_mine("X "
                                      ". "
                                      ". "
                                      "X "
                                      ". "
                                      "X "
                                      ". "), (mine5, s5, v5))


class Test10(unittest.TestCase):
    def test_01_preberi_pot(self):
        self.assertEqual(
            preberi_pot(
"""DESNO
DESNO
3
LEVO
4
LEVO
1
DESNO
3
DESNO
1"""), [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)])

        self.assertEqual(
            preberi_pot(
"""DESNO
LEVO
DESNO
DESNO
DESNO
DESNO
DESNO
3"""), [(0, 0), (3, 0)])

        self.assertEqual(
            preberi_pot(
"""LEVO
DESNO
LEVO
LEVO
LEVO
LEVO
DESNO
3"""), [(0, 0), (3, 0)])

        self.assertEqual(
            preberi_pot(
"""LEVO
DESNO
LEVO
LEVO
LEVO
LEVO
DESNO
3"""), [(0, 0), (3, 0)])

        self.assertEqual(
            preberi_pot(
"""DESNO
3
DESNO
3
DESNO
3
DESNO
3"""), [(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])

        self.assertEqual(
            preberi_pot(
"""DESNO
1
DESNO
DESNO
1
LEVO
LEVO
1
DESNO
3
LEVO
2
DESNO
DESNO"""), [(0, 0), (1, 0), (0, 0), (1, 0), (1, 3), (3, 3)])

    def test_02_zapisi_pot(self):
        pot = [(0, 0), (3, 0)]
        self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

        pot = [(0, 0), (3, 0), (3, 3)]
        self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

        pot = [(0, 0), (3, 0), (3, 3), (3, 5), (5, 5), (5, 1), (4, 1), (6, 1), (6, 8), (6, 3)]
        self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

        pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]
        self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

if __name__ == "__main__":
    unittest.main()

