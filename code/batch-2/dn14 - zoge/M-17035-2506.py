import risar
import time
from random import *

#NALOGA ZA 6

spremenljiva_x = randint(1,5) * 2
spremenljiva_y = randint(1,5) * 2
y = risar.maxY -12
x = risar.maxX -12
konec = time.time() + 20
krog = risar.krog(randint(0,y),randint(0,y),10,barva = risar.nakljucna_barva(),sirina=3)

while(time.time() < konec):
        krog.setPos(krog.x() + spremenljiva_x, krog.y() + spremenljiva_y)
        if not (12 < krog.x() < x):
            spremenljiva_x = -spremenljiva_x
        if not (12 < krog.y() < y):
            spremenljiva_y = -spremenljiva_y
        risar.cakaj(0.01)




#NALOGA ZA 7

seznam_krog = []
spremenljiva_x = []
spremenljiva_y = []
y = risar.maxY -12
x = risar.maxX -12
konec = time.time() + 20

for krogi in range(30):
    faca = risar.krog(randint(0,400),randint(0,400),10,barva = risar.nakljucna_barva(),sirina=3)
    seznam_krog.append(faca)
    spremenljiva_x.append(randint(1,5) * 2)
    spremenljiva_y.append(randint(1,5) * 2)


while(time.time() < konec):
    for i in range(30):
        krog = seznam_krog[i]
        krog.setPos(krog.x() + spremenljiva_x[i], krog.y() + spremenljiva_y[i])
        if not (0 < krog.x() < x):
            spremenljiva_x[i] = -spremenljiva_x[i]
        if not (0 < krog.y() < y):
            spremenljiva_y[i] = -spremenljiva_y[i]
    risar.cakaj(0.01)