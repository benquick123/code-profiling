import unittest


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
    with open(ime_datoteke, 'r') as infile:
        x = y = 0
        smer = 'N'
        list_of_commands = [(x, y, smer)]
        for line in infile:
            preety_line = line.split()
            if preety_line[0] == "DESNO":
                x, y, smer = premik('R', x, y, smer)
                list_of_commands.append((x, y, smer))
            elif preety_line[0] == "LEVO":
                x, y, smer = premik('L', x, y, smer)
                list_of_commands.append((x, y, smer))
            else:
                x, y, smer = premik(int(preety_line[1]), x, y, smer)
                list_of_commands.append((x, y, smer))
    return list_of_commands


def opisi_stanje(x, y, smer):
    ezi_naloga = {'N': '^', 'S': 'v', 'E': '>', 'W': '<'}
    return "{x:>3}:{y:<3} {smer}".format(x=x,y=y,smer=ezi_naloga[smer])


def prevedi(ime_vhoda, ime_izhoda):
    sez_ukazov = izvedi(ime_vhoda)
    sez_lepih_ukazov = [opisi_stanje(x, y, smer) for (x, y, smer) in sez_ukazov]
    file = open(ime_izhoda, 'w')
    for lep_ukaz in sez_lepih_ukazov:
        file.write(str(lep_ukaz + "\n"))
    file.close()


def opisi_stanje_2(x, y, smer):
    ezi_naloga2 = {'N': '^', 'S': 'v', 'E': '>', 'W': '<'}
    return "{smer}{x:>5}:{y})".format(smer=ezi_naloga2[smer], x="("+str(x), y=y)




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
