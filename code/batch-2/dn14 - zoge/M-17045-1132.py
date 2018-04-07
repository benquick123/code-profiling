import risar
from random import randint, random, choice
from PyQt5.QtWidgets import QMessageBox
import time
from math import *


class Krog:
    def __init__(self):
        self.x, self.y = randint(0, risar.maxX-1), randint(0, risar.maxY-1)
        self.r = 10
        self.objekt = 0
        self.barva = risar.nakljucna_barva()
        self.hitrostx = randint(-5,5)
        self.hitrosty = sqrt((5**2) - (self.hitrostx**2))
        self.time_creation = time.time()
        self.time_explosion = 0
        self.mobile = True
        self.brush = 0

    def __del__(self):
        pass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_r(self):
        return self.r

    def narisi(self):
        self.objekt = risar.krog(self.x, self.y, self.r, barva=self.barva)

    def update(self):
        self.x += self.hitrostx
        self.y += self.hitrosty
        self.objekt.setPos(self.x, self.y)
        if self.x >= risar.maxX-1 or self.x <= 0:
            self.hitrostx = -self.hitrostx
            # risar.barvaOzadja(risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)))
            # Če hočete epileptični napad
        elif self.y >= risar.maxY-1 or self.y <= 0:
            self.hitrosty = -self.hitrosty
            # risar.barvaOzadja(risar.barva(randint(0, 255), randint(0, 255), randint(0, 255)))
            # Če hočete epileptični napad.

    def explode(self):
        self.time_explosion = time.time()
        self.objekt.setRect(-30, -30, 60, 60)
        self.brush = self.objekt.pen().color().lighter()
        self.brush.setAlpha(192)
        self.objekt.setBrush(self.brush)
        self.mobile = False

    def hide(self):
        self.objekt.hide()


def level(ballNum, points_to_achif, level_stage):
    risar.pobrisi()
    risar.klik = False
    QMessageBox.information(None, f"Start Game: Level {level_stage}",
                            f"You get {ballNum} ball. You need at least this many points my frend: {points_to_achif}")
    sez_krog = []
    for i in range(ballNum):
        t = Krog()
        t.narisi()
        sez_krog.append(t)
    fall_count = 0
    embeded = False  # Ali je miska v canvasu aktive
    miska_krog = risar.krog(*risar.miska, r=30)
    mouse_existence = True
    fallen = {}
    timer_of_mouse = 0
    while sez_krog:
        if not risar.klik:
            miska_krog.setPos(*risar.miska)
            timer_of_mouse = time.time()
        else:
            embeded = True
        timer_of_life = time.time()
        if abs(timer_of_life - timer_of_mouse) > 4:
            miska_krog.hide()
            mouse_existence = False
        for ind, krogec in enumerate(sez_krog):
            if krogec.mobile:
                for objekt in list(fallen):
                    if abs(krogec.get_x() - fallen[objekt][0]) < 30 and abs(krogec.get_y() - fallen[objekt][1]) < 30 and embeded:
                        # Tukaj kar kliče za funkcijo, vendar ura je bila 11.
                        # Stvarno je bilo dosta.
                        krogec.explode()
                        fallen[krogec] = (krogec.get_x(), krogec.get_y())
                if abs(krogec.get_x() - miska_krog.x()) < 30 and abs(krogec.get_y() - miska_krog.y()) < 30 and embeded and mouse_existence:
                    krogec.explode()
                    fallen[krogec] = (krogec.get_x(), krogec.get_y())
                krogec.update()
        risar.cakaj(0.02)
        for i in list(fallen):
            timer = time.time()
            if abs(timer - i.time_explosion) > 4:
                i.hide()
                del fallen[i]
                fall_count += 1
        if fall_count and not fallen or (not mouse_existence and not fallen):
            break
    if fall_count < points_to_achif and not mouse_existence:
        QMessageBox.information(None, "Restart Level", "un-optimal algorithm, try again.".format(fall_count))
        level(ballNum=ballNum, points_to_achif=points_to_achif, level_stage=level_stage)
    else:
        QMessageBox.information(None, "Victory", "You have achieved VIKTORI MY BRUDER")


def main():
    diffikulty = {x: (x+4)*5 for x in range(10)}
    levels = [i for i in range(1, 11)]
    incr_difikulty = 2
    for i, j in zip(diffikulty, levels):
        level(diffikulty[i], int(diffikulty[i]/incr_difikulty), j)
        incr_difikulty -= 0.09
        print(incr_difikulty)
    QMessageBox.information(None, "Ultimate Victory", "Dobil si 10 programiranje, čestitke vendarle")


if __name__ == "__main__":
    main()
