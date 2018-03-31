import risar
from random import randint, uniform
from PyQt5.QtWidgets import QMessageBox


class krogec:
    def __init__(self):
        self.premer = 10
        self.x = randint(self.premer, risar.maxX - self.premer)
        self.y = randint(self.premer, risar.maxY - self.premer)
        self.ky = 1
        self.kx = 1
        self.px = randint(-5, 5)
        self.py = randint(-5, 5)
        self.hitrost = uniform(0.000001, 0.000009)
        self.barva = risar.nakljucna_barva()
        self.lik = risar.krog(self.x, self.y, self.premer, self.barva, 2)
        self.pocen = False
        self.timer = 500

    def premikanje(self):
        if not self.pocen and self.timer > 2:
            self.lik.setPos(self.x, self.y)
            if self.y + self.premer >= risar.maxY or self.y - self.premer <= 0:
                self.ky *= -1
            if self.x + self.premer >= risar.maxX or self.x - self.premer <= 0:
                self.kx *= -1
            self.x += self.px * self.kx
            self.y += self.py * self.ky

    def konec(self):
        self.risar.stoj()

    def pok(self, x, y):
        if not self.pocen:
            if abs(self.x - x) < 30 and abs(self.y - y) < 30 or \
                    any([True if abs(self.x - i[0]) < 30 and abs(self.y - i[1]) < 30 else False for i in pocene_s]):
                risar.odstrani(self.lik)
                self.lik = risar.krog(self.x, self.y, 30, self.barva, 2)
                c = self.lik.pen().color().lighter()
                c.setAlpha(192)
                self.lik.setBrush(c)
                self.pocen = True
                pocene_s.append((self.x, self.y))
        if self.pocen:
            if self.timer != 0:
                self.timer -= 1
            else:
                if pocene_s:
                    pocene_s.pop(0)
                    m.max()
                    risar.odstrani(self.lik)
                    risar.odstrani(self.lik)
                    self.timer = -10


class mis:
    def __init__(self):
        self.x, self.y = risar.miska
        self.da = True
        self.merek = risar.krog(self.x, self.y, 30)
        self.timer = 3000
        self.konec = False
        self.maksimalni = 0

    def premik(self):
        if self.da:
            self.x, self.y = risar.miska
            self.merek.setPos(self.x, self.y)
            if risar.klik:
                risar.odstrani(self.merek)
                self.pocen = risar.krog(self.x, self.y, 30)
                self.da = False
        if risar.klik and not self.da:
            if self.timer != 0:
                self.timer -= 1
                return self.x, self.y
            else:
                risar.odstrani(self.pocen)
                self.konec = True
                return -300, -300
        else:
            return -300, -300

    def koncano(self):
        if self.konec and not pocene_s:
            self.izpis()
            self.konec = False
            self.zakljuci()

    def max(self):
            self.maksimalni += 1

    def zakljuci(self):
        risar.stoj()

    def izpis(self):
        if self.konec:
            QMessageBox.information(None, "RAZTRELJENIH", "RAZTRELJENO \n{pocenih}/{vse}".format(pocenih=self.maksimalni,vse=stevilo))
            self.konec=False

global pocene_s
pocene_s = []
krogi = []
stevilo = 5
m = mis()

for x in range(stevilo):
    k = krogec()
    krogi.append(k)

while 1:
    for x in range(stevilo):
        krogi[x].premikanje()
        q, w = m.premik()
        krogi[x].pok(q, w)
        m.koncano()
    risar.cakaj(0.01)
