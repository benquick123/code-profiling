import risar
import math
import time
import random

class Circle:
	def __init__(self):
		self.destroyed = False;
		self.exploded = False;
		self.x, self.y = risar.nakljucne_koordinate()
		self.dir = random.randrange(0,360)
		self.rad = 10
		self.speed = 15
		self.outline = 2
		self.color = risar.nakljucna_barva()

	def move(self):
		self.check_bounds()
		self.x += math.cos(math.radians(self.dir)) * self.speed
		self.y += math.sin(math.radians(self.dir)) * self.speed

	def check_bounds(self):
		if self.x < (self.rad+self.outline) or self.x > (risar.maxX-self.rad-self.outline):
			horizontal = math.cos(math.radians(self.dir))
			vertical = math.sin(math.radians(self.dir))
			self.dir = math.degrees(math.atan2(vertical,-horizontal))

		if self.y < (self.rad+self.outline) or self.y > (risar.maxY-self.rad-self.outline):
			horizontal = math.cos(math.radians(self.dir))
			vertical = math.sin(math.radians(self.dir))
			self.dir = math.degrees(math.atan2(-vertical,horizontal))

	def draw(self):
		circle = risar.krog(self.x,self.y,self.rad,self.color,self.outline)
		if self.exploded:
			color = circle.pen().color().lighter()
			color.setAlpha(192)
			circle.setBrush(color)


	def check_collision(self,circle):
		if math.sqrt( (circle.x-self.x)**2 + (circle.y-self.y)**2 )+self.outline < self.rad+circle.rad+circle.outline:
			return True
		return False

	def explode(self):
		self.exploded = True
		self.explode_time = time.time()
		self.speed = 0
		self.rad = 30
	
	def destroy(self):
		self.destroyed = True
		self.rad = 0
		self.outline = 0

class GUI:
	def __init__(self):
		self.x = self.y = 0
		self.rad = 30
		self.explosions = 0

	def draw(self):

		if not risar.klik:
			self.x, self.y = risar.miska

		risar.krog(self.x,self.y,self.rad)

	def check_collision(self,circle):
		if math.sqrt( (circle.x-self.x)**2 + (circle.y-self.y)**2 ) < self.rad+circle.rad+circle.outline:
			return True
		return False

circles = [Circle() for i in range(30)]
gui = GUI()
fps = 100

while(True):
	risar.pobrisi()
	active_explosions = 0

	#iterating trough all circles
	for circle in circles:

		#check if user clicked the button hit the ui circle and isn't exploded already
		if risar.klik and gui.check_collision(circle) and not circle.exploded:
			circle.explode()
			gui.explosions += 1
			
		if circle.exploded:
			active_explosions += 1
			for other_circle in circles:
				if not other_circle.exploded and circle.check_collision(other_circle):
					other_circle.explode()
					gui.explosions += 1

			if (time.time()-circle.explode_time)>4:
				circle.destroy()
			
		circle.move()
		circle.draw()

	if risar.klik and active_explosions == 0 and gui.explosions > 0:
		risar.besedilo(risar.maxX/2, risar.maxY/2, str(gui.explosions))
		risar.stoj()

	destroyed_index = 0
	while destroyed_index < len(circles):
		circle = circles[destroyed_index]
		if circle.destroyed:
			circles.remove(circle)
			destroyed_index = 0
		destroyed_index += 1

	gui.draw()

	time.sleep(1/fps)
