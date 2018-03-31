"""13.01.2018 Daniil Popov"""

import risar
import random
import math

class balls():
    def __init__(self):
        self.colour = risar.nakljucna_barva()
        self.randPositionX, self.randPositionY = risar.nakljucne_koordinate()
        self.randFloat = random.uniform(-1, 1)
        self.randDirection = math.acos(self.randFloat)
        print("Rand float is: ", self.randFloat)
        print("Rand ArcCos is: ", self.randDirection)
        self.game = risar.krog(self.randPositionX, self.randPositionY, 10, self.colour, 1)

    def moving(self):
        if ((self.randPositionX) < risar.maxX) and (self.randPositionX > 0):
            self.randPositionX += 5 * math.cos(self.randDirection)
            self.game.setPos(self.randPositionX, self.randPositionY)
        else:
            self.randDirection = math.pi - self.randDirection
            self.randPositionX += 5 * math.cos(self.randDirection)
            self.game.setPos(self.randPositionX, self.randPositionY)

        if ((self.randPositionY) < risar.maxY) and (self.randPositionY > 0):
            self.randPositionY += 5 * math.sin(self.randDirection)
            self.game.setPos(self.randPositionX, self.randPositionY)
        else:
            self.randDirection = math.pi*2 - self.randDirection
            self.randPositionY += 5 * math.sin(self.randDirection)
            self.game.setPos(self.randPositionX, self.randPositionY)

#class mouseEvents():
#    def __init__(self):
#        self.mousePositionX, self.mousePositionY = risar.miska
#        self.radius = 30
#        self.waitForActtion = risar.klik
#        risar.krog(mouse.mousePositionX, mouse.mousePositionY, 30, risar.nakljucna_barva(),  1)
#
#    def updatePosition(self):
#        if not risar.click:
#            self.mousePositionX, self.mousePositionY = risar.miska

mousePositionX, mousePositionY = risar.miska
mouse = risar.krog(mousePositionX, mousePositionY, 30, risar.nakljucna_barva(),  1)

thirtyBalls = []
for i in range(30):
    thirtyBalls.append(balls())

ifHit = False

while True:
        if risar.klik != True:
            mousePositionX, mousePositionY = risar.miska
            mouse.setPos(mousePositionX, mousePositionY)
        else:
            for i in range(len(thirtyBalls)):
                if math.sqrt((thirtyBalls[i].randPositionX - mousePositionX)**2 + (thirtyBalls[i].randPositionY - mousePositionY)**2) <= 40:
                    ifHit = True
        if ifHit:
            print("Game over")
            risar.cakaj(1)
            break
        for i in range(len(thirtyBalls)):
            thirtyBalls[i].moving()
        risar.cakaj(0.02)
