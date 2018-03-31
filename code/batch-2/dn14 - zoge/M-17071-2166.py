import risar
from random import *
from math import sin
from math import cos
from math import sqrt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Krog(QGraphicsEllipseItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.x,self.y = randint(20, risar.maxX - 20), randint(20, risar.maxY - 20)
        self.barva = risar.nakljucna_barva()
        self.circle = risar.krog(0, 0, 10, self.barva, 3)
        self.rotation = randint(0, 360)
        self.speed = 5
        self.vx = cos(self.rotation) * self.speed
        self.vy = sin(self.rotation) * self.speed
        self.risi()
        self.time = 4
        self.boom = False

    def risi(self):
        self.circle.setPos(self.x, self.y)

    def remove(self):
        self.circle.hide()

class Miska():
    def __init__(self):
        self.x, self.y = risar.maxX/2, risar.maxY/2
        self.circle = risar.krog(0, 0, 30, barva=risar.bela, sirina=3)
        self.update()
        self.time = 4
        self.shown = True

    def update(self):
        (x,y) = risar.miska
        (self.x, self.y) = risar.miska
        self.circle.setPos(x, y)

    def remove(self):
        self.circle.hide()
        self.shown = False

    def reset(self):
        self.x, self.y = risar.maxX / 2, risar.maxY / 2
        self.circle = risar.krog(0, 0, 30, barva=risar.bela, sirina=3)
        self.update()
        self.time = 4
        self.shown = True
        self.circle.show()
        risar.klik = False

def premik(A):
    A.x = A.x + A.vx
    A.y = A.y + A.vy
    if not (10 < A.x < risar.maxX - 10):
        A.vx = -A.vx
    if not (10 < A.y < risar.maxY - 10):
        A.vy = -A.vy
    A.risi()

def Ocena6():
    A = Krog()
    for i in range (1, 100000000000):
        premik(A)
        risar.cakaj(0.02)
    risar.pobrisi()

def Ocena7():
    zoge = []
    stevilo = 30
    for x in range(0, stevilo):
        zoge.append(Krog())
    for i in range(1, 1000):
        for A in zoge:
            premik(A)
        risar.cakaj(0.02)

def Ocena8():
    zoge = []
    M = Miska()
    stevilo = 30
    hit = False
    for x in range(0, stevilo):
        zoge.append(Krog())
    while hit == False:
        for A in zoge:
            premik(A)
            if not risar.klik:
                M.update()
            else:
                d = sqrt(((A.x - M.x))**2 + ((A.y - M.y))**2)
                if d < 40:
                    zoge.remove(A)
                    hit = True
        risar.cakaj(0.02)


def Ocena9():
    QMessageBox.information(None, "Chain Reaction Demo", "Welcome to Chain Reaction Demo level....bugs inbound")
    zoge = []
    M = Miska()
    count = 0
    sum = 0
    stevilo = 30
    for x in range(0, stevilo):
        zoge.append(Krog())
    while M.shown or count != 0:
        for A in zoge:
            premik(A)
            if not risar.klik:
                M.update()
            else:
                d = sqrt(((A.x - M.x)) ** 2 + ((A.y - M.y)) ** 2)
                if d < 40:
                    if A.boom == False:
                        A.vx, A.vy = 0, 0
                        A.circle.setRect(-30, -30, 60, 60)
                        c = A.circle.pen().color().lighter()
                        c.setAlpha(192)
                        A.circle.setBrush(c)
                        A.boom = True
                        count += 1
                        sum += 1
            for B in zoge:
                if B.boom == True:
                    if A.boom == False:
                        if sqrt(((B.x - A.x)) ** 2 + ((B.y - A.y)) ** 2) < 40:
                            A.vx, A.vy = 0, 0
                            A.circle.setRect(-30, -30, 60, 60)
                            c = A.circle.pen().color().lighter()
                            c.setAlpha(192)
                            A.circle.setBrush(c)
                            A.boom = True
                            count += 1
                            sum += 1
            if A.boom == True:
                A.time -= 0.02
                if A.time < 0:
                    A.circle.hide()
                    zoge.remove(A)
                    count -= 1
        if risar.klik:
            M.time -= 0.02
            if M.time < 0:
                M.remove()
                M.x = -1000
                M.y = -1000
        risar.cakaj(0.02)
    QMessageBox.information(None, "Chain Reaction Demo", "Demo over. You popped " + str(sum) + " ball(-s)!")

def Ocena10():
    QMessageBox.information(None, "Chain Reaction Demo", "Welcome to Chain Reaction!")
    _continue = True
    gamerule = [(1, 5), (4, 10), (8, 15), (10, 20), (14, 25), (16, 25), (18, 25), (20, 25), (22, 25), (28, 30)]
    round = 0
    M = Miska()
    M.circle.hide()
    while _continue == True:
        (limit, stevilo) = gamerule[round]
        QMessageBox.information(None, "Chain Reaction Demo", "Explode " + str(limit) + " balls out of " + str(stevilo))
        zoge = []
        M.reset()
        count = 0
        sum = 0
        for x in range(0, stevilo):
            zoge.append(Krog())
        while M.shown or count != 0:
            for A in zoge:
                premik(A)
                if not risar.klik:
                    M.update()
                else:
                    d = sqrt(((A.x - M.x)) ** 2 + ((A.y - M.y)) ** 2)
                    if d < 40:
                        if A.boom == False:
                            A.vx, A.vy = 0, 0
                            A.circle.setRect(-30, -30, 60, 60)
                            c = A.circle.pen().color().lighter()
                            c.setAlpha(192)
                            A.circle.setBrush(c)
                            A.boom = True
                            count += 1
                            sum += 1
                for B in zoge:
                    if B.boom == True:
                        if A.boom == False:
                            if sqrt(((B.x - A.x)) ** 2 + ((B.y - A.y)) ** 2) < 40:
                                A.vx, A.vy = 0, 0
                                A.circle.setRect(-30, -30, 60, 60)
                                c = A.circle.pen().color().lighter()
                                c.setAlpha(192)
                                A.circle.setBrush(c)
                                A.boom = True
                                count += 1
                                sum += 1
                if A.boom == True:
                    A.time -= 0.02
                    if A.time < 0:
                        A.circle.hide()
                        zoge.remove(A)
                        count -= 1
            if risar.klik:
                M.time -= 0.02
                if M.time < 0:
                    M.remove()
                    M.x = -1000
                    M.y = -1000
            risar.cakaj(0.02)

        if sum < limit:
            QMessageBox.information(None, "Chain Reaction Demo","You failed to explode enough balls this time, but you are welcome to try again :)")
            M.circle.hide()
            M.reset()
            for A in zoge:
                A.circle.hide()
            M.circle.hide()
        if sum >= limit:
            round += 1
            for A in zoge:
                A.circle.hide()
            M.circle.hide()
        if round >= 10:
            _continue = False


    QMessageBox.information(None, "Chain Reaction Demo","Congratulations, you have completed the game!")

Ocena10()

