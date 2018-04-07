import risar
from random import randint, random, choice
from PyQt5.QtWidgets import QMessageBox
import time
import math
risar.obnavljaj = True
#MAJOR
#TODO  6 ... OK
#TODO  7 ... OK
#TODO  8 ... OK
#TODO  9 ... OK
#TODO 10 ... OK

#MINOR
#TODO fix speed ... OK

#MISC
#TODO create helper function to create circles ... OK
#TODO create helper function to paint circles ... OK



'''
NAVODILA ZA IZVAJANJE PROGRAMA
Za izvajanje funkcije za nalogo 10 zaženite program. 
Za izvanjanje drugih funkcij na koncu datoteke odkomentirajte klic funkcije, ki jo želite zagnati. 
'''

'''
    POMOŽNE FUNKCIJE
'''

'''
Kreiranje krogov
'''
def create_circles(stevilo):
    '''
    Creates a list for each object risar.krog with random coordinates, random radius, random color and thickness of 5.
    Values stored in list are: risar.krog object, horizontal speed, vertical speed, counter, explosion start time
    and explotion status bool.

    New speed is calculated using pythagorean theorem.
    Function returns a list of lists if there is more than 1 circle created otherwise it returns a single list with
    above values.
    :param stevilo:
    :return:
    '''
    krogi = []
    for i in range(stevilo):
        krog = risar.krog(randint(30, risar.maxX - 30), randint(30, risar.maxY - 30), 10,
                          risar.barva(randint(30, 240), randint(30, 240), randint(30, 240)), 5)
        x = choice([-4, -3, -2, -1, 1, 2, 3, 4])
        y = math.sqrt((5**2)-(x**2))
        krogi.append([krog, x, y, 0, 0, False])
    return krogi if len(krogi)>1 else krogi[0]

def pobarvaj(item, alpha):
    '''
    Colors inside of a item with same color and given alpha.
    :param item:
    :param alpha:
    :return:
    '''
    color = item.pen().color().lighter()
    color.setAlpha(alpha)
    item.setBrush(color)

'''
Nivoji za funkcijo za_10()
'''
def za_10_game(krogov):
    '''
    Draws x circles - krogov - at random positions, moves them around. Draws an extra circle, around mouse coordinates.
    Mouse circle follows mouse until first left click. After the click mouse circle stops, each circle that touches
    that circle explodes, thus creating another explosion node. Each circle that touches an explosion node, explodes
    as well. Program ends when there is no more exploded circles on canvas or time runs out. It display how many circles
    have exploded and terminates.
    Speed of movement is 5, circles bounce upon hitting edge.
    Explotion time is 4 seconds. Runout time is 20 seconds.
    Calls create_circles, to create actual objects.
    :return:
    '''

    krogi = create_circles(krogov)

    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
                       risar.barva(255, 255, 255), 3)

    miska_start = 0
    miska_klik = False
    stevec = 0
    stop_koordinate = {"miska": (risar.miska[0], risar.miska[1])}
    while True:
        if not risar.klik:
            stop_koordinate["miska"] = (risar.miska[0], risar.miska[1])
            miska.setPos(risar.miska[0], risar.miska[1])

        for n in range(len(krogi)):
            item, new_x, new_y, count, startime, status = krogi[n]
            if time.time() - miska_start >= 4 and miska_klik:
                miska.hide()
                miska_klik = False
                del stop_koordinate["miska"]
                if len(stop_koordinate) == 0:
                    return stevec
            if startime != 0 and time.time() - krogi[n][4] >= 4:
                item.hide()
                krogi[n][4] = 0
                del stop_koordinate[item]
                if len(stop_koordinate) == 0:
                    return stevec
                continue
            elif status == True:
                continue
            item.setPos(item.x() + new_x, item.y() + new_y)
            if risar.klik and miska_start == 0:
                pobarvaj(miska, 200)
                miska_start = time.time()
                miska_klik = True
            for x, y in stop_koordinate.values():
                if x - 35.0 < item.x() < x + 35.0 and y - 35.0 < item.y() < y + 33.0 and risar.klik:
                    item.setRect(-30, -30, 60, 60)
                    pobarvaj(item, randint(120, 180))
                    stop_koordinate[item] = (item.x(), item.y())
                    krogi[n][4] = time.time()
                    krogi[n][5] = True
                    stevec += 1
                    break
            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY - 15):
                krogi[n][2] = -new_y
        risar.cakaj(0.02)



'''
    DOMAČA NALOGA
'''
'''
 6. OK
'''
def za_6():
    '''
    Draws a circle at random position, moves it around for 20 seconds.
    Speed of movement is 5. Bounces upon hitting edge.
    Calls create_circles, to create actual objects.
    :return:
    '''
    krog, x, y, *n = create_circles(1)
    st = time.time()
    while True:
        if time.time()-st > 20:
            exit()
        krog.setPos(krog.x() + x, krog.y() + y)
        if not (15 < krog.x() < risar.maxX-15):
            x = -x
        if not (15 < krog.y() < risar.maxY-15):
            y = -y
        risar.cakaj(0.02)

'''
 7. OK
'''
def za_7():
    '''
    Draws randomly colored circles 30 circles on random coordinates, moves them around for 20 seconds.
    Speed of movement is 5, circles bounce upon hitting edge.
    Calls create_circles, to create actual objects.
    :return:
    '''
    krogi = create_circles(30)
    st = time.time()
    while True:
        if time.time() - st > 20:
            exit()
        for n in range(len(krogi)):
            item, new_x, new_y, *s = krogi[n]
            item.setPos(item.x() + new_x, item.y() + new_y)
            if not (15 < item.x() < risar.maxX-15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY-15):
                krogi[n][2] = -new_y

        risar.cakaj(0.02)

'''
 8. OK
'''
def za_8():
    '''
    Draws 30 circles at random positions, moves the around. Draws an extra circle, around mouse coordinates.
    Mouse circle follows mouse until first left click. After the click circle stops, program terminates when first
    circle touches mouse circle.
    Speed of movement is 5, circles bounce upon hitting edge.
    Calls create_circles, to create actual objects.
    :return:
    '''
    krogi = create_circles(30)
    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
                       risar.barva(255, 255, 255), 3)

    while True:
        if not risar.klik:
            checkx, checky = risar.miska
            miska.setPos(checkx, checky)
        for n in range(len(krogi)):
            item, new_x, new_y, *s = krogi[n]
            item.setPos(item.x() + new_x, item.y() + new_y)
            if checkx-33 < item.x() < checkx+33 \
                    and checky-33 < item.y() < checky+33 and risar.klik:
                     exit()
            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY - 15):
                krogi[n][2] = -new_y
        risar.cakaj(0.02)

'''
 9. OK
'''
def za_9():
    '''
    Draws 30 circles at random positions, moves them around. Draws an extra circle, around mouse coordinates.
    Mouse circle follows mouse until first left click. After the click mouse circle stops, each circle that touches
    that circle explodes, thus creating another explosion node. Each circle that touches an explosion node, explodes
    as well. Program ends when there is no more exploded circles on canvas or time runs out. It display how many circles
    have exploded and terminates.
    Speed of movement is 5, circles bounce upon hitting edge.
    Explotion time is 4 seconds. Runout time is 20 seconds.
    Calls create_circles, to create actual objects.
    :return:
    '''
    krogi = create_circles(30)

    miska = risar.krog(risar.miska[0], risar.miska[1], 30,
                       risar.barva(255, 255, 255), 3)

    miska_start = 0
    miska_klik = False
    stevec = 0
    stop_koordinate = {"miska": (risar.miska[0], risar.miska[1])}
    while True:
        if not risar.klik:
            stop_koordinate["miska"] = (risar.miska[0], risar.miska[1])
            miska.setPos(risar.miska[0], risar.miska[1])

        for n in range(len(krogi)):
            item, new_x, new_y, count, startime, status = krogi[n]
            if time.time()-miska_start >= 4 and miska_klik:
                miska.hide()
                miska_klik = False
                del stop_koordinate["miska"]
                if len(stop_koordinate) == 0:
                    QMessageBox.information(None, "Konec",
                                            "Zadeli ste {} zog. ".format(stevec))
                    exit()
            if startime != 0 and time.time() - krogi[n][4] >= 4:
                item.hide()
                krogi[n][4] = 0
                del stop_koordinate[item]
                if len(stop_koordinate) == 0:
                    QMessageBox.information(None, "Konec",
                                            "Zadeli ste {} zog. ".format(stevec))
                    exit()
                continue

            elif status == True:
                continue
            item.setPos(item.x() + new_x, item.y() + new_y)
            if risar.klik and miska_start == 0:
                pobarvaj(miska, 150)
                miska_start = time.time()
                miska_klik = True
            for x, y in stop_koordinate.values():
                if x - 35.0 < item.x() < x + 35.0 and y - 35.0 < item.y() < y + 33.0 and risar.klik:
                        item.setRect(-30, -30, 60, 60)
                        pobarvaj(item, randint(120, 180))
                        stop_koordinate[item] = (item.x(), item.y())
                        krogi[n][4] = time.time()

                        krogi[n][5] = True
                        stevec += 1
                        break

            if not (15 < item.x() < risar.maxX - 15):
                krogi[n][1] = -new_x
            if not (15 < item.y() < risar.maxY - 15):
                krogi[n][2] = -new_y
        risar.cakaj(0.02)
    
'''
10. OK
'''
def za_10():
    '''
    Repeats the call of function za_10_game() for each element in pravila, if enough circles have exploded it continues,
    otherwise it repeats the loop. Program terminates when all levels have been completed. It also changes the color
    of the background for each iteration.

    :return:
    '''
    pravila = [(1, 5), (2, 8), (5, 10), (8, 16), (12, 20), (16, 24), (20, 28), (25, 30), (28, 30), (30, 30)]
    i = 0
    while i < len(pravila):
        potrebnih, vseh = pravila[i]
        risar.klik = False
        QMessageBox.information(None, "Nivo {}".format(pravila.index((potrebnih, vseh)) + 1),
                                "Zadeni {} od {} zog.".format(potrebnih, vseh))
        rezultat = za_10_game(vseh)
        if potrebnih <= rezultat:

            i += 1
        else:
            QMessageBox.information(None, "Nivo {}".format(pravila.index((potrebnih, vseh)) + 1),
                                    "Zadeli ste {} od {} zog. Poskusite ponovno!".format(rezultat, vseh))
        risar.pobrisi()
        risar.barvaOzadja(risar.barva(randint(0, 100), randint(0, 100), randint(0, 100)))
    
'''
KLICI FUNKCIJ ZA DOMAČO NALOGO
'''

#za_6()
#za_7()
#za_8()
#za_9()
za_10()

