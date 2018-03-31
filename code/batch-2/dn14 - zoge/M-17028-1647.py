import risar
from math import sqrt
from random import randint

class zoga:
	def __init__(self,x,y,r,vx,vy,barva):
		self.x=x
		self.y=y
		self.r=r
		self.vx = vx
		self.vy = vy
		self.krog = risar.krog(self.x, self.y, self.r,barva=barva)


	def move(self):
		self.x += self.vx
		self.y += self.vy
		self.krog.setPos(self.x, self.y)

koordinate_vektorji=list()

for i in range(30):
	x, y = randint(10, risar.maxX-10), randint(10, risar.maxY-10)
	rnd=randint(-5,5)
	vx,vy= rnd,sqrt(5**2)-sqrt(rnd**2)
	koordinate_vektorji.append((x,y,vx,vy))

polje_zog=[zoga(koordinate_vektorji[i][0],koordinate_vektorji[i][1],10,koordinate_vektorji[i][2],koordinate_vektorji[i][3],risar.nakljucna_barva()) for i in range(30)]
#	polje_zog=[(zoga(koordinate_vektorji[i][0],koordinate_vektorji[i][1],10,koordinate_vektorji[i][2],koordinate_vektorji[i][3],risar.nakljucna_barva())) for i in range(30)]

for i in range(2000):
	for zoga in polje_zog:
		zoga.move()
		if not (10 < zoga.x < risar.maxX-10):
			zoga.vx = -zoga.vx
		if not (10< zoga.y < risar.maxY-10):
			zoga.vy = -zoga.vy
	risar.cakaj(0.02)
