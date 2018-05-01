from math import sqrt
class Minobot:
    #Minobot se v začetku nahaja na koordinatah (0, 0) in je obrnjen na desno. Koordinatni sistem je takšen kot pri matematiki: koordinata y narašča navzgor.
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "E"
        self.directions = "NESW"
        self.ismer = self.directions.index(self.direction)
        self.archive = [(self.x, self.y, self.direction, self.ismer)]

    def naprej(self, d):

        if self.direction == "N":
            self.y+=d
        if self.direction == "E":
            self.x+=d
        if self.direction == "S":
            self.y-=d
        if self.direction == "W":
            self.x-=d
        self.archive.append((self.x, self.y, self.direction, self.ismer))

    def desno(self):
        self.direction = self.directions[(self.ismer + 1) % 4]
        self.ismer = self.directions.index(self.direction)
        self.archive.append((self.x, self.y, self.direction, self.ismer))

    def levo(self):
        self.direction = self.directions[(self.ismer - 1) % 4]
        self.ismer = self.directions.index(self.direction)
        self.archive.append((self.x, self.y, self.direction, self.ismer))

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        ogx,ogy = 0,0
        calc = sqrt((ogx - self.x)**2) + sqrt((ogy - self.y)**2)
        return (int(calc))


    def razveljavi(self):
        if len(self.archive) > 1:
            self.x, self.y, self.direction, self.ismer = self.archive[-2]
            del self.archive[-1]







