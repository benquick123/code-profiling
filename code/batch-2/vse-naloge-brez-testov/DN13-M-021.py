class Minobot:
    def __init__(self):
        self.x=0
        self.y=0
        self.direction=90
        self.tab=[]

    def koordinate(self):
        return self.x,self.y

    def naprej(self, d):
        self.tab.append(['naprej',d])
        if self.direction == 0 or self.direction == 360:
            self.y+=d
        elif self.direction == 90 or self.direction == -90:
            self.x+=d
        elif self.direction == 180 or self.direction == -180:
            self.y-=d
        elif self.direction == 270 or self.direction == -270:
            self.x-=d


    def desno(self):
        self.tab.append(['desno',90])
        self.direction += 90
        if self.direction >= 360:
                self.direction = 0


    def levo(self):
        self.tab.append(['levo',-90])
        self.direction -= 90
        if self.direction <= 0:
                self.direction = 360


    def razdalja(self):
        return abs(self.x)+abs(self.y)

    def razveljavi(self):
        print(self.tab)
        if self.tab:
            if self.tab[len(self.tab)-1][0] == 'naprej':
                self.naprej(-(self.tab[len(self.tab)-1][1]))

            elif self.tab[len(self.tab)-1][0] == 'desno':
                self.levo()

            elif self.tab[len(self.tab)-1][0] == 'levo':
                self.desno()
            self.tab.pop()
            self.tab.pop()




