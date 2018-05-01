import risar
from math import sin, cos, radians

class Minobot:

    def __init__(self):
        self.x, self.y = 0, 0
        self.angle = 90

    def naprej(self, d):
        if self.angle == 90:
            self.x += d
        if self.angle == 270:
            self.x -= d
        if self.angle == 0:
            self.y += d
        if self.angle == 180:
            self.y -= d

    def desno(self):
        self.angle += 90
        if self.angle >= 360:
            self.angle -= 360

    def levo(self):
        self.angle -= 90
        if self.angle < 0:
            self.angle += 360

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

