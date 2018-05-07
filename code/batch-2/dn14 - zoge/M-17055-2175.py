import risar
import time

import time
from random import randint, random, choice
x, y = risar.nakljucne_koordinate()
vx, vy = randint(-5, 5),randint(-5, 5)
barva = risar.nakljucna_barva()
r= 10

cas = time.time()
t = 0.02

risar.krog(x, y, r, barva, sirina=1)
while True:

    if x < r:
        vx = abs(vx)
    if x > risar.maxX - r:
        vx = -abs(vx)
    if y < r:
        vy = abs(vy)
    if y > risar.maxY - r:
        vy = -abs(vy)


    x += vx
    y += vy
    risar.krog(x, y, 10, barva, sirina=1)
    risar.cakaj(t)
    risar.pobrisi()







    c=abs(cas - time.time())
    if c > 20:
        print("a")
        break


risar.krog(x, y, 10, barva, sirina=1)
risar.stoj()




