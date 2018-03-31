import collections
import math
from random import randint
import risar
import random
import os
import time
from datetime import datetime
from threading import Timer

def exitfunc():
    datetime.now()
    os._exit(0)

Timer(20, exitfunc).start()

nak_barva=risar.nakljucna_barva()
#nak_koordinate=risar.nakljucne_koordinate()
#x, y=nak_koordinate
x=randint(10, risar.maxX-10)
y=randint(10, risar.maxY-10)
okrogla_stvar=risar.krog(x, y, 10, barva=nak_barva, sirina=1)
randpremik=randint(-5, 5)
randome=random.choice([-1, 1])
vx=randpremik
vy=randome*math.sqrt(vx*vx+25)
for i in range(10000):
    okrogla_stvar.setPos(okrogla_stvar.x()+vx, okrogla_stvar.y()+vy)
    if not (10 < okrogla_stvar.x() < risar.maxX - 10):
        vx=-vx

    if not (10 < okrogla_stvar.y() < risar.maxY - 10):
        vy=-vy




    risar.cakaj(0.02)




