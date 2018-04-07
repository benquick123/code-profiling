import math
from random import randint
from time import time

b = randint(10, risar.maxY - 10)
a = randint(10, risar.maxX - 10)

speeda = randint(-5, 5)
speedb = math.sqrt(10 - speeda * 2)


v = time()
ball = risar.krog(a, b, 10, risar.nakljucna_barva(), 3)

while v - time() < 20:
    if b <= 10:
        speedb = -speedb
	if b >= risar.maxY - 10:
        speedb = -speedb
    if a <= 10:
        speeda = -speeda
	if a >= risar.maxX - 10:
        speeda = -speeda
    b += speedb
	a += speeda
    ball.setPos(a, b)
    risar.cakaj(0.02)
