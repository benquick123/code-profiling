import risar
from math import cos,sin,radians,sqrt,pi
from random import randint,random
class Krog():
    def __init__(self,r = 10):
        self.r = r
        self.x = randint(0, risar.maxX-self.r-2)
        self.y = randint(0, risar.maxY-self.r-2)
        self.kot = randint(0,360)
        self.colour = risar.nakljucna_barva()
        self.krog = risar.krog(self.x,self.y,self.r,self.colour)
        self.premik_v_x = randint(-5,5)
        self.predznaky = self.predznakx = 1 if random() < 0.5 else -1
        self.hitrost_x = self.premik_v_x*self.predznakx
        self.hitrost_y = sqrt(5**2 - self.premik_v_x**2)*self.predznaky

    def get_coord(self):
        return self.x,self.y

    def miska(self):
        self.x, self.y = risar.miska
        self.hitrost_y, self.hitrost_x = 0,0
        self.premik()

    def polmer(self):
        return self.r

    def premik(self):
        if not (0 < self.x < risar.maxX - self.r-2):
            self.hitrost_x *= -1
        if not (0 < self.y < risar.maxY - self.r-2):
            self.hitrost_y *= -1
        self.x += self.hitrost_x
        self.y -= self.hitrost_y
        self.krog.setPos(self.x,self.y)

class Krogi():
    def __init__(self,st_krogov):
        self.pavza = 0.02
        self.krogi = [Krog() for _ in range(st_krogov)]
        self.cursor = Krog(30)

    def premiki(self):
        i = self.pavza
        while (i < 20):
            for k in range(len(self.krogi)):
                krog = self.krogi[k]
                krog.premik()
                if risar.klik:
                    x1,y1 = krog.get_coord()
                    x0,y0 = self.cursor.get_coord()
                    distance = sqrt((x1-x0)**2 + (y1-y0)**2)-krog.polmer()
                    if distance <= self.cursor.polmer():
                        self.explode(krog.krog)
                        return None
                else:
                    self.cursor.miska()
            risar.cakaj(self.pavza)
            i += self.pavza

    def explode(self,n):
        c = n.pen().color().lighter()
        c.setAlpha(192)
        n.setRect(-30, -30, 60, 60)
        n.setBrush(c)
        risar.cakaj(self.pavza)

a = Krogi(30)
a.premiki()
# ni se mi dalo delat za višje oceno, ker se moram učiti Diskretne :( bi popravljal če lahko
