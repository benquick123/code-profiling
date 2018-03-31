import risar
from random import randint
from math import sqrt

x_zacetni, y_zacetni = risar.nakljucne_koordinate()
x_premik_hitrost = randint(-5, 5)
y_premik_hitrost = sqrt(25 - x_premik_hitrost **2)
barva_kroglice = risar.nakljucna_barva()
kroglica = risar.krog(x_zacetni, y_zacetni, 10, barva_kroglice)
i = 0

while i < 1000:

    kroglica.setPos(kroglica.x() + x_premik_hitrost, kroglica.y() + y_premik_hitrost)

    if not (10 < kroglica.x() and kroglica.x() < risar.maxX - 10):

        x_premik_hitrost = -x_premik_hitrost

    if not (10 < kroglica.y() and kroglica.y() < risar.maxY - 10):

        y_premik_hitrost = -y_premik_hitrost

    i +=1

    risar.cakaj(0.02)
