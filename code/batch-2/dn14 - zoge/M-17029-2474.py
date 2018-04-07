from random import randint
import risar, datetime
from math import sqrt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox

def naredi_krogi(n):
    krogi = []
    i = x = y = 0
    while i < n:
        x = randint(-5, 6)
        x1 = sqrt(x**2)
        y = (5 - x1)**2
        if sqrt(x ** 2 + y ** 2) == 5:
            krogi.append([risar.krog(randint(15, risar.maxX-15), randint(15, risar.maxY-15), 10, risar.nakljucna_barva()), x, y])
            x = y = 0
            i += 1
    return krogi

def pobarvaj(krog):
    c = krog.pen().color().lighter()
    c.setAlpha(192)
    krog.setBrush(c)
    return krog

def eksplodiraj(krog, x, y):
    krog.setPos(x, y)
    krog.setRect(-30, -30, 60, 60)

def za_ekplodiranje(krog, eksplodirani):
    for e in eksplodirani:
        dis = sqrt((krog.x() - e[0].x()) ** 2 + (krog.y() - e[0].y()) ** 2)
        if dis <= 40:
            eksplodiraj(krog, krog.x(), krog.y())
            return True
    return False

def izgini(eksplodirani):
    for e in eksplodirani:
        if abs(e[1] - datetime.datetime.now().second) > 4:
            e[0].hide()
            eksplodirani.remove(e)

def elementi(n):
    return naredi_krogi(n), False, False, "", [], 0

def window(n, u, s):
    QMessageBox.information(None, "ŽOGE", str.format("Uspelo ti je raztreliti {} žog od {}.{}", n, u, s))



n, u = 7, 1
krogi, klikneno, risar.klik, miska_krog, eksplodirani, kolku = elementi(n)
level = 1
while True:
    izgini(eksplodirani)
    x, y = risar.miska

    if level > 10:
        break

    if risar.maxX / 2 != x and risar.maxY / 2 != y and not miska_krog:
        miska_krog = risar.krog(x, y, 30, risar.nakljucna_barva())

    if miska_krog and not klikneno:
        miska_krog.setPos(x, y)

    if risar.klik and not klikneno:
        if not za_ekplodiranje(miska_krog, krogi):
            risar.pobrisi()
            window(0, n, " Premalo!")
            krogi, klikneno, risar.klik, miska_krog, eksplodirani, kolku = elementi(n)
        else:
            eksplodirani.append((miska_krog, datetime.datetime.now().second))
            klikneno = True

    for krog in krogi:
        krog[0].setPos(krog[0].x() - krog[1], krog[0].y() + krog[2])
        if not (15 < krog[0].x() < risar.maxX - 15):
            krog[1] = -krog[1]
        if not (15 < krog[0].y() < risar.maxY - 15):
            krog[2] = -krog[2]
        if miska_krog:
             if za_ekplodiranje(krog[0], eksplodirani):
                eksplodirani.append((pobarvaj(krog[0]), datetime.datetime.now().second))
                krogi.remove(krog)
                kolku += 1

    if klikneno and not eksplodirani:
        if kolku >= u:
            risar.pobrisi()
            window(kolku, n, " Bravo!")
            n += 2
            u += 2
            level += 1
            krogi, klikneno, risar.klik, miska_krog, eksplodirani, kolku = elementi(n)
        else:
            risar.pobrisi()
            window(kolku, n, " Premalo!")
            krogi, klikneno, risar.klik, miska_krog, eksplodirani, kolku = elementi(n)
    risar.cakaj(0.02)


