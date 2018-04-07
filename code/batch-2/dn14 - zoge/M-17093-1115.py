import risar
from random import randint
from math import radians, sin, cos, sqrt
from PyQt5.QtWidgets import QMessageBox



class Krog:
    def __init__(self, polmer):
        self.polmer = polmer
        self.x, self.y = randint(15, risar.maxX - 15), randint(15, risar.maxY - 15)
        self.barva = risar.nakljucna_barva()
        self.smer = randint(1,360)
        self.hitrost = 5
        self.vx = self.hitrost*cos(radians(self.smer))
        self.vy = self.hitrost*sin(radians(self.smer))
        self.zoga = risar.krog(self.x, self.y, self.polmer, self.barva, sirina=1)
        self.eksplodiran = False
        self.obstaja = True
        self.pocena = 0

    def premakni(self):
        self.zoga.setPos(self.x, self.y)
        if risar.maxX - self.x <= 10 or self.x <= 10:
            self.vx = -self.vx
        if risar.maxY - self.y <= 10 or self.y <= 10 :
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy

    def eksplodira(self):
        self.zoga.setRect(-30, -30, 60, 60)
        self.eksplodiran = True
        self.vx = 0
        self.vy = 0



class Miska(Krog):
    def __init__(self, polmer):
        self.polmer = polmer
        self.x, self.y = risar.miska
        self.barva = risar.nakljucna_barva()
        self.zoga = risar.krog(self.x, self.y, self.polmer, self.barva, sirina=1)
        self.eksplodiran = False
        self.obstaja = True
        self.pocena = 0

    def update(self):
        self.x, self.y = risar.miska
        self.zoga.setPos(self.x, self.y)

#============================ ZA 6 ===============================

def zogica():
    risar.pobrisi()
    a = Krog(10)
    for i in range(round(1000/1.6)):
        a.premakni()
        risar.cakaj(0.02)

#============================ ZA 7 ===============================

def zogice1(stev):
    risar.pobrisi()
    s = []
    for x in range(stev):
        a = Krog(10)
        s.append(a)

    for i in range(round(1000/1.6)):
        for x in s:
            x.premakni()
        risar.cakaj(0.02)

#============================ ZA 8 ===============================

def zogice2(stev):
    risar.pobrisi()
    risar.klik = False
    eks_koordinate = []
    s = []
    bum = []
    b = Miska(30)

    for x in range(stev):
        a = Krog(10)
        s.append(a)

    while not risar.klik:
        b.update()
        for x in s:
            x.premakni()
        risar.cakaj(0.02)
    b.x, b.y = b.x, b.y
    eks_koordinate.append((b.x, b.y))

    b.eksplodira()
    while not bum:
        for cela in s:
            for x, y in eks_koordinate:
                if abs(cela.x - x) ** 2 + abs(cela.y - y) ** 2 <= 1600:
                    bum.append(cela)
            cela.premakni()
        risar.cakaj(0.02)

#============================ ZA 9 ===============================

def zogice3(stev):
    risar.pobrisi()
    risar.klik = False
    eks_koordinate = []
    eksplodiranih = 0
    s = []
    bum = []
    b = Miska(30)

    for x in range(stev):
        a = Krog(10)
        s.append(a)

    while not risar.klik:
        b.update()
        for x in s:
            x.premakni()
        risar.cakaj(0.02)
    b.x, b.y = b.x, b.y
    eks_koordinate.append((b.x, b.y))
    bum.append(b)
    b.eksplodira()

    while eks_koordinate:
        for cela in s:
            if not cela.eksplodiran:
                for x, y in eks_koordinate:
                    if abs(cela.x - x)**2 + abs(cela.y - y)**2 <= 1600 and (cela.x, cela.y) not in eks_koordinate:
                        cela.eksplodira()
                        eks_koordinate.append((cela.x, cela.y))
                        bum.append(cela)
                        eksplodiranih += 1
                        c = cela.zoga.pen().color().lighter()
                        c.setAlpha(192)
                        cela.zoga.setBrush(c)
            cela.premakni()

        for eks in bum:
            eks.pocena += 1
            if eks.pocena >= sqrt(500/0.02):
                if (eks.x, eks.y) in eks_koordinate:
                    eks.zoga.hide()
                    eks_koordinate.remove((eks.x, eks.y))
                if eks in s:
                    eks.zoga.hide()
                    s.remove(eks)

        risar.cakaj(0.02)
    QMessageBox.information(None, "Okno", "Število razstreljenih žogic: [{}]".format(eksplodiranih))

#============================ ZA 10 ===============================

def zogice(stev, cilj, stopnja):
    eksplodiranih = 0
    while cilj > eksplodiranih:
        risar.klik = False
        eks_koordinate = []
        eksplodiranih = 0
        s = []
        bum = []
        b = Miska(30)
        QMessageBox.information(None, "Stopnja {}".format(stopnja), "Zadeni {} od {}".format(cilj, stev))

        for x in range(stev):
            a = Krog(10)
            s.append(a)

        while not risar.klik:
            b.update()
            for x in s:
                x.premakni()
            risar.cakaj(0.02)
        b.x, b.y = b.x, b.y
        eks_koordinate.append((b.x, b.y))
        bum.append(b)
        b.eksplodira()

        while eks_koordinate:
            for cela in s:
                if not cela.eksplodiran:
                    for x, y in eks_koordinate:
                        if abs(cela.x - x) ** 2 + abs(cela.y - y) ** 2 <= 1600 and (cela.x, cela.y) not in eks_koordinate:
                            cela.eksplodira()
                            eks_koordinate.append((cela.x, cela.y))
                            bum.append(cela)
                            eksplodiranih += 1
                            c = cela.zoga.pen().color().lighter()
                            c.setAlpha(192)
                            cela.zoga.setBrush(c)
                cela.premakni()

            for eks in bum:
                eks.pocena += 1
                if eks.pocena >= sqrt(500 / 0.02):
                    if (eks.x, eks.y) in eks_koordinate:
                        eks.zoga.hide()
                        eks_koordinate.remove((eks.x, eks.y))
                    if eks in s:
                        eks.zoga.hide()
                        s.remove(eks)

            risar.cakaj(0.02)

        QMessageBox.information(None, "Stopnja {}".format(stopnja), "Število razstreljenih žogic: [{}] \nPotrebno število razstreljenih žogic: [{}]".format(eksplodiranih, cilj))
        risar.pobrisi()


def igra_zogice():
    risar.pobrisi()
    zogice(5, randint(1, 2), 1)
    zogice(5, randint(3, 4), 2)
    zogice(10, randint(5, 6), 3)
    zogice(10, randint(7, 8), 4)
    zogice(15, randint(9, 10), 5)
    zogice(15, randint(10, 11), 6)
    zogice(20, randint(11, 13), 7)
    zogice(20, randint(14, 17), 8)
    zogice(30, randint(20, 23), 9)
    zogice(30, randint(24, 30), 10)
    QMessageBox.information(None, "KONEC!!","Bravo uspelo ti je! Ti si car :D")

#==========================================================

zogica()
zogice1(30)
zogice2(30)
zogice3(30)
igra_zogice()
risar.stoj()
