import risar
from random import randint, choice
from math import sqrt


class Zasest:
    def __init__(self):
        self.aball = []
        self.dx = []
        self.dy = []
        for _ in range(1):
            ball = risar.krog(randint(0, risar.maxX), randint(0, risar.maxY), 10)
            self.aball.append(ball)
            dx = randint(-5, 5)
            dy = choice([-1,1]) * sqrt(5**2 - dx ** 2)
            self.dx.append(dx)
            self.dy.append(dy)
        for i in range(1000):
            for i in range(len(self.aball)):
                ball = self.aball[i]
                ball.setPos(ball.x() + self.dx[i], ball.y() + self.dy[i])
                if not (0 < ball.x() < risar.maxX):
                    self.dx[i] = -self.dx[i]
                if not (0 < ball.y() < risar.maxY):
                    self.dy[i] = -self.dy[i]
            risar.cakaj(0.02)

class Zasedem:
    def __init__(self):
        self.aball = []
        self.dx = []
        self.dy = []
        for _ in range(30):
            barva = risar.nakljucna_barva()
            ball = risar.krog(randint(0, risar.maxX), randint(0, risar.maxY), 10, barva)
            self.aball.append(ball)
            dx = randint(-5, 5)
            dy = choice([-1, 1]) * sqrt(5**2 - dx ** 2)
            self.dx.append(dx)
            self.dy.append(dy)
        for i in range(1000):
            for i in range(len(self.aball)):
                ball = self.aball[i]
                ball.setPos(ball.x() + self.dx[i], ball.y() + self.dy[i])
                if not (0 < ball.x() < risar.maxX):
                    self.dx[i] = -self.dx[i]
                if not (0 < ball.y() < risar.maxY):
                    self.dy[i] = -self.dy[i]
            risar.cakaj(0.02)

#sest
a = Zasest()

#sedem
#a = Zasedem()