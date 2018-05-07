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


#Uporabniske funkcije:

def izvedi(ime_datoteke):
    s = [(0, 0, 'N')]
    try:
        with open(ime_datoteke) as the_file:
            line = the_file.readline()
            if line:
                if line.strip() == "DESNO":
                    prejsnji = premik("R", 0, 0, "N")
                elif line.strip() == "LEVO":
                    prejsnji = premik("L", 0, 0, "N")
                else:
                    st = int(line.strip().split(" ")[1])
                    prejsnji = premik(st, 0, 0, "N")
                s.append(prejsnji)
                line = the_file.readline()
                while line:
                    if line.strip() == "DESNO":
                        prejsnji = premik("R", prejsnji[0], prejsnji[1], prejsnji[2])
                    elif line.strip() == "LEVO":
                        prejsnji = premik("L", prejsnji[0], prejsnji[1], prejsnji[2])
                    else:
                        st = int(line.strip().split(" ")[1])
                        prejsnji = premik(st, prejsnji[0], prejsnji[1], prejsnji[2])
                    s.append(prejsnji)
                    line = the_file.readline()
            else:
                print("Prazna datoteka!")
    finally:
        the_file.close()
    return s


def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "S":
        znak = 'v'
    else:
        znak = '<'
    return '{:>3}:{:<3} {}'.format(x, y, znak)


def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    with open(ime_izhoda, "w") as the_file:
        for x, y, smer in s:
            the_file.write(opisi_stanje(x, y, smer) + "\n")


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "S":
        znak = 'v'
    else:
        znak = '<'
    return '{} {:>4}:{})'.format(znak, "(" + str(x), y)




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
