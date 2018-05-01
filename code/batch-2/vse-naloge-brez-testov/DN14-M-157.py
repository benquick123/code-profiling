from math import *
import risar, os
from random import randint, random
from risar import stoj

storage = []
vx = []
vy = []
for a in range(30):
    ball = risar.krog(randint(0, 255), randint(0, 255), 10 ,risar.nakljucna_barva(), 5)
    storage.append(ball)
    vx.append(2+random() * 3)
    vy.append(2+random() * 3)

for i in range(5000):
    for i in range(len(storage)):
        ball = storage[i]
        ball.setPos(ball.x() + vx[i], ball.y() + vy[i])
        if not (0 < ball.x() < risar.maxX - 35):
            vx[i] = -vx[i]
        if not (0 < ball.y() < risar.maxY - 35):
            vy[i] = -vy[i]
    risar.cakaj(0.01)