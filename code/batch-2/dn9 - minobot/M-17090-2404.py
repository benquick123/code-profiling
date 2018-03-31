def premik(ukaz, x, y, smer): #vrne koordinate in smer minobota po premiku
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R": #obrat v desno
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L": #obrat v levo
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer] #premik za 'ukaz' polj
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer


#OBVEZNI DEL

def izvedi(ime_datoteke): #vrne seznam vseh premikov robota
    datoteka = open(ime_datoteke)
    x = 0
    y = 0
    smer = 'N'
    ukaz = 0
    seznam_ukazov = [(0, 0, 'N')]
    for vrstica in datoteka:
        vrstica = vrstica.split() #preberemo vrstice v datoteki z ukazi
        if vrstica[0] == 'LEVO': #pretvorimo ukaze za funkcijo premik()
            ukaz = 'L'
        if vrstica[0] == 'DESNO':
            ukaz = 'R'
        if vrstica[0] == 'NAPREJ':
            ukaz = int(vrstica[1])
        x, y, smer = premik(ukaz, x, y, smer) #dobimo nove koordinate in smer s pomočjo funkcije premik()
        seznam_ukazov.append((x, y, smer)) #seznamu pripnemo koordinate in smer po premiku
    #print(seznam_ukazov)
    return seznam_ukazov

def opisi_stanje(x, y, smer): #v drugačnem zapisu vrne trenutne koordinate in smer robota
    smer_znak = ''
    if smer == 'N':
        smer_znak = '^'
    if smer == 'E':
        smer_znak = '>'
    if smer == 'S':
        smer_znak = 'v'
    if smer == 'W':
        smer_znak = '<'
    #print ('{x:>3}:{y:<3} {smer_znak}'.format(x=x, y=y, smer_znak=smer_znak))
    return '{x:>3}:{y:<3} {smer_znak}'.format(x=x, y=y, smer_znak=smer_znak)

def prevedi(ime_vhoda, ime_izhoda): #ustvari novo datoteko z drugačnimi zapisi stanj med premiki
    ukazi = izvedi(ime_vhoda) #seznam ukazov
    datoteka = open(ime_izhoda, "w") #nova datoteka, kamor bomo zapisali premike
    for ukaz in ukazi:
        x, y, smer = ukaz[0], ukaz[1], ukaz[2]
        datoteka.write(opisi_stanje(x, y, smer)) #v datoteko zapišemo stanje
        datoteka.write('\n') #in se prestavimo v naslednjo vrstico
    datoteka.close() #po pisanju datoteko zapremo
    return


#DODATNI DEL

def opisi_stanje_2(x, y, smer): #še drugače zapiše stanje robota
    smer_znak = ''
    if smer == 'N':
        smer_znak = '^'
    if smer == 'E':
        smer_znak = '>'
    if smer == 'S':
        smer_znak = 'v'
    if smer == 'W':
        smer_znak = '<'
    stanje = '{smer_znak}'.format(smer_znak=smer_znak)
    if x >= 0 and x <= 9: #zasede eno mesto (0:9)
        stanje += '   ({x:>}:{y:<})'.format(x=x, y=y)
        #print(stanje)
        return stanje
    if (x >= -9 and x < 0) or x <= 99: #zasede 2 mesti (-9:-1, 10:99)
        stanje += '  ({x:>}:{y:<})'.format(x=x, y=y)
        #print(stanje)
        return stanje
    if (x >= -99 and x < -9) or x <= 999: #zasede 3 mesta (-99:-10, 100:999)
        stanje += ' ({x:>}:{y:<})'.format(x=x, y=y)
        #print(stanje)
        return stanje


########################
#TESTI (ne spreminjaj)
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
