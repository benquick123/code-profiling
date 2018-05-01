alpha = (1,2,3,4)

class Minobot():
    def razdalja(self):
        one = (self.l[1]**2)**0.5
        two = (self.l[0]**2)**0.5
        return one + two

    def koordinate(self):
        return self.l

    def desno(self):
        cost = (alpha.index(self.j) + alpha[0])
        cilj= cost % len(alpha)
        self.j = alpha[cilj]

    def levo(self):
        cost = (alpha.index(self.j) - alpha[0])
        cilj = cost % len(alpha)
        self.j = alpha[cilj]

    def naprej(self, lop):
        if self.j == alpha[0] : self.l = (self.l[0], self.l[1] + lop)
        elif self.j == alpha[1] : self.l = (self.l[0] + lop, self.l[1])
        if self.j == alpha[2] : self.l = (self.l[0], self.l[1] - lop)
        elif self.j == alpha[3] : self.l = (self.l[0] - lop, self.l[1])

    def __init__(o):
        o.l, o.j = (0, 0), alpha[1]

