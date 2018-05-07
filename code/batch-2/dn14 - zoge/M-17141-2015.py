import risar
from random import randint
from math import sqrt
import time
class Ball(): #ni nujno da jih nastavim
    def __init__(self, x=None, y=None, r=None, vx=None, vy=None, barva=None):

        if r is None:
            self.r = randint(15,30)
        if x is None or y is None:
            self.x = randint((0+self.r),(risar.maxX-self.r))
            self.y = randint((0+self.r), (risar.maxY-self.r))
        else:
            self.x, self.y = x, y
        if vx is None or vy is None:
            v = randint(5, 10)
            vx = randint(-v, v)
            vy = sqrt(v ** 2 - vx ** 2)
        self.vx = vx
        self.vy = vy
        if barva == None:



            barva = risar.barva(randint(0, 255), randint(0, 255), randint(0, 255))




        self.krog = risar.krog(self.x, self.y, self.r, barva,5)
        c = self.krog.pen().color().lighter()
        c.setAlpha(111)
        self.krog.setBrush(c)


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def get_r(self):
        return self.r

    def get_shape(self):
        return self.krog

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.krog.setPos(self.x, self.y)
        #check x boundaries
        if self.x-self.r <= 0:
            self.vx = abs(self.vx)
        if self.x+self.r >= risar.maxX:
            self.vx = -abs(self.vx)
        #check y bounds
        if self.y-self.r <= 0:
            self.vy = abs(self.vy)
        if self.y+self.r >= risar.maxY:
            self.vy = -abs(self.vy)


krogle=list()
for i in range(30):
    krogle.append(Ball())

start = time.time()
end_at = time.time() + 20.0

while time.time() < end_at:
    for i, ball in enumerate(krogle):
        zogice_x, zogice_y, zogice_r = ball.get_x(), ball.get_y(), ball.get_r()

        ball.move()


        if risar.klik is True:
            klik_x, klik_y = risar.miska
            Circle = risar.krog(klik_x,klik_y,30)
            c = Circle.pen().color().lighter()
            c.setAlpha(111)
            Circle.setBrush(c)
            risar.klik = False




    risar.cakaj(0.02)






exit()






# def setup_igre(stevilo_zog):
#     objs = list()
#     for i in range(stevilo_zog):
#         objs.append(Ball())
#     return objs
#
#
# def game():
#     active_zoge = setup_igre(4)
#     while True:
#         for i, j in enumerate(active_zoge):
#
#
#             j.move()
#         time.sleep(0.01)






