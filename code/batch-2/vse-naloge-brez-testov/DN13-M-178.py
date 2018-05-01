class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.seznam = []
        self.razveljavljanje = False

    def naprej(self, d):
        if self.rotation == 0 or abs(self.rotation) == 360:
            #desno
            self.x += d
            self.rotation = 0
        elif self.rotation == -270 or self.rotation == 90:
            #dol
            self.y -= d
        elif abs(self.rotation) == 180:
            #levo
            self.x -= d
        elif self.rotation == 270 or self.rotation == -90:
            #gor
            self.y += d

        if not self.razveljavljanje:
            self.seznam.append((self.rotation, d))
        else:
            self.seznam.remove(self.seznam[-1])
            self.razveljavljanje = False

    def desno(self):
        self.rotation += 90
        if not self.razveljavljanje:
            self.seznam.append((self.rotation, 0))
        else:
            self.seznam.remove(self.seznam[-1])
            self.razveljavljanje = False

    def levo(self):
        self.rotation -= 90
        if not self.razveljavljanje:
            self.seznam.append((self.rotation, 0))
        else:
            self.seznam.remove(self.seznam[-1])
            self.razveljavljanje = False

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        prejsnji = 0

        if len(self.seznam) == 0:
            return

        self.razveljavljanje = True
        premik = self.seznam[-1]

        if premik[1] > 0:
            self.naprej(-premik[1])
        else:
            if premik[0] <= prejsnji:
                self.desno()
            elif premik[0] > prejsnji:
                self.levo()
            prejsnji = premik[0]

