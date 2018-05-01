def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    x = 0
    y = 0
    smer = "N"
    move = []
    move.append((x, y, smer))
    datoteka = open(ime_datoteke)

    for all in datoteka:
        order = all.strip()
        if order == "DESNO":
            ukaz = "R"
            x, y, smer = premik(ukaz, x, y, smer)
            move.append((x, y, smer))
        elif order == "LEVO":
            ukaz = "L"
            x, y, smer = premik(ukaz, x, y, smer)
            move.append((x, y, smer))
        else:
            ukaz = order.split(" ")
            x, y, smer = premik(int(ukaz[1]), x, y, smer)
            move.append((x, y, smer))

    datoteka.close()

    return move

def opisi_stanje(x, y, smer):
    spacey = ""
    spacex = ""
    if smer== "N":
        smer="^"

    if smer== "S":
        smer= "v"

    if smer== "E":
        smer= ">"

    if smer== "W":
        smer= "<"

    for i in range(3,len(str(x)),-1):
        spacex= spacex+" "

    for i in range(3, len(str(y))-1 , -1):
        spacey = spacey + " "


    return spacex+str(x)+":"+str(y)+ spacey+smer


def prevedi(ime_vhoda, ime_izhoda):
    Igotdamoves=izvedi(ime_vhoda)
    orders=[]
    for x,y,smer in Igotdamoves:
        orders.append(opisi_stanje(x,y,smer))
    datoteka=open(ime_izhoda,"w")

    for order in orders:
        datoteka.write(order+"\n")

    datoteka.close()

def opisi_stanje_2(x, y, smer):
    spacex = ""
    if smer == "N":
        smer = "^"

    if smer == "S":
        smer = "v"

    if smer == "E":
        smer = ">"

    if smer == "W":
        smer = "<"

    for i in range(4, len(str(x)), -1):
        spacex = spacex + " "


    return smer+spacex + "("+ str(x) +  ":" + str(y) + ")"



