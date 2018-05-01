
class Minobot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.smer = 'vzhod'

    def naprej(self, d):
        if self.smer == 'vzhod':
            self.x += d
        if self.smer == 'zahod':
            self.x -= d
        if self.smer == 'sever':
            self.y += d
        if self.smer == 'jug':
            self.y -= d

    def levo(self):
        i = 0
        if i == 0 and self.smer == 'vzhod':
            self.smer = 'sever'
            i += 1
        if i == 0 and self.smer == 'sever':
            self.smer = 'zahod'
            i += 1
        if i == 0 and self.smer == 'zahod':
            self.smer = 'jug'
            i += 1
        if i == 0 and self.smer == 'jug':
            self.smer = 'vzhod'
            i += 1

    def desno(self):
        i = 0
        if i == 0 and self.smer == 'vzhod':
            self.smer = 'jug'
            i += 1
        if i == 0 and self.smer == 'jug':
            self.smer = 'zahod'
            i += 1
        if i == 0 and self.smer == 'zahod':
            self.smer = 'sever'
            i += 1
        if i == 0 and self.smer == 'sever':
            self.smer = 'vzhod'
            i += 1

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return (abs(self.x) + abs(self.y))



