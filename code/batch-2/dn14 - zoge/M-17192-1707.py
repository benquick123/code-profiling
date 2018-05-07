import risar
from random import randint
risar.obnavljaj=True
barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
sirina = randint(2, 10)
x=risar.nakljucne_koordinate()[0]
y=risar.nakljucne_koordinate()[1]

zoga=risar.krog(x,y,10,barva,sirina)

hitrostX=randint(-4,4)
hitrostY=randint(-4,4)

for i in range(0,1200):
    risar.cakaj(0.01)
    print(x,y)

    if x+11>=risar.maxX or x-11<=0:
        hitrostX=hitrostX*(-1)

    elif y+11>=risar.maxY or y-11<=0:
        hitrostY=hitrostY*(-1)
        

    x+=hitrostX
    y+=hitrostY

    zoga.setPos(x,y)

    i=i+1




risar.stoj()

