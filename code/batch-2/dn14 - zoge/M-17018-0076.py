import risar
import math
import random
from PyQt5.QtWidgets import QMessageBox

class Ball:
    def __init__(self, color):
        self.x, self.y = risar.nakljucne_koordinate()
        self.speed_x = random.randrange(-5, 5)
        self.speed_y = math.sqrt((5 * 5) - self.speed_x * self.speed_x)
        self.color = color
        self.width = 10
        self.krog = risar.krog(self.x, self.y, self.width, self.color, 2)
        self.exploded = False
        self.time = 4
        self.dead = False

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.krog.setPos(x, y)

    def set_width(self, width):
        self.width = width
        self.krog.setRect(-width, -width, width * 2, width * 2)

    def set_color(self, r, g, b):
        self.krog.setBorder(risar.barva(r, g, b))

    def explode(self, exploading):
        if not self.exploded:
            self.exploded = True
            self.set_width(30)
            c = self.krog.pen().color().lighter()
            c.setAlpha(192)
            self.krog.setBrush(c)
            exploading.append(self)

    def update(self, time, exploading, dead):
        if self.dead:
            return

        if self.exploded:
            self.time -= time
            if self.time < 0:
                self.krog.hide()
                self.dead = True
                dead[0] += 1
                exploading.remove(self)
        else:
            self.x += self.speed_x
            self.y += self.speed_y

            if self.x - self.width < 0:
                self.speed_x *= -1
                self.x = self.width
            if self.x + self.width > risar.maxX-1:
                self.speed_x *= -1
                self.x = risar.maxX-1 - self.width
            if self.y - self.width < 0:
                self.speed_y *= -1
                self.y = self.width
            if self.y + self.width > risar.maxY-1:
                self.speed_y *= -1
                self.y = risar.maxY-1 - self.width

            self.set_pos(self.x, self.y)

    def collide(self, ball):
        if self.dead or ball.dead:
            return False

        d_x = self.x - ball.x
        d_y = self.y - ball.y
        d = math.sqrt(pow(d_x, 2) + pow(d_y, 2))
        if d < self.width + ball.width:
            return True
        else:
            return False


tick = 0.02

exploding = []
zoge = []
for i in range(30):
    zoge.append(Ball(risar.nakljucna_barva()))

cursor = Ball(risar.barva(255, 255, 255))
cursor.set_width(30)
stopped = False

running = True
dead = [0]
while running:
    for zoga in zoge:
        zoga.update(tick, exploding, dead)

    if risar.klik:
        stopped = True
        cursor.explode(exploding)
        risar.klik = False

    if stopped:
        cursor.update(tick, exploding, dead)
        if len(exploding) > 0:
            for e in exploding:
                for zoga in zoge:
                    if zoga.collide(e):
                        zoga.explode(exploding)
        else:
            QMessageBox.information(None, "Konec", "Uničenih " + str(dead[0]) + " od 30")
            running = False
            break
    else:
        mouse_pos = risar.miska
        cursor.set_pos(mouse_pos[0], mouse_pos[1])

    risar.obnovi()
    risar.cakaj(tick)