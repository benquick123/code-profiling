
from math import *

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.seznam = [(0, 0, 0)]

    def naprej(self, d):
        phi = (pi * self.angle)/180
        nx = self.x + round(d * cos(phi))
        ny = self.y + round(d * sin(phi))
        self.x = nx
        self.y = ny
        self.seznam.append((self.x, self.y, self.angle))


    def desno(self):
        self.angle += -90
        self.seznam.append((self.x, self.y, self.angle))

    def levo(self):
        self.angle += 90
        self.seznam.append((self.x, self.y, self.angle))

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.seznam) < 2:
            self.x = 0
            self.y = 0
            self.angle = 0
        if len(self.seznam) > 1:
            self.x = self.seznam[-2][0]
            self.y = self.seznam[-2][1]
            self.angle = self.seznam[-2][2]
            self.seznam[:] = self.seznam[:-1]


