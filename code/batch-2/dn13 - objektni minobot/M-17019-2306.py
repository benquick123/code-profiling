from math import radians,cos,sin


class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90
        #self.pen_active = True
        #self.pause = 0
        #self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        #self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.pot= [(0,0,90)]

    def update(self):
        self.pot.append((self.x, self.y, self.angle))
        print('Koordinata x = ', self.x, "Koordinata y =", self.y, 'Kot je ', self.angle)


    def naprej(self, d):
        phi = radians(90 - self.angle)
        nx = self.x + d * cos(phi)
        ny = self.y + d * sin(phi)
        self.x = round(nx,0)
        self.y = round(ny,0)
        #self.update()
        #print('Koordinata x = ' ,self.x ,"Koordinata y =", self.y)
        self.update()

    def turn(self, phi):
        self.angle += phi
        #print('Koordinata x = ', self.x, "Koordinata y =", self.y)
        self.update()

    def desno(self):
        self.turn(90)

    def levo(self):
        self.turn(-90)

    def koordinate(self):
        #print('Koordinata x = ', self.x, "Koordinata y =", self.y)
        #print('Koordinata x = ', int(self.x), "Koordinata y =", int(self.y))
        #print('Koordinata x = ', int(round(self.x,0)), "Koordinata y =", int(round(self.y,0)))
        return (int(round(self.x,0)), int(round(self.y,0)))


    def razdalja(self):
        razdalja = round((abs(self.x) + abs(self.y)),0)
        return razdalja

    def razveljavi(self):
        print("RAZVELJAVI")
        #print(self.pot)
        if len(self.pot) > 1:
            #if len(self.pot) > 2:
            self.pot.pop(-1)
            nx,ny,nang = self.pot[-1]
            self.x = nx
            self.y = ny
            self.angle = nang

        print(self.pot)

        #print('Koordinata x = ', self.x, "Koordinata y =", self.y)




#klici funcije:

'''
a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)

a.levo()
a.naprej(4)
a.desno()
a.naprej(3)
a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)

a.levo()
a.naprej(4)
a.desno()
a.naprej(3)
print(a.koordinate())
print(a.pot)
'''






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
