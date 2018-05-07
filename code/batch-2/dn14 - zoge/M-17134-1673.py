import risar
import math
from random import *
import random
import time
cas =0
x1 = randint(10, risar.maxX-100)
y1 = randint(10, risar.maxY-100)
color = risar.nakljucna_barva()
x2 = randint(-5, 5)
c = math.sqrt((25 - math.pow(x2, 2)))
y2 = random.choice([c,-c])
krogec = risar.krog(x1, y1, 10, barva=color, sirina=3)
for j in range(3500):
    zacni = time.time()
    krogec.setPos(krogec.x()+x2, krogec.y()+y2)
    if krogec.x() < 0 or krogec.x() > risar.maxX:
        x2 = -x2
    if krogec.y() < 0 or krogec.y() > risar.maxY:
        y2 = -y2
    risar.cakaj(0.02)
    koncaj = time.time()
    cas = cas + (koncaj-zacni)
    if 20.0 <= cas <= 20.6:
        risar.stoj()
