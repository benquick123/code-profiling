import collections

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
    """
    Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
    Polje samo ne šteje.

    Args:
        x (int): koordinata x
        y (int): koordinata y
        mine (set of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """
    stevilo_sosedov = 0
    mozni_sosedi = set([(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)])
    for mina in mine:
        if mina in mozni_sosedi:
            stevilo_sosedov += 1

    return stevilo_sosedov


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

    max_sosedov_tocka = (0, 0)
    max_sosedov = 0

    for visina in range(0, v):
        for sirina in range(0, s):
            st_min = sosedov(sirina, visina, mine)
            if st_min > max_sosedov:
                max_sosedov_tocka = (sirina, visina)
                max_sosedov = st_min

    return max_sosedov_tocka


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
    brez_s = set()
    for visina in range(0, v):
        for sirina in range(0, s):
            if sosedov(sirina, visina, mine) == 0:
                brez_s.add((sirina, visina))

    return brez_s


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
    urejeni_sosedi = {}
    for i in range(0, 9):
        urejeni_sosedi[i] = set()
    for visina in range(0, v):
        for sirina in range(0, s):
            st_min_na_tocki = sosedov(sirina, visina, mine)
            urejeni_sosedi[st_min_na_tocki].add((sirina, visina))

    return urejeni_sosedi


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
    dolzina = 0
    for korak in range(0, len(pot) - 1):
        x1, y1 = pot[korak]
        x2, y2 = pot[korak + 1]

        if x1 == x2:
            dolzina = dolzina + abs(y1 - y2)

        else:
            dolzina = dolzina + abs(x1 - x2)

    return dolzina


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
    if (x0, y0) in mine or (x1, y1) in mine:
        return False

    if x0 == x1:
        if y1 < y0:
            y0, y1 = y1, y0
        razlika = y1 - y0

        while razlika > 0:
            y0 += 1
            if (x0, y0) in mine:
                return False
            else:
                razlika -= 1
                continue

    else:
        if x1 < x0:
            x0, x1 = x1, x0

        razlika = x1 - x0

        while razlika > 0:
            x0 += 1
            if (x0, y0) in mine:
                return False
            else:
                razlika -= 1
                continue

    return True


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    if len(pot) == 1:
        if pot[0] not in mine:
            return True
        else:
            return False

    elif len(pot) == 0:
        return True

    else:
        for korak in range(0, len(pot) - 1):
            x1, y1 = pot[korak]
            x2, y2 = pot[korak + 1]

            if varen_premik(x1, y1, x2, y2, mine):
                continue

            else:
                return False

        return True


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
    mine = set()
    vrstice = polje.split()
    sirina = len(vrstice[0])
    visina = len(vrstice)

    for y in range(0, visina):
        for x in range(0, sirina):
            if vrstice[y][x] == "X":
                mine.add((x, y))

    return mine, sirina, visina


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.

def sosedov(x, y, mine):
    return len([(minax, minay) for minax, minay in mine if ((minax, minay) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1) ,(x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)])])


def najvec_sosedov(mine, s, v):
    return (max([(sosedov(x, y, mine), x, y) for x, y in vsa_polja(s, v)]))[1:]


def brez_sosedov(mine, s, v):
    return set((x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0)


def po_sosedih(mine, s, v):
    return {x:{(x1,y1) for x1,y1 in vsa_polja(s,v) if sosedov(x1,y1,mine)==x} for x in range(0,9)}


def dolzina_poti(pot):
    return sum(abs(pot[i][0] - pot[i + 1][0]) + abs(pot[i][1] - pot[i + 1][1]) for i in range(0, len(pot) - 1))


def varen_premik(x0, y0, x1, y1, mine):
    return not (any([min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1) for x,y in mine]))


def varna_pot(pot, mine):
    return (all([varen_premik(pot[i][0], pot[i][1], pot[i+1][0], pot[i+1][1], mine) for i in range(0,len(pot)-1)] or [varen_premik(pot[i][0], pot[i][1], pot[i][0], pot[i][1], mine) for i in [0] if len(pot)==1] or [True for i in [] if len(pot)==0]))


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

    seznam_ukazov = ukazi.split()
    smer = "GOR"
    indeks_zadnje_tocke = 0
    pot = [(0, 0)]

    for ukaz in seznam_ukazov:
        if not ukaz.isdigit():
            if ukaz == "DESNO":
                if smer == "GOR":
                    smer = "DESNO"
                    continue

                elif smer == "DESNO":
                    smer = "DOL"
                    continue

                elif smer == "DOL":
                    smer = "LEVO"
                    continue

                elif smer == "LEVO":
                    smer = "GOR"
                    continue

            if ukaz == "LEVO":
                if smer == "GOR":
                    smer = "LEVO"
                    continue

                elif smer == "LEVO":
                    smer = "DOL"
                    continue

                elif smer == "DOL":
                    smer = "DESNO"
                    continue

                elif smer == "DESNO":
                    smer = "GOR"
                    continue

        else:
            x0 = pot[indeks_zadnje_tocke][0]
            y0 = pot[indeks_zadnje_tocke][1]

            if smer == "GOR":
                pot.append((x0, y0 - int(ukaz)))
                indeks_zadnje_tocke = indeks_zadnje_tocke + 1

            elif smer == "DOL":
                pot.append((x0, y0 + int(ukaz)))
                indeks_zadnje_tocke = indeks_zadnje_tocke + 1

            elif smer == "DESNO":
                pot.append((x0 + int(ukaz), y0))
                indeks_zadnje_tocke = indeks_zadnje_tocke + 1

            elif smer == "LEVO":
                pot.append((x0 - int(ukaz), y0))
                indeks_zadnje_tocke = indeks_zadnje_tocke + 1

            continue

    return pot


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """

    def spremeni_smer(nova_smer, ukaz):
        if ukaz == "DESNO":
            if nova_smer == "GOR":
                nova_smer = "DESNO"
                return nova_smer

            elif nova_smer == "DESNO":
                nova_smer = "DOL"
                return nova_smer

            elif nova_smer == "DOL":
                nova_smer = "LEVO"
                return nova_smer

            elif nova_smer == "LEVO":
                nova_smer = "GOR"
                return nova_smer

        if ukaz == "LEVO":
            if nova_smer == "GOR":
                nova_smer = "LEVO"
                return nova_smer

            elif nova_smer == "LEVO":
                nova_smer = "DOL"
                return nova_smer

            elif nova_smer == "DOL":
                nova_smer = "DESNO"
                return nova_smer

            elif nova_smer == "DESNO":
                nova_smer = "GOR"
                return nova_smer

    def pridobi_smer(premik1, premik2):
        pot1x, pot1y = premik1
        pot2x, pot2y = premik2

        if pot1y == pot2y:
            if pot1x < pot2x:
                return "DESNO"

            else:
                return "LEVO"

        elif pot1y < pot2y:
            return "DOL"

        else:
            return "GOR"

    izpis = ""
    smer = "GOR"

    for i in range(0, len(pot) - 1):
        pot1 = pot[i]
        pot2 = pot[i + 1]
        zeljena_smer = pridobi_smer(pot1, pot2)
        while smer != zeljena_smer:
            izpis = izpis + "DESNO\n"
            smer = spremeni_smer(smer, "DESNO")

        dolzina_premika = dolzina_poti([pot1, pot2])
        izpis = izpis + (str(dolzina_premika) + "\n")

    return izpis


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
