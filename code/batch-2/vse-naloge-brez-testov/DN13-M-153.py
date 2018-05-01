# Napiši razred Minobot. Ta sicer ne bo imel več nobene zveze z minami, imel pa bo zvezo z nalogo Minobot, ki smo jo reševali pred časom.
# Minobot se v začetku nahaja na koordinatah (0, 0) in je obrnjen na desno.
# Koordinatni sistem je takšen kot pri matematiki: koordinata y narašča navzgor.
# Razred Minobot ima naslednje metode.
#   naprej(d) gre za d naprej v podani smeri;
#   desno() se obrne za 90 stopinj v desno;
#   levo() se obrne za 90 stopinj levo;
#   koordinate() vrne trenutne koordinate (x in y)
#   razdalja() vrne pravokotno razdaljo (Manhattansko razdaljo) do koordinat (0, 0): če se robot nahaja na (5, -3), je razdalja do (0, 0) enaka 8.
#   Če, recimo izvedemo
#       a = Minobot()
#       a.levo()
#       a.naprej(4)
#       a.desno()
#       a.naprej(3)
#       print(a.koordinate())
#       se izpiše (3, 4).

class Minobot:

    def __init__(self):
        self.koord = (0, 0)
        self.stran = 0
        self.spr1 = 360
        self.spr2 = 0

    def naprej(self, d):
        x, y = self.koord
        if self.stran == 0:
            x += d
            self.koord = (x, y)
        elif self.stran == 90:
            y += d
            self.koord = (x, y)
        elif self.stran == 180:
            x -= d
            self.koord = (x, y)
        elif self.stran == 270:
            y -= d
            self.koord = (x, y)

    def desno(self):
        self.stran = self.spr1 - 90
        self.spr1 -= 90

        if self.spr1 == 0:
            self.spr1 = 360

    def levo(self):
        self.stran = self.spr2 + 90
        self.spr2 += 90

        if self.spr2 == 360:
            self.spr2 = 0

    def koordinate(self):
        return self.koord

    def razdalja(self):
        zx, zy = self.koord
        kx, ky = (0, 0)
        return abs(kx - zx) + abs(ky - zy)


