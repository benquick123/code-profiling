import risar
import math
from random import randint
from time import time


x = randint(10, risar.maxX - 10)
y = randint(10, risar.maxY - 10)
hitrostx = randint(-5, 5)
hitrosty = math.sqrt(5 ** 2 - hitrostx ** 2)
zoga = risar.krog(x, y, 10, risar.nakljucna_barva(), 3)
cas = time()

while cas - time() < 20:
    if x <= 10 or x >= risar.maxX - 10:
        hitrostx = -hitrostx
    if y <= 10 or y >= risar.maxY - 10:
        hitrosty = -hitrosty
    x += hitrostx
    y += hitrosty
    zoga.setPos(x, y)
    risar.cakaj(0.02)