import unittest

def migracije(ime_datoteke):
    dat=open(ime_datoteke)
    sez=[]
    for a in dat:
        str=a.split("->")
        niz1=str[0].split(" ")
        if len(niz1)>3:
            kraj1=niz1[1]+" "+niz1[2]
        else:
            kraj1=niz1[1]
        st=niz1[0].rstrip(":")

        niz2=str[1].split(" ")
        if len(niz2)>1:
            kraj2=niz2[0]+" "+niz2[1][:-1]
        else:
            kraj2=niz2[0][:-1]

        terka=(st,kraj1,kraj2)
        sez.append(terka)

        maribor = (0, 0,"Maribor")
        ljubljana = (0, 0,"Ljubljana")
        gorica = (0, 0,"Nova Gorica")
        koper = (0, 0,"Koper")
        nmesto = (0, 0,"Novo mesto")

        for b in sez:
            if b[1] == "Ljubljana":
                b[0] = "10"
                ljubljana[0] += int(b[0])
            if b[1]=="Maribor":
                maribor[0] += int(b[0])

            if b[1]=="Koper":
                koper[0] += int(b[0])
            if b[1]=="Novo mesto":
                nmesto[0] += int(b[0])
            if b[1]=="Nova Gorica":
                gorica[0] += int(b[0])

            if b[1] == "Ljubljana":
                b[0] = "10"
                ljubljana[1] += int(b[0])
            if b[1]=="Maribor":
                maribor[1] += int(b[0])
            if b[1]=="Koper":
                koper[1] += int(b[0])
            if b[1]=="Novo mesto":
                nmesto[1] += int(b[0])
            if b[1]=="Nova Gorica":
                gorica[1] += int(b[0])

        sez2=[ljubljana,maribor,gorica,koper,nmesto]
        maxout = sez2[0][0]
        maxin = sez2[0][1]
        krajout = ""
        krajin = ""

        for kraji in sez2:
            if kraji[0] > maxout:
                maxout == kraji[0]
                krajout=kraji[2]

            if kraji[1] > maxin:
                maxin = kraji[1]
                krajin=kraji[2]
        dat.close()
        return (krajout,krajin)



def roboti(navodila,n):
    seznam=[]
    for roboti in range(0,n):
        seznam.append((0,0))

    stevec=0
    str=[]
    for a in range(len(navodila)):
        str.append(navodila[a])

    for navodilo in str:
        if stevec==n:
            stevec=0
        x,y=seznam[stevec]

        if navodilo=="J":
            y=y-1
        elif navodilo=="S":
            y+=1
        elif navodilo=="V":
            x+=1
        elif navodilo=="Z":
            x-=1
        seznam[stevec]=(x,y)
        stevec+=1

    return seznam

class Delitelj:
    def __init__(self,k):
        self.delitelj=k
        self.cena=0

    def akcija(self,s):

        sez2=[s]
        seznam=[]
        for st in s:#konec s časom. menjava po indeksih bi delovala.

            if st%self.delitelj==0:
                self.cena=self.cena+st/self.delitelj
                seznam.append((st/self.delitelj))
        sez2[0]=seznam[:]

    def cena(self):
        return self.cena

##funkcija zakladi spodaj v klasu robot

class Robot:
    def __init__(self):
        self.x = self.y = 0
        self.smer = 1

    def desno(self):
        self.smer = (self.smer + 1) % 4

    def levo(self):
        self.smer = (self.smer - 1) % 4

    def naprej(self, d):
        if self.smer == 0:
            self.y += d
        elif self.smer == 1:
            self.x += d
        elif self.smer == 2:
            self.y -= d
        else:
            self.x -= d

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def zakladi(self,navodila):
        if not navodila:
            return 1

        zaklad=0
        prejeto=set()
        for ukaz in navodila:
            vs = abs(self.x + self.y)
            if vs % 7 == 0 and not (self.x, self.y) in prejeto:
                zaklad += 1
                prejeto.add((self.x, self.y))
            if ukaz=="D":
                self.desno()
            if ukaz=="L":
                self.levo()
            else:
                self.naprej(int(ukaz))

        return zaklad







class Test01Migracije(unittest.TestCase):
    def test_migracije(self):
        import os
        from random import randint
        fn = "m".format(randint(10000, 99999))
        try:
            with open(fn, "wt") as f:
                f.write("""8: Maribor -> Ljubljana
3: Maribor -> Nova Gorica
10: Ljubljana -> Maribor
5: Koper -> Nova Gorica
3: Novo mesto -> Nova Gorica
""")
            self.assertEqual(migracije(fn), ("Maribor", "Nova Gorica"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
3: Mb -> Ng
12: Lj -> Mb
5: Kp -> Ng
3: Nm -> Ng""")
            self.assertEqual(migracije(fn), ("Lj", "Mb"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
3: Mb -> Ng""")
            self.assertEqual(migracije(fn), ("Mb", "Lj"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
9: Ng -> Lj""")
            self.assertEqual(migracije(fn), ("Ng", "Lj"))

            with open(fn, "wt") as f:
                f.write("""11: Maribor -> Lj
5: Lj -> Celje
9: Ng -> Celje""")
            self.assertEqual(migracije(fn), ("Maribor", "Celje"))
        finally:
            os.remove(fn)


class Test02Zakladi(unittest.TestCase):
    def test_zakladi(self):
        self.assertEqual(zakladi(""), 1)
        self.assertEqual(zakladi("L"), 1)
        self.assertEqual(zakladi("LLL"), 1)
        self.assertEqual(zakladi("7"), 2)
        self.assertEqual(zakladi("77"), 3)
        self.assertEqual(zakladi("733"), 2)
        self.assertEqual(zakladi("7331"), 3)
        self.assertEqual(zakladi("7D32"), 2)
        self.assertEqual(zakladi("7D322"), 3)
        self.assertEqual(zakladi("7D3221LL"), 3)
        self.assertEqual(zakladi("7D322LL7"), 3)
        self.assertEqual(zakladi("7D322LL77"), 4)
        self.assertEqual(zakladi("7D331"), 3)
        self.assertEqual(zakladi("7D33D1"), 2)
        self.assertEqual(zakladi("7LLL77LLL"), 4)


class Test03Roboti(unittest.TestCase):
    def test_roboti(self):
        self.assertEqual(roboti("V", 1), [(1, 0)])
        self.assertEqual(roboti("Z", 1), [(-1, 0)])
        self.assertEqual(roboti("S", 1), [(0, 1)])
        self.assertEqual(roboti("J", 1), [(0, -1)])

        self.assertEqual(roboti("VZVZ", 2), [(2, 0), (-2, 0)])
        self.assertEqual(roboti("VZVZV", 2), [(3, 0), (-2, 0)])

        self.assertEqual(roboti("SJVZSJVZSJVZ", 4), [(0, 3), (0, -3), (3, 0), (-3, 0)])
        self.assertEqual(roboti("SJVZSJVZSJVZ", 12), 3 * [(0, 1), (0, -1), (1, 0), (-1, 0)])

        self.assertEqual(roboti("S", 3), [(0, 1), (0, 0), (0, 0)])
        self.assertEqual(roboti("", 300), 300 * [(0, 0)])
        self.assertEqual(roboti("SJ" * 100, 200), 100 * [(0, 1), (0, -1)])


class Test04BrezPonavljanja(unittest.TestCase):
    def test_brez_ponavljanja(self):
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 2]), [3, 1, 4, 2])
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 2, 1]), [3, 1, 4, 2, 1])
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 4, 15, 4, 2, 1]), [3, 1, 4, 15, 4, 2, 1])

        self.assertEqual(brez_ponavljanja([3, 42, 42]), [3, 42])
        self.assertEqual(brez_ponavljanja([42, 42, 3]), [42, 3])

        self.assertEqual(brez_ponavljanja([42, 42]), [42])
        self.assertEqual(brez_ponavljanja([42]), [42])
        self.assertEqual(brez_ponavljanja([]), [])


class Test05Delitelj(unittest.TestCase):
    def test_delitelj(self):
        deli1 = Delitelj(1)
        deli3 = Delitelj(3)
        deli5 = Delitelj(5)

        self.assertEqual(deli1.cena, 0)
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        s = [25, 8, 9, 15, 3, 81]

        self.assertIsNone(deli1.akcija(s))
        self.assertEqual(s, [25, 8, 9, 15, 3, 81])
        self.assertEqual(deli1.cena, sum(s))
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli1.akcija(s))
        self.assertEqual(s, [25, 8, 9, 15, 3, 81])
        self.assertEqual(deli1.cena, 2 * sum(s))
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli3.akcija(s))
        self.assertEqual(s, [25, 8, 3, 5, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [5, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, 5 + 1)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [1, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, (5 + 1) + 1)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [1, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, (5 + 1) + 1)

        self.assertIsNone(deli3.akcija(s))
        self.assertEqual(s, [1, 8, 1, 1, 1, 9])
        self.assertEqual(deli3.cena, (3 + 5 + 1 + 27) + (1 + 9))
        self.assertEqual(deli5.cena, (5 + 1) + 1)


if __name__ == "__main__":
    unittest.main()
