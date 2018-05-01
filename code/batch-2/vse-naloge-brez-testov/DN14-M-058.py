import risar

from math import radians, cos, sin
from random import randint

risar.obnavljaj = True

class Zoga:
    def __init__(self):
        self.x, self.y = risar.nakljucne_koordinate()
        self.kot = randint(0, 359)
        self.polmer = 10
        self.zoga = risar.krog(0, 0, self.polmer, risar.nakljucna_barva(), 3)
        self.cas = 0

    def premikaj(self):
        self.zoga.setPos(self.x, self.y)
        while self.cas <= 13:
            if self.kot == 0:
                if (risar.maxX - 1 - self.x) <= 10:
                    self.kot = 270
                self.x += 5
                self.zoga.setPos(self.x, self.y)
            elif 0 < self.kot < 90:
                if (risar.maxX - 1 - self.x) <= 10:
                    self.kot = 180 - self.kot
                elif (risar.maxY - 1 - self.y) <= 10:
                    self.kot = 360 - self.kot
                beta = radians(self.kot)
                self.x += 5 * cos(beta)
                self.y += 5 * sin(beta)
                self.zoga.setPos(self.x, self.y)
            elif self.kot == 90:
                if (risar.maxY - 1 - self.y) <= 10:
                    self.kot = 270
                self.y += 5
                self.zoga.setPos(self.x, self.y)
            elif 90 < self.kot < 180:
                if self.x <= 10:
                    self.kot = 180 - self.kot
                elif (risar.maxY - 1 - self.y) <= 10:
                    self.kot = 360 - self.kot
                beta = radians(180 - self.kot)
                self.x -= 5 * cos(beta)
                self.y += 5 * sin(beta)
                self.zoga.setPos(self.x, self.y)
            elif self.kot == 180:
                if self.x <= 10:
                    self.kot = 0
                self.x -= 5
                self.zoga.setPos(self.x, self.y)
            elif 180 < self.kot < 270:
                if self.x <= 10:
                    self.kot = 540 - self.kot
                elif self.y <= 10:
                    self.kot = 360 - self.kot
                beta = radians(self.kot - 180)
                self.x -= 5 * cos(beta)
                self.y -= 5 * sin(beta)
                self.zoga.setPos(self.x, self.y)
            elif self.kot == 270:
                if self. y <= 10:
                    self.kot = 90
                self.y -= 5
                self.zoga.setPos(self.x, self.y)
            elif 270 < self.kot < 360:
                if (risar.maxX - 1 - self.x) <= 10:
                    self.kot = 540 - self.kot
                elif self.y <= 10:
                    self.kot = 360 - self.kot
                beta = radians(360 - self.kot)
                self.x += 5 * cos(beta)
                self.y -= 5 * sin(beta)
                self.zoga.setPos(self.x, self.y)
            risar.cakaj(0.02)
            self.cas += 0.02


z = Zoga()
z.premikaj()
#risar.stoj()