import risar
from random import randint
from math import *

class Zoga:
    def __init__(self):
        self.MAX_X, self.MAX_Y = risar.maxX, risar.maxY
        self.X, self.Y = randint(5, self.MAX_X - 5), randint(5, self.MAX_Y - 5)
        self.krog = risar.krog(self.X, self.Y, 10, risar.nakljucna_barva(), 2)
        self.x_hitrost = randint(-5, 5)
        self.y_hitrost = sqrt(25-self.x_hitrost**2)

    def posodobi(self):
        self.krog.setPos(self.X, self.Y)

    def premikaj_se(self):
        if self.X <= 5: self.x_hitrost=-self.x_hitrost
        elif self.X >= self.MAX_X -5: self.x_hitrost=-self.x_hitrost
        if self.Y <= 5: self.y_hitrost=-self.y_hitrost
        elif self.Y >= self.MAX_Y-5: self.y_hitrost = -self.y_hitrost
        self.X += self.x_hitrost
        self.Y+= self.y_hitrost
        self.posodobi()

    def dobi_x(self):
        return self.X
    def dobi_y(self):
        return self.Y

class Level:
    def __init__(self):
        self.kliknjeno=False
        self.zogice = []
        for i in range(30):
            self.zogice.append(Zoga())
        self.m_krog_x, self.m_krog_y = 0,0
        self.zoga_miska = risar.krog(0, 0, 10, risar.bela, 3)
        c = 0
        timer_c = 0
        while timer_c<20000:
            if self.kliknjeno:
                pass
            if not risar.klik:
                self.zoga_miska.setPos(risar.miska[0], risar.miska[1])
                self.m_krog_x, self.m_krog_y = risar.miska[0], risar.miska[1]
            else:
                self.klik()
            if c == 30:
                c = 0
                risar.cakaj(0.02)
            zoga = self.zogice[c]
            if self.kliknjeno:
                razdalja = sqrt((self.m_krog_x-zoga.dobi_x())**2 + (zoga.dobi_y()-self.m_krog_y)**2)
                if razdalja < 40:
                    co = zoga.krog.pen().color().lighter()
                    co.setAlpha(192)
                    zoga.krog.setBrush(co)
                    zoga.krog.setRect(-30, -30, 60, 60)
                    print(razdalja)
                    zoga.x_hitrost=0
                    zoga.y_hitrost=0
                    break
            zoga.premikaj_se()
            c += 1
            timer_c+=1
        print("konec")
    def klik(self):
        self.zoga_miska.setRect(-30, -30, 60, 60)
        c = self.zoga_miska.pen().color().lighter()
        c.setAlpha(192)
        self.zoga_miska.setBrush(c)
        self.kliknjeno=True


l = Level()

risar.stoj()
