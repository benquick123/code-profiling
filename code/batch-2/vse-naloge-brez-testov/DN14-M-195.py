import risar
import random
import math

risar.obnavljaj = True
v = 5
krogi = []
vxs = []
vys = []
for i in range(30):
    x,y = random.randint(10, risar.maxX-10), random.randint(10, risar.maxY-10)
    r = 10
    barva = risar.nakljucna_barva()
    a = risar.krog(x, y, r, barva)
    krogi.append(a)
    vx = random.randint(-5, 5)
    vxs.append(vx)
    vys.append(math.sqrt(v ** 2 - vx ** 2))
for j in range(900):
    for k in range(len(krogi)):
        krog = krogi[k]
        krog.setPos(krog.x()+vxs[k],krog.y()+vys[k])
        if not (0 < krog.x() < risar.maxX - 10):
            vxs[k] = -vxs[k]
        if not (0 < krog.y() < risar.maxY - 10):
            vys[k] = -vys[k]
    risar.cakaj(0.02)
risar.stoj()



