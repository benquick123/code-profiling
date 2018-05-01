from math import *
import risar


class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.log = []

    def naprej(self, d):
        self.log.append((self.x, self.y, self.angle))
        phi = radians(self.angle)
        nx = self.x + d * cos(phi)
        ny = self.y + d * sin(phi)
        self.x = int(round(nx))
        self.y = int(round(ny))

    def desno(self):
        self.log.append((self.x, self.y, self.angle))
        self.angle -= 90

    def levo(self):
        self.log.append((self.x, self.y, self.angle))
        self.angle += 90

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if self.log:
            self.x, self.y, self.angle = self.log.pop()


