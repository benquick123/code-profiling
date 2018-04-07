import risar
from random import randint
from math import sqrt
import time
from PyQt5.QtWidgets import QMessageBox

leveli = [(2, 5), (2, 6), (3, 8), (5, 10), (6, 14), (7, 16), (10, 22), (10, 24), (12, 26), (15, 30)]

def game(l):
    lvl = l
    (destroy, balls) = leveli[lvl]
    risar.klik = False
    risar.pobrisi()
    krogi = []
    hx = []
    hy = []
    eksplodirani_krog = []
    krog_miska = risar.krog(risar.maxX / 2, risar.maxY / 2, 30, risar.bela, 3)
    krog_miska_pogoj = 0
    krog_miska_timer = 1
    rezultat = 0
    kraj = 1

    def exploding_krog(a, krogg):
        krogg.setRect(-30, -30, 60, 60)
        c = krogg.pen().color().lighter()
        c.setAlpha(192)
        krogg.setBrush(c)
        (hx[a], hy[a]) = (0, 0)
        """Doing BOOM BOOM"""

    QMessageBox.information(None, "Game", "Destroy {} out of {} balls.".format(destroy, balls))

    for j in range(balls):
        (x, y) = randint(10, risar.maxX - 15), randint(10, risar.maxY - 15)
        krogi.append(risar.krog(x, y, 10, risar.nakljucna_barva(), 3))
        vx = randint(-5, 5)
        hx.append(vx)
        hy.append(sqrt(5 ** 2 - vx ** 2))
        eksplodirani_krog.append(("F", "F"))
        """Quickly gets all values"""

    for i in range(50000):
        for h in range(len(krogi)):
            krog = krogi[h]
            krog.setPos(krog.x() + hx[h], krog.y() + hy[h])
            if not (10 < krog.x() < risar.maxX - 10):
                hx[h] = -hx[h]
            if not (10 < krog.y() < risar.maxY - 10):
                hy[h] = -hy[h]
            if not risar.klik:
                (miska_x, miska_y) = risar.miska
                krog_miska.setPos(miska_x, miska_y)
            if risar.klik:
                if krog_miska_timer == 1:
                    krog_miska_timer = time.time()
                    krog_miska_pogoj = 1
                if hx[h] != 0 or hy[h] != 0:
                    if krog.x() - 40 < krog_miska.x() < krog.x() + 40 and \
                            krog.y() - 40 < krog_miska.y() < krog.y() + 40:
                        if krog not in eksplodirani_krog[h]:
                            exploding_krog(h, krog)
                            krog_time = time.time()
                            eksplodirani_krog[h] = (krog, krog_time)
                            kraj += 1
                            rezultat += 1
                            """Checking if any ball collide with mouse_ball"""
                    for s in range(len(krogi)):
                        if hx[s] == 0 and hy[s] == 0:
                            krogs = krogi[s]
                            if krogs.x() - 40 < krog.x() < krogs.x() + 40 and \
                                    krogs.y() - 40 < krog.y() < krogs.y() + 40:
                                if krog not in eksplodirani_krog[h]:
                                    exploding_krog(h, krog)
                                    krog_time = time.time()
                                    eksplodirani_krog[h] = (krog, krog_time)
                                    kraj += 1
                                    rezultat += 1
                                    """Checking if any ball collide with another_ball"""
            if eksplodirani_krog[h][0] is krog:
                if time.time() - eksplodirani_krog[h][1] > 4 and krog.x() != -100:
                    krog.setPos(-100, -100)
                    krogi[h] = krog
                    kraj -= 1
                    """Making ball disappear"""
            if krog_miska_pogoj == 1:
                if time.time() - krog_miska_timer > 4:
                    krog_miska.setPos(-100, -100)
                    krog_miska_pogoj = 2
                    kraj -= 1
        if kraj == 0:
            if lvl == 9:
                QMessageBox.information(None, "Game",
                                        "YOU HAVE WON. CONGRATULATIONS. Now, get back to your work")
                exit()
            if rezultat == balls:
                QMessageBox.information(None, "Game",
                                        "You are the master of the game. All balls destroyed. Next level.")
                lvl += 1
                game(lvl)
            elif rezultat >= destroy:
                QMessageBox.information(None, "Game",
                                        "You have destroyed {} out of {}. Next level.".format(rezultat, balls))
                lvl += 1
                game(lvl)
            else:
                QMessageBox.information(None, "Game",
                                        "You have destroyed {} out of {}. Try again.".format(rezultat, balls))
                game(lvl)
        risar.cakaj(0.02)

game(0)
