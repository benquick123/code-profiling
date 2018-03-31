import risar
import time
from random import *
from math import *
cas_odbijanja = time.time()
def odboj(zoga, x, y, hitrost_X, hitrost_Y):
    while True:
        x += hitrost_X
        y += hitrost_Y
        zoga.setPos(x, y) #hvala asistent Lazar
        if x not in range(0, risar.maxX):
            hitrost_X = hitrost_X * (-1)
        if y not in range (0, risar.maxY):
            hitrost_Y = hitrost_Y * (-1)
        risar.cakaj(0.02)
        if (cas_odbijanja+20 <= time.time()):
            break



x,y = risar.nakljucne_koordinate()
zoga = risar.krog(x, y, 10, risar.nakljucna_barva(),3)
hitrost_X = randint(-5, 5)
hitrost_Y = int(sqrt(25 - hitrost_X**2)) #pitagorov izrek
odboj(zoga, x, y, hitrost_X, hitrost_Y)
risar.stoj()
