from math import radians, sin, cos

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 0
        self.seznam = []
        self.update()

    def update(self):
        self.seznam.append((self.x, self.y, self.kot))

    def naprej(self, d):
        self.x += int(d * cos(radians(self.kot)))
        self.y += int(d * sin(radians(self.kot)))
        self.update()

    def desno(self):
        self.kot -= 90
        self.update()

    def levo(self):
        self.kot += 90
        self.update()

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.seznam) > 1:
            self.seznam = self.seznam[:-1]
        self.x, self.y, self.kot = self.seznam[-1]





a = Minobot()
a.naprej(3)
a.razveljavi()
a.razveljavi()
a.naprej(2)
a.razveljavi()
a.razveljavi()

print(a.koordinate())

