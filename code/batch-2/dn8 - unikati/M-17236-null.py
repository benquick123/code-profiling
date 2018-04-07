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

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda


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
    x = 0
    y = 0
    smeri = "NESW"
    ismer = 0
    smer = (smeri[ismer])
    seznam = []
    seznam.append(premik(0, x, y, smer))
    for vrstica in datoteka:

        if (izloci_besedo(vrstica) == "DESNO"):
            seznam.append(premik("R", x, y, smeri[ismer]))
            if (ismer < 3):
                ismer += 1
            else:
                ismer = 0

        if (izloci_besedo(vrstica) == "LEVO"):
            seznam.append(premik("L", x, y, smeri[ismer]))
            if (ismer > 0):
                ismer -= 1
            else:
                ismer = 3

        if (vrstica.split(" ")[0] == "NAPREJ"):
            seznam.append(premik(int(vrstica.split(" ")[1]), x, y, smeri[ismer]))
            x = seznam[len(seznam) - 1][0]
            y = seznam[len(seznam) - 1][1]

    return seznam


def opisi_stanje(x,y,smer):
    znak=""
    if(smer=="N"):
        znak="^"
    if(smer=="E"):
        znak=">"
    if(smer=="S"):
        znak="v"
    if(smer=="W"):
        znak="<"

    return("{a:>3}:{b:<4}".format(a=x, b=y)+znak)


def prevedi(ime_vhoda,ime_izhoda):
    datoteka2 = open(ime_izhoda, "w+")

    for i in izvedi(ime_vhoda):
        datoteka2.write(opisi_stanje(i[0], i[1], i[2])+"\n")



def opisi_stanje_2(x,y,smer):
    znak = ""
    if (smer == "N"):
        znak = "^"
    if (smer == "E"):
        znak = ">"
    if (smer == "S"):
        znak = "v"
    if (smer == "W"):
        znak = "<"
    x="("+str(x)
    y= str(y)+")"
    return(znak+"{a:>5}:{b}".format(a=x, b=y))



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
