from math import radians, cos, sin, pi


class Minobot:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 0

    def naprej(self, d):
        kot = self.kot % 360
        if kot == 0:
            self.x += d
        if kot == 90:
            self.y -= d
        if kot == 180:
            self.x -= d
        if kot == 270:
            self.y += d

    def desno(self):
        self.kot += 90

    def levo(self):
        self.kot -= 90

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

