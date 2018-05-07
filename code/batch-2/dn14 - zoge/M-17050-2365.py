import risar
import math
from random import randint
import time

class Zoga(object):
    def __init__(self):


        self.x = randint(15,risar.maxX-15)
        self.y = randint(15, risar.maxY - 15)
        self.barva=risar.nakljucna_barva()
        self.krog = risar.krog(self.x,self.y, 10, barva=self.barva, sirina=2)

        self.x_komponenta = randint(-4, 4)
        while self.x_komponenta == 0:
            self.x_komponenta = randint(-4, 4)
        self.y_komponenta = (5 ** 2) - (self.x_komponenta ** 2)
        self.y_komponenta = math.sqrt(self.y_komponenta)
        self.update()
    def update(self):
        self.krog.setPos(self.x, self.y)

    def premikaj(self):


            self.x = self.x + self.x_komponenta
            self.y = self.y + self.y_komponenta

            if self.x < 14 or self.x > risar.maxX - 14:
                self.x_komponenta = -self.x_komponenta
            if self.y < 14 or self.y > risar.maxY - 14:
                self.y_komponenta = -self.y_komponenta

            self.update()

    def vrni_x(self):
        return self.x
    def vrni_y(self):
        return self.y
class Miska(object):


    def __init__(self):
        barva = risar.nakljucna_barva()
        self.x_miske,self.y_miske = risar.miska
        self.krog = risar.krog(self.x_miske,self.y_miske, 30, barva=barva, sirina=2)


    def update(self,x,y):
        self.krog.setPos(x, y)


zogice={}

miska = Miska()


def se_dotikata(x_kroga,y_kroga):
    if risar.klik == False:
        return False
    else:
        x2,y2 = risar.miska

        x1=x_kroga
        y1 = y_kroga

        razdalja = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))

        if razdalja<44:
            risar.stoj()

def loop():
    risar.klik = False
    p_runtime = time.time() + 20
    while time.time() < p_runtime:

        for x in zogice.values():
            x.premikaj()

            if risar.klik:
                x_kroga = x.vrni_x()
                y_kroga = x.vrni_y()
                se_dotikata(x_kroga,y_kroga)

        risar.cakaj(0.03)

        if risar.klik == False:
            f, d = risar.miska
            miska.update(f, d)
            risar.cakaj(0.0)

for x in range(0,30):
    zogice[x]=Zoga()






loop()


risar.stoj()




