class Minobot:
    def __init__(self):
        self.xk= 0
        self.yk= 0
        self.o= 1

    def nastavi_x(self, xk):
        self.xk= xk
    def nastavi_y(self, yk):
        self.yk= yk
    def nastavi_o(self, o):
        self.o= o

    def vrni_x(self):
        return self.xk
    def vrni_y(self):
        return self.yk
    def vrni_o(self):
        return self.o

    def naprej(self, d):
        if self.vrni_o() == 0:
            i= self.vrni_y()
            self.nastavi_y(i+d)
        elif self.vrni_o() == 1:
            self.nastavi_x(self.vrni_x()+d)
        elif self.vrni_o() == 2:
            self.nastavi_y(self.vrni_y()-d)
        else:
            self.nastavi_x(self.vrni_x()-d)

    def desno(self):
        h= self.vrni_o()
        if h +1 > 3:
            self.nastavi_o(0)
        else:
            self.nastavi_o(h+1)

    def levo(self):
        h= self.vrni_o()
        if h -1 < 0:
            self.nastavi_o(3)
        else:
            self.nastavi_o(h-1)

    def koordinate(self):
        return (self.vrni_x(),self.vrni_y())


    def razdalja(self):
        return abs(self.vrni_x())+ abs(self.vrni_y())












