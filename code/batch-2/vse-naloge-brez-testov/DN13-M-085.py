from math import *
class Minobot:
    def __init__(self): # konstruktor, oz. ko se minobot pokliče
        self.x = 0 # koordinate so na začetku na 0
        self.y = 0
        self.angle = 0 # na začetku je obrnejen desno, torej mora bit kot enak 0
    def naprej(self, d):
        if self.angle==0 or self.angle%360==0: # če je kot enak 0 ali večkratnik števila 360
            self.x +=d #potem se premikamo v desno po x osi
        if self.angle==180 or self.angle%360==180: # če je kot enak 180 ali je pa kot pri deljenju z 360 enak 180
            self.x -= d # potem se pomikamo v levo po x osi
        if self.angle==90 or self.angle%360==90: # če je kot enak 90 ali je pa kot pri deljenju z 360 enak 90
            self.y += d # potem se pomikamo gor po y osi
        if self.angle==270 or self.angle%360==270: # če je kot enak 270 ali je pa kot pri deljenju z 360 enak 270
            self.y -=d # potem se pomikamo dol po y osi
    def desno(self):
        self.angle += -90 # po koordinatnem sistemu se obrnemo v desno če odštejemo 90
    def levo(self):
        self.angle += +90 # po koordinatnem sistemu se obrnemo v desno če prištejmo 90
    def koordinate(self):
        return self.x, self.y # vrnemo samo koordinate x in y
    def razdalja(self):
        vrednost_x=abs(self.x) # sem spravim koliko je razlika med koordinatami x= 0 in pozicijo x na kateri je minobot
        vrednost_y=abs(self.y) # sem spravim koliko je razlika med koordinatami y= 0 in pozicijo y na kateri je minobot
        skupna_vrednost=vrednost_x+ vrednost_y
        return skupna_vrednost












