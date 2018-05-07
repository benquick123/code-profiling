import math
import random
import risar

risar.obnavljaj=True
krogi=[]
vx_s=[]
vy_s=[]

def koordinate():
    x, y = 0, 0
    while not 11 < x < risar.maxX - 11:
        x, y = risar.nakljucne_koordinate()
    while not 11 < y < risar.maxY - 11:
        x, y = risar.nakljucne_koordinate()
    return x, y

for i in range(30):
    x, y = koordinate()
    b=risar.nakljucna_barva()
    krog = risar.krog(x, y, 10, b, sirina=1)
    c = krog.pen().color().lighter()
    c.setAlpha(192)
    krog.setBrush(c)
    krogi.append(krog)
    vx = random.randint(-5, 5)
    vx_s.append(vx)
    vy = random.choice([-1, 1])*math.sqrt(25 - (vx ** 2))
    vy_s.append(vy)

for i in range(0, 5000, 5):
    for i in range(len(krogi)):
        krog1=krogi[i]
        krog1.setPos(krog1.x() + vx_s[i], krog1.y() + vy_s[i])
        if not (10 < krog1.x() < risar.maxX - 10):
            vx_s[i] = -vx_s[i]
        if not (10 < krog1.y() < risar.maxY - 10):
            vy_s[i] = -vy_s[i]
    risar.cakaj(0.02)
risar.stoj()