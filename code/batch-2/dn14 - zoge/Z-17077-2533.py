import math
import random

import risar


class Circle:
    def __init__(self):
        self.radius = 10
        self.color = risar.nakljucna_barva()
        self.x = random.randint(self.radius + 5, risar.maxX - (self.radius + 5))
        self.y = random.randint(self.radius + 5, risar.maxY - (self.radius + 5))
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])
        self.angle = math.radians(random.randint(0, 360))
        self.head = risar.krog(self.x, self.y, self.radius, self.color)
        self.timer = risar.QTimer()
        self.exploded = False

    def move(self, mouse):
        if not self.exploded:
            self.x, self.y = self.x + self.dx * math.cos(self.angle), self.y - self.dy * math.sin(self.angle)
            self.update()
        if not mouse.clicked:
            mouse.update()
        if risar.klik:
            if self.distance():
                self.exploded = True
                self.explode()

    def update(self):
        if not (self.radius < self.x < risar.maxX - self.radius):
            self.dx = -self.dx
        if not (self.radius < self.y < risar.maxY - self.radius):
            self.dy = -self.dy
        self.head.setPos(self.x, self.y)

    def distance(self):
        for circle in exploded_circles:
            if math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2) < 40:
                return True

    def explode(self):
        self.head.setRect(-30, -30, 60, 60)
        self.fill()
        if self not in exploded_circles:
            exploded_circles.append(self)
        self.timer.singleShot(4000, self.izbrisi_krog)
        izbrisi_od_krogi(self)

    def izbrisi_krog(self):
        risar.odstrani(self.head)
        izbrisi_od_seznam(self)

    def fill(self):
        c = self.head.pen().color().lighter()
        c.setAlpha(192)
        self.head.setBrush(c)


class Mouse(Circle):
    def __init__(self):
        self.x, self.y = risar.miska
        self.head = risar.krog(self.x, self.y, 30)
        self.timer = risar.QTimer()
        self.clicked = False

    def update(self):
        if not risar.klik:
            self.x, self.y = risar.miska
            self.head.setPos(self.x, self.y)
        else:
            self.clicked = True
            self.fill()
            if self not in exploded_circles:
                exploded_circles.append(self)
            self.timer.singleShot(4000, self.izbrisi_krog)


def izbrisi_od_seznam(circle):
    del exploded_circles[exploded_circles.index(circle)]


def izbrisi_od_krogi(circle):
    counter.append(1)
    del circles[circles.index(circle)]



balls = 20
req = int(balls / 2)
circles = []
m = Mouse()
exploded_circles = []
counter = []

risar.QMessageBox.information(None, "Konec", "Razpočiti moraš {} žogic od {}.".format(req, balls))

for fn in range(balls):
    circles.append(Circle())

while not m.clicked or len(exploded_circles) > 0:
    i = 0
    while len(circles) > i:
        circ = circles[i]
        circ.move(m)
        i += 1
    risar.cakaj(0.02)

if risar.klik and len(exploded_circles) == 0:
    number = len(counter)
    if number >= req:
        risar.QMessageBox.information(None, "Konec",
                                      "Uspelo ti je koncati igro. Razpočil si {} žogic.".format(number))
    else:
        risar.QMessageBox.information(None, "Konec",
                                      "Žal ti ni useplo. Razpočil si {} žogic od potrebnih {}.".format(number, req))
risar.pobrisi()
risar.klik = False
