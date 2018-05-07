import risar
from random import randint
import math
from PyQt5.QtWidgets import QMessageBox

class Ball:
    def __init__(self, x = None, y = None, radius = 10):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        else:
            pos = random_pos()
            self.x = pos[0]
            self.y = pos[1]

        self.speed = 5
        self.radius = radius
        self.sprite = risar.krog(self.x, self.y, self.radius, risar.nakljucna_barva(), 2)
        self.timer = 4

        direction = random_direction()
        self.dx = self.speed * math.sin(direction)
        self.dy = self.speed * math.cos(direction)

    def update(self):
        self.resolve_collision()

        self.x += self.dx
        self.y += self.dy

        self.sprite.setPos(self.x, self.y)

    def resolve_collision(self):
        if self.y + self.dy < 0 or self.y + self.dy > risar.maxY:
            self.dy = -self.dy

        if self.x + self.dx < 0 or self.x + self.dx > risar.maxX:
            self.dx = -self.dx

    def is_colliding(self, ball):
        distance = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
        if distance <= self.radius + ball.radius:
            return True

        return False

    def set_pos(self, x, y):
        self.x = x
        self.y = y

        self.sprite.setPos(self.x, self.y)

    def explode(self):
        self.radius = 30

        # Set the visuals of the ball to match the new radius
        self.sprite.setRect(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)
        color = self.sprite.pen().color().lighter()
        color.setAlpha(192)
        self.sprite.setBrush(color)

    # Returns true if the timer has ended
    def tick(self, loop_delay):
        self.timer -= loop_delay
        if self.timer <= 0:
            return True

        return False

    def hide(self):
        self.sprite.hide()


def random_direction():
    return randint(0, 360)

def random_pos():
    # -10 to compensate for the ball size
    return randint(10, risar.maxX - 10), randint(10, risar.maxY - 10)

player_ball = Ball(risar.miska[0], risar.miska[1], 30)
risar.klik = False

balls = []
number_of_balls = 20
for i in range(0, number_of_balls):
    balls.append(Ball())

number_of_exploded_balls = 0
exploded_balls = []

# Do the simulation for 20s
stop = False
clicked = False
loop_delay = 0.02
while not stop:
    # Update balls
    for ball in balls:
        ball.update()

    # Check the collision or update the player_ball position
    if risar.klik or clicked:
        # Add the player_ball in the exploded_balls when first clicked
        if clicked is False:
            exploded_balls.append(player_ball)
        clicked = True

        # Check the collision for the exploded balls
        for e_ball in exploded_balls:
            for ball in balls:
                if e_ball.is_colliding(ball):
                    ball.explode()
                    balls.remove(ball)
                    exploded_balls.append(ball)

                    number_of_exploded_balls += 1
    else:
        player_ball.set_pos(risar.miska[0], risar.miska[1])

    # Update the exploded_balls expire timers
    for e_ball in exploded_balls:
        if e_ball.tick(loop_delay):
            e_ball.hide()
            exploded_balls.remove(e_ball)

    # Check if the are no more exploded balls once the 'game has started'
    if clicked and len(exploded_balls) == 0:
        stop = True
        # break is just because it will exit faster this way
        break

    risar.cakaj(loop_delay)

QMessageBox.information(None, "Rezultat", "Počil si " + str(number_of_exploded_balls) + " od " + str(number_of_balls) +
                        " žogic")

risar.stoj()
