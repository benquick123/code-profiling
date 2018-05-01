
from math import radians, cos, sin

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 90
        self.zgodovina_pozicij = []
        self.update()

    def update(self):
        if self.kot == 360:
            self.kot = 0
        elif self.kot == -360:
            self.kot = 0
        self.zgodovina_pozicij.append((self.x, self.y, self.kot))

    def naprej(self, d):
        delta = radians(90 - self.kot)
        self.x = self.x + d * cos(delta)
        self.y = self.y + d * sin(delta)
        self.update()

    def desno(self):
        self.kot += 90
        self.update()

    def levo(self):
        self.kot -= 90
        self.update()

    def koordinate(self):
        return (int(self.x), int(self.y))

    def razdalja(self):
        return int(abs(self.x) + abs(self.y))

    def razveljavi(self):
        if len(self.zgodovina_pozicij):
            if len(self.zgodovina_pozicij) >= 2:
                del self.zgodovina_pozicij[-1]
            self.x, self.y, self.kot = self.zgodovina_pozicij[-1]



