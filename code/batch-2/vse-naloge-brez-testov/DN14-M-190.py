import risar
import math
import random
import time
from PyQt5.QtWidgets import QMessageBox



class Zoga:
    def __init__(self):
        self.x = random.randint(10, risar.maxX - 10)
        self.y = random.randint(10, risar.maxY - 10)
        self.r = 10
        self.barva = risar.barva(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        self.dx = random.randint(-4, 5)
        self.dy = math.sqrt(5 ** 2 - self.dx ** 2)

        self.status = False
        self.exploded = False

        self.ttl = time.time() + 60 * 60
        self.alive = True

        self.removed = False

        self.krog = risar.krog(self.x, self.y, self.r, self.barva, sirina=2)

    def explode(self):
        c = self.krog.pen().color().lighter()
        c.setAlpha(192)
        self.krog.setBrush(c)

        self.krog.setRect(-30, -30, 60, 60)
        self.dx = 0
        self.dy = 0


class Cursor:
    def __init__(self):
        self.x, self.y = risar.miska
        self.r = 30
        self.circle = risar.krog(self.x, self.y, self.r, risar.bela, sirina=2)
        self.status = False
        self.alive = True

    def explode(self):
        c = self.circle.pen().color().lighter()
        c.setAlpha(192)
        self.circle.setBrush(c)


objs = []
for i in range(10):
    objs.append(Zoga())

uniceni = 0

miska = Cursor()

timer = time.time() * 60 + 15

while True:

    if not miska.status and risar.klik:
        miska.status = True
        miska.explode()
        timer = time.time() + 4

    if time.time() > timer and miska.alive:
        miska.circle.hide()
        miska.alive = False
        del miska.circle

    if not miska.status:
        miska.x, miska.y = risar.miska
        miska.circle.setPos(miska.x, miska.y)

    for obj in objs:
        obj.x += obj.dx
        obj.y += obj.dy
        if obj.x > risar.maxX - obj.r or obj.x < obj.r:
            obj.dx *= -1
        elif obj.y > risar.maxY - obj.r or obj.y < obj.r:
            obj.dy *= -1

        if miska.status and miska.alive and miska.circle.collidesWithItem(obj.krog):
            obj.explode()
            obj.status = True
            if not obj.exploded:
                obj.exploded = True
                obj.ttl = time.time() + 4
                uniceni += 1

        for o in objs:
            if o != obj and obj.alive:
                if miska.status and o.status and o.alive and obj.krog.collidesWithItem(o.krog):
                    obj.explode()
                    obj.status = True
                    if not obj.exploded:
                        obj.exploded = True
                        uniceni += 1
                        obj.ttl = time.time() + 4

        #print(objs.index(obj), obj.ttl, obj.status, obj.alive, obj.exploded)

        if time.time() > obj.ttl and obj.alive:
            obj.alive = False
            obj.krog.hide()
            obj.exploded = False
            del obj.krog

        if obj.alive:
            obj.krog.setPos(obj.x, obj.y)

    if not miska.alive and not any(obj.exploded for obj in objs):
        str = 'Razstrelil si {} žod od 10'.format(uniceni)
        QMessageBox.information(None, "Unicenih zog", str)
        break

    #print(time.time())
    risar.cakaj(0.02)

risar.stoj()
