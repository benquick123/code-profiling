
from math import sin, cos, radians
class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90
    def naprej(self, s):
        phi = radians(90 - self.angle)
        nx, ny = self.x + s * cos(phi), self.y + s * sin(phi)
        self.x, self.y = nx, ny
    def desno(self):
        self.angle += 90
    def levo(self):
        self.angle -= 90
    def koordinate(self):
        return round(self.x), round(self.y)
    def razdalja(self):
        return abs(round(self.x)) + abs(round(self.y))


from math import sin, cos, radians
class Minobot:
    def __init__(self):
        self.seznam =[]
        self.x = 0
        self.y = 0
        self.angle = 90
    def naprej(self, s):
        phi = radians(90 - self.angle)
        nx, ny = self.x + s * cos(phi), self.y + s * sin(phi)
        self.x, self.y = nx, ny
        self.seznam.append(["naprej", s])
    def desno(self):
        self.angle += 90
        self.seznam.append(["desno"])
    def levo(self):
        self.angle -= 90
        self.seznam.append(["levo"])
    def koordinate(self):
        return round(self.x), round(self.y)
    def razdalja(self):
        return abs(round(self.x)) + abs(round(self.y))
    def razveljavi(self):
        if self.seznam:
            if len(self.seznam[-1]) > 1:
                if self.seznam[-1][0] == "naprej":
                    phi = radians(90 - self.angle)
                    nx, ny = self.x -  self.seznam[-1][1] * cos(phi), self.y - self.seznam[-1][1] * sin(phi)
                    self.x, self.y = nx , ny
            for e in self.seznam[-1]:
                if e == "desno":
                    self.angle -= 90
                if e == "levo":
                    self.angle += 90
            self.seznam = self.seznam[:-1]




