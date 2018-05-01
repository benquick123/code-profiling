class Minobot:

	def __init__(self):
		self.x = 0
		self.y = 0
		self.smer = 0   #0 desno, 1 dol, 2 levo, 3 gor
		
	def naprej(self,d):
		if self.smer == 0:
			self.x += d
		if self.smer == 1:
			self.y -= d
		if self.smer == 2:
			self.x -= d
		if self.smer == 3:
			self.y += d
	
	def desno(self):
		self.smer = (self.smer+1)%4
		
	def levo(self):
		self.smer = (self.smer-1)%4
		
	def koordinate(self):
		return (self.x, self.y)
		
	def razdalja(self):
		return (abs(self.x)+abs(self.y))