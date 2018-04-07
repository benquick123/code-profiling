import risar
import math
import time
from random import randint

start = time.time()
time.clock()
sekunde = 20
cas=0
sez=[]
sez1=[]

for x in range(29):
    barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
    sirina = 6
    x0 = randint(0, risar.maxX)
    y0 = randint(0, risar.maxY)
    zoge = risar.krog(x0, y0, 10, barva, sirina)
    sez.append(zoge)
    x1 = randint(-5, 5)
    c = x1 ** 2 + 5 ** 2
    d = math.sqrt(c)
    f = round(d)
    sez1.append([x1,d])


while cas < sekunde:
    for zoge, b in zip(sez, sez1):
        zoge.setPos(zoge.x() + b[0], zoge.y() + b[1])
        if not (0 < zoge.x() < (risar.maxX - 1)):
            b[0] = -b[0]

        if not (0 < zoge.y() < (risar.maxY - 1)):
            b[1] = -b[1]

        cas = time.time() - start
    risar.cakaj(0.02)

risar.odstrani(zoge)
