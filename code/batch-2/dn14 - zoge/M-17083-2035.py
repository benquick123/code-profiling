import risar
import time
from math import sqrt
from random import randint

st_kroglic = 30

kroglice = []
premiki = []
stanja = []
explozije = []
polnila = []
e_stanja = []
indexi = []
e_casi = []
st_eksplozij = 0


for i in range(st_kroglic):
    x = randint(11, risar.maxX - 15)
    y = randint(11, risar.maxY - 15)
    barva = risar.nakljucna_barva()
    radius = 10
    x_premik = randint(-5000, 5000) / 1000
    y_premik = sqrt(5 ** 2 - x_premik ** 2)
    if randint(0, 1):
        y_premik = -y_premik
    kroglica = risar.krog(x, y, radius, barva, 3)
    kroglice.append(kroglica)
    premiki.append((x_premik, y_premik))
    stanja.append((x, y))
    indexi.append(i)

kursor = risar.krog(risar.maxX / 2, risar.maxY / 2, 30, risar.bela, 3)
start_time = time.time()
while 1:
    for i, paket in enumerate(zip(kroglice, premiki, stanja)):
        kroglica, xiny_premik, xiny = paket
        x_premik, y_premik = xiny_premik
        x, y = xiny
        if x > risar.maxX - 15:
            x_premik = -x_premik
        if x < 15:
            x_premik = -x_premik
        if y > risar.maxY - 15:
            y_premik = -y_premik
        if y < 15:
            y_premik = -y_premik
        novx = x + x_premik
        novy = y + y_premik
        stanja[i] = (novx, novy)
        premiki[i] = (x_premik, y_premik)
        kroglica.setPos(novx, novy)

        if risar.klik:
            for eksplozija in e_stanja:
                if eksplozija is not None:
                    x_eksplozija, y_eksplozija = eksplozija
                    d = sqrt((x - x_eksplozija)**2 + (y - y_eksplozija)**2)
                    if d < 43 and i == indexi[i]:
                        e_stanja.append((x, y))
                        kroglica.hide()
                        c = kroglica.pen().color().lighter()
                        a = c
                        a.setAlpha(192)
                        indexi[i] = None
                        polnila.append(risar.krog(x, y, 15, c, 30))
                        explozije.append(risar.krog(x, y, 30, a, 3))
                        e_casi.append(time.time())
                        st_eksplozij += 1

    if not risar.klik:
        x_kursor, y_kursor = risar.miska
        kursor.setPos(x_kursor, y_kursor)
        kursor.x = x_kursor
        kursor.y = y_kursor
        e_stanja = []
        e_stanja.append((kursor.x, kursor.y))

    for i, cas in enumerate(e_casi):
        if cas is not None:
            elapsed_time = time.time() - cas
            if elapsed_time > 4:
                explozije[i].hide()
                polnila[i].hide()
                e_stanja[i] = None
                e_casi[i] = None

    risar.cakaj(0.02)
    for cas in e_casi:
        if cas is not None:
            print(cas)

risar.stoj()