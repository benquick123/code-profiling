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
    movement = []
    file = open(ime_datoteke)
    temp = file.read().split("\n")
    smer = "N"
    x = 0
    y = 0
    movement.append(premik(0, 0, 0, "N"))
    for line in temp:
        if line == "":
            continue
        tl = line.split()
        if tl[0] == "LEVO":
            ukaz = "L"
        elif tl[0] == "DESNO":
            ukaz = "R"
        else:
            ukaz = int(tl[1])
        pozicija = premik(ukaz, x, y, smer)
        movement.append(pozicija)
        x, y, smer = pozicija
    return(movement)

def opisi_stanje(x,y,smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    else:
        smer = "<"
    stanje = "{:>3}:{:<3} {}"
    return(stanje.format(x, y, smer))

def prevedi(ime_vhoda, ime_izhoda):
    file = open(ime_vhoda)
    movement_raw = izvedi(ime_vhoda)
    movements = []
    for (x,y,smer) in movement_raw:
        movements.append(opisi_stanje(x,y,smer))
    file = open(ime_izhoda, "w")
    for movement in movements:
        file.write(str(movement) + "\n")
    file.close()

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    else:
        smer = "<"
    stanje = "{} {:>4}:{})"
    return(stanje.format(smer, "(" + str(x), y))

