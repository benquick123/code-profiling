class Minobot:
    def __init__(self):
        self.x = self.y = 0
        self.angle = 90
    def naprej(self, d):
        if self.angle == 0:
            self.y = self.y + d
        if self.angle == 90 or self.angle == -270:
            self.x = self.x + d
        if self.angle == 180 or self.angle == -180:
            self.y = self.y - d
        if self.angle == 270 or self.angle == -90:
            self.x = self.x - d
        if self.angle == 360 or self.angle == -360:
            self.y = self.y + d
            self.angle = 0

    def desno(self):
        self.angle = self.angle + 90

    def levo(self):
        self.angle = self.angle - 90

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return (abs(0-self.x) + abs(0-self.y))









