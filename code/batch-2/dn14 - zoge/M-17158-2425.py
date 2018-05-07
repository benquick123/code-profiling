import risar
from PyQt5.QtWidgets import QMessageBox
t = 0.02                        #frequency of updating in seconds

class Ball:
    def __init__(self):
        from random import uniform
        from math import cos, sin, pi
        self.x, self.y = risar.nakljucne_koordinate()
        self.direction = uniform(0, 2*pi)
        self.xspeed, self.yspeed = cos(self.direction) * 5, sin(self.direction) * 5
        self.color = risar.nakljucna_barva()
        self.ball = risar.krog(self.x, self.y, 10, self.color, 3)

    def move(self):
        from math import cos, sin, pi
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x > risar.maxX or self.x < 0:
            self.direction = pi - self.direction
            self.xspeed, self.yspeed = cos(self.direction) * 5, sin(self.direction) * 5
        if self.y > risar.maxY or self.y < 0:
            self.direction = 2*pi  - self.direction
            self.xspeed, self.yspeed = cos(self.direction) * 5, sin(self.direction) * 5
        self.ball.setPos(self.x, self.y)

    def delete(self):
        self.ball.hide()

class Round:
    def __init__(self, x, y, color):
        self.color = color
        self.x, self.y = x, y
        self.round = risar.krog(self.x, self.y, 30, self.color, 3)
        self.timer = 0

    def update(self):
        if risar.klik:
            self.timer += t
        else:
            self.follow()
    
    def follow(self):
        self.x, self.y = risar.miska
        self.round.setPos(self.x, self.y)

    def delete(self):
        self.round.hide()

#
#
#
#
#

def level(amount):
    from math import sqrt

    balls = []
    rounds = [Round(risar.maxX / 2, risar.maxY / 2, risar.bela)]
    cnt = 0
    for i in range(amount):
        balls.append(Ball())

    while len(rounds) and len(balls):
        for ball in balls:
            ball.move()
            if risar.klik:
                for r in rounds:
                    if sqrt((ball.x - r.x) ** 2 + (ball.y - r.y) ** 2) <= 40:
                        rounds.append(Round(ball.x, ball.y, ball.color))
                        ball.delete()
                        balls.pop(balls.index(ball))
                        cnt += 1
                        break
        
        for r in rounds:
            r.update()
            if r.timer >= 4:
                r.delete()
                rounds.pop(rounds.index(r))
            
        risar.cakaj(t)

    return cnt

def game():
    lvl = 1

    lvls = {1: lambda: (1, 5),
            2: lambda: (2, 10),
            3: lambda: (4, 15),
            4: lambda: (6, 20),
            5: lambda: (10, 25),
            6: lambda: (15, 30),
            7: lambda: (18, 35),
            8: lambda: (22, 40),
            9: lambda: (30, 45),
            10: lambda: (37, 50),
    }

    while lvl < 11:
        needed, amount = lvls[lvl]()
        st = "Level " + str(lvl)
        st1 = "Get " + str(needed) + " out of " + str(amount) + " balls"
        QMessageBox.information(None, st, st1)
        cnt = level(amount)
        if cnt >= needed:
            st1 = "You got " + str(cnt) + " out of " + str(amount) + " balls"
            QMessageBox.information(None, "Level passed", st1)
            lvl += 1
        else:
            QMessageBox.information(None, "Level failed", "Try again!")
        
        risar.pobrisi()
        risar.klik = False

    QMessageBox.information(None, "Congratulations!", "You beat the game! Thank You for playing!")

game()