from math import *

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = "E"

    def koordinate(self):
        return (self.x,self.y)

    def desno(self):
        smeri1 = ["E","S","W","N"]

        while self.smer != smeri1[0]:
            smeri1.append(smeri1[0])
            smeri1.remove(smeri1[0])

        self.smer = smeri1[1]

    def levo(self):
        smeri2 = ["E","N","W","S"]

        while self.smer != smeri2[0]:
            smeri2.append(smeri2[0])
            smeri2.remove(smeri2[0])

        self.smer = smeri2[1]


    def naprej(self,d):
        if self.smer == "E":
            self.x += d
        if self.smer == "S":
            self.y -= d
        if self.smer == "W":
            self.x -= d
        if self.smer == "N":
            self.y += d

    def razdalja(self):
        vrni = 0
        vrni += abs(self.x - 0) + abs(self.y - 0)
        return vrni



