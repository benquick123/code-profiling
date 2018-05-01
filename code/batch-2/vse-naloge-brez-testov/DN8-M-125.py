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
    i = 1
    x, y = 0, 0
    smer = "N"
    seznamterk = []
    seznamterk.append((x, y, smer))
    for vrstica in open(ime_datoteke):
        vrstica = vrstica.split()
        if vrstica[0] == "DESNO":
            seznamterk.append(premik("R", x, y, smer))
            x = int(seznamterk[i][0])
            y = int(seznamterk[i][1])
            smer = str(seznamterk[i][2])
            i += 1
        elif vrstica[0] == "LEVO":
            seznamterk.append(premik("L", x, y, smer))
            x = int(seznamterk[i][0])
            y = int(seznamterk[i][1])
            smer = str(seznamterk[i][2])
            i += 1

        elif vrstica[0] == "NAPREJ":
            seznamterk.append(premik(int(vrstica[1]), x, y, smer))
            x = int(seznamterk[i][0])
            y = int(seznamterk[i][1])
            smer = str(seznamterk[i][2])
            i += 1
    return seznamterk

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{0:>3}:{1:<3} {2}".format(x,y,"^")
    elif smer == "E":
        return "{0:>3}:{1:<3} {2}".format(x,y,">")
    elif smer == "S":
        return "{0:>3}:{1:<3} {2}".format(x,y,"v")
    elif smer == "W":
        return "{0:>3}:{1:<3} {2}".format(x,y,"<")

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x, y, smer)+"\n")




