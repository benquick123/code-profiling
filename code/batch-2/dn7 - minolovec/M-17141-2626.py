import math

#mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}


def sosedov(x, y, mine):
    cifra_min = 0
    sez = []
    for x1, y1 in mine:

        if (x == x1) & ((y - 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))


        elif ((x + 1) == x1) & ((y - 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x - 1) == x1) & ((y - 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x + 1) == x1) & (y == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x + 1) == x1) & ((y + 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x) == x1) & ((y + 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x - 1) == x1) & ((y + 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x - 1) == x1) & (y == y1):
            cifra_min += 1
            sez.append((x1, y1))

    return cifra_min


# print(sosedov(2, 1, mine))

def setup_board(s, v):
    coordinates = []
    for x in range(0, s):
        for y in range(0, v):
            coordinates.append((x, y))
    return coordinates


def najvec_sosedov(mine, s, v):
    ogX, ogY = 0, 0
    max_sosedov = 0
    for x, y in setup_board(s, v):
        if sosedov(x, y, mine) > max_sosedov:
            max_sosedov = sosedov(x, y, mine)
            ogX, ogY = x, y

    return (ogX, ogY)


# print(najvec_sosedov(mine, 7, 4))

def brez_sosedov(mine, s, v):
    brez = []
    for x, y in setup_board(s, v):
        if sosedov(x, y, mine) == 0:
            brez.append((x, y))
    return set(brez)


# print(brez_sosedov(mine, 7, 4))

def po_sosedih(mine, s, v):
    # setup slovarja s praznimi seti do kljuca stevila 8
    slovar = {}
    for i in range(0, 9):
        slovar[i] = set()

    for x, y in setup_board(s, v):
        slovar[sosedov(x, y, mine)].add((x, y))
    return slovar


# print(po_sosedih(mine, 8, 4))

pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]


def dolzina_poti(pot):
    dolzina, i = 0, 0
    while i < len(pot) - 1:
        x, y = pot[i]
        x1, y1 = pot[i + 1]
        this_dolzina = math.sqrt((x1 - x) ** 2) + math.sqrt((y1 - y) ** 2)
        dolzina += this_dolzina
        i += 1
    return int(dolzina)


# print(dolzina_poti(pot))

def is_mine(x, y, mine):
    if (x, y) in mine:
        return True
    else:
        return False


def get_premiki(x0, y0, x1, y1):
    premiki = []
    if (x0 < x1) & (y0 < y1):  # 0,0 -> 1,5
        while x0 < x1:
            x0 += 1
            premiki.append((x0, y0))
            # if is_mine(x0, y0, mine): return False
        while y0 < y1:
            y0 += 1
            premiki.append((x0, y0))
        return premiki

    if (x0 < x1) & (y0 > y1):  # 0,6 -> 3,4
        while x0 < x1:
            x0 += 1
            premiki.append((x0, y0))
        while y0 > y1:
            y0 -= 1
            premiki.append((x0, y0))
        return premiki

    if (x0 > x1) & (y0 < y1):  # 5,0 -> 3,4
        while x0 > x1:
            x0 -= 1
            premiki.append((x0, y0))
        while y0 < y1:
            y0 += 1
            premiki.append((x0, y0))
        return premiki

    if (x0 > x1) & (y0 > y1):  # 6,6 -> 1,1
        while x0 > x1:
            x0 -= 1
            premiki.append((x0, y0))
        while y0 > y1:
            y0 -= 1
            premiki.append((x0, y0))
        return premiki

    if (x0 > x1) & (y0 == y1):
        while x0 > x1:
            x0 -= 1
            premiki.append((x0, y0))
        return premiki

    if (x0 < x1) & (y0 == y1):
        while x0 < x1:
            x0 += 1
            premiki.append((x0, y0))
        return premiki
    if (x0 == x1) & (y0 > y1):
        while y0 > y1:
            y0 -= 1
            premiki.append((x0, y0))
        return premiki
    if (x0 == x1) & (y0 < y1):
        while y0 < y1:
            y0 += 1
            premiki.append((x0, y0))
        return premiki


# print(get_premiki(3,6,1,6))

def varen_premik(x0, y0, x1, y1, mine):
    if len(mine) == 0:
        return True
    if is_mine(x0, y0, mine):
        return False
    for (x, y) in get_premiki(x0, y0, x1, y1):
        if is_mine(x, y, mine):
            return False
    return True


# print(varen_premik(0,3,3,3,mine))

def varna_pot(pot, mine):
  i = 0
  if len(pot) == 1:
    (x,y) = pot[0]
    if is_mine(x,y,mine):
      return False
  while i < len(pot)-1 & len(pot)>1:
    x0,y0 = pot[i]
    if (i == 0) & (is_mine(x0,y0,mine)):
        return False
    x1, y1 = pot[i+1]
    i+=1
    if varen_premik(x0, y0, x1, y1, mine):
      pass
    else:
      return False
  return True


# print(varna_pot(pot, mine))

#polje = "...X.... .X....X. .XX..... ......X."


def polje_v_mine(polje):
    vrste = []
    found_mines = []
    x, y = 0, 0

    for vrstica in polje.split():
        vrste.append(vrstica)

        for znak in vrstica:
            s = len(vrstica)
            if znak == "X":
                found_mines.append((x, y))
            x = x + 1
        y = y + 1
        x = 0
    v = len(vrste)
    return set(found_mines), s, v

# print(polje_v_mino(polje))



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
                                      "."), (mine5, s5, v5))


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
















