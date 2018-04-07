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


# Napiši funkcijo izvedi(ime_datoteke), ki kot argument dobi ime datoteke z ukazi, ki naj jih robot izvede. Datoteka je oblike:
#   DESNO
#   NAPREJ 12
#   DESNO
#   NAPREJ 2
#   LEVO
#   NAPREJ 3
#   LEVO
#   LEVO
# Funkcija mora vrniti seznam zaporednih stanj, torej trojk z vrednostmi x, y in smeri, skozi katere gre robot, ko izvaja ta program.
# Robot je v začetku na koordinatah (0, 0) in obrnjen proti severu.
# Gornji ukazi so shranjeni v datoteki primer.txt. Če pokličemo funkcijo z izvedi("primer.txt"), vrne
#   [(0, 0, 'N'), (0, 0, 'E'), (12, 0, 'E'),
#   (12, 0, 'S'),  (12, 2, 'S'), (12, 2, 'E'),
#   (15, 2, 'E'), (15, 2, 'N'), (15, 2, 'W')]
# Funkcija lahko uporablja podano funkcijo premik (oziroma je to celo priporočeno). Samo za prevajanje ukazov v angleščino in številke boste morali poskrbeti.

def izvedi(ime_datoteke):
    seznam = []
    seznam2 = []
    seznamT = []
    dat = open(ime_datoteke, encoding='utf8')

    for vrstica in dat:
        seznam.append(vrstica.strip())

    for i in seznam:
        if i == "DESNO":
            seznam2.append("R")
            continue

        elif i == "LEVO":
            seznam2.append("L")
            continue

        else:
            novNiz = i.split()
            seznam2.append(int(novNiz[1]))

    seznamT.append((0, 0, "N"))
    zadnjaP = (0, 0, "N")

    for u in seznam2:
        seznamT.append(premik(u, zadnjaP[0], zadnjaP[1], zadnjaP[2]))
        zadnjaP = premik(u, zadnjaP[0], zadnjaP[1], zadnjaP[2])

    dat.close()

    return seznamT


# Napiši funkcijo opisi_stanje(x, y, smer), ki vrne niz z opisom stanja.
# Stanje je opisano s koordinatama, med katerima je dvopičje; koordinata x je poravnana desno, y pa levo.
# Obe sta izpisani na tri mesta. Sledi presledek in znak, ki pove smer. Znaki za smeri so ^, >, v in < (za N, E, S in W).
# Klic opisi_stanje(0, 12, "N") vrne niz "  0:12  ^". (Pazi na presledke).

def opisi_stanje(x, y, smer):
    if smer == "N":
        smeri = "^"

    elif smer == "E":
        smeri = ">"

    elif smer == "S":
        smeri = "v"

    elif smer == "W":
        smeri = "<"

    return "{:>3}:{:<4}{}".format(x, y, smeri)


# Napiši funkcijo prevedi(ime_vhoda, ime_izhoda).
# Funkcija mora prebrati vhodno datoteko (najbrž tako, da pokliče funkcijo izvedi?) in v izhodno datoteko izpisati zaporedje stanj v obliki,
# kot jo vrača funkcija opisi_stanje.
# Če pokličemo prevedi("primer.txt", "stanja.txt"), mora ustvariti datoteko stanja.txt z naslednjo vsebino:
#   0:0   ^
#   0:0   >
#   12:0   >
#   12:0   v
#   12:2   v
#   12:2   >
#   15:2   >
#   15:2   ^
#   15:2   <

def prevedi(ime_vhoda, ime_izhoda):
    datotekaVpis = izvedi(ime_vhoda)
    datotekaIzpis = open(ime_izhoda, "w")

    for t in datotekaVpis:
        datotekaIzpis.write(opisi_stanje(t[0], t[1], t[2]) + "\n")

    datotekaIzpis.close()


# Napiši funkcijo opisi_stanje_2(x, y, smer), ki je podobna funkciji opisi_stanje,
# le da je smer na začetku in da so okrog koordinat oklepaji, takole ^   (0:12).
# Koordinata x naj, skupaj z oklepajem, zasede štiri mesta.

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smeri = "^"

    elif smer == "E":
        smeri = ">"

    elif smer == "S":
        smeri = "v"

    elif smer == "W":
        smeri = "<"

    return "{}{:>3}{}{}:{}{}".format(smeri," ", "(", x, y, ")")


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
