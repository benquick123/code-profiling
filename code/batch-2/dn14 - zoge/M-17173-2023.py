from math import sqrt

import risar
from random import randint

# Naloga za 6:
"""
x, y = risar.nakljucne_koordinate()
krog = risar.krog(x, y, 10, risar.zelena, 3)

vx = randint(-5, 5)
k = randint(-3, 3)
vy = vx*k
for i in range(750):
    krog.setPos(krog.x() + vx, krog.y() + vy)
    risar.cakaj(0.02)
    if not (0 < krog.x() < risar.maxX - 10):
        vx = -vx
    if not (0 < krog.y() < risar.maxY - 10):
        vy = -vy
"""


# Naloga za 7:
seznam_imen = []
xs = []
ys = []
for i in range(30):
    x, y = risar.nakljucne_koordinate()
    krog = risar.krog(x, y, 10, risar.nakljucna_barva(), 3)
    vx = randint(-5, 5)
    vy = sqrt(25-vx)
    seznam_imen.append(krog)
    xs.append(vx)
    ys.append(vy)

for i in range(2000):
    for n in range(len(seznam_imen)):
        seznam_imen[n].setPos(seznam_imen[n].x() + xs[n], seznam_imen[n].y() + ys[n])
        if not (0 < seznam_imen[n].x() < risar.maxX - 10):
            xs[n] -= 2*xs[n]
        if not (0 < seznam_imen[n].y() < risar.maxY - 10):
            ys[n] -= 2*ys[n]
    risar.cakaj(0.02)
