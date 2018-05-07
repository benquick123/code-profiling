from math import*

s = (1, 2, 3, 4)

class Minobot():
    def __init__(self):
        global s
        self.loc, self.smer = (0, 0), s[1]

    def koordinate(self):
        return self.loc

    def razdalja(self):
        x, y = fabs(self.loc[0]), fabs(self.loc[1])
        return x + y

    def naprej(self, i):
        # set x
        if self.smer == s[1]:
            self.loc = (self.loc[0] + i, self.loc[1])
        elif self.smer == s[3]:
            self.loc = (self.loc[0] - i, self.loc[1])

        # set y
        if self.smer == s[0]:
            self.loc = (self.loc[0], self.loc[1] + i)
        elif self.smer == s[2]:
            self.loc = (self.loc[0], self.loc[1] - i)

    def desno(self):
        self.smer = s[(s.index(self.smer) + 1) % 4]

    def levo(self):
        self.smer = s[(s.index(self.smer) + -1) % 4]


