class Minobot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 90
        self.nazaj = []

    def naprej(self, d):
        if self.kot == 90:
            self.x += d
            self.nazaj.append(('naprej', d))
        elif self.kot == 270:
            self.x -= d
            self.nazaj.append(('nazaj', d))
        elif self.kot == 0:
            self.y += d
            self.nazaj.append(('gor', d))
        else:
            self.y -= d
            self.nazaj.append(('dol', d))


    def desno(self):
        if self.kot + 90 == 360:
            self.kot = 0
        else:
            self.kot += 90
        self.nazaj.append('obrni desno')


    def levo(self):
        if self.kot - 90 < 0:
            self.kot = 270
        else:
            self.kot -= 90
        self.nazaj.append('obrni levo')


    def koordinate(self):
        return (self.x, self.y)


    def razdalja(self):
        return abs(self.x) + abs(self.y)


    def help(self, d):
        if self.kot == 90:
            self.x += d
        elif self.kot == 270:
            self.x -= d
        elif self.kot == 0:
            self.y += d
        else:
            self.y -= d
            

    def helpLevo(self):
        if self.kot + 90 == 360:
            self.kot = 0
        else:
            self.kot += 90
            

    def helpDesno(self):
        if self.kot - 90 == 0:
            self.kot = 0
        else:
            self.kot -= 90


    def razveljavi(self):
        if self.nazaj:
            temp = self.nazaj.pop()
            if 'naprej' in temp:
                a, b = temp
                self.help(-b)
            elif 'nazaj' in temp:
                a, b = temp
                self.help(-b)
            elif 'gor' in temp:
                a, b = temp
                self.help(-b)
            elif 'dol' in temp:
                a, b = temp
                self.help(-b)
            elif temp == 'obrni desno':
                self.helpDesno()
            elif temp == 'obrni levo':
                self.helpLevo()


