
def vsa_polja(s, v): #vrne vse točke od (0, 0) do (s, v)
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine): #vrne število min okoli polja (polje samo ne šteje)
    '''sosedi = 0
    if (x-1, y-1) in mine:
        sosedi += 1
    if (x-1, y) in mine:
        sosedi += 1
    if (x-1, y+1) in mine:
        sosedi += 1
    if (x, y-1) in mine:
        sosedi += 1
    if (x, y+1) in mine:
        sosedi += 1
    if (x+1, y-1) in mine:
        sosedi += 1
    if (x+1, y) in mine:
        sosedi += 1
    if (x+1, y+1) in mine:
        sosedi += 1
    return sosedi'''
    return (len([(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) #dolžina seznama sosednjih polj
                 if (i, j) in mine                                        #ki imajo mine
                 if (i, j) != (x, y)]))                                   #brez trenutnega polja


def najvec_sosedov(mine, s, v): #vrne koordinate polja, ki je obkroženo z največ minami
    '''najvec = 0
    najvec_polje = (0, 0)
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) > najvec: #če ima polje več sosedov kot prejšnji največji
                najvec = sosedov(i, j, mine)
                najvec_polje = (i, j) #se zamenjata
    return najvec_polje'''
    return max({(x, y): sosedov(x, y, mine) for x in range(s) for y in range(v)},           #slovar vseh polj in njihovih sosedov
               key = {(x, y): sosedov(x, y, mine) for x in range(s) for y in range(v)}.get) #vrne ključ največje vrednosti(polje z največ sosedi)
    #slovar = {(x, y): sosedov(x, y, mine) for x in range(s) for y in range(v)} #slovar vseh polj in njihovih sosedov
    #return max(slovar, key=slovar.get)


def brez_sosedov(mine, s, v): #vrne množico polj, ki nimajo na sosednjih poljih nobene mine
    '''brez = set()
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == 0: #če je brez sosedov
                brez.add((i, j)) #polje dodamo v množico
    return brez'''
    return {(x, y) for x in range(s) for y in range(v) #vrne množico polj
            if sosedov(x, y, mine) == 0}               #ki okoli nimajo nobene mine


def po_sosedih(mine, s, v): #vrne slovar s ključi od 0 do 8, ki vsebujejo množice polj z ustreznim številom sosedov
    '''slovar = {}
    for i in range(9):
        slovar[i] = set() #napolni slovar s praznimi množicami
    for i in range(s):
        for j in range(v):
            slovar[sosedov(i, j, mine)].add((i, j)) #doda polje z 'x' sosedi v ustrezno množico v slovarju
    return slovar'''
    return {i: {(x, y) for x in range(s) for y in range(v) #vrne slovar množic
                if sosedov(x, y, mine) == i}               #kjer so ključi število sosedov
                for i in range(9)}                         #vrednosti pa polja s tolikimi sosedi (če takih polj ni, vrne prazno množico)


########################
# Za oceno 7

def dolzina_poti(pot): #vrne dolžino poti
    '''dolzina = 0
    if pot: #če list ni prazen
        zacetek = pot[0]
        for i in pot[1:]: #vedno primerja s prejšnjim
            dolzina += abs(zacetek[0] - i[0]) #premik vodoravno
            dolzina += abs(zacetek[1] - i[1]) #premik navpično
            zacetek = i #nastavi novo pozicijo
    return dolzina'''
    return sum((abs(x0 - x1)) + abs(y0 - y1)                #vsota razlik med trenutno in naslednjo pozicijo (premik)
               for (x0, y0), (x1, y1) in zip(pot, pot[1:])) #za vse korake na poti


def varen_premik(x0, y0, x1, y1, mine): #vrne False, če ob premiku naletimo na mino (drugače True)
    '''if y0 == y1: #vodoraven premik
        if x0 < x1: #v desno
            for i in range(x0, x1+1):
                if (i, y0) in mine: #če je na poti mina
                    return False #R.I.P.
        else: #v levo
            for i in range(x1, x0+1):
                if (i, y0) in mine:
                    return False
    if x0 == x1: #navpičen premik
        if y0 < y1: #v desno
            for i in range(y0, y1+1):
                if (x0, i) in mine:
                    return False
        else: #v desno
            for i in range(y1, y0+1):
                if (x0, i) in mine:
                    return False
    return True'''
    return [(x, y) for x in range(min(x0, x1), max(x0+1, x1+1)) #vrne True, če je seznam polj z minami na poti prazen
            for y in range(min(y0, y1), max(y0+1, y1+1))        #min() in max(), ker ne vemo ali se premikamo gor ali dol (x0 je lahko manjši kot x1)
            if (x, y) in mine] == []                            #pri max() je +1, zaradi indeksiranja


def varna_pot(pot, mine): #vrne False, če po poti naletimo na mino (drugače True)
    '''if pot: #če list ni prazen
        if pot[0] in mine: #in če ne začnemo na mini
            return False
        zacetek = pot[0]
        for i in pot[1:]: #gremo po poti
            if not varen_premik(zacetek[0], zacetek[1], i[0], i[1], mine): #če je kjerkoli na poti mina
                return False #ded
            zacetek = i #nova pozicija
    return True'''
    return True if pot == []\
            else False if pot[0] in mine\
            else all([varen_premik(x0, y0, x1, y1, mine)  #vrne True, če so vsi premiki po poti varni (brez min)
            for (x0, y0), (x1, y1) in zip(pot, pot[1:])]) #True, če je pot prazna in False, če je začetno polje mina


########################
# Za oceno 8

def polje_v_mine(polje): #vrne množico koordinat polj z minami, ter širino in višino polja
    mreza = polje.split(' ') #razdeli polje po vrsticah
    sirina = 0 #x
    visina = 0 #y
    mine = set()
    for i in mreza: #i = vrstica
        if i: #če ni prazna vrstica, lahko resetira širino in prišteje višino (problem pri i = [] -> širina = 0, višina 1 preveč)
            sirina = 0
            for j in i: #j = stolpec
                if j == 'X': #če je na polju 'X'
                    mine.add((sirina, visina)) #zabeleži mino
                sirina += 1
            visina += 1
    return (mine, sirina, visina)


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi): #navodila za pot pretvori v seznam terk, ki kažejo premik po koordinatnem sistemu
    smer = 0 #0 = gor, 1 = desno, 2 = dol, 3 = levo (v smeri urinega kazalca)
    pot = [(0, 0)]
    x = 0 #x in y ne kot tuple (0, 0), saj se terk ne da spreminjati
    y = 0
    for i in ukazi.split():
        if i == 'DESNO': #obrat
            smer += 1
            smer = abs(smer % 4) #poskrbi, da ne gre pod 0 ali preko 3
        if i == 'LEVO': #obrat
            smer -= 1
            smer = abs(smer % 4)
        if i != 'DESNO' and i != 'LEVO': #premik (samo else ne dela)
            if smer == 0: #gor
                y -= int(i)
            if smer == 1: #desno
                x += int(i)
            if smer == 2: #dol
                y += int(i)
            if smer == 3: #levo
                x -= int(i)
            pot.append((x, y)) #v seznam pripne lokacijo po premiku
    return pot


def zapisi_pot(pot): #pot pretvori v ukaze
    navodila = []
    trenutno_polje = pot[0]
    smer = 0 #0 = gor, 1 = desno, 2 = dol, 3 = levo
    for i in pot[1:]:
        if trenutno_polje[0] == i[0]: #ni spremembe po x
            if trenutno_polje[1] < i[1]: #premik dol
                while smer != 2: #dokler ni poravnan v pravo smer
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO') #se obrača v desno
                navodila += str(i[1] - trenutno_polje[1]) #in doda dolžino premika
                trenutno_polje = i #po premiku ponastavimo trenutno polje
            if trenutno_polje[1] > i[1]: #gor
                while smer != 0:
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO')
                navodila += str(trenutno_polje[1] - i[1])
                trenutno_polje = i
        if trenutno_polje[1] == i[1]: #ni spremembe po y
            if trenutno_polje[0] < i[0]: #desno
                while smer != 1:
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO')
                navodila += str(i[0] - trenutno_polje[0])
                trenutno_polje = i
            if trenutno_polje[0] > i[0]: #levo
                while smer != 3:
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO')
                navodila += str(trenutno_polje[0] - i[0])
                trenutno_polje = i
    return ' '.join(navodila)


########################
#Testi (ne spreminjaj)
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

