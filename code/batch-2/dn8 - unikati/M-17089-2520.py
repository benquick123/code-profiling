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
    smer = 'N'
    x = 0
    y = 0
    stanja = [(0, 0, 'N')]
    datoteka = open(ime_datoteke, encoding='utf-8')
    b = datoteka.read().splitlines()
    for ukaz in b:
        if ukaz == 'DESNO':
            raz = 'R'
        if ukaz == 'LEVO':
            raz = 'L'
        if ukaz.split(" ")[0] == "NAPREJ":
            dm = ukaz.split(" ")[1]
            raz = float(dm)
        c = premik(raz, x, y, smer)
        x = c[0]
        y = c[1]
        smer = c[2]
        stanja.append(c)
    return stanja

def opisi_stanje(x, y, smer):
    if smer == 'N':
        smer = '^'
    elif smer == 'E':
        smer = '>'
    elif smer == 'S':
        smer = 'v'
    elif smer == 'W':
        smer = '<'
    x = x
    y = y
    c = "{x:>3}:{y:<3}{s:>2}".format(s=smer, x=x, y=y)
    return c

def prevedi(ime_vhoda, ime_izhoda):
    b = izvedi(ime_vhoda)
    ime_izhoda = open(ime_izhoda, "w")
    for tocka in b:
        x = tocka[0]
        y = tocka[1]
        smer = tocka[2]
        c = opisi_stanje(int(x), int(y), smer)
        d = c[8]
        z = "{x:>3.0f}:{y:<3.0f}{d:>2}".format(x=x, y=y, d=d)
        ime_izhoda.write(z + '\n')
    ime_izhoda.close()

def opisi_stanje_2(x, y, smer):
    z = opisi_stanje(x, y, smer)
    h = "{:<2}{:>4}:{:<0}".format(z[8], '('+str(x), str(y)+')')
    return h


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
