import random
import math
import risar
import time

def zoga():

    hitr_X = random.randint(-5, 5)
    hitr_Y = math.sqrt(5 ** 2 - hitr_X ** 2) * random.choice([-1, 1])

    nakX, nakY = risar.nakljucne_koordinate()
    barva_krog = risar.nakljucna_barva()
    krog = risar.krog(nakX, nakY, 10, barva_krog, 1)

    return (krog, nakX, nakY, hitr_X, hitr_Y)


# def Krog_6():
#
#     krog, nakX, nakY, hitr_X, hitr_Y = zoga()
#
#     cas = time.time() + 20
#
#     while time.time() < cas:
#         risar.obnovi()
#         krog.setPos(nakX, nakY)
#
#         if nakX < 1 or nakX > risar.maxX - 1:
#             hitr_X = hitr_X * -1
#         if nakY < 1 or nakY > risar.maxY - 1:
#             hitr_Y = hitr_Y * -1
#
#         nakX += hitr_X
#         nakY += hitr_Y
#
#         risar.cakaj(0.02)
#
#     risar.odstrani(krog)
#
#Krog_6()

def Krog():
    krogi = []
    hitrosti = []

    for i in range(30):
        krog, nakX, nakY, hitr_X, hitr_Y = zoga()
        hitrosti.append([hitr_X, hitr_Y])
        krogi.append(krog)

    cas = time.time() + 20

    while time.time() < cas:
        risar.obnovi()
        for i, krog in enumerate(krogi):
            hitr_X = hitrosti[i][0]
            hitr_Y = hitrosti[i][1]

            krog.setPos(krog.x() + hitr_X, krog.y() + hitr_Y)

            if krog.x() < 1 or krog.x() > risar.maxX - 1:
                hitrosti[i][0] = hitr_X * -1
            if krog.y() < 1 or krog.y() > risar.maxY - 1:
                hitrosti[i][1] = hitr_Y * -1
        risar.cakaj(0.02)
Krog()