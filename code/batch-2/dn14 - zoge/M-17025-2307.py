import risar
from random import randrange, randint, choice
from math import *

risar.obnavljaj = True

seznam_krogov = []
for o in range(30):
    seznam_krogov.append(risar.krog(randint(15, risar.maxX - 15), randint(15, risar.maxY - 15), 15,
                                    risar.barva(choice([100, 255]), choice([100, 255]), choice([100, 255])), 3))

seznam_hitrosti = []
for krog in seznam_krogov:
    x = randint(-5, 5)
    y = sqrt(pow(5, 2) - pow(x, 2))
    seznam_hitrosti.append([x, y])

krog1 = risar.krog(risar.miska[0], risar.miska[1], 25,
                   risar.barva(choice([255, 255]), choice([255, 255]), choice([255, 255])), 5)


while 1:
    if not risar.klik:
        krog1.setPos(risar.miska[0], risar.miska[1])

    for i in range(len(seznam_krogov)):
        krog = seznam_krogov[i]
        x, y = seznam_hitrosti[i]
        krog.setPos(krog.x() + x, krog.y() + y)
        if krog.x() < 15 or krog.x() > risar.maxX - 15:
            seznam_hitrosti[i][0] = -x
        elif krog.y() < 15 or krog.y() > risar.maxY - 15:
            seznam_hitrosti[i][1] = -y
        if risar.klik and krog1.x() - 40 < krog.x() < krog1.x() + 40 and krog1.y() - 40 < krog.y() < krog1.y() + 40:
                exit()

    risar.cakaj(0.02)
