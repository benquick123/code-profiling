import risar
import random
from math import *

x = float(random.randrange(-risar.maxX, risar.maxX))
y = float(random.randrange(-risar.maxY, risar.maxY))
barva = risar.nakljucna_barva()
risar.krog(abs(x), abs(y), 10, barva , 1)

x1 = float(random.uniform(-5,5))
y1 = sqrt(5**2 - x1**2)
x = abs(x)
y = abs(y)
for a in range(900):
    if x > risar.maxX-1 or x < 0:
        x1 = -x1
    if y > risar.maxY-1 or y < 0:
        y1 = -y1
    x = x + x1
    y = y + y1
    risar.pobrisi()
    risar.krog(x, y, 10, barva, 1)
    risar.cakaj(0.02)