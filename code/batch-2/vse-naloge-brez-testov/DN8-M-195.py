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
    pot = [(0,0,"N")]
    i = 0
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        if vrstica.split()[0] == "DESNO":
            pot.append(premik("R",pot[i][0],pot[i][1],pot[i][2]))
        elif vrstica.split()[0] == "LEVO":
            pot.append(premik("L",pot[i][0],pot[i][1],pot[i][2]))
        elif vrstica.split()[0] == "NAPREJ":
            pot.append(premik(int(vrstica.split()[1]),pot[i][0],pot[i][1], pot[i][2]))
        i += 1
    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer="^"
    elif smer == "E":
        smer=">"
    elif smer== "S":
        smer ="v"
    elif smer == "W":
        smer="<"
    return "{:>3}:{:<3} {}".format(x,y,smer)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_vhoda)
    pot = izvedi(ime_vhoda)
    datoteka2 = open(ime_izhoda,"w")
    for x,y,smer in pot:
        datoteka2.write(opisi_stanje(x,y,smer)+"\n")
    datoteka.close()
    datoteka2.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer="^"
    elif smer == "E":
        smer=">"
    elif smer== "S":
        smer ="v"
    elif smer == "W":
        smer="<"
    return "{} {:>4}:{}".format(smer,"(" + str(x),str(y)+ ")")



