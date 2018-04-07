
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
    stevec = 1
    dat = open(ime_datoteke, encoding="utf8")
    x = y = 0
    s = [(0,0,"N")]
    smer = "N"
    for vrstica in dat:
        vrstica = vrstica.rstrip()
        if vrstica == "DESNO":
            ukaz = "R"
        elif vrstica == "LEVO":
            ukaz = "L"
        else:
            a = vrstica.split(" ")
            ukaz = a[1]
            ukaz = int(ukaz)

        s.append(premik(ukaz, x, y, smer))
        x = s[stevec][0]
        y = s[stevec][1]
        smer = s[stevec][2]
        stevec +=1
    return s

def opisi_stanje(x, y, smer):
    if smer == "N":
        puscica = "^"
    elif smer == "S":
        puscica = "v"
    elif smer == "E":
        puscica = ">"
    elif smer == "W":
        puscica = "<"
    return ("{x:>3}:{y:<4}{puscica}".format(x=x,y=y,puscica=puscica))

def prevedi(ime_vhoda, ime_izhoda):
    dat = open(ime_vhoda, encoding="utf8")
    u = open(ime_izhoda,"w", encoding="utf8")
    b = izvedi(ime_vhoda)
    for x, y, smer in b:
        print(opisi_stanje(x,y,smer),file=u)

    dat.close()
    u.close()





def opisi_stanje_2(x, y, smer):
    if smer == "N":
        puscica = "^"
    elif smer == "S":
        puscica = "v"
    elif smer == "E":
        puscica = ">"
    elif smer == "W":
        puscica = "<"
    return ("{puscica}{x:>5}:{y})".format(x=("("+str(x)),y=y,puscica=puscica))









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
