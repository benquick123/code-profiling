import risar
import random
import math

seznam_krogov = list()
for i in range(30):
    x, y = risar.nakljucne_koordinate()

    #Da ne pride do zatikanja ob rob
    if x > risar.maxX - 10:
        x = risar.maxX - 10
    if x < 10:
        x = 10
    if y > risar.maxY - 10:
        y = risar.maxY - 10
    if y < 10:
        y = 10

    vx = random.uniform(-5, 5)
    vy = math.sqrt((5 ** 2) - (vx ** 2))

    seznam_krogov.append([risar.krog(x, y, 10, risar.nakljucna_barva(), 2), vx, vy])

x_miske, y_miske = risar.miska
krog_miske = risar.krog(x_miske, y_miske, 20, risar.barva(255, 255, 255), 2)

konec = False
while not konec:
    if not risar.klik :
        x_miske, y_miske = risar.miska
        krog_miske.setPos(x_miske, y_miske)
    for j in range(30):
        x = seznam_krogov[j][0].x()
        y = seznam_krogov[j][0].y()

        if math.sqrt((krog_miske.x() - x) ** 2 + (krog_miske.y() - y) ** 2) <= 30 and risar.klik:
            konec = True
            break

        if x + 10 > risar.maxX or x - 10 < 0:
            seznam_krogov[j][1] = - seznam_krogov[j][1]
        elif y + 10 > risar.maxY or y - 10 < 0:
            seznam_krogov[j][2] = -seznam_krogov[j][2]
        seznam_krogov[j][0].setPos(x + seznam_krogov[j][1], y + seznam_krogov[j][2])

    risar.cakaj(0.02)
