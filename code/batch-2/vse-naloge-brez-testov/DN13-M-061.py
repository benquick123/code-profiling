class Minobot():
    def __init__(self):
        self.x=0
        self.y=0
        #smeri 0=desno, 1=dol, 2=levo, 3=gor
        self.smer=0
        self.zgodovina=[(0,0,0)]
    def naprej(self, d):
        if self.smer==0: self.x+=d
        elif self.smer==1: self.y-=d
        elif self.smer==2: self.x-=d
        elif self.smer==3: self.y+=d
        self.zgodovina.append((self.x, self.y, self.smer))

    def desno(self):
        self.smer+=1
        if self.smer==4: self.smer=0
        self.zgodovina.append((self.x, self.y, self.smer))

    def levo(self):
        self.smer -= 1
        if self.smer==-1: self.smer=3
        self.zgodovina.append((self.x, self.y, self.smer))

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x)+abs(self.y)

    def razveljavi(self):
        if len(self.zgodovina)>1:
            self.x, self.y, self.smer = self.zgodovina[-2]
            del self.zgodovina[-1]



