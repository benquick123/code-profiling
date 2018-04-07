import math
class Minibot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.kot = 0
        self.poteze = [[self.x, self.y, self.kot]]

    def naprej(self, d):
        if self.kot == 0:
            self.x += d
        elif self.kot == 180:
            self.x -= d
        elif self.kot == 90:
            self.y += d
        elif self.kot == 270:
            self.y -= d
        self.poteze.append([self.x, self.y, self.kot])


    def desno(self):
        if self.kot == 0:
            self.kot = 270
        else:
            self.kot -= 90
        self.poteze.append([self.x, self.y, self.kot])


    def levo(self):
        if self.kot == 360:
            self.kot = 0
        self.kot += 90
        if self.kot == 360:
            self.kot = 0
        self.poteze.append([self.x, self.y, self.kot])

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return math.sqrt(self.x ** 2) + math.sqrt(self.y ** 2)

    def razveljavi(self):
        if len(self.poteze) > 1:
            self.poteze.pop(len(self.poteze) - 1)
            self.x, self.y, self.kot = self.poteze[len(self.poteze) - 1]

