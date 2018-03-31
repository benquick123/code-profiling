

#Napiši funkcijo najvec_sosedov(mine, s, v), ki vrne koordinati polja, ki je obkroženo z največ minami. Pri tem sta s in v širini in višina polja. Za gornji primer bi klic najvec_sosedov(mine, 8, 4) vrnil polje (2, 1).

#Napiši funkcijo brez_sosedov(mine, s, v), ki vrne množico vseh polj, ki nimajo na sosednjih poljih nobene mine. (Dovoljeno pa je, da mina stoji prav na tem polju). V gornjem primeru klic brez_sosedov(mine, 8, 4) vrne {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)}

#Napiši funkcijo po_sosedih(mine, s, v), ki vrne slovar, katerega ključi so števila od 0 do 8, pripadajoče vrednosti pa so množice koordinat polj, ki vsebujejo toliko min. V gornjem primeru bi klic po_sosedih(mine, 8, 4) vrnil slovar

# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):

    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6
# Napiši funkcijo sosedov(x, y, mine), ki pove, na koliko sosedov polja s koordinatami (x, y) je postavljena mina.
#  Klic sosedov(2, 1, mine) v gornjem primeru vrne 4, saj je polje obkroženo s štirimi minami.
#  Klic sosedov(3, 0) vrne 0,
# saj nobeno od sosednjih polj nima mine; mina je seveda prav na polju (3, 0),
#  vendar ta ne šteje.

def preveri_mino(x, y, mine):

    for x_koordinata,y_koordinata in mine:
        if x_koordinata==x  and y_koordinata==y:
            return True #true
    return False

def max_velikost(mine):
    max_x=0
    max_y=0
    for x, y in mine:
        if x > max_x:
            max_x=x


        if y > max_y:
            max_y=y

    return (max_x,max_y)


def sosedov(x, y, mine):


    mina_1=preveri_mino(x-1,y-1,mine)
    mina_2=preveri_mino(x+0,y-1,mine)
    mina_3=preveri_mino(x+1,y-1,mine)
    mina_4=preveri_mino(x+1,y+0,mine)
    mina_5=preveri_mino(x+1,y+1,mine)
    mina_6=preveri_mino(x+0,y+1,mine)
    mina_7=preveri_mino(x-1,y+1,mine)
    mina_8=preveri_mino(x-1,y+0,mine)

    seznam_min=[mina_1,mina_2,mina_3, mina_4, mina_5, mina_6, mina_7, mina_8]
    return  sum(seznam_min)



def najvec_sosedov(mine, s, v):
    št_sosednih_min=[]
    for x, y in vsa_polja(s,v):
        sosednje_mine= sosedov(x,y,mine)
        št_sosednih_min.append((x,y, sosednje_mine))
    največja_terka_max=max(št_sosednih_min, key=lambda mina:mina[2])

    return (največja_terka_max[0],največja_terka_max[1])


def brez_sosedov(mine, s, v):
    ni_sosedov=[]
    for x, y in vsa_polja(s, v):
       # sosednje_mine=sosedov (x,y,mine)
        if sosedov(x,y,mine)==0:
            mesta_kjer_ni_sosedov=(x,y)
            ni_sosedov.append(mesta_kjer_ni_sosedov)
    return set(ni_sosedov)

 #Napiši funkcijo po_sosedih(mine, s, v),
# ki vrne slovar, katerega ključi so števila od 0 do 8, pripadajoče vrednosti pa so množice
def po_sosedih (mine, s,v ):
    slovar= {}
    for i in range(0,9):
        seznam_koordinat=[]
        for x,y in vsa_polja(s,v):
            if sosedov(x,y,mine)==i:
                seznam_koordinat.append((x,y))
        slovar[i]=set(seznam_koordinat)
    return slovar


#NALOGA za 7

def dolzina_poti(pot):

    # dolžina=0
    # vsota=0
    # for i in range(0,len(pot)-1):
    #
    #     x1=pot[i][0]
    #     y1=pot[i][1]
    #     x2=pot[i+1][0]
    #     y2=pot[i+1][1]
    #
    #     dolžina=abs(y2-y1)+abs(x2-x1)
    #
    #     vsota+=dolžina
    #
    # return vsota

    return sum([abs(pot[i][0] - pot[i + 1][0]) + abs(pot[i][1] - pot[i + 1][1]) for i in range(len(pot) - 1)])

def varen_premik(x0,y0,x1,y1, mine):
    for x in range(min(x0,x1), max(x0, x1)+1): #za vodoravno
        if preveri_mino(x,y0,mine):
            return False


    for y in range(min(y0,y1),max(y0,y1)+1): #za navpično
        if preveri_mino(x0,y, mine):
            return False

    return True

def varna_pot(pot, mine):
    if len(pot)==1 and preveri_mino(pot[0][0],pot[0][1],mine):
        return False




    for i in range(0, len(pot) - 1):#ker zanji nima več para/ ne obstaja več  je -1!!!!"!!!!

        x1 = pot[i][0]
        y1 = pot[i][1]
        x2 = pot[i + 1][0]
        y2 = pot[i + 1][1]

        if varen_premik(x1,y1,x2,y2, mine)==False: #pot ni varna

            return False
    return True



#naloga 8
def polje_v_mine(polje):

    razdeljeni_znaki_po_vrsticah=polje.strip().split(" ")
    visina=len(razdeljeni_znaki_po_vrsticah)
    dolžina=len(razdeljeni_znaki_po_vrsticah[0])

    novi_seznam=[]
    for y in range(0, visina):
        for x in range(0, dolžina):
            if razdeljeni_znaki_po_vrsticah[y][x] =="X":
                novi_seznam.append((x,y))
    return (set(novi_seznam),dolžina, visina)





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


