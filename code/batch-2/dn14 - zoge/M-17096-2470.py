import risar

krogi = []
hitr_x = []
hitr_y = []

for i in range(30):
    x, y = risar.nakljucne_koordinate()
    krog = risar.krog(x, y, 10, barva=risar.nakljucna_barva(), sirina=1)
    krogi.append(krog)
    hitr_x.append(5)
    hitr_y.append(5)

for e in range(1000):
    for i in range(len(krogi)):
        krog = krogi[i]
        krog.setPos(krog.x() + hitr_x[i], krog.y() + hitr_y[i])
        if not (0 < krog.x() < risar.maxX - 20):
            hitr_x[i] = -hitr_x[i]
        if not (0 < krog.y() < risar.maxY - 20):
            hitr_y[i] = -hitr_y[i]
    risar.cakaj(0.02)