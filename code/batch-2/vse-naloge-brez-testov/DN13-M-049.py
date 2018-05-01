from math import pi, sin, cos, radians

class Minobot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.angle = 90

    def naprej(self, d):
        if self.angle == 360:
            self.angle = 0
        angle = radians(90 - self.angle)
        nx, ny = self.x + d * cos(angle), self.y + d * sin(angle)
        self.x, self.y = int(nx), int(ny)

    def desno(self):
        self.angle += 90

    def levo(self):
        self.angle -= 90

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)


