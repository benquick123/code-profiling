import risar
from math import *
from random import randint
import time

x_os = randint(0, (risar.maxX - 10))
y_os = randint(0, (risar.maxY - 10))
polmer = 10
barva = risar.nakljucna_barva()
sirina = 2

krog = risar.krog(x_os, y_os, polmer, barva, sirina)
x = randint(-5, 5)
y = sqrt(5 ** 2 - x ** 2)
t = time.time() + 20

while t > time.time():
    krog.setPos(krog.x() + x, krog.y() + y)

    if krog.x() > (risar.maxX - 10):
        x = -x
        krog.setPos(risar.maxX-10, krog.y())

    elif krog.y() > (risar.maxY - 10):
        y = -y
        krog.setPos(krog.x(), risar.maxY-10)

    elif krog.x() < 10:
        x = -x
        krog.setPos(10, krog.y())

    elif krog.y() < 10:
        y = -y
        krog.setPos(krog.x(), 10)

    risar.cakaj(0.02)

