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
    pot = [(0, 0, 'N')]
    x = 0
    y = 0
    smer = "N"

    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        if vrstica.split()[0] == "DESNO":
            p = premik("R", x, y, smer)
            pot.append(p)
            x = p[0]
            y = p[1]
            smer = p[2]
        elif vrstica.split()[0] == "LEVO":
            p = premik("L", x, y, smer)
            pot.append(p)
            x = p[0]
            y = p[1]
            smer = p[2]
        elif vrstica.split()[0] == "NAPREJ":
            p = premik(int(vrstica.split()[1]), x, y, smer)
            pot.append(p)
            x = p[0]
            y = p[1]
            smer = p[2]
    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:>3}:{:<3} ^".format(x, y)
    elif smer == "E":
        return "{:>3}:{:<3} >".format(x, y)
    elif smer == "S":
        return "{:>3}:{:<3} v".format(x, y)
    elif smer == "W":
        return "{:>3}:{:<3} <".format(x, y)

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    print(datoteka)

    for element in seznam:
        datoteka.write(opisi_stanje(element[0], element[1], element[2]) + '\n')
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        oklepaj_in_x = "(" + str(x)
        return "^ {:>4}:{})".format(oklepaj_in_x, y)
    elif smer == "E":
        oklepaj_in_x = "(" + str(x)
        return "> {:>4}:{})".format(oklepaj_in_x, y)
    elif smer == "S":
        oklepaj_in_x = "(" + str(x)
        return "v {:>4}:{})".format(oklepaj_in_x, y)
    elif smer == "W":
        oklepaj_in_x = "(" + str(x)
        return "< {:>4}:{})".format(oklepaj_in_x, y)


#PRINT

ime_datoteke = "primer.txt"
print(izvedi(ime_datoteke))

print(opisi_stanje(0, 12, "N"))

ime_vhoda = "ukazi.txt"
ime_izhoda = "stanja.txt"
print(prevedi(ime_vhoda, ime_izhoda))

print(opisi_stanje_2(0, 3, "N"))


#TESTI

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
