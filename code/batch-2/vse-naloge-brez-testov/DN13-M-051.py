import math
class Minobot  :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.pozicija = (0,0)
        self.ukazi = [self.x, self.y, self.angle]
        self.do = True

    def update(self):
        self.pozicija = self.x, self.y
        if self.do:
            self.ukazi.append(self.x)
            self.ukazi.append(self.y)
            self.ukazi.append(self.angle)
        self.do = True
        self.x = self.ukazi[-3]
        self.y = self.ukazi[-2]
        self.angle = self.ukazi[-1]

    def naprej(self,d):
        phi = math.radians(self.angle)
        xx = math.cos(phi)
        yy = math.sin(phi)
        if abs(xx) < 0.00001 :
            xx = 0
        if abs(yy) < 0.00001 :
            yy = 0
        x = int(self.x + d * xx)
        y = int(self.y + d * yy)
        self.x = x
        self.y = y
        self.update()

    def desno(self):
        self.angle = self.angle - 90
        self.update()

    def levo(self):
        self.angle = self.angle + 90
        self.update()

    def koordinate(self):
        x,y = self.x, self.y
        return (x,y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.ukazi) > 3:
            self.ukazi = self.ukazi[:-3]
            self.do = False
            self.update()







