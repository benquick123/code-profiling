import risar
import time
import random
from PyQt5.QtWidgets import QMessageBox
from math import sin, cos, tan, radians, sqrt
cas = time.clock()

class Circle:

    def __init__(self, x0, y0, r0, barva, control):

        self.x = x0
        self.y = risar.maxY - y0
        self.r = r0
        if random.randint(1,2) == 1:
            self.speed = 0.2
        else:
            self.speed = -0.2
        self.kot = random.randint(0,180)
        self.krog = risar.krog(x0, y0, r0, barva)
        self.fill = self.krog.pen().color().lighter()
        self.fill.setAlpha(192)
        if control:
            self.popped = True
            self.active = False
            self.krog.setBrush(self.fill)
        else:
            self.popped = False
            self.active = True

    def premakni(self, popravek):
        if not self.popped:
            self.x += cos(radians(self.kot)) * (self.speed * popravek)
            self.y -= sin(radians(self.kot)) * (self.speed * popravek)
        else:
            if not self.active:
                self.x = risar.miska[0]
                self.y = risar.miska[1]
        self.krog.setPos(self.x, self.y)
    def preveri(self, eksplodirani):
        if self.active:
            if self.x >= risar.maxX or self.x <= 0:
                self.kot = 180 - self.kot

            if self.y >= risar.maxY or self.y <= 0:
                self.kot = 180 - self.kot
                self.speed *= -1
            for i in eksplodirani:
                if sqrt((i.x - self.x)**2 + (i.y - self.y)**2)- 10 <= 30:
                    self.explode()
                    return "eksplodiral"
        else:
            if risar.klik:
                self.active = True
                self.timer = time.clock()
                return "postavil"
        return False


    def explode(self):
        self.popped = True
        self.timer = time.clock()
        self.krog.setRect( -30, -30, 60, 60)
        self.krog.setBrush(self.fill)

    def has_expired(self):
        if self.popped:
            if time.clock() - self.timer > 4:
                return True
        return False

    def hide(self):
        self.krog.hide()




zbirnik = [risar.bela, risar.rdeca, risar.zelena, risar.modra, risar.vijolicna, risar.rumena, risar.siva, risar.rjava ]
nivoji = [(1,5), (2, 10), (4, 15), (6, 20), (10, 25), (15, 30), (18, 35), (22, 40), (30, 45), (37, 50) ]
counter = 0
first_loop = True
napreduj = False
while counter < 10:
    risar.pobrisi()
    risar.klik = False
    if napreduj == False and first_loop == False:
        QMessageBox.information(None, "Skoda!", "Ni ti uspelo! Samo {} od {} zog je eksplodiralo".format(exp_count, nivoji[counter][1]))
    elif napreduj == True and first_loop == False:
        QMessageBox.information(None, "Bravo!", "Uspelo ti je!")
    first_loop = False
    QMessageBox.information(None, "Nivo", "od {} zogic eksplodiraj vsaj {} zogic".format(nivoji[counter][1], nivoji[counter][0]) )

    b = [Circle(random.randint(1, risar.maxX-1), random.randint(1, risar.maxY-1), 10, zbirnik[random.randint(0, len(zbirnik)- 1)], False) for i in range(nivoji[counter][1]) ]
    a = Circle(risar.miska[0], risar.miska[1],30, risar.rdeca, True)
    eksplodirani = []
    exp_count = 0
    playing = True
    placed = False
    napreduj = False
    popravek = 1
    while(playing):
        beg_time = time.time()
        a.premakni(0)
        if a.preveri([]) == "postavil":
            placed = True
            eksplodirani.append(a)
        for i in b:
            if i.preveri(eksplodirani) == "eksplodiral":
                eksplodirani.append(i)
                exp_count += 1
                b.remove(i)
                break
            i.premakni(popravek)

        for i in eksplodirani:
            if i.has_expired():
                i.hide()
                eksplodirani.remove(i)
                break
        if placed == True and len(eksplodirani) == 0:
            playing = False
        risar.obnovi()
        end_time = time.time()
        popravek = (end_time - beg_time) * 1000
    if exp_count >= nivoji[counter][0]:
        counter += 1
        napreduj = True


QMessageBox.information(None, "Konec!","Prišel/a si do konca! Cestitam!")