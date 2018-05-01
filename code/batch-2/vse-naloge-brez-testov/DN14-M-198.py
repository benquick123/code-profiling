import PyQt5
from PyQt5.QtWidgets import QMessageBox
import risar
from math import *
from random import random,randint
import time

class Ball:
	def __init__(self, x, y, r, vx, vy, color):
		self.x = x
		self.y = y
		self.r = r
		self.color = color
		self.circle = risar.krog(self.x, self.y, self.r, barva=self.color,sirina=3)

		if vx is None or vy is None:
			v = randint(-5,5)
			vx = randint(-v,v)
			vy = sqrt(v**2-vx**2)
		self.vx=vx
		self.vy=vy

		self.explode = False
		self.exr=30#polmer po eklsploziji
		self.extime=4#tok časa ko je ekslpodiran

	def Move(self):
		self.x += self.vx
		self.y += self.vy
		self.circle.setPos(self.x,self.y)

	def Explode(self):#da se žogica počasi povečuje
		if self.explode:
			self.vx=0
			self.vy=0
			self.circle.setRect(-30,-30,60,60)
			c=self.circle.pen().color().lighter()
			c.setAlpha(192)
			self.circle.setBrush(c)
	def OnCollisionEnter(self,x,y):
		if GetDistance(self.x, self.y, x, y) < 30:
			return True

			


#############ostale funkcije##############################
def MessageBox(naslov, besedilo):#za krajsi klic message boxa 
	QMessageBox.information(None, naslov, besedilo)

def GetDistance(x1,y1,x2,y2):#pridobi razdaljo med dvema točkama
	distX = x2 - x1#tuki si dau round stran
	distY = y2 - y1
	return sqrt(pow(distX, 2) + pow(distY, 2))
#########################################################


###############INITIALIZATION---START####################

#ustvarim žogice
#spremenljivke
ball_num = 30#žogice, ki se bodo odbijale po ekranu
ball_r = 10#polmer žog, ki se odbijajo
cur_stop = False#ali je uporabnik že kliknil, da se cursor ustavi
klik_count=0#kolkrat je že uporabnik kliknu
cur_cor=risar.miska#kordinate kurzorja
curcordod=False#a so kordinate že dodane
futureEx=False#pomožna spremenljivka za naslednjo explodirano
odstranjenCursor=False#odpravi napako da se da cursor še kr zaznat tut če ga ni več

cursor_explod=0
num_ex=0
ura=0

msg_show=True#če je že končen msgbox 

#seznami
balls = []#žoge, ki se odbijajo
ex_balls = []#kordinate žog, ki so občutljive na dotik
#PyQt5 stuff:
cor_mouse = risar.besedilo(0,0,"(,)",barva=risar.rdeca)#besedilo za kordinate miske
cursor = risar.krog(risar.miska[0],risar.miska[1],30,risar.bela)#krogec ki sledi miski
collision = risar.besedilo(80,450,"LenExBalls:"+str(len(ex_balls)),barva=risar.zelena)

#ustvarim žogice
for i in range(ball_num):
	x, y = randint(ball_r, risar.maxX-ball_r), randint(ball_r, risar.maxY-ball_r)#kje se bojo zogice spawnale
	#ali bom potreboval seznam kordinat??
	vx, vy = 2 + random() * 3, 2 + random() * 3
	ball = Ball(x, y, ball_r, vx, vy, risar.nakljucna_barva())
	balls.append(ball)#zogo dodamo v seznam zog
########################################################


#####################################UPDATE###########################################
for i in range(2000):#Called every...
	#spawnanje zogic iz arraya
	for j in range(len(balls)):
		current_ball = balls[j]
		current_ball.Move()#premakni trenutno zogo iz arraya

		#pogoj za odbijanje od roba okna
		if not (ball_r < current_ball.x < risar.maxX-ball_r):
			current_ball.vx = -current_ball.vx
		if not (ball_r < current_ball.y < risar.maxY-ball_r):
			current_ball.vy = -current_ball.vy

	#če uporabnik klikne se nastavi cur stop na true, kar je kasneje uporabljeno za fiskiranje cursor kroga		
	if risar.klik:
		klik_count+=1
		if not cur_stop:
			cur_stop = True#to se uporabi zato, da se uposteva le prvi klik, in ne vsak ko ga uporabnik klikne


	if klik_count==1:#samo enkrat se nastavijo kordinate ustaveljenega kurzorja
		cur_cor=risar.miska
		if not curcordod:
			risar.odstrani(cursor)
			kurzor = Ball(cur_cor[0], cur_cor[1], 30, 0, 0, risar.bela)
			ex_balls.append(kurzor)
			curcordod=True

	risar.odstrani(collision)
	collision = risar.besedilo(80,450,"LenExBalls:"+str(len(ex_balls)),barva=risar.zelena)	
	
	if cur_stop:

		for exball in ex_balls:
			if not exball.extime < 0:
				 exball.extime-=0.06
				 if not odstranjenCursor:
				 	odstranjenCursor=True
			if exball.extime < 0:
				risar.odstrani(exball.circle)
				ex_balls.remove(exball)

		cursor_explod=1
	#cursor krogec se ne premika več
	#v zanki začne preverjati, če se stoječ krogec dotika katere izmed premikajočih se žogic
		for ball in balls:
			if not odstranjenCursor:		
				if GetDistance(ball.x, ball.y, cur_cor[0], cur_cor[1]) < 30 and len(ex_balls)>0:#če se katera od kroglic dotika kurzorjevega kroga
					ball.explode = True
					ball.Explode()
					ex_balls.append(ball)
					balls.remove(ball)

			for exball in ex_balls:
				if GetDistance(ball.x, ball.y,exball.x, exball.y)<40:#namest 30 je 40, ker je različlna velikost žogic
					futureEx=True

			if futureEx:
				ball.explode=True
				ball.Explode()
				ex_balls.append(ball)
				num_ex+=1
				if ball in balls: balls.remove(ball)
				futureEx=False
		
	else:
		#cursor krogec se premika skupaj s cursorjem
		risar.odstrani(cursor)#odstranim prejšno instanco cursorja, da lahko narišemo novo
		cursor = risar.krog(risar.miska[0],risar.miska[1],30,risar.bela,sirina=3)

		#izpisujemo kordinate miske
		risar.odstrani(cor_mouse)
		cor_mouse = risar.besedilo(80,80,str(risar.miska),barva=risar.rdeca)
	#sekunde obstoja šteješ tko da eno spremenljivko skos odštevaš da pride do 0 pol brišeš zadnjega v seznamu in ponastvaiš spremenljivko


	if len(ex_balls) <= 0 and cursor_explod > 0:
		if msg_show:
			MessageBox("Konec igre","Eksplodiralo je: "+str(num_ex)+" žog.")
			msg_show=False
			break 
	risar.cakaj(0.02)
##################################################################################





risar.stoj()