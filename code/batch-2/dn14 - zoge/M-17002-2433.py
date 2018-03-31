import risar
import random
import math
zoge = []
koordinatex = []
koordinatey = []
for i in range(30):
    x, y = risar.nakljucne_koordinate()
    zoge.append(risar.krog(x, y, 10, risar.nakljucna_barva(), sirina=2))
    x1 = random.uniform(-5, 5)
    y1 = math.sqrt((5 ** 2) - (x1 ** 2))
    koordinatex.append(x1)
    koordinatey.append(y1)

for i in range(1000):
    for y in range(len(zoge)):
        zoga = zoge[y]
        x1,y1 = koordinatex[y], koordinatey[y]
        zoga.setPos(zoga.x() + x1, zoga.y() + y1)
        if zoga.x() < 0 or zoga.x() > risar.maxX:
            koordinatex[y] = -x1
        elif zoga.y() < 0 or zoga.y() > risar.maxY:
            koordinatey[y] = -y1
    risar.cakaj(0.02)
risar.stoj()

