class Minobot:

    def __init__(self):
        self.x=0
        self.y=0
        self.pogled=1 #0 je Sever, 2 je jug, 1 je vzgod, 3 je zahod
        self.zgodovina=[]

    def desno(self):
        self.pogled=(self.pogled+1)%4
        self.zgodovina.append('desno')

    def levo(self):
        self.pogled=(self.pogled+3)%4
        self.zgodovina.append('levo')

    def naprej(self, d):
        if(self.pogled==0):
            self.y+=d
        if (self.pogled == 1):
            self.x += d
        if (self.pogled == 2):
            self.y -= d
        if (self.pogled == 3):
            self.x -= d
        self.zgodovina.append('naprej ' + str(d))
    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return abs(self.x)+abs(self.y)

    def razveljavi(self):
        if(len(self.zgodovina)>=1):
            ukaz=self.zgodovina[-1]
            ukaz=ukaz.split(" ")
            if(ukaz[0]=='desno'):
                self.pogled = (self.pogled - 1) % 4
            if(ukaz[0]=='levo'):
                self.pogled = (self.pogled - 3) % 4
            if(ukaz[0]=='naprej'):
                if (self.pogled == 0):
                    self.y += -int(ukaz[1])
                if (self.pogled == 1):
                    self.x += -int(ukaz[1])
                if (self.pogled == 2):
                    self.y -= -int(ukaz[1])
                if (self.pogled == 3):
                    self.x -= -int(ukaz[1])
            self.zgodovina.pop()
