import collections
import operator
from math import sqrt

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

def sosedov(x, y, mine):
#    """
#       Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
#       Polje samo ne šteje.
#
#       Args:
#           x (int): koordinata x
#           y (int): koordinata y
#           mine (set of tuple of int): koordinate min
#
#       Returns:
#           int: število sosedov
#       """
#    stevc = 0
#    for poz_X_mine, poz_Y_mine in mine:
#        if (poz_X_mine, poz_Y_mine) != (x, y) and (x - 1) <= poz_X_mine <= (x + 1) and (y - 1) <= poz_Y_mine <= (y + 1):
#            stevc += 1
#    return stevc
    return len([x for poz_X_mine, poz_Y_mine in mine if (poz_X_mine, poz_Y_mine) != (x, y) and (x - 1) <= poz_X_mine <= (x + 1) and (y - 1) <= poz_Y_mine <= (y + 1)])


def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """
    #presteto = collections.Counter()
    #for x, y in vsa_polja(s, v):
    #    presteto[(x, y)] = sosedov(x, y, mine)
    #return(max(presteto(mine, s, v).items(), key=operator.itemgetter(1))[0])
    return (max({(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.items(), key=operator.itemgetter(1))[0])


def brez_sosedov(mine, s, v):
    """
    Vrni množico koordinat polj brez min na sosednjih poljih. Polje samo lahko
    vsebuje mino.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        set of tuple: polja brez min na sosednjih poljih
    """
    #presteto = collections.Counter()
    #for x, y in vsa_polja(s, v):
    #    presteto[(x, y)] = sosedov(x, y, mine)
    return {koordinata for koordinata, sosedi in {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.items() if sosedi == 0}



def po_sosedih(mine, s, v):
    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        dict: (glej zgoraj)
    """
    #urejeno = {x: set() for x in range(9)}
    #for koordinata, sosedi in presteto(mine, s, v).items():
    #    if sosedi not in urejeno:
    #        urejeno[sosedi] = {koordinata}
    #    else:
    #        urejeno[sosedi].update({koordinata})
    #return urejeno
    return {x: {(x_poz, y_poz) for x_poz, y_poz in vsa_polja(s, v) if sosedov(x_poz, y_poz, mine) == x} for x in range(9)}



########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """
    return sum(sqrt((drugi[0] - prvi[0])**2 + ((drugi[1] - prvi[1])**2)) for prvi, drugi in zip(pot[0::1], pot[1::1]))

def razdalja(x0, y0, x1, y1):
    return sqrt((x1 - x0)**2 + (y1 - y0)**2)

def varen_premik(x0, y0, x1, y1, mine):
    """
    Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.

    Args:
        x0 (int): koordinata x začetnega polja
        y0 (int): koordinata y začetnega polja
        x1 (int): koordinata x končnega polja
        y1 (int): koordinata y končnega polja
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je premik varen, `False`, če ni.
    """
    #for x_koordinata, y_koordinata in mine:
    #    if x_koordinata in range(min(x0, x1), max(x0, x1) + 1) and y_koordinata in range(min(y0, y1), max(y0, y1) + 1):
    #        return False
    #else:
    #    return True
    return (False if False in [False for x, y in mine if min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1)] else True)



def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    #if len(pot) == 1 and pot[0] in mine:
    #    return False
    #for prve_koordinate, druge_koordinate in zip(pot[0::1], pot[1::1]):
    #    if not varen_premik(prve_koordinate[0], prve_koordinate[1], druge_koordinate[0], druge_koordinate[1], mine):
    #        return False
    #return True
    return (False if False in [False for prve_koordinate, druge_koordinate in zip(pot[0::1], pot[1::1])
                               if not varen_premik(prve_koordinate[0], prve_koordinate[1], druge_koordinate[0], druge_koordinate[1], mine)]
            else False if len(pot) == 1 and pot[0] in mine else True)


########################
# Za oceno 8

def polje_v_mine(polje):
    """
    Vrni koordinate min v podanem polju.

    Niz polje opisuje polje tako, da so vodoravne "vrstice" polja ločene s
    presledki. Prosta polja so označena z znako `.`, mine z `X`.

    Args:
        polje (str): polje

    Returns:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja.
    """
    sirina, visina = len(polje.split()[0]), len(polje.split())
    koordinati = set()
    for index, vrsta in enumerate(polje.split()):
        for index_mine, mina in enumerate(vrsta):
            if mina == "X":
                koordinati.add((index_mine, index))
    return (koordinati, sirina, visina)



########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """
    smer = 0
    poz_X, poz_Y = (0, 0)
    premiki = [(0, 0), ]
    for i in ukazi.split():
        if i == "DESNO":
            smer += 90
        elif i == "LEVO":
            smer -= 90
        elif i.isnumeric():
            if smer % 360 == 90:
                poz_X, poz_Y = (poz_X + int(i), poz_Y)
                premiki.append((poz_X, poz_Y))
            elif smer % 360 == 180:
                poz_X, poz_Y = (poz_X, poz_Y + int(i))
                premiki.append((poz_X, poz_Y))
            elif smer % 360 == 270:
                poz_X, poz_Y = (poz_X - int(i), poz_Y)
                premiki.append((poz_X, poz_Y))
            elif smer % 360 == 0:
                poz_X, poz_Y = (poz_X, poz_Y - int(i))
                premiki.append((poz_X, poz_Y))
    return premiki


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    od_do_pozicije = {('Levo', 'Levo'): 270, ('Dol', 'Dol'): 180, ('Gor', 'Desno'): 90, ('Gor', 'Dol'): 180, ('Gor', 'Levo'): 270, ('Desno', 'Gor'): 270, ('Desno', 'Dol'): 90, ('Desno', 'Levo'): 180, ('Dol', 'Gor'): 180, ('Dol', 'Desno'): 270, ('Dol', 'Levo'): 90, ('Levo', 'Gor'): 90, ('Levo', 'Desno'): 180, ('Levo', 'Dol'): 270}
    kje_sem_zdej = "Gor"
    poz_x, poz_y = (0, 0)
    zapisana_pot = []
    for ta_x, ta_y in pot:
        print(ta_x, ta_y)

        #if (ta_x, ta_y) == (0, 0):
        #    continue

        if ta_y > poz_y:
            if kje_sem_zdej == "Dol":
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Dol")] // 90))
                zapisana_pot[-1] = str(abs((ta_y)))
                poz_x, poz_y = (ta_x, ta_y)
            else:
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Dol")] // 90))
                zapisana_pot.append(str(abs((ta_y))))
                poz_x, poz_y = (ta_x, ta_y)
                kje_sem_zdej = "Dol"


        elif ta_y < poz_y:
            if kje_sem_zdej == "Levo":
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Levo")] // 90))
                zapisana_pot[-1] = str(abs((ta_y)))
                poz_x, poz_y = (ta_x, ta_y)
            else:
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Levo")] // 90))
                zapisana_pot.append(str(ta_y))
                poz_x, poz_y = (ta_x, ta_y)
                kje_sem_zdej = "Levo"

        elif ta_x > poz_x:
            zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Desno")] // 90))
            zapisana_pot.append(str(ta_x))
            poz_x, poz_y = (ta_x, ta_y)
            kje_sem_zdej = "Desno"

        elif ta_x > poz_x:
            zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Gor")] // 90))
            zapisana_pot.append(str(ta_x))
            poz_x, poz_y = (ta_x, ta_y)
            kje_sem_zdej = "Gor"


    print(zapisana_pot)
    return " ".join(zapisana_pot)


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

