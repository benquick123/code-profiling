from math import cos, sin, pi


class Minobot(object):

    def __init__(self):
        self.x, self.y = 0, 0
        self.usmerjen = 0
        self.ukazi = []

    def naprej(self, d):
        self.x += d * cos(self.usmerjen)
        self.y += d * sin(self.usmerjen)
        self.ukazi.append(d)

    def desno(self):
        self.usmerjen -= pi / 2
        self.ukazi.append("desno")

    def levo(self):
        self.usmerjen += pi / 2
        self.ukazi.append("levo")

    def koordinate(self):
        return (round(self.x), round(self.y))

    def razdalja(self):
        return round(abs(self.x) + abs(self.y))

    def razveljavi(self):
        if self.ukazi:
            zadnji = self.ukazi.pop()
            if zadnji == "desno":
                self.usmerjen += pi / 2
            elif zadnji == "levo":
                self.usmerjen -= pi / 2
            else:
                self.x -= zadnji * cos(self.usmerjen)
                self.y -= zadnji * sin(self.usmerjen)


