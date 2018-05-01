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
    x,y = 0,0
    polozaj="N"
    smeri = "NESW"
    datoteka = open(ime_datoteke)
    seznam=[(x,y,polozaj)]
    for vrstice in datoteka:
        ismer = smeri.index(polozaj)
        if "DESNO" in vrstice:
            polozaj = smeri[(ismer + 1) % 4]
        elif "LEVO" in vrstice:
            polozaj = smeri[(ismer - 1) % 4]
        elif "NAPREJ" in vrstice:
            a = int(vrstice.replace('NAPREJ ',''))
            if polozaj == 'N':
                y = y-a
            if polozaj == 'E':
                x = x+a
            if polozaj == 'S':
                y = y+a
            if polozaj == 'W':
                x = x-a
        seznam.append((x,y,polozaj))
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:3}:{:<3}{:2}".format(x, y, " ^")
    elif smer == "E":
        return "{:3}:{:<3}{:2}".format(x, y, " >")
    elif smer == "S":
        return "{:3}:{:<3}{:2}".format(x, y, " v")
    elif smer == "W":
        return "{:3}:{:<3}{:2}".format(x, y, " <")

def prevedi(ime_vhoda, ime_izhoda):
    izhod = open(ime_izhoda, "w")
    for x,y,smer in izvedi(ime_vhoda):
        izhod.write(opisi_stanje(x,y,smer))
        izhod.write("\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return "{:2}{:>4}:{:>2}".format("^","("+str(x),str(y)+")")
    elif smer == "E":
        return "{:2}{:>4}:{:>2}".format(">", "(" + str(x), str(y) + ")")
    elif smer == "S":
        return "{:2}{:>4}:{:>2}".format("v", "(" + str(x), str(y) + ")")
    elif smer == "W":
        return "{:2}{:>4}:{:>2}".format("<", "(" + str(x), str(y)+")")

