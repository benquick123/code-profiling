"""
Napiši razred Minobot. Ta sicer ne bo imel več nobene zveze z minami, imel pa bo zvezo z nalogo Minobot, ki smo jo reševali pred časom.

Minobot se v začetku nahaja na koordinatah (0, 0) in je obrnjen na desno. Koordinatni sistem je takšen kot pri matematiki: koordinata y narašča navzgor.

Razred Minobot ima naslednje metode.

naprej(d) gre za d naprej v podani smeri;
desno() se obrne za 90 stopinj v desno;
levo() se obrne za 90 stopinj levo;
koordinate() vrne trenutne koordinate (x in y)
razdalja() vrne pravokotno razdaljo (Manhattansko razdaljo) do koordinat (0, 0): če se robot nahaja na (5, -3), je razdalja do (0, 0) enaka 8.
Če, recimo izvedemo

a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)
print(a.koordinate())




se izpiše (3, 4).
"""


class Minobot:
	def __init__(self):
		self.x, self.y = 0, 0
		self.smer = "D"
		
	def naprej(self,d):
		if self.smer == "D":
			x = self.x + d
			self.x = x
		elif self.smer == "L":
			x = self.x - d
			self.x = x
		elif self.smer == "N":
			y = self.y + d
			self.y = y 
		elif self.smer == "S":
			y = self.y - d
			self.y = y
		
			 
			
	def levo(self):
		if self.smer == "D":
			self.smer = "N"
		elif self.smer == "L":
			self.smer = "S"
		elif self.smer == "S":
			self.smer = "D"
		elif self.smer == "N":
			self.smer = "L"
		print (self.smer)
			
	def desno(self):
		if self.smer == "D":
			self.smer = "S"
		elif self.smer == "L":
			self.smer = "N"
		elif self.smer == "S":
			self.smer = "L"
		elif self.smer == "N":
			self.smer = "D"
		
			
	def razdalja(self):
		razdalja = abs (self.x)+ abs(self.y)
		return razdalja
	
	def koordinate(self):
		return self.x, self.y


a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)
print(a.koordinate()) 
























