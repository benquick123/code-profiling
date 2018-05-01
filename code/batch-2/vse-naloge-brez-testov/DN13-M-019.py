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






