import risar, random, math, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox

class Zoga:
    def __init__(self):
        self.x = random.randint(11, risar.maxX - 11) # 11 da bo zaagotovo dovolj v notranjosti
        self.y = random.randint(11, risar.maxY - 11)
        self.color = risar.nakljucna_barva()
        self.krog = risar.krog(self.x, self.y, 10, self.color, 3)

        angle = random.randint(0, 360)
        v = 5
        self.vx = math.sin(math.radians(angle)) * v
        self.vy = - math.cos(math.radians(angle)) * v

    def update_pos(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= risar.maxX-10 or self.x <= 10:
            self.vx = -self.vx
        if self.y >= risar.maxY-10 or self.y <= 10:
            self.vy = -self.vy
        self.update()

    def update(self):
        self.krog.setPos(self.x, self.y)

    def hide(self):
        self.krog.hide()

class VelikoZog:
    def __init__(self, st_zog):
        self.seznam_zog = list()
        self.st_eksplodiranih = 0
        for i in range(st_zog):
            self.seznam_zog.append(Zoga())

    def update_pos(self):
        for k in self.seznam_zog:
            k.update_pos()
            for x, y in koordinate_eksplodiranih:
                if risar.klik:
                    d = math.sqrt((k.x - x) ** 2 + (k.y - y) ** 2)
                    if d <= 40:
                        eksplodirane.append(EksplodiranaZoga(k.x, k.y, k.color))
                        cas_eksplodiranih.append(time.time() + 4)
                        koordinate_eksplodiranih.append((k.x, k.y))
                        k.hide()
                        self.seznam_zog.remove(k)
                        self.st_eksplodiranih += 1
                        break

class ZogaMiska(Zoga):
    def __init__(self):
        self.x = risar.maxX/2
        self.y = risar.maxY/2
        self.color = risar.bela
        self.krog = risar.krog(self.x, self.y, 30, self.color, 3)

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.update()

class EksplodiranaZoga(Zoga):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.krog = risar.krog(self.x, self.y, 30, self.color, 3)
        cc = self.krog.pen().color().lighter()
        cc.setAlpha(192)
        self.krog.setBrush(cc)

eksplodirane = list()
cas_eksplodiranih = list()
koordinate_eksplodiranih = list()

def ponastavi_globalne():
    global eksplodirane
    global cas_eksplodiranih
    global koordinate_eksplodiranih
    eksplodirane = list()
    cas_eksplodiranih = list()
    koordinate_eksplodiranih = list()
    risar.klik = False
    risar.pobrisi()


def level(za_zmago, st_zog):
    ponastavi_globalne()
    QMessageBox.information(None, "Zoganje", "Razstreli {} zog od {}.".format(za_zmago, st_zog))
    z = VelikoZog(st_zog)
    miska = ZogaMiska()
    global eksplodirane
    global cas_eksplodiranih
    global koordinate_eksplodiranih
    mogoc_konec = False

    while not mogoc_konec:
        risar.cakaj(0.02)
        x, y = risar.miska
        if miska != None:
            if risar.klik:
                eksplodirane.append(miska)
                koordinate_eksplodiranih.append(risar.miska)
                cas_eksplodiranih.append(time.time()+4)
                miska = None
            else:
                miska.update_pos(x, y)
        i = 0
        while i < len(cas_eksplodiranih):
            if time.time() >= cas_eksplodiranih[i]:
                eksplodirane[i].hide()
                del eksplodirane[i]
                del koordinate_eksplodiranih[i]
                del cas_eksplodiranih[i]
                if len(eksplodirane) == 0:
                    mogoc_konec = True
            else:
                i += 1
        z.update_pos()
    if z.st_eksplodiranih >= za_zmago:
        return True
    QMessageBox.information(None, "Zoganje", "Uspelo ti je razstreliti {} žog. Premalo.".format(z.st_eksplodiranih))
    return False

leveli = [(1, 5), (2, 5), (3, 8), (5, 13), (5, 11), (5, 10), (6, 13), (6, 11), (27, 30), (98, 100)]

for e in leveli:
    while True:
        zmaga = level(*e)
        if zmaga:
            break

risar.stoj()