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
    datoteka = open(ime_datoteke)
    seznam = [(0,0,"N")]
    counter = 0
    for vse in datoteka:
        if vse.startswith("DESNO"):
            x,y,smer = seznam[counter]
            nekaj = premik("R",x,y,smer)
            seznam.append(nekaj)
            counter += 1
        if vse.startswith("LEVO"):
            x, y, smer = seznam[counter]
            nekaj = premik("L", x, y, smer)
            seznam.append(nekaj)
            counter += 1
        if vse.startswith("NAPREJ"):
            x,y,smer = seznam[counter]
            drugo = vse.split(" ")
            nekaj = premik(int(drugo[1]),x,y,smer)
            seznam.append(nekaj)
            counter += 1
    return(seznam)

def opisi_stanje(x,y,smer):
    if smer == "N":
        stanje = "^"
    if smer == "E":
        stanje = ">"
    if smer == "S":
        stanje = "v"
    if smer == "W":
        stanje = "<"
    return("{X:3}:{Y:<3} {S}".format(X=x, Y=y, S=stanje))

def prevedi(ime_vhoda,ime_izhoda):
    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for vse in seznam:

        x,y,smer = vse
        opis = opisi_stanje(x,y,smer)
        datoteka.write(opis + "\n")
    datoteka.close()



def opisi_stanje_2(x,y,smer):
    if smer == "N":
        stanje = "^"
    if smer == "E":
        stanje = ">"
    if smer == "S":
        stanje = "v"
    if smer == "W":
        stanje = "<"
    x = "(" + str(x)
    return("{S} {X:>4}:{Y})".format(X=x, Y=y, S=stanje))


