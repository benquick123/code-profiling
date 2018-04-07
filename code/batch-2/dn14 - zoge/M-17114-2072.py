from random import randint
from PyQt5.QtWidgets import QMessageBox
from math import sqrt
import time

import risar

class Kroglica:
    def __init__(self):
        self.x = randint(10, risar.maxX - 10)
        self.y = randint(10, risar.maxY - 10)
        self.vx = randint(-5,5)
        self.vy  = sqrt(25 - self.vx**2)
        self.krog = risar.krog(self.x, self.y, 10, risar.nakljucna_barva())
        self.cas = 0

    def poci(self):
        self.krog.setRect(-30, -30, 60, 60)
        c = self.krog.pen().color().lighter()
        c.setAlpha(192)
        self.krog.setBrush(c)
        self.vx, self.vy = 0, 0

    def premik(self):
        self.x += self.vx
        self.y += self.vy
        if not (10 <= self.x <= risar.maxX - 10):
            self.vx *= -1
        if not (10 <= self.y <= risar.maxY - 10):
            self.vy *= -1
        self.krog.setPos(self.x, self.y)

class Miska:
    def __init__(self):
        (self.x, self.y) = risar.miska
        self.krog = risar.krog(self.x, self.y, 30)
        self.miruje = False
        self.cas = 0

    def update(self):
        if not risar.klik:
            (self.x, self.y) = risar.miska
            self.krog.setPos(self.x, self.y)

def razdalja(x0, y0, x1, y1):
    return(sqrt((x0-x1)**2 + (y0-y1)**2))

def za_6():
    zac = time.time()
    kroglica = Kroglica()
    while time.time() - zac < 20:
        kroglica.premik()
        risar.cakaj(0.02)

def za_7():
    zac = time.time()
    s = [Kroglica() for i in range(30)]
    while time.time() - zac < 20:
        for kroglica in s:
            kroglica.premik()
        risar.cakaj(0.02)

def za_8():
    a = 1
    miska = Miska()
    s = [Kroglica() for i in range(30)]
    while True and a:
        for kroglica in s:
            kroglica.premik()
            if risar.klik:
                if razdalja(kroglica.x, kroglica.y, miska.x, miska.y) <= 40:
                    a = 0
                    break
        miska.update()
        risar.cakaj(0.02)

def stopnja(st_zog):
    vsota = 0
    miska = Miska()
    s = [Kroglica() for i in range(st_zog)]
    pocene = [miska]
    while pocene :
        for kroglica in s:
            kroglica.premik()
            if risar.klik:
                    for pocena in pocene:
                        if razdalja(kroglica.x, kroglica.y, pocena.x, pocena.y) <= 40:
                            if kroglica in s:
                                s.remove(kroglica)
                                kroglica.poci()
                                kroglica.cas = time.time()
                                pocene.append(kroglica)
                                vsota += 1
        miska.update()
        if risar.klik:
            if miska.cas == 0:
                miska.cas = time.time()
            for pocena in pocene:
                if time.time() - pocena.cas > 4:
                    pocene.remove(pocena)
                    pocena.krog.hide()
        risar.cakaj(0.02)
    for ostali in s:
        ostali.krog.hide()
    risar.klik = False
    return vsota

def za_9():
    vsota = stopnja(30)
    QMessageBox.information(None, "", "Razstrelil si {} žog!".format(vsota))

def za_10():
    tezavnost = [(5,1), (20,8), (20,10), (18,10),(10, 4), (10,5), (18,12), (10,6), (10,7), (10,8)]
    for i, (st_zog, zahtevano) in enumerate(tezavnost):
        QMessageBox.information(None, "Level {}".format(i+1), "Razstreli {} žog od {}!".format(zahtevano, st_zog))
        while True:
            vsota = stopnja(st_zog)
            if vsota >= zahtevano:
                break
            else:
                QMessageBox.information(None, "Level {}".format(i+1), "Uspelo ti je razstreliti {} žog. Premalo!".format(vsota))

za_10()