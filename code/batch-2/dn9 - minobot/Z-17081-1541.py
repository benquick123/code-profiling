#
#1.Napiši funkcijo izvedi(ime_datoteke), ki kot argument dobi ime datoteke z ukazi, ki naj jih robot izvede. Datoteka je oblike:

def izvedi(ime_datoteke):
    datoteka=open(ime_datoteke)
    novi_seznam_premikov=[]
    x=0
    y=0
    novo_stanje=(0,0,"N")
    novi_seznam_premikov.append(novo_stanje)
    trenutna_smer= "N"

    for vrstica in datoteka:
        ukazi=vrstica.split(" ")
        print(ukazi)
        if len(ukazi) ==1:
            smer_ukaz="" #prazni niz
            smer=ukazi[0].strip()
            if smer == "DESNO":
                smer_ukaz="R"
            elif smer == "LEVO":
                smer_ukaz= "L"

            novo_stanje=premik(smer_ukaz,x,y,trenutna_smer)

        elif len(ukazi)==2:
            premik_kvadratek=int(ukazi[1].strip())
            novo_stanje=premik(premik_kvadratek,x,y,trenutna_smer)
        novi_seznam_premikov.append(novo_stanje)
        x = novo_stanje[0]
        y = novo_stanje[1]
        trenutna_smer = novo_stanje[2]
    print(novi_seznam_premikov)
    return novi_seznam_premikov

def opisi_stanje(x,y,smer): # ^, >, v in <
    if smer == "N":
        smer_znak="^"
    elif smer== "W":
        smer_znak="<"
    elif smer =="S":
        smer_znak="v"
    elif smer=="E":
        smer_znak=">"

    niz= "{x:3}:{y:3}".format(x=x, y=str(y)) + " " + smer_znak

    return niz

#Napiši funkcijo prevedi(ime_vhoda, ime_izhoda). Funkcija mora prebrati vhodno datoteko (najbrž tako, da pokliče funkcijo izvedi?) in v izhodno datoteko izpisati zaporedje stanj v obliki, kot jo vrača funkcija opisi_stanje.

#Če pokličemo prevedi("primer.txt", "stanja.txt"), mora ustvariti datoteko stanja.txt z naslednjo vsebino:

def prevedi(ime_vhoda, ime_izhoda):
    seznam_premikov=izvedi(ime_vhoda)
    datoteka_za_pisanje=open(ime_izhoda,"w")
    for x,y,smer in seznam_premikov:

        stanje=opisi_stanje(x,y,smer)
        datoteka_za_pisanje.write(stanje + "\n")
    datoteka_za_pisanje.close()

#DODATNA

def popravi(str):
    for i in range (len(str)):
        znak=str[i]
        if znak!=" ":
            str=str[:i]+"("+str[i:]

            break
    return str

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        smer_znak = "^"
    elif smer == "W":
        smer_znak = "<"
    elif smer == "S":
        smer_znak = "v"
    elif smer == "E":
        smer_znak = ">"

    niz = smer_znak+ popravi("{x:4}:{y})".format(x=x, y=str(y)) )

    return niz































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
