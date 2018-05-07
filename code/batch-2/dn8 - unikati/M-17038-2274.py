def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    x = 0
    y = 0
    smer = "N"
    move = []
    move.append((x, y, smer))
    datoteka = open(ime_datoteke)

    for all in datoteka:
        order = all.strip()
        if order == "DESNO":
            ukaz = "R"
            x, y, smer = premik(ukaz, x, y, smer)
            move.append((x, y, smer))
        elif order == "LEVO":
            ukaz = "L"
            x, y, smer = premik(ukaz, x, y, smer)
            move.append((x, y, smer))
        else:
            ukaz = order.split(" ")
            x, y, smer = premik(int(ukaz[1]), x, y, smer)
            move.append((x, y, smer))

    datoteka.close()

    return move

def opisi_stanje(x, y, smer):
    spacey = ""
    spacex = ""
    if smer== "N":
        smer="^"

    if smer== "S":
        smer= "v"

    if smer== "E":
        smer= ">"

    if smer== "W":
        smer= "<"

    for i in range(3,len(str(x)),-1):
        spacex= spacex+" "

    for i in range(3, len(str(y))-1 , -1):
        spacey = spacey + " "


    return spacex+str(x)+":"+str(y)+ spacey+smer


def prevedi(ime_vhoda, ime_izhoda):
    Igotdamoves=izvedi(ime_vhoda)
    orders=[]
    for x,y,smer in Igotdamoves:
        orders.append(opisi_stanje(x,y,smer))
    datoteka=open(ime_izhoda,"w")

    for order in orders:
        datoteka.write(order+"\n")

    datoteka.close()

def opisi_stanje_2(x, y, smer):
    spacex = ""
    if smer == "N":
        smer = "^"

    if smer == "S":
        smer = "v"

    if smer == "E":
        smer = ">"

    if smer == "W":
        smer = "<"

    for i in range(4, len(str(x)), -1):
        spacex = spacex + " "


    return smer+spacex + "("+ str(x) +  ":" + str(y) + ")"



import unittest
class TestObvezna(unittest.TestCase):
    def test_branje(self):
        self.assertEqual(
            izvedi("primer.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (12, 0, 'E'), (12, 0, 'S'), (12, 2, 'S'),
             (12, 2, 'E'), (15, 2, 'E'), (15, 2, 'N'), (15, 2, 'W')]
        )
        self.assertEqual(
            izvedi("ukazi.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'), (1, 0, 'W'),
             (0, 0, 'W'), (0, 0, 'S'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'),
             (1, 3, 'S'), (1, 3, 'E'), (2, 3, 'E'), (2, 3, 'S'), (2, 3, 'W')]
        )

    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje(0, 12, "N"), "  0:12  ^")
        self.assertEqual(opisi_stanje(111, 0, "E"), "111:0   >")
        self.assertEqual(opisi_stanje(-2, 111, "S"), " -2:111 v")
        self.assertEqual(opisi_stanje(0, 0, "W"), "  0:0   <")

    def test_prevedi(self):
        from random import randint
        import os
        ime = "izhod{:05}.txt".format(randint(0, 99999))
        try:
            self.assertIsNone(prevedi("primer.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
 12:0   >
 12:0   v
 12:2   v
 12:2   >
 15:2   >
 15:2   ^
 15:2   <""")

            self.assertIsNone(prevedi("ukazi.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
  1:0   >
  1:0   v
  1:0   <
  0:0   <
  0:0   v
  0:0   >
  1:0   >
  1:0   v
  1:3   v
  1:3   >
  2:3   >
  2:3   v
  2:3   <""")
        finally:
            os.remove(ime)

        vime = "vhod{:05}.txt".format(randint(0, 99999))
        open(vime, "wt").write("NAPREJ 23\nLEVO\nNAPREJ 17\n")
        try:
            self.assertIsNone(prevedi(vime, ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:-23 ^
  0:-23 <
-17:-23 <""")
        finally:
            os.remove(ime)
            os.remove(vime)


class TestDodatna(unittest.TestCase):
    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje_2(0, 12, "N"),   "^   (0:12)")
        self.assertEqual(opisi_stanje_2(111, 0, "E"),  "> (111:0)")
        self.assertEqual(opisi_stanje_2(-2, 111, "S"), "v  (-2:111)")
        self.assertEqual(opisi_stanje_2(0, 0, "W"),    "<   (0:0)")


if __name__ == "__main__":
    unittest.main()
