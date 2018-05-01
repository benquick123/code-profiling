
# Obvezna

class Minobot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.pot = [((0,0), 0)]

    def naprej(self,d):
        if self.angle == 0:
            self.x += d
        if self.angle == 90 or self.angle == -270:
            self.y -= d
        if self.angle == 180 or self.angle == -180:
            self.x -= d
        if self.angle == 270 or self.angle == -90:
            self.y += d
        self.pot.append((self.koordinate(), self.angle))

    def desno(self):
        self.angle = (self.angle + 90) % 360
        self.pot.append((self.koordinate(), self.angle))

    def levo(self):
        self.angle = (self.angle - 90) % 360
        self.pot.append((self.koordinate(), self.angle))

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

# Dodatna

    def razveljavi(self):
        if len(self.pot) >= 2:
            (self.x, self.y), self.angle = self.pot[-2]
            del self.pot[-1]





