class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 0
        self.undolist = []
        self.undod = []

    def naprej(self, d):
        if self.smer == 0:
            self.x += d
        elif self.smer == 1:
            self.y += d
        elif self.smer == 2:
            self.x -= d
        else:
            self.y -= d
        self.undod.append(-d)
        self.undolist.append(self.napreju)

    def napreju(self, d):
        if self.smer == 0:
            self.x += d
        elif self.smer == 1:
            self.y += d
        elif self.smer == 2:
            self.x -= d
        else:
            self.y -= d

    def desno(self):
        self.smer -= 1
        self.smercheck()
        self.undolist.append(self.levou)

    def levou(self):
        self.smer += 1
        self.smercheck()

    def levo(self):
        self.smer += 1
        self.smercheck()
        self.undolist.append(self.desnou)

    def desnou(self):
        self.smer -= 1
        self.smercheck()

    def smercheck(self):
        if self.smer > 3:
            self.smer = 0
        elif self.smer < 0:
            self.smer = 3
        else:
            return

    def koordinate(self):
        return(self.x, self.y)

    def razdalja(self):
        return(abs(self.x) + abs(self.y))

    def razveljavi(self):
        if not self.undolist:
            return
        if self.undolist[-1] == self.napreju:
            return self.undolist.pop()(self.undod.pop())
        else:
            return self.undolist.pop()()

