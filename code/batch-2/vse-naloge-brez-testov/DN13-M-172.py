
class Minobot:

    def __init__(self):
        self.x, self.y = 0, 0
        self.smer = 0

    def naprej(self, d):

        if self.smer % 4 == 0:
            self.x += d
        if self.smer % 4 == abs(1):
            self.y -= d
        if self.smer % 4 == abs(2):
            self.x -= d
        if self.smer % 4 == abs(3):
            self.y += d

    def desno(self):
        self.smer += 1

    def levo(self):
        self.smer -= 1

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return (abs(self.x) + abs(self.y))


