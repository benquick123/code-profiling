from math import *

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "E"
        self.ismeri = 1
        self.smeri = ["N", "E", "S", "W"]

    def desno(self):
        self.ismeri += 1
        if self.ismeri > 3:
            self.ismeri = 0
        self.smer = self.smeri[(self.ismeri)]

    def levo(self):
        self.ismeri -= 1
        if self.ismeri < 0:
            self.ismeri = 3
        self.smer = self.smeri[(self.ismeri)]

    def naprej(self, d):
        self.smer = self.smeri[self.ismeri]
        if self.smer == "N":
            self.y += d
        elif self.smer == "E":
            self.x += d
        elif self.smer == "S":
            self.y -= d
        elif self.smer == "W":
            self.x -= d

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        dist = abs(self.x)+abs(self.y)
        return dist






