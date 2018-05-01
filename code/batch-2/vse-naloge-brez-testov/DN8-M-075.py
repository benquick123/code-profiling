#########

def izvedi(ime_datoteke):
    result = []
    x = 0
    y = 0
    smer = "N"
    commands = open(ime_datoteke).read()
    result.append((x, y, smer))
    for command in commands.split("\n")[:-1]:
        if command.startswith("D"):
            ukaz = "R"
        elif command.startswith("L"):
            ukaz = "L"
        else:
            ukaz = int(command.split(" ")[1])
        temp = premik(ukaz, x, y, smer)
        result.append(temp)
        x = temp[0]
        y = temp[1]
        smer = temp[2]
    return result

###

def opisi_stanje(x, y, smer):
    if smer == "N":
        direction = "^"
    elif smer == "S":
        direction = "v"
    elif smer == "E":
        direction = ">"
    elif smer == "W":
        direction = "<"
    return ("{x:>3}:{y:<3} {d:}".format(x = x, y = y, d = direction))

###

def prevedi(ime_vhoda, ime_izhoda):
    t = open(ime_izhoda, "w")
    for entry in izvedi(ime_vhoda):
        x = opisi_stanje(entry[0], entry[1], entry[2])
        t.write(x + "\n")
    t.close()

###

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        direction = "^"
    elif smer == "S":
        direction = "v"
    elif smer == "E":
        direction = ">"
    elif smer == "W":
        direction = "<"
    return ("{d:} {x:>4}:{y:}".format(x = "(" + str(x), y = str(y) + ")", d = direction))

#########

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


