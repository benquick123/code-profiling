__author__ = 'Haris'

class Minobot:
    def __init__(self):
        self.x=0
        self.y=0
        self.angle = 0

        self.undo_list = []

    def naprej(self,d):
        if self.angle == 0 or self.angle == 360:
            self.x = self.x+d
        if self.angle == 180:
            self.x=self.x-d
        if self.angle == 90:
            self.y = self.y-d
        if self.angle == 270:
            self.y = self.y+d

    def desno(self):
        if self.angle==0 or self.angle==360:
            self.angle=90
        else:
            self.angle=self.angle+90

    def levo(self):
        if self.angle==0 or self.angle==360:
            self.angle=270
        else:
            self.angle=self.angle-90

    def koordinate(self):
        return (self.x,self.y)

    def razdalja(self):
        return abs(self.x)+abs(self.y)




