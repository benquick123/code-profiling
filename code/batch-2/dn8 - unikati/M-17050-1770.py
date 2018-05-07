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

def  izvedi(ime_datoteke):
    elementi = open(ime_datoteke).read().split("\n")
    smer = "N"
    x=0
    y=0
    nov = []

    nov.append(premik(0,x,y,smer))

    for element in elementi:

        if element == "DESNO":
            ukaz = "R"

        elif element== "LEVO":
            ukaz = "L"

        elif element.__len__()>6:

            if element.__len__()<7:
                ukaz = int(element[7])
            else:
                ukaz = int(element[7:])

        vpisi = premik(ukaz, x, y, smer)
        x=vpisi[0]
        y=vpisi[1]
        smer = vpisi[2]
        nov.append(vpisi)

    return nov[:len(nov)-1]

def opisi_stanje(x,y,smer):

    if smer=="N":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s="^")
    if smer=="E":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s=">")
    if smer=="S":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s="v")
    if smer=="W":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s="<")

def  prevedi(ime_vhoda,ime_izhoda):

    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")

    for element in seznam:
        datoteka.write(opisi_stanje(element[0],element[1],element[2])+"\n")
    datoteka.close()

def opisi_stanje_2(x,y,smer):

    if smer=="N":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s="^")
    if smer=="E":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s=">")
    if smer=="S":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s="v")
    if smer=="W":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s="<")





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
