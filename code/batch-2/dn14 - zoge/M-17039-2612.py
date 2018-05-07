from math import sqrt

import risar
from random import randint, choice, random
from PyQt5.QtWidgets import QMessageBox

class Zoga:
    def __init__(self):
        zoge = []
        vx =2
        vy=2
        self.x = randint(0, risar.maxX)
        self.y = randint(0, risar.maxY)
        self.angle = randint(0,360)
        self.barva = risar.nakljucna_barva()
        krog = risar.krog(self.x, self.y, 10, self.barva)
        zoge.append(krog)
        for i in range(1667):
            for i in range(len(zoge)):
                faca = zoge[i]
                faca.setPos(faca.x() + vx, faca.y() + vy)
                if not (0 < faca.x() < risar.maxX - 10):
                    vx = -vx
                if not (0 < faca.y() < risar.maxY - 10):
                    vy = -vy
            risar.cakaj(0.01)

        risar.stoj()





class Veliko_zog():
    def __init__(self):
        zoge = []
        vx = []
        vy = []
        x, y = risar.miska
        miska = risar.krog(x, y, 20, risar.rdeca)
        cnt = 0
        for i in range(30):
            zoga = risar.krog(randint(0, risar.maxX), randint(0, risar.maxY), 10, risar.nakljucna_barva())
            zoge.append(zoga)
            vx.append(1.5 + random())
            vy.append(1.5 + random())
        for i in range(1667):
            for i in range(len(zoge)):
                zogica = zoge[i]
                if risar.klik == False:
                    a = miska.setPos(x + risar.miska[0] - 394, y + risar.miska[1] - 244)
                if risar.klik == True and cnt == 0:
                    risar.krog(x + risar.miska[0] - 394, y + risar.miska[1] - 244, 20, risar.rdeca)
                    x, y = x + risar.miska[0] - 394, y + risar.miska[1] - 244
                zogica.setPos(zogica.x() + vx[i], zogica.y() + vy[i])
                if not (0 < zogica.x() <= risar.maxX - 10):
                    vx[i] = -vx[i]
                if not (0 < zogica.y() <= risar.maxY - 10):
                    vy[i] = -vy[i]
                if sqrt((zogica.x()- x)**2 +(zogica.y()- y)**2)<= 20:
                    break
            risar.cakaj(0.01)
            cnt+= 1


ana = Veliko_zog()
