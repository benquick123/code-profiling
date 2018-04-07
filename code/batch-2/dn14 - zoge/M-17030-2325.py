import risar
from math import sqrt,pow
from random import randint
krogi = []
slovarx = []
slovary = []
barva = risar.nakljucna_barva()
krog = risar.krog(randint(0, risar.maxX - 100), randint(0, risar.maxY - 100), 10, barva, 5)
krogi.append(krog)
x=randint(-5,5)
y=(pow(5,2)-pow(x,2))
y=sqrt(y)
slovary.append(y)
slovarx.append(x)
def premik(krogi,slovarx,slovary):
    for i in range(1350):
        for i in range(len(krogi)):
            krog = krogi[i]
            krog.setPos(krog.x() + slovarx[i], krog.y() + slovary[i])
            if not (0 < krog.x() < risar.maxX - 35):
                slovarx[i] = -slovarx[i]
            if not (0 < krog.y() < risar.maxY - 35):
                slovary[i] = -slovary[i]
        risar.cakaj(0.02)
print(premik(krogi,slovarx,slovary))


