import math

class Minobot:
    def __init__(self):
        self.x=0
        self.y=0
        self.smer="E"
        self.ukazi=[]

    def naprej(self,d):
        self.ukazi.append("naprej"+":"+str(d))
        if self.smer == "E":
            self.x=self.x+d
        if self.smer == "W":
            self.x=self.x-d
        if self.smer == "N":
            self.y=self.y+d
        if self.smer == "S":
            self.y=self.y-d
    def nazaj(self):

        beseda = self.ukazi[-1]

        razcleni = beseda.split(":")
        k=int(razcleni[1])
        if self.smer == "E":
            self.x=self.x-k
        if self.smer == "W":
            self.x=self.x+k
        if self.smer == "N":
            self.y=self.y-k
        if self.smer == "S":
            self.y=self.y+k
        self.ukazi[:]=self.ukazi[:-1]

    def desno(self):
        self.ukazi.append("desno")
        if self.smer=="E":
            self.smer="S"
        elif self.smer=="S":
            self.smer="W"
        elif self.smer=="W":
            self.smer="N"
        elif self.smer=="N":
            self.smer="E"

    def desno_nazaj(self):

        if self.smer=="E":
            self.smer="S"
        elif self.smer=="S":
            self.smer="W"
        elif self.smer=="W":
            self.smer="N"
        elif self.smer=="N":
            self.smer="E"
        self.ukazi[:] = self.ukazi[:-1]
    def levo(self):
        self.ukazi.append("levo")
        if self.smer=="E":
            self.smer="N"
        elif self.smer=="N":
            self.smer="W"
        elif self.smer=="W":
            self.smer="S"
        elif self.smer=="S":
            self.smer="E"
    def levo_nazaj(self):

        if self.smer=="E":
            self.smer="N"
        elif self.smer=="N":
            self.smer="W"
        elif self.smer=="W":
            self.smer="S"
        elif self.smer=="S":
            self.smer="E"
        self.ukazi[:] = self.ukazi[:-1]
    def koordinate(self):
        return self.x,self.y
    def razdalja(self):
        x1=0
        y1=0
        return abs(self.x-x1)+abs(self.y-y1)

    def razveljavi(self):
        if len(self.ukazi)>0:
            beseda = self.ukazi[-1]
            razcleni = beseda.split(":")

            if self.ukazi[-1]=="levo":
                #print("obracam levo")
                self.desno_nazaj()
            elif self.ukazi[-1]=="desno":
                #print("obracam desno")
                self.levo_nazaj()

            elif "naprej" in razcleni[0]:

                self.nazaj()

    def zbrisi_zadnjega(self):
        return self.ukazi[:-1]

    def printaj(self):
        return self.ukazi
    def printaj2(self):
        return self.smer



import unittest


class TestObvezna(unittest.TestCase):
    def test_minobot(self):
        a = Minobot()
        b = Minobot()

        self.assertEqual(a.koordinate(), (0, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 0)
        self.assertEqual(b.razdalja(), 0)

        a.naprej(1)
        self.assertEqual(a.koordinate(), (1, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 1)
        self.assertEqual(b.razdalja(), 0)

        a.naprej(2)
        self.assertEqual(a.koordinate(), (3, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 3)
        self.assertEqual(b.razdalja(), 0)

        b.naprej(2)
        self.assertEqual(a.koordinate(), (3, 0))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 3)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # zdaj je obrnjen dol
        a.naprej(4)
        self.assertEqual(a.koordinate(), (3, -4))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 7)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen je levo
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -4))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 6)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen je gor
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -3))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 5)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen desno
        a.naprej(3)
        self.assertEqual(a.koordinate(), (5, -3))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 8)
        self.assertEqual(b.razdalja(), 2)

        b.levo()  # obrnjen gor
        b.naprej(3)
        self.assertEqual(b.koordinate(), (2, 3))
        self.assertEqual(b.razdalja(), 5)

        b.levo()  # obrnjen levo
        b.naprej(3)
        self.assertEqual(b.koordinate(), (-1, 3))
        self.assertEqual(b.razdalja(), 4)

        a.naprej(5)
        self.assertEqual(a.koordinate(), (10, -3))
        self.assertEqual(a.razdalja(), 13)


class TestDodatna(unittest.TestCase):
    def test_undo(self):
        a = Minobot()
        a.desno()  # gleda dol
        a.naprej(4)
        a.levo()  # gleda desno
        a.naprej(1)
        a.naprej(2)

        self.assertEqual(a.koordinate(), (3, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (1, -4))
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (1, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.naprej(1)
        self.assertEqual(a.koordinate(), (1, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.razveljavi()  # spet gleda dol
        self.assertEqual(a.koordinate(), (0, -4))
        a.naprej(2)
        self.assertEqual(a.koordinate(), (0, -6))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(3)
        self.assertEqual(a.koordinate(), (0, -3))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # spet gleda desno
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(3)
        self.assertEqual(a.koordinate(), (3, 0))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(2)
        self.assertEqual(a.koordinate(), (2, 0))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))


if __name__ == "__main__":
    unittest.main()
