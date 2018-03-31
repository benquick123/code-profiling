import risar
from random import randint
import math

class Krog:

	def __init__(self):
		self.x0, self.y0 = risar.nakljucne_koordinate()
		self.barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))
		self.krog = risar.krog(self.x0, self.y0, 10, self.barva, sirina=10)	
		self.c = self.krog.pen().color().lighter()
		self.c.setAlpha(192)
		self.krog.setBrush(self.c)
		self.x_speed = randint(-5,5)
		self.y_speed = (-1)**randint(1,2) * math.sqrt(25 - self.x_speed ** 2)

	def vrniKrog(self):
		return self.krog
		
	def vrniXspeed(self):
		return self.x_speed
		
	def vrniYspeed(self):
		return self.y_speed
		
	def setXspeed(self, novX):
		self.x_speed = novX
		
	def setYspeed(self, novY):
		self.y_speed = novY

krogi = []
		
for i in range(30):
	krogi.append(Krog())

miskaX, miskaY = risar.miska

krogMiska = risar.krog(miskaX, miskaY, 30, risar.barva(255,255,255), sirina=10)
krogMiska.setPos(miskaX, miskaY)
postavljen = False
zadet = False	
	
while True:
	if not postavljen:
		miskaX, miskaY = risar.miska
		krogMiska.setPos(miskaX, miskaY)
	if risar.klik:
		postavljen = True
	risar.cakaj(0.02)
	for i in range(30):
		k1 = krogi[i]
		k1.vrniKrog().setPos(k1.vrniKrog().x()+k1.vrniXspeed(), k1.vrniKrog().y()+k1.vrniYspeed())
		if k1.vrniKrog().y() > risar.maxY:
			k1.setYspeed(- k1.vrniYspeed())
		if k1.vrniKrog().y() < 0:
			k1.setYspeed(- k1.vrniYspeed())
		if k1.vrniKrog().x() > risar.maxX:
			k1.setXspeed(- k1.vrniXspeed())
		if k1.vrniKrog().x() < 0:
			k1.setXspeed(- k1.vrniXspeed())
		tX = k1.vrniKrog().x()
		tY = k1.vrniKrog().y()
		if postavljen and tX < miskaX+33 and tX > miskaX-33 and tY < miskaY+33 and tY > miskaY-33:
			zadet=True
	if zadet:
		break