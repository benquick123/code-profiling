import risar
from math import sqrt
from random import randint

x, y = risar.nakljucne_koordinate()
krog = risar.krog(x, y, 10, risar.nakljucna_barva())
x1 = randint (-5, 5)
y1 = sqrt(25 - (x1**2))
for a in range(1, 650):
    krog.setPos(x, y)
    if x >= risar.maxX or x <= 0:
        x1 = -x1
    if y >= risar.maxY or y <= 0:
        y1 = -y1
    x += x1
    y += y1
    risar.cakaj(0.02)
