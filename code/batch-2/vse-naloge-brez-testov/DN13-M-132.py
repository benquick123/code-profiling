from math import *

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 0
        self.zgodovina_ukazov = []

    def naprej(self, d):
        rad = radians(self.kot)
        nx = self.x + d * cos(rad)
        ny = self.y + d * sin(rad)
        self.x = int(round(nx))
        self.y = int(round(ny))
        self.zgodovina_ukazov.append(("n", d))

    def desno(self):
        self.kot -= 90
        self.zgodovina_ukazov.append(("d", 0))

    def levo(self):
        self.kot += 90
        self.zgodovina_ukazov.append(("l", 0))

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.zgodovina_ukazov) == 0: return None
        zadnji = self.zgodovina_ukazov[-1]
        if zadnji[0] == "n":
            d = zadnji[1] * -1
            self.naprej(zadnji[1] * -1)
        elif zadnji[0] == "d":
            self.levo()
        elif zadnji[0] == "l":
            self.desno()
        self.zgodovina_ukazov = self.zgodovina_ukazov[:len(self.zgodovina_ukazov) - 2]

