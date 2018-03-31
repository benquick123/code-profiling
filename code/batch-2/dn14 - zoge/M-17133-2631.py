from PyQt5.QtWidgets import QMessageBox
import risar
import random
import math
import time
from collections import Counter

class Zogica:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.barva = risar.nakljucna_barva()
        self.r = 10
        self.premikx, self.premiky = 0, 0
        self.kx, self.ky = 0, 0
        self.vx, self.vy, self.krogla, self.eksplozija, self.eksp_time = [], [], [], [], []
        self.mispos = risar.krog(0, 0, 30, risar.bela, 2)
        self.vec_kroglic()

    def kroglica(self):
        self.barva = risar.nakljucna_barva()
        self.x, self.y = (random.randint(20, risar.maxX - 40), random.randint(20, risar.maxY-40))
        return risar.krog(self.x, self.y, self.r, self.barva, 4)

    def vec_kroglic(self):
        for i in range(30):
            k = self.kroglica()
            r = random.randint(-5, 5)
            self.krogla.append(k)
            self.vx.append(r)
            self.vy.append(math.sqrt((5**2)-(r**2)))

    def mis(self):
        self.kx, self.ky = risar.miska
        return self.mispos.setPos(self.kx, self.ky)

    def premik(self):
        i = len(self.krogla)-1
        while i >= 0:
            self.krog = self.krogla[i]
            self.krog.setPos(self.krog.x() + self.vx[i], self.krog.y() + self.vy[i])
            if not (15 < self.krog.x() < risar.maxX - 35):
                    self.vx[i] = -self.vx[i]
            if not (15 < self.krog.y() < risar.maxY - 35):
                self.vy[i] = -self.vy[i]
            if not risar.klik:
                a.mis()
            else:
                if not (self.kx, self.ky) in self.eksplozija:
                    self.eksplozija.append((self.kx, self.ky))
                    self.eksp_time.append(time.time())
                '''
                b = ((self.kx - self.krog.x()) ** 2) + ((self.ky - self.krog.y()) ** 2)
                if b < 40 ** 2:
                    if not (self.krog.x(), self.krog.y()) in self.eksplozija:
                        self.eksplozija.append((self.krog.x(), self.krog.y()))
                        self.eksp_time.append(time.time())
                    self.vx[i] = 0
                    self.vy[i] = 0
                    c = self.krog.pen().color().lighter()
                    c.setAlpha(192)
                    self.krog.setBrush(c)
                    self.krog.setRect(-30, -30, 60, 60)
                '''

                cc = Counter(self.eksplozija).most_common()
                boom = len(self.eksplozija)-1
                while boom >= 0:
                    if 2 == cc[0][1] and (-550, -550) == cc[0][0]:
                        QMessageBox.information(None, "Konec", "Eksplodiralo je {} žog.".format(cc[0][1]-1))
                        risar.stoj()
                    if (time.time() - self.eksp_time[boom]) > 4:
                        if (self.eksplozija[boom][0], self.eksplozija[boom][1]) == (self.kx, self.ky):
                            self.mispos.hide()
                            self.kx, self.ky = -550, -550
                        self.eksp_time[boom] = 0
                        self.eksplozija[boom] = (-550, -550)
                    b = ((self.eksplozija[boom][0]-self.krog.x())**2) + ((self.eksplozija[boom][1]-self.krog.y())**2)
                    if b < 45**2:
                        if not (self.krog.x(), self.krog.y()) in self.eksplozija:
                            self.eksplozija.append((self.krog.x(), self.krog.y()))
                            self.eksp_time.append(time.time())
                        self.vx[i] = 0
                        self.vy[i] = 0
                        c = self.krog.pen().color().lighter()
                        c.setAlpha(192)
                        self.krog.setBrush(c)
                        self.krog.setRect(-30, -30, 60, 60)
                    boom -= 1

            i -= 1
        risar.cakaj(0.02)





a = Zogica()
for j in range(1000):
    a.premik()

risar.stoj()




