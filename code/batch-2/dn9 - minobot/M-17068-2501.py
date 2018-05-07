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

def angleski(ime_datoteke):
    t = open(ime_datoteke, encoding="utf - 8")
    s = t.read().split()
    popsez = []
    for i, x in enumerate(s):
        if x[0] == "D":
            popsez.append("R")
        if x[0] == "L":
            popsez.append(x[0])
        if x[0] == "N":
            popsez.append(s[i + 1])
    return popsez

def izvedi(ime_datoteke):
    x, y, smer = 0, 0, "N"
    stanja = []
    stanja.append((x, y, smer))
    for e in angleski(ime_datoteke):
        if e == "R" or e == "L":
            ukaz = e
        else:
            ukaz = int(e)
        stanja.append(premik(ukaz, x, y, smer))
        x, y, smer = premik(ukaz, x, y, smer)
    return stanja

def opisi_stanje(x, y, smer):
    s = {"N" : "^", "E" : ">",
        "S" : "v", "W" : "<" }
    return "{:>3}:{:<3}{:>2}".format(x,y,s[smer])

def prevedi(ime_vhoda, ime_izhoda):
    t = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        t.write(opisi_stanje(x, y, smer) + "\n")
    t.close()

def opisi_stanje_2(x, y, smer):
    s = {"N" : "^", "E" : ">",
            "S" : "v", "W" : "<"}
    if 99 > x > 9 or x < 0:
        return "{:<3}({:}:{:>})".format(s[smer], x ,y)
    if x > 99:
        return "{:<2}({:}:{:>})".format(s[smer], x ,y)
    else:
        return "{:<4}({:}:{:>})".format(s[smer], x ,y)



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
