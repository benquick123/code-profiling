import random
import risar
import math
import time
from PyQt5.QtWidgets import QMessageBox

class Zogica:
    def __init__(self):
        self.x = random.uniform(11, risar.maxX - 11)
        self.y = random.uniform(11, risar.maxY - 11)
        self.r = 10
        self.zoga = risar.krog(self.x, self.y, self.r, risar.nakljucna_barva(), 3)
        self.angle = random.uniform(0,360)
        self.update()
        self.start = None

    def update(self):
        self.zoga.setPos(self.x, self.y)
        self.angle = self.angle % 360

        if self.x < 11:
            self.wall(3)
            self.x = 11
        if self.x > (risar.maxX-11):
            self.wall(1)
            self.x = risar.maxX-11
        if self.y > (risar.maxY-11):
            self.wall(2)
            self.y = risar.maxY-11
        if self.y < 11:
            if self.angle == 0:
                self.angle += 180
            else:
                self.angle = -self.angle + 180
            self.y = 11

        self.angle = self.angle % 360

    def eksplozija(self):
        c = self.zoga.pen().color().lighter()
        c.setAlpha(192)
        self.zoga.setBrush(c)
        self.zoga.setRect(-30, -30, 60, 60)
        self.start = time.time()

    def forward(self):
        phi = math.radians(90 - self.angle)
        nx = self.x + 5 * math.cos(phi)
        ny = self.y - 5 * math.sin(phi)
        self.x = nx
        self.y = ny
        self.update()

    def wall(self,a):
        if self.angle == a*90:
            self.angle += 180
        else:
            self.angle = -self.angle + (a - 1) * 180

    def hide(self):
        self.zoga.hide()

pozicija = risar.krog(1000, 1000, 30, risar.nakljucna_barva(), 3)
zogice = set()
zogice_zacasno = set()
eksplodirane_zogice = eksplodirane_zogice_zacasno = set()
koordinate_eksplodiranih = set()
koordinate_eksplodiranih_zacasno = set()
eksplozija = znak = 0
regulator = False
stopnja = True
level = 0
a = 0
b = 4

stopnja = True
while True:
    if stopnja:

        pozicija = risar.krog(1000, 1000, 30, risar.nakljucna_barva(), 3)
        zogice.clear()
        zogice_zacasno.clear()
        eksplodirane_zogice.clear()
        eksplodirane_zogice_zacasno.clear()
        koordinate_eksplodiranih.clear()
        koordinate_eksplodiranih_zacasno.clear()
        eksplozija = 0
        znak = 0
        regulator = False
        risar.klik = False

        level += 1
        a += 1
        b += 2
        if level > 10:
            QMessageBox.information(None, "Uspelo ti je", "Vsega lepega je enkrat konec!")
            break

        QMessageBox.information(None, "Stopnja {}".format(level), "Razstreli {} od {} žogic".format(a, b))
        stopnja = False
        for i in range(b):
            zoga = Zogica()
            zogice.add(zoga)

    for zoga in zogice:
        zoga.forward()

        if not risar.klik:
            x0, y0 = risar.miska
            pozicija.setPos(x0, y0)
            if znak == 0:  #
                cas_klika = time.time()
        else:
            znak = 1
            if not regulator:
                koordinate_eksplodiranih.add((x0, y0))
            for x,y in koordinate_eksplodiranih:
                if math.sqrt((abs(zoga.x - x))**2 + (abs(zoga.y-y))**2)<=40:
                    koordinate_eksplodiranih_zacasno.add((zoga.x, zoga.y))
                    zoga.eksplozija()
                    zogice_zacasno.add(zoga)
                    eksplozija += 1
                    break
            koordinate_eksplodiranih = koordinate_eksplodiranih | koordinate_eksplodiranih_zacasno
            koordinate_eksplodiranih_zacasno = set()

    eksplodirane_zogice = eksplodirane_zogice | zogice_zacasno
    zogice = zogice - zogice_zacasno

    risar.obnovi()
    risar.cakaj(0.01)

    for ezoga in eksplodirane_zogice:
        if ezoga.start and (time.time() - ezoga.start) > 4:
            koordinate_eksplodiranih = koordinate_eksplodiranih - {(ezoga.x, ezoga.y)}
            eksplodirane_zogice_zacasno = eksplodirane_zogice_zacasno | {ezoga}
            ezoga.hide()

    eksplodirane_zogice = eksplodirane_zogice - eksplodirane_zogice_zacasno

    if ((time.time() - cas_klika) > 4) and znak and not regulator:
        pozicija.hide()
        regulator = True
        koordinate_eksplodiranih = koordinate_eksplodiranih - {(x0,y0)}
    if znak and not koordinate_eksplodiranih:
        if eksplozija < a:
            for zoga in zogice:
                zoga.hide()
            QMessageBox.information(None, "Poskusi znova", "Eksplodiralo je {} žogic - premalo".format(eksplozija))
            stopnja = True
            level -= 1
            a -= 1
            b -= 2

        else:
            for zoga in zogice:
                zoga.hide()
            QMessageBox.information(None, "Bravo", "Eksplodiralo je {} žogic - zadosti".format(eksplozija))
            stopnja = True
