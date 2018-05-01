def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    file = open(ime_datoteke)
    str = file.read()
    seznamUkazov = str.split()
    seznamUkazov = [ukaz for ukaz in seznamUkazov if ukaz != "NAPREJ"]
    i = 0
    while i < len(seznamUkazov):
        if seznamUkazov[i] != "DESNO" and seznamUkazov[i] != "LEVO":
            seznamUkazov[i] = int(seznamUkazov[i])
        i += 1

    seznamStanj = []
    stanje = 0,0,"N"
    seznamStanj.append(stanje)

    for ukaz in seznamUkazov:
        stanje = premik(ukaz,stanje[0],stanje[1],stanje[2])
        seznamStanj.append(stanje)
    return seznamStanj

def opisi_stanje(x, y, smer):
    x = str(x)
    y = str(y)

    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer = "v"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"

    stanje = "{0:>3}:{1:<3} {2}".format(x,y,smer)
    return stanje

def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    file = open(ime_izhoda,"w")
    for stanje in stanja:
        stanjeStr = opisi_stanje(stanje[0],stanje[1],stanje[2])
        file.write(stanjeStr)
        file.write("\n")
    file.close()

