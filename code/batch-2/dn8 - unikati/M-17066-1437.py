def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    elif (isinstance(ukaz, int)):
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    premiki = [(0,0,"N")]
    datoteka = open(ime_datoteke)
    ukazi = datoteka.read();
    splitted_u = ukazi.split("\n")
    startx = 0
    starty = 0
    smer = "N"
    for ukaz in splitted_u:
        ukaz_x = ukaz.split(" ")
        if (len(ukaz_x) == 2):
            ukaz = int(ukaz_x[1])
        pmk = premik(ukaz, startx, starty, smer)
        premiki.append(pmk)
        startx = pmk[0]
        starty = pmk[1]
        smer = pmk[2]
    premiki.remove(premiki[len(premiki) - 1])
    return premiki

def opisi_stanje(x, y, smer):
    if (smer == "N"):
        pusc = "^"
    elif (smer == "E"):
        pusc = ">"
    elif (smer == "S"):
        pusc = "v"
    elif (smer == "W"):
        pusc = "<"

    if (x < 10)and(x>=0):
        x = "  " + str(x)
    elif (x > 9)and(x < 100):
        x = " " + str(x)
    elif (x > -10) and (x < 0):
        x = " " + str(x)


    if (y < 10)and(y>=0):
        y = str(y) + "  "
    elif (y > 9)and(y<100):
        y = str(y) + " "
    elif (y > -10) and (y < 0):
        y = " " + str(y)

    return (str(x)+":"+str(y)+" "+pusc)

def prevedi(vhod, izhod):
    pot = izvedi(vhod)
    string_o = ""
    for x, y, smer in pot:
        string_o += opisi_stanje(x,y,smer) + "\n"

    dat = open(izhod, "w")
    dat.write(string_o)

def opisi_stanje_2(x,y, smer):
    if (smer == "N"):
        pusc = "^"
    elif (smer == "E"):
        pusc = ">"
    elif (smer == "S"):
        pusc = "v"
    elif (smer == "W"):
        pusc = "<"

    if (x < 10)and(x>=0):
        x = "  (" + str(x)
    elif (x > 9)and(x < 100):
        x = " (" + str(x)
    elif (x > 99)and(y<1000):
        x = "(" + str(x)
    elif (x > -10) and (x < 0):
        x = " (" + str(x)
    elif (x > -100) and (x < -9):
        x = "(" + str(x)


    y = str(y) + ")"

    return (pusc + " " + x + ":" + y)

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
