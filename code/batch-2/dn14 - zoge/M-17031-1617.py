import risar
from random import randint, choice
from math import sqrt
import time
from PyQt5.QtWidgets import QMessageBox

def game(ball_num, ball_goal):
    risar.pobrisi()
    QMessageBox.information(None, "", "Razstreli %d žog od %d." % (ball_goal, ball_num))
    balls = [risar.krog(*risar.nakljucne_koordinate(), 10, sirina = 3,
                        barva = risar.nakljucna_barva()) for i in range(ball_num)]
    vx = [randint(-4, 4) or 1 for i in balls]
    vy = [sqrt(25 - v**2) * choice((1, -1)) for v in vx]
    mouse_circle = risar.krog(*risar.miska, 30)
    passed_times_since_explosions = []
    exploded_balls = []
    mouse_ball_placed = False
    while exploded_balls or not mouse_ball_placed:

        if risar.klik:
            risar.klik = False
            mouse_ball_placed = True
            exploded_balls.append(mouse_circle)
            passed_times_since_explosions.append(time.time())
        elif not mouse_ball_placed:
            mouse_circle.setPos(*risar.miska)

        for t in passed_times_since_explosions:
            if time.time() - t > 4:
                risar.odstrani(exploded_balls.pop(0))
                passed_times_since_explosions = passed_times_since_explosions[1:] 

        for i,b in enumerate(balls):
            if b is None:
                continue

            if b.y() < 0 or b.y() > risar.maxY:
                vy[i] = -vy[i]
            if b.x() < 0 or b.x() > risar.maxX:
                vx[i] = -vx[i]
            b.setPos(b.x() + vx[i], b.y() + vy[i])

            for k in exploded_balls:
                dx = b.x() - k.x()
                dy = b.y() - k.y()
                if sqrt(dx**2 + dy**2) <= 40:
                    c = b.pen().color().lighter()
                    c.setAlpha(192)
                    b.setBrush(c)
                    b.setRect(-30, -30, 60, 60)
                    exploded_balls.append(b)
                    balls[i] = None
                    passed_times_since_explosions.append(time.time())
                    break

        risar.cakaj(0.02)

    if balls.count(None) < ball_goal:
        QMessageBox.information(None, "", "Razstrelili ste %d žog. Premalo." % balls.count(None))
        return False
    else:
        return True

for i in range(1,11):
    while not game(i*3, int(i**1.45)):
        continue
 
