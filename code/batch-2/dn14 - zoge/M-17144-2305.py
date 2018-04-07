import risar
import time
import sys
from random import randint
from math import sqrt

zacetek= 0
x= randint(0, 800)
y= randint(0, 500)
krog = risar.krog(x,y,10,risar.barva(randint(0,255),randint(0,255),randint(0,255)))
sx= randint(-5,5)
sy= sqrt(25 - sx**2)
while True:
    start= time.time()
    x += sx
    y += sy
    if y - 10 < 0:
        sy *= -1
    if y + 10 > 500:
        sy *= -1
    if x - 10 < 0:
        sx *= -1
    if x + 10 > 800:
        sx *= -1
    krog.setPos(x, y)
    risar.cakaj(0.02)
    end = time.time()
    zacetek +=(end-start)
    if zacetek > 20:
        sys.exit(0)

