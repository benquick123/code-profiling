__author__ = 'Haris'

import risar
import random
from math import *


krogle = []
vx = []
vy = []
for i in range(30):

    kroglica = risar.krog(random.randint(0, risar.maxX - 100), random.randint(0, risar.maxY - 100),10, barva=risar.nakljucna_barva(), sirina=1)
    krogle.append(kroglica)
    hitrost=random.uniform(-5,5)
    vx.append(hitrost)
    if hitrost>0:
        a=sqrt(hitrost**2)-sqrt(25)
        vy.append(random.choice([-a,a]))
    else:
        b=sqrt(25)-sqrt(hitrost**2)
        vy.append(random.choice([-b,b]))

#900 ponovitev je 21s, 850 je prbl. 20s
for p in range(850):
    for i in range(len(krogle)):
        kroglica = krogle[i]

        kroglica.setPos(kroglica.x() + vx[i], kroglica.y() + vy[i])
        if not (0 < kroglica.x() < risar.maxX - 10):
            vx[i] = -vx[i]
        if not (0 < kroglica.y() < risar.maxY - 10):
            vy[i] = -vy[i]
    risar.cakaj(0.02)
