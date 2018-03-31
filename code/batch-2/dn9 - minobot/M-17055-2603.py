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
    rezultat = []
    ukaz = 0
    kon = "N"
    x,y = 0,0
    rezultat.append((premik(ukaz,x,y,kon)))

    with open(ime_datoteke) as f:
        vsebina = f.read().splitlines()
        #print(vsebina)

    for i in vsebina:
        n = i[-1:]
        for u in n:
            if u.isdigit():
                a = i[-2:]
                a = int(a)
                #print (a)
                break

        crka = i[0]
        if crka == "D":
            crka = "R"
        #print (crka)

        if crka == "N":
            rezultat.append((premik(a, x, y, kon)))
            for e in rezultat:
                x,y,kon = e

        elif crka == "D" or "L":
            rezultat.append((premik(crka, x, y, kon)))
            for e in rezultat:
                x, y, kon = e
        print(rezultat)
    return rezultat


def opisi_stanje(x,y,smer):

    if smer =="N":
        smer = "^"

    elif smer =="W":
        smer = "<"

    elif smer =="S":
        smer = "v"

    elif smer =="E":
        smer = ">"
    return("{:>3}:{:<3} {}".format(x,y,smer))


def prevedi(ime_vhoda, ime_izhoda):

    datoteka = open(ime_izhoda,"w")
    a = izvedi(ime_vhoda)
    for i in a:
        x,y,smer = i
        c = opisi_stanje(x,y,smer)
        datoteka.write(c)
        datoteka.write("\n")
    datoteka.close()
    return





def opisi_stanje_2(x, y, smer):
    a = []
    if smer =="N":
        smer = "^"

    elif smer =="W":
        smer = "<"

    elif smer =="S":
        smer = "v"

    elif smer =="E":
        smer = ">"
    b = "({}:".format(x)
    c = "{})".format(y)

    a.append(smer)
    a.append(b)
    a.append(c)

    return ("{a[0]}{a[1]:"">6}{a[2]}".format(a = a))


































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
