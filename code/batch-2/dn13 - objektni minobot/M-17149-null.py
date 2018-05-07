import unittest
import math
class Minobot:
    global zgodovinaX,zgodovinaY,zgodovinaSMER,ukaz
    zgodovinaX = [0]
    zgodovinaY = [0]
    zgodovinaSMER = [90]
    ukaz = [0]
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 90 #desno
        #SMERI:
        # [ 1/4  = Gor]
        # [  0   = Desno]
        # [ 0.5  = Dol]
        # [0.75  = Levo]

    def naprej(self,d): #premik za "d" naprej
        global zgodovinaX,zgodovinaY,ukaz
        n = self.smer/360
        if n%1 == 0.25: #Desno
            self.x = self.x + d

        elif n%1 == 0: #Gor
            self.y = self.y + d

        elif n%1 == 0.5: #Dol
            self.y = self.y - d

        elif n%1 == 0.75: #Levo
            self.x = self.x - d
        zgodovinaX.insert(len(zgodovinaX),self.x)
        zgodovinaY.insert(len(zgodovinaY),self.y)
        ukaz.insert(len(ukaz),'naprej')

    def koordinate(self): #trenutni (x,y)
        return (self.x,self.y)

    def razdalja(self): #pravokotna razdalja
        return (abs(self.x) + abs(self.y))

    def desno(self): #90 v desno
        global zgodovinaSMER,ukaz
        zgodovinaSMER.insert(len(zgodovinaSMER),self.smer+90)
        self.smer = self.smer + 90
        ukaz.insert(len(ukaz),'desno')

    def levo(self):  #90 v levo
        global zgodovinaSMER,ukaz
        zgodovinaSMER.insert(len(zgodovinaSMER),self.smer-90)
        self.smer = self.smer - 90
        ukaz.insert(len(ukaz),'levo')

    def razveljavi(self): #razveljavitev zadnjega ukaza
        global zgodovinaX,zgodovinaY,zgodovinaSMER,ukaz
        if ukaz != []:
            if ukaz[-1] == 'naprej':
                if len(ukaz) == 1:
                    self.x = zgodovinaX[0]
                    self.y = zgodovinaY[0]
                    zgodovinaX.pop(0)
                    zgodovinaY.pop(0)
                    ukaz.pop(-1)
                else:
                    self.x = zgodovinaX[-2]
                    self.y = zgodovinaY[-2]
                    zgodovinaX.pop(len(zgodovinaX)-1)
                    zgodovinaY.pop(len(zgodovinaY)-1)
                    ukaz.pop(-1)

            elif ukaz[-1] == 'desno' or ukaz[-1] == 'levo':
                if len(ukaz) == 1:
                    self.smer = zgodovinaSMER[0]
                    zgodovinaSMER.pop(0)
                    ukaz.pop(-1)
                else:
                    self.smer = zgodovinaSMER[-2]
                    zgodovinaSMER.pop(len(zgodovinaSMER)-1)
                    ukaz.pop(-1)
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
