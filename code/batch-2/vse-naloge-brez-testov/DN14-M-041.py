import risar
from math import sqrt
import random
from time import *


color = risar.nakljucna_barva()
width = 1
radius_pixels = 10
x = random.uniform(0 + radius_pixels, risar.maxX - radius_pixels)
y = random.uniform(0 + radius_pixels, risar.maxY - radius_pixels)
speed_x = random.uniform(-5, 5)
speed_y = sqrt(25 - speed_x ** 2)
circle = risar.krog(x, y, radius_pixels, color, width)

end = time() + 20

while time() < end:
    x += speed_x
    y += speed_y
    circle.setPos(x, y)
    if x < radius_pixels:
        speed_x = abs(speed_x)
    if x > risar.maxX - radius_pixels:
        speed_x = -abs(speed_x)
    if y < radius_pixels:
        speed_y = abs(speed_y)
    if y > risar.maxY - radius_pixels:
        speed_y = -abs(speed_y)
    risar.cakaj(0.02)