import risar
import random
import time
import multiprocessing
def f(x,y,n,m):
    if time.time() > start + cajt:
        quit()
    print(start)
    print(x,y)
    print(m,n)
    while True:
        if y == 486:
            if time.time() > start + cajt:
                print(time.time())
                quit()
            n="-"
            print("maxY")
            while True:
                if time.time() > start + cajt:
                    print(time.time())
                    quit()
                krog.setPos(x, y)
                risar.cakaj(0.005)
                if x == 10:
                    m = "+"
                    if y==10:
                        n="+"
                    f(x, y, n, m)
                if y == 10:
                    n= "+"
                    if x==10:
                        m="+"
                    f(x, y, n, m)
                if x ==  796:
                    print("je")
                    m="-"
                    if y==486:
                        n="-"
                    f(x,y,n,m)
                if n == "+":
                    y = y + 1
                else:
                    y = y - 1
                if m == "+":
                    x = x + 1
                else:
                    x = x - 1


        if x == risar.maxX - 10:
            if time.time() > start + cajt:
                print(time.time())
                quit()
            print("maxX")
            m="-"
            while True:
                if time.time() > start + cajt:
                    print(time.time())
                    quit()
                krog.setPos(x, y)
                risar.cakaj(0.005)
                if x == 10:
                    m = "+"
                    if y==10:
                        n="+"
                    f(x, y, n, m)
                if y == 10:
                    n= "+"
                    if x==10:
                        m="+"
                    f(x, y, n, m)
                if y ==  risar.maxY - 10:
                    n="-"
                    if x==786:
                        m="-"
                    f(x,y,n,m)
                if m == "+":
                    x = x + 1
                else:
                    x = x - 1
                if n == "+":
                    y = y + 1
                else:
                    y = y - 1

        if x == 10:
            if time.time() > start + cajt:
                print(time.time())
                quit()
            print("x10")
            m="+"
            while True:
                if time.time() > start + cajt:
                    print(time.time())
                    quit()
                krog.setPos(x, y)
                risar.cakaj(0.005)
                if y == 10:
                    n = "+"
                    if x== 10:
                        m="+"
                    f(x, y, n, m)
                if x == risar.maxX-10:
                    m = "-"
                    if y==486:
                        n="-"
                    f(x, y, n, m)
                if y == risar.maxY - 10:
                    n = "-"
                    if x==786:
                        m="-"
                    f(x, y, n, m)
                if m == "+":
                    x = x + 1
                else:
                    x = x - 1
                if n == "+":
                    y = y + 1
                else:
                    y = y - 1

        if y == 10:
            if time.time() > start + cajt:
                print(time.time())
                quit()
            print("y10")
            n="+"
            while True:
                if time.time() > start + cajt:
                    print(time.time())
                    quit()
                krog.setPos(x, y)
                risar.cakaj(0.005)
                if x == 10:
                    m = "+"
                    if y==10:
                        n="+"
                    f(x, y, n, m)
                if y == 486:
                    if x==786:
                        m="-"
                    n = "-"
                    f(x, y, n, m)
                if x == 786:
                    if y==486:
                        n="-"
                    m = "-"
                    f(x, y, n, m)
                if n == "+":
                    y = y + 1
                else:
                    y = y - 1
                if m == "+":
                    x = x + 1
                else:
                    x = x - 1

        if time.time()>start+cajt:
            print(time.time())
            quit()
        if m=="+":
            x = x + 1
        else:
            x=x-1
        if n == "+":
            y = y + 1
        else:
            y = y - 1
        krog.setPos(x, y)
        risar.cakaj(0.005)



global start
start=time.time()
global cajt
cajt=20

x,y=risar.nakljucne_koordinate()
krog=risar.krog(x,y,10, barva=risar.nakljucna_barva())

m=random.choice(['+', '-'])
n=random.choice(['+', '-'])
f(x,y,n,m)