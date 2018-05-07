import risar
from math import sqrt, ceil
from random import randint, choice
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Igralec:
    def __init__(self):
        self.x, self.y = risar.miska
        self.r = 30
        self.oblika = risar.krog(self.x, self.y, self.r)
        self.odstranjen = False
        risar.klik = False

    def odstrani(self):
        self.x, self.y = risar.maxX + 100, risar.maxY + 100
        self.odstranjen = True
        risar.odstrani(self.oblika)


    def posodobi(self):
        self.x, self.y = risar.miska
        self.oblika.setPos(self.x, self.y)

    def klik(self):
        return risar.klik

    def se_dotika(self, x, y, r):
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= (self.r + r) ** 2:
            return 1
        return 0

    def get_odstranjen(self):
        return self.odstranjen


class Krog:
    def __init__(self):
        self.r = 10
        self.x, self.y = risar.nakljucne_koordinate()
        self.x += self.r
        self.y += self.r
        self.barva = risar.nakljucna_barva()
        self.oblika = risar.krog(self.x, self.y, self.r, self.barva)
        v = 5
        self.vx = randint(-v, v)
        self.vy = sqrt(v**2 - self.vx**2)
        self.eksplodiran = False
        self.odstranjen = False

    def premakni(self):
        self.x += self.vx
        self.y += self.vy
        self.oblika.setPos(self.x, self.y)

    def dotikanje_robov(self):
        if self.x < self.r:
            self.vx = abs(self.vx)
        if self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        if self.y < self.r:
            self.vy = abs(self.vy)
        if self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

    def povecaj(self):
        risar.odstrani(self.oblika)
        self.r = 30
        self.oblika = risar.krog(self.x, self.y, self.r, self.barva)
        self.eksplodiran = True
        self.vx = 0
        self.vy = 0
        c = self.oblika.pen().color().lighter()
        c.setAlpha(192)
        self.oblika.setBrush(c)

    def se_dotika(self, other):
        if (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2:
            return 1
        return 0

    def odstrani(self):
        self.x = risar.maxX + 100
        self.y = risar.maxY + 100
        risar.odstrani(self.oblika)
        self.odstranjen = True

    def get_eksplodirana(self):
        return self.eksplodiran

    def get_odstranjen(self):
        return self.odstranjen

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_r(self):
        return self.r

class Igra:
    def __init__(self):
        self.stev_ez = 0
        self.st_zog = 30
        self.sporocilo = ""

    def izpisi_rezultat(self, level = "konec"):
        QMessageBox.information(None, level, self.sporocilo)
        risar.pobrisi()


    def za_oceno_6(self):
        i = 0
        zoga = Krog()
        while (i < 1000):
            i += 1
            zoga.premakni()
            zoga.dotikanje_robov()
            risar.cakaj(0.02)
        risar.pobrisi()

    def za_oceno_7(self):
        zoge = []
        for i in range(30):
            zoge.append(Krog())
        i = 0
        while (i < 1000):
            i += 1
            for zoga in zoge:
                zoga.premakni()
                zoga.dotikanje_robov()
            risar.cakaj(0.02)
        risar.pobrisi()

    def za_oceno_8(self):
        stop = 1
        zoge = []
        igralec = Igralec()
        for i in range(30):
            zoge.append(Krog())
        while (stop):
            risar.cakaj(0.02)
            for zoga in zoge:
                zoga.premakni()
                zoga.dotikanje_robov()
                if not igralec.klik():
                    igralec.posodobi()
                if igralec.klik() and igralec.se_dotika(zoga.get_x(), zoga.get_y(), zoga.get_r()):
                    QTimer.singleShot(4000, igralec.odstrani)
                    zoga.povecaj()
                    stop = 0
                    break
        risar.pobrisi()

    def za_oceno_9(self, st_zog = 30, meja = 0):
        neeksplodirane = []
        for i in range(st_zog):
            neeksplodirane.append(Krog())
        i = 0
        eksplodirane = []
        igralec = Igralec()
        stop = 0
        cr = 0
        ez = 0
        while (not stop):
            risar.cakaj(0.02)
            for zoga in neeksplodirane[:]:
                zoga.premakni()
                zoga.dotikanje_robov()
                if not igralec.klik():
                    igralec.posodobi()
                if igralec.klik():
                    QTimer.singleShot(4000, igralec.odstrani)
                    cr = 1
                    if igralec.se_dotika(zoga.get_x(), zoga.get_y(), zoga.get_r()):
                        zoga.povecaj()
                        eksplodirane.append(zoga)
                        neeksplodirane.remove(zoga)
                        ez = 1
                        self.stev_ez += 1
                        QTimer.singleShot(4000, zoga.odstrani)
            for zoga in eksplodirane:
                for zoga2 in neeksplodirane[:]:
                    if zoga.se_dotika(zoga2):
                        zoga2.povecaj()
                        QTimer.singleShot(4000, zoga2.odstrani)
                        neeksplodirane.remove(zoga2)
                        eksplodirane.append(zoga2)
                        self.stev_ez += 1
            for zoga in eksplodirane[:]:
                if zoga.get_odstranjen():
                    eksplodirane.remove(zoga)
            if (cr and ez and not eksplodirane and igralec.get_odstranjen()) or igralec.get_odstranjen() and not ez:
                stop = 1
        if self.stev_ez >= meja:
            self.sporocilo = str(self.stev_ez) + " od " + str(self.st_zog) + " žog!"
            tmp = True
        else:
            self.sporocilo = str(self.stev_ez) + " od " + str(self.st_zog) + " žog! Žal premalo"
            tmp = False
        self.izpisi_rezultat()
        return tmp

    def za_oceno_10(self):
        i = 1
        meja = 1
        self.st_zog = 5
        self.stev_ez = 0
        while(i <= 10):
            self.sporocilo = "Eliminiraj " + str(meja) + " od " + str(self.st_zog) + " žog!"
            self.izpisi_rezultat("Level " + str(i))
            if self.za_oceno_9(self.st_zog, meja):
                self.st_zog += 5
                i += 1
                meja += round(self.st_zog - i*4 + (i-i/2) - meja/4) - 2
                print(self.st_zog, i, 4*i,  meja)
            self.stev_ez = 0









igra = Igra()

igra.za_oceno_6()
igra.za_oceno_7()
igra.za_oceno_8()
igra.za_oceno_9(30)
igra.za_oceno_10()




risar.stoj()