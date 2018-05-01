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
    rezSez = []
    currentSide = 'N'
    currX = 0
    currY = 0
    rezSez.append((currX, currY, currentSide))
    with open(ime_datoteke) as f:
        for line in f:
            if(line.__contains__("DESNO")):
                currentSide = premik("R", currX, currY, currentSide)[2]
                rezSez.append((currX, currY, currentSide))
            if (line.__contains__("LEVO")):
                currentSide = premik("L", currX, currY, currentSide)[2]
                rezSez.append((currX, currY, currentSide))
            if(line.__contains__("NAPREJ")):
                moveLen = int(line.split()[1])
                currX = premik(moveLen, currX, currY, currentSide)[0]
                currY = premik(moveLen, currX, currY, currentSide)[1]
                rezSez.append((currX, currY, currentSide))
    return rezSez

def opisi_stanje(x, y, smer):
    returnStr = ""
    if x >= 100 or x <= -10:
        returnStr += str(x)
    elif x >= 10 or x <= -1:
        returnStr += " " + str(x)
    else:
        returnStr += "  " + str(x)

    returnStr += ":"

    if y >= 100 or y <= -10:
        returnStr += str(y)
    elif y >= 10 or y <= -1:
        returnStr += str(y) + " "
    else:
        returnStr += str(y) + "  "

    returnStr += " "

    if smer == "N":
        returnStr += "^"
    if smer == "E":
        returnStr += ">"
    if smer == "W":
        returnStr += "<"
    if smer == "S":
        returnStr += "v"

    return returnStr


def prevedi(ime_vhoda, ime_izhoda):
    seznamPremik = izvedi(ime_vhoda)
    newFile = open(ime_izhoda, 'w+')
    for currPremik in seznamPremik:
        newFile.write(opisi_stanje(currPremik[0], currPremik[1], currPremik[2]) + "\n")
    newFile.close()


def opisi_stanje_2(x, y, smer):
    returnStr = ""
    if smer == "N":
        returnStr += "^"
    if smer == "E":
        returnStr += ">"
    if smer == "W":
        returnStr += "<"
    if smer == "S":
        returnStr += "v"

    returnStr += " "

    getX = "(" + str(x)
    for i in range(len(getX), 4):
        returnStr += " "
    returnStr += getX + ":" + str(y) + ")"

    return returnStr




