import risar
from random import uniform, choice, randint
from math import sqrt
import time
from PyQt5.QtWidgets import QMessageBox


class Ball:
    def __init__(self):
        self.r = 10
        self.x = randint(0 + 30, risar.maxX - 30)
        self.y = randint(0 + 30, risar.maxY - 30)
        self.dirx = uniform(-5, 5)
        self.diry = choice([-1, 1])
        self.color = risar.nakljucna_barva()
        self.destroyed = False
        self.circle = risar.krog(self.x, self.y, self.r,
                                 barva=self.color, sirina=3)

    def forward(self):
        if not self.destroyed:
            self.x = self.x + self.dirx
            self.y = self.y + sqrt(25 - self.dirx ** 2) * self.diry
            for i in exploded_balls:
                if (sqrt((self.x - i.x) ** 2 + (self.y - i.y) ** 2) <=
                        (self.r + i.r)):
                    self.explode()
                    break
            if not((0 + 12) < self.x < (risar.maxX - 12)):
                # Odboj v levo ali desno stranico
                self.dirx = -self.dirx
            elif not((0 + 12) < self.y < (risar.maxY - 12)):
                # Odboj v zgornjo ali spodnjo stranico
                self.diry = -self.diry
            self.circle.setPos(self.x, self.y)

    def explode(self):
        t = ExplodedBall(self.x, self.y, self.color)
        exploded_balls.append(t)
        counter.append(True)
        self.circle.hide()
        self.destroyed = True


class ExplodedBall:
    def __init__(self, x, y, color):
        self.r = 30
        self.x = x
        self.y = y
        self.color = color
        self.circle = risar.krog(self.x, self.y, self.r,
                                 barva=self.color, sirina=3)
        self.time = time.time()
        alpha = self.circle.pen().color().lighter()
        alpha.setAlpha(192)
        self.circle.setBrush(alpha)


levels = [(5, 1), (10, 2), (15, 4), (20, 6), (25, 10), (30, 15),
          (35, 18), (40, 22), (45, 30), (50, 37), (55, 48), (60, 55)]

for given_balls, goal in levels:
    QMessageBox.information(None, "NAVODILA",
        "Razstreli {} od {} žog".format(goal, given_balls))
    level_finished = False
    while not level_finished:
        balls = []
        exploded_balls = []
        counter = []
        for i in range(given_balls):
            b = Ball()
            balls.append(b)
        cursor = risar.krog(0, 0, 30, barva=risar.bela, sirina=3)
        clicked = False
        while True:
            for i in balls:
                x, y = risar.miska
                cursor.setPos(x, y)
                if risar.klik and not clicked:
                    t = ExplodedBall(x, y, risar.bela)
                    exploded_balls.append(t)
                    risar.klik = False
                    clicked = True
                    cursor.hide()
                i.forward()
            for j in exploded_balls:
                if time.time() - j.time >= 4:
                    j.circle.hide()
                    exploded_balls.remove(j)
            risar.cakaj(0.02)
            if risar.klik and clicked:  # Če umes ponesreč kliknš
                risar.klik = False
            if clicked and not exploded_balls:
                if sum(counter) >= goal:
                    level_finished = True
                    QMessageBox.information(None, "USPELO TI JE", "Uničil si {} od {} žog".format(sum(counter), given_balls))
                else:
                    QMessageBox.information(None, "NEUSPEŠNO", "Uničil si jih {} moral bi {}".format(sum(counter), goal))
                for h in balls:
                    h.circle.hide()
                break
QMessageBox.information(None, "ZMAGAL",
    "BRAVO!!! DOKONČAL SI VSEH 12 LEVELOV")
