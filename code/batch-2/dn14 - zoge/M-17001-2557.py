import risar
import random
import time
from math import *




class Ball:
    def __init__(self, x=None, y=None, r=None, vx=None, vy=None, color=None):
        if r is None:
            r = 10
        self.r = r
        if x is None or y is None:
            x = random.randint(self.r, risar.maxX - self.r)
            y = random.randint(self.r, risar.maxY - self.r)
        self.x = x
        self.y = y


        if vx is None or vy is None:
            v = 5
            vx = random.randint(-v, v)
            vy = sqrt(v ** 2 - vx ** 2)

        self.vx = vx
        self.vy = vy

        if color is None:
            color = risar.barva(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circle = risar.krog(self.x, self.y, self.r, color, 3)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.circle.setPos(self.x, self.y)


    def walls(self):
        if self.x < self.r:
            self.vx = abs(self.vx)
        if self.x > risar.maxX - self.r:
            self.vx = -abs(self.vx)
        if self.y < self.r:
            self.vy = abs(self.vy)
        if self.y > risar.maxY - self.r:
            self.vy = -abs(self.vy)

    def boom(self):
        self.circle.setRect(-30, -30, 60, 60)
        c = self.circle.pen().color().lighter()
        c.setAlpha(192)
        self.circle.setBrush(c)
        (self.vx, self.vy) = (0, 0)

balls = []
mouse_counter = 1
a = risar.krog(10, 10, 30, risar.bela, 3)
c = a.pen().color().lighter()
c.setAlpha(192)
dead = []

for i in range(0, 20):
    balls.append(Ball())
    dead.append(("", ""))

for b in range(800):
    for d in range(len(balls)):
        for s in balls:
            s.move()
            s.walls()
            if not risar.klik:
                (mouse_x, mouse_y) = risar.miska
                a.setPos(mouse_x, mouse_y)
            if risar.klik:
                a.setRect(-30, -30, 60, 60)
                a.setBrush(c)
                if mouse_counter == 1:
                    mouse_counter = time.time()
                if s.vx != 0 and s.vy != 0:
                    if s.x -40 < a.x() < s.x + 40 and s.y -40 < a.y() < s.y + 40:
                        if s not in dead[d]:
                                s_time = time.time()
                                dead[d] = (s, s_time)
                                s.boom()
                                risar.stoj()
        if mouse_counter != 1:
            if time.time() - mouse_counter > 3:
                a.setPos(-100, -100)
        risar.cakaj(0.02)
risar.stoj()





