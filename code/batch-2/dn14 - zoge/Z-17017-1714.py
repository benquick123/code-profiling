import risar
from random import randint
from math import sqrt

#naloga 6
barva = risar.nakljucna_barva()
x, y = risar.nakljucne_koordinate()
krog = risar.krog(x, y, 10, barva)
a = randint(-5, 5)
b = sqrt(25 - a**2)
for i in range(900):
    krog.setPos(krog.x() + a, krog.y() + b)
    if not (10 < krog.x() < risar.maxX - 10):
        a = -a
    if not (10 < krog.y() < risar.maxY - 10):
        b = -b
    risar.cakaj(0.02)

#naloga 7
krogi = []
a = []
b = []
for i in range(30):
    x, y = risar.nakljucne_koordinate()
    barva = risar.nakljucna_barva()
    krogi.append(risar.krog(x, y, 10, barva))
    c = randint(-5, 5)
    a.append(c)
    b.append(sqrt(25 - c**2))

for j in range(900):
    for k in range(len(krogi)):
        krog = krogi[k]
        krog.setPos(krog.x() + a[k], krog.y() + b[k])
        if not (10 < krog.x() < risar.maxX - 10):
            a[k] = -a[k]
        if not (10 < krog.y() < risar.maxY - 10):
            b[k] = -b[k]
        risar.cakaj(0.02)