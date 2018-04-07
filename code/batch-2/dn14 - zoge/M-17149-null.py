import math, random, risar, time
class Zoge:
    def __init__(self):#konstruktor
        self.x, self.y = random.randint(10, risar.maxX - 10), random.randint(10, risar.maxY - 10) #Omejitev na polje
        self.zoga = risar.krog(self.x, self.y,10,risar.nakljucna_barva(), 1)#x,y,polmer,barva,sirina
        hitrost_X = random.randint(-5,5)
        hitrost_Y = math.sqrt(25 - hitrost_X**2)#25 = kost.hirtost(5)**2 --> PITAGORA
        self.hitrost_X = hitrost_X
        self.hitrost_Y = hitrost_Y

    def premik(self): #premikanje žog
        self.x = self.x + self.hitrost_X
        self.y = self.y + self.hitrost_Y
        self.zoga.setPos(self.x, self.y)

        #"Meje" od "Janezovo zasilno platno"
        if self.x > risar.maxX - 10: #Desna stena
            self.hitrost_X = -abs(self.hitrost_X)

        elif self.y > risar.maxY - 10: #Spodnja stena
            self.hitrost_Y = -abs(self.hitrost_Y)

        elif self.y < 10: #Zgornja stena
            self.hitrost_Y = abs(self.hitrost_Y)

        elif self.x < 10: #Leva stena
            self.hitrost_X = abs(self.hitrost_X)

def Animiraj():
    zoge = []
    for i in range(30): #30 --> število žog
        zoge.append(Zoge())
    cas_izvajanja = time.time() + 20 #aktualnemu času, prišteje 20 sekund
    while time.time() < cas_izvajanja:
        for k in zoge:
            k.premik() #izvaja premik za vsako žogo random
        risar.cakaj(0.02) #0.01 -> animacija je bolj "tekoča"

Animiraj()



