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
    datoteka = open(ime_datoteke)
    x, y = 0, 0
    sm = "N"
    s = [(x, y, sm)]
    for ukaz in datoteka:
        if ukaz[0] == "D":
            p = premik("R", x, y, sm)
            s.append(p)
            x = p[0]
            y = p[1]
            sm = p[2]
        elif ukaz[0] == "L":
            p = premik("L", x, y, sm)
            s.append(p)
            x = p[0]
            y = p[1]
            sm = p[2]
        else:
            st = int(ukaz.split()[1])
            p = premik(st, x, y, sm)
            s.append(p)
            x = p[0]
            y = p[1]
            sm = p[2]
    return s


def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "W":
        znak = '<'
    else:
        znak = 'v'
    return("{x:>3}:{y:<3} {znak}".format(y=y, x=x, znak=znak))



def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    s = izvedi(ime_vhoda)
    for ukaz in s:
        bla = opisi_stanje(ukaz[0], ukaz[1], ukaz[2])
        datoteka.write("{}\n".format(bla))
    datoteka.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "W":
        znak = '<'
    else:
        znak = 'v'
    oklepaj = "({x}".format(x=x)
    return ("{znak} {x:>4}:{y})".format(y=y, x=oklepaj, znak=znak))



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
