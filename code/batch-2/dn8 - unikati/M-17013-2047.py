#__________________________ NALOGA 9 ______________________________

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

#____________________________________________________________________

def izvedi(ime_datoteke):
    x, y = 0, 0
    s = 'N'
    pot = [(x, y, s)]
    for i in open(ime_datoteke):
        if i == "DESNO\n":
            x, y, s = premik("R",x, y, s)
            pot.append((x, y, s))
        elif i == "LEVO\n":
            x, y, s = premik("L", x, y, s)
            pot.append((x, y, s))
        elif i.split()[0] == "NAPREJ":
            stevilo = i.split()[1]
            x, y, s = premik(int(stevilo), x, y, s)
            pot.append((x, y, s))
    return pot

print(izvedi("primer.txt"))


def opisi_stanje(x,y,smer):
    smeri = {'N' : '^', 'E' : '>', 'S' : 'v', 'W' : '<'}

    sx = ' ' * (3-len(str(x))) + str(x)
    sy = str(y) + ' ' * (3 + 1 - len(str(y)))
    return (sx + ":" + sy + smeri[smer])

print(opisi_stanje(0, 12, "N"))


def prevedi(ime_vhoda, ime_izhoda):
    pot = izvedi(ime_vhoda)
    s = open(ime_izhoda, 'w')
    for i in pot:
        s.write(opisi_stanje(i[0], i[1], i[2]) + '\n')
    s.close()

def opisi_stanje_2(x, y, smer):
    smeri = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
    sp = " " * (4 - len(str(x)))
    return (smeri[smer] + sp + "(" + str(x) + ":" + str(y) + ")")

print(opisi_stanje_2(0, 12, "N"))

#_________________________________________ TESTI  _________________________________________

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
