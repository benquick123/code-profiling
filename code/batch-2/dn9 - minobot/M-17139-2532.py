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
    ukazi = [(0, 0, "N")]
    tre_ukaz = (0, 0, "N")

    dat = open(ime_datoteke)
    vrstice = dat.readlines()
    dat.close()

    for vrstica in vrstice:

        vrstica = vrstica.strip()

        if vrstica == "DESNO":
            nov_ukaz = premik("R", tre_ukaz[0], tre_ukaz[1], tre_ukaz[2])
            ukazi.append(nov_ukaz)
            tre_ukaz = nov_ukaz
            continue

        elif vrstica == "LEVO":
            nov_ukaz = premik("L", tre_ukaz[0], tre_ukaz[1], tre_ukaz[2])
            ukazi.append(nov_ukaz)
            tre_ukaz = nov_ukaz
            continue

        else:
            ukaz = vrstica.split()
            nov_ukaz = premik(int(ukaz[1]), tre_ukaz[0], tre_ukaz[1], tre_ukaz[2])
            ukazi.append(nov_ukaz)
            tre_ukaz = nov_ukaz
            continue

    return ukazi


def opisi_stanje(x, y, smer):
    if smer == "N":
        smer_puscica = "^"

    elif smer == "E":
        smer_puscica = ">"

    elif smer == "S":
        smer_puscica = "v"

    else:
        smer_puscica = "<"

    izpis = "{:>3}:{:<3} {}".format(x, y, smer_puscica)

    return izpis


def prevedi(ime_vhoda, ime_izhoda):
    osnovna_pot = izvedi(ime_vhoda)
    koncna_pot = []

    for korak in osnovna_pot:
        koncna_pot.append(opisi_stanje(korak[0], korak[1], korak[2]))

    pisanje = open(ime_izhoda, "w")

    for korak in koncna_pot:
        pisanje.write(korak)
        pisanje.write("\n")

    pisanje.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer_puscica = "^"

    elif smer == "E":
        smer_puscica = ">"

    elif smer == "S":
        smer_puscica = "v"

    else:
        smer_puscica = "<"

    str_x = "(" + str(x)

    izpis = "{} {:>4}:{})".format(smer_puscica, str_x, y)

    return izpis


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
        self.assertEqual(opisi_stanje_2(0, 12, "N"), "^   (0:12)")
        self.assertEqual(opisi_stanje_2(111, 0, "E"), "> (111:0)")
        self.assertEqual(opisi_stanje_2(-2, 111, "S"), "v  (-2:111)")
        self.assertEqual(opisi_stanje_2(0, 0, "W"), "<   (0:0)")


if __name__ == "__main__":
    unittest.main()
