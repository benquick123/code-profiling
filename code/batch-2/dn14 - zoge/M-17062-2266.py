import risar
import math
import  random

class skokica:
    def __init__(self):
        self.x,self.y =  risar.nakljucne_koordinate()
        self.r = 10
        self.color = risar.nakljucna_barva()
        self.object = risar.krog(self.x, self.y, self.r, self.color)
        self.sx = random.randint(-5,5)
        self.sy = math.sqrt(25 - self.sx)


klovn = []
gledacx = []
gledacy = []
for i in range(30):
    a = skokica()
    klovn.append(a)
    gledacx.append(a.sx)
    gledacy.append(a.sy)
for i in range(5000):
    for x,a,b in zip(klovn,gledacx,gledacy):
        risar.odstrani(x.object)
        x.x += x.sx
        x.y += x.sy
        x.object = risar.krog(x.x + a, x.y + b, x.r, x.color)
        if x.x > risar.maxX - 5 or x.x < 5:
            x.sx = -x.sx
        if x.y > risar.maxY - 5 or x.y < 5:
           x.sy = -x.sy
