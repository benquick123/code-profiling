from math import *

class Minobot:
    def __init__(self):
        self.x,self.y = 0, 0
        self.angle = 90

    def naprej(self, d):
        angle = radians(90-self.angle)
        nx, ny = self.x + d * cos(angle), self.y + d * sin(angle)
        self.x, self.y = nx, ny

    def desno(self):
        self.angle += 90

    def levo(self):
        self.angle -= 90

    def koordinate(self):
        return round(self.x, 1), round(self.y, 1)

    def razdalja(self):
        return int(abs(round(self.x, 1))+abs(round(self.y, 1)))









