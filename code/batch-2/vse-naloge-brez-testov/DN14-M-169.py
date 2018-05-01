import risar
from random import randint, random
from math import sqrt
def zab():
    krogi = []
    vx = []
    vy = []
    for i in range(25):
        r = 10
        krog = risar.krog(randint(10, risar.maxX - 10), randint(10, risar.maxY - 10),
                        r,risar.nakljucna_barva(), sirina=1)
        krogi.append(krog)
        vx.append(2 + random() * 3)
        vy.append(2 + random() * 3)
    x, y = risar.miska
    k = risar.krog(x, y, 30, risar.bela, sirina=1)
    for i in range(5000):
        for i in range(len(krogi)):
            krog = krogi[i]
            krog.setPos(krog.x() + vx[i], krog.y() + vy[i])
            if risar.klik == False:
                x, y = risar.miska
                k.setPos(x, y)
            else:
                k.setPos(x, y)
                razdalja = (sqrt((x - krog.x())**2 + (y - krog.y())**2))
                if razdalja < 42: ##ker je sirina dveh zogic upostevana zraven, polmer vecjaga in manjsega sqrt((30+10)**2)

                    risar.stoj()
            if not (r < krog.x() < risar.maxX - r):
                vx[i] = -vx[i]
            if not (r < krog.y() < risar.maxY - r):
                vy[i] = -vy[i]
        risar.cakaj(0.02)
    risar.stoj()

zab()