def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    elif (isinstance(ukaz, int)):
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    premiki = [(0,0,"N")]
    datoteka = open(ime_datoteke)
    ukazi = datoteka.read();
    splitted_u = ukazi.split("\n")
    startx = 0
    starty = 0
    smer = "N"
    for ukaz in splitted_u:
        ukaz_x = ukaz.split(" ")
        if (len(ukaz_x) == 2):
            ukaz = int(ukaz_x[1])
        pmk = premik(ukaz, startx, starty, smer)
        premiki.append(pmk)
        startx = pmk[0]
        starty = pmk[1]
        smer = pmk[2]
    premiki.remove(premiki[len(premiki) - 1])
    return premiki

def opisi_stanje(x, y, smer):
    if (smer == "N"):
        pusc = "^"
    elif (smer == "E"):
        pusc = ">"
    elif (smer == "S"):
        pusc = "v"
    elif (smer == "W"):
        pusc = "<"

    if (x < 10)and(x>=0):
        x = "  " + str(x)
    elif (x > 9)and(x < 100):
        x = " " + str(x)
    elif (x > -10) and (x < 0):
        x = " " + str(x)


    if (y < 10)and(y>=0):
        y = str(y) + "  "
    elif (y > 9)and(y<100):
        y = str(y) + " "
    elif (y > -10) and (y < 0):
        y = " " + str(y)

    return (str(x)+":"+str(y)+" "+pusc)

def prevedi(vhod, izhod):
    pot = izvedi(vhod)
    string_o = ""
    for x, y, smer in pot:
        string_o += opisi_stanje(x,y,smer) + "\n"

    dat = open(izhod, "w")
    dat.write(string_o)

def opisi_stanje_2(x,y, smer):
    if (smer == "N"):
        pusc = "^"
    elif (smer == "E"):
        pusc = ">"
    elif (smer == "S"):
        pusc = "v"
    elif (smer == "W"):
        pusc = "<"

    if (x < 10)and(x>=0):
        x = "  (" + str(x)
    elif (x > 9)and(x < 100):
        x = " (" + str(x)
    elif (x > 99)and(y<1000):
        x = "(" + str(x)
    elif (x > -10) and (x < 0):
        x = " (" + str(x)
    elif (x > -100) and (x < -9):
        x = "(" + str(x)


    y = str(y) + ")"

    return (pusc + " " + x + ":" + y)

