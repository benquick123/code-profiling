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
    list = []
    list.append(premik(0, x, y, smer))

    s = [line.rstrip('\n') for line in open(ime_datoteke)]

    for i in s:
        if " " in i:
            a, b = i.split(" ")
            b = int(b)


            if smer == "N":
                list.append(premik(b, x, y, smer))
                y = y - b
            elif smer == "S":
                list.append(premik(b, x, y, smer))
                y = y + b
            elif smer == "W":
                list.append(premik(b, x, y, smer))
                x = x - b
            elif smer == "E":
                list.append(premik(b, x, y, smer))
                x = x + b

        else:
            if smer == "N":
                if i == "DESNO":
                    smer = "E"
                elif i == "LEVO":
                    smer = "W"
            elif smer == "E":
                if i == "DESNO":
                    smer = "S"
                elif i == "LEVO":
                    smer = "N"
            elif smer == "S":
                if i == "DESNO":
                    smer = "W"
                elif i == "LEVO":
                    smer = "E"
            elif smer == "W":
                if i == "DESNO":
                    smer = "N"
                elif i == "LEVO":
                    smer = "S"

            list.append(premik(0, x, y, smer))
    return list

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer = "v"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"

    return("{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer=smer))

def prevedi(ime_vhoda, ime_izhoda):
    #datoteka = open(ime_izhoda, "w")
    s = izvedi(ime_vhoda)

    with open(ime_izhoda, "w") as datoteka:
        for i in s:
            x, y, smer = i
            datoteka.write(opisi_stanje(x, y, smer) + "\n")
    datoteka.close()

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
