from math import *
from random import randint, uniform
from time import time, sleep
import risar
from PyQt5.QtWidgets import QMessageBox

class Zoga:
    def __init__(self):
        self.x = randint(0, risar.maxX)
        self.y = randint(0, risar.maxY)
        self.r = 10
        self.vx = uniform(-5, 5)
        self.vy = sqrt(25 - self.vx ** 2)
        self.color = risar.nakljucna_barva()
        self.circle = risar.krog(self.x, self.y, self.r, self.color)
        self.exploded = False
        self.hidden = False
        self.t = 0
        self.update()

    def update(self):
        self.circle.setPos(self.x, self.y)

    def naprej(self):
        tx, ty = self.x + self.vx, self.y + self.vy
        if tx > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        if tx < self.r:
            self.vx = abs(self.vx)

        if ty > risar.maxY - self.r:
            self.vy = -abs(self.vy)
        if ty < self.r:
            self.vy = abs(self.vy)

        self.x += self.vx
        self.y += self.vy
        self.update()

    def se_dotika(self, x, y, r):
        return sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= self.r + r

    def explode(self):
        self.r = 30
        self.vx, self.vy = 0, 0
        self.circle.setRect(-30, -30, 60, 60)
        c = self.circle.pen().color().lighter()
        c.setAlpha(192)
        self.circle.setBrush(c)
        self.exploded = True





class Mis:
    def __init__(self):
        self.x, self.y = risar.miska
        self.circle = risar.krog(self.x, self.y, 30)
        self.kliknjena = False
        self.t = 0
        self.update()

    def update(self):
        self.x, self.y = risar.miska
        self.circle.setPos(self.x, self.y)






# and not((self.vx < 0 and self.x + 15 > risar.maxX) or ())

def za_6():
    z = Zoga()
    t = time()
    while time() - t <= 20:
        z.naprej()
        risar.cakaj(0.02)

def za_7():
    zoge = {Zoga() for j in range(30)}
    t = time()
    while time() - t <= 20:
        for z in zoge:
            z.naprej()
        risar.cakaj(0.02)

def za_8():
    zoge = {Zoga() for j in range(30)}
    m = Mis()
    t = time()
    konc = False
    while time() - t <= 20 and not konc:
        for z in zoge:
            z.naprej()
            if m.kliknjena:
                if z.se_dotika(m.x, m.y, 30):
                    konc = True

        if not m.kliknjena:
            m.update()

        if risar.klik:
            m.kliknjena = True
        risar.cakaj(0.02)

def za_9():
    st_zog = 30
    zoge = {Zoga() for j in range(st_zog)}
    m = Mis()
    konc = False
    st_eksplodiranih = 0
    eksplodirane = {m}
    while not konc:
        for z in zoge:
            z.naprej()
            if m.kliknjena:
                for e in eksplodirane:
                    if z.se_dotika(e.x, e.y, 30):
                        if z.exploded:
                            if m.t - z.t >= 4:
                                z.circle.hide()
                                z.hidden = True
                        else:
                            z.explode()
                            st_eksplodiranih += 1
                            z.t = time()
                        break
                if z.hidden:
                    eksplodirane.discard(z)
                    if len(eksplodirane) == 1: #ce je not samo se m, pol ni not nobene zoge
                        QMessageBox.information(None, "Konec", "Razstrelili ste {} žog od {}".format(st_eksplodiranih, st_zog))
                        konc = True
                        break
                elif z.exploded:
                    eksplodirane.add(z)

        if not m.kliknjena:
            m.update()

        if risar.klik:
            m.kliknjena = True
            m.t = time()
        risar.cakaj(0.02)

def za_10():
    i = 1
    while i <= 10:
        cilj, st_zog = i + 2, 9 + int(i / 3)
        QMessageBox.information(None, "", "Razstreli {} žog od {}".format(cilj, st_zog))
        i += stopnja(cilj, st_zog)
    QMessageBox.information(None, "", "Zmaga!")

def stopnja(cilj, st_zog):
    risar.pobrisi()
    risar.klik = False
    zoge = {Zoga() for j in range(st_zog)}
    m = Mis()
    t = time()
    fix = True
    m.kliknjena = False
    st_eksplodiranih = 0
    eksplodirane = {m}
    while m.t == 0 or len(eksplodirane) > 1 or abs(m.t - time()) <= 4:
        for z in zoge:
            z.naprej()
            if m.kliknjena:
                for e in eksplodirane:
                    if z.se_dotika(e.x, e.y, 30):
                        if z.exploded:
                            if abs(time() - z.t) >= 4:
                                z.circle.hide()
                                z.hidden = True
                        else:
                            z.explode()
                            st_eksplodiranih += 1
                            z.t = time()
                        break
                if z.hidden:
                    eksplodirane.discard(z)
                    if len(eksplodirane) == 1:  # ce je not samo se m, pol ni not nobene zoge
                        if st_eksplodiranih >= cilj:
                            return 1
                        else:
                            QMessageBox.information(None, "",
                                                    "Uspelo ti je razstreliti {} žog. Premalo.".format(st_eksplodiranih))
                            return 0
                elif z.exploded:
                    eksplodirane.add(z)

        if not m.kliknjena:
            m.update()


        if risar.klik and fix:
            m.kliknjena = True
            m.t = time()
            fix = False
        risar.cakaj(0.02)
    QMessageBox.information(None, "", "Uspelo ti je razstreliti 0 žog. Premalo.")
    return 0

#sqrt((m.x - z.x) ** 2 + (m.y - z.y) ** 2) <= 30 + z.r


# za_6()

# za_7()

# za_8()

# za_9()

za_10()
