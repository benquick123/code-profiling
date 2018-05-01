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
    list = []
    list.append(premik(0, x, y, smer))

    s = [line.rstrip('\n') for line in open(ime_datoteke)]

    for i in s:
        if " " in i:
            a, b = i.split(" ")
            b = int(b)


            if smer == "N":
                list.append(premik(b, x, y, smer))
                y = y - b
            elif smer == "S":
                list.append(premik(b, x, y, smer))
                y = y + b
            elif smer == "W":
                list.append(premik(b, x, y, smer))
                x = x - b
            elif smer == "E":
                list.append(premik(b, x, y, smer))
                x = x + b

        else:
            if smer == "N":
                if i == "DESNO":
                    smer = "E"
                elif i == "LEVO":
                    smer = "W"
            elif smer == "E":
                if i == "DESNO":
                    smer = "S"
                elif i == "LEVO":
                    smer = "N"
            elif smer == "S":
                if i == "DESNO":
                    smer = "W"
                elif i == "LEVO":
                    smer = "E"
            elif smer == "W":
                if i == "DESNO":
                    smer = "N"
                elif i == "LEVO":
                    smer = "S"

            list.append(premik(0, x, y, smer))
    return list

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    elif smer == "S":
        smer = "v"
    elif smer == "E":
        smer = ">"
    elif smer == "W":
        smer = "<"

    return("{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer=smer))

def prevedi(ime_vhoda, ime_izhoda):
    #datoteka = open(ime_izhoda, "w")
    s = izvedi(ime_vhoda)

    with open(ime_izhoda, "w") as datoteka:
        for i in s:
            x, y, smer = i
            datoteka.write(opisi_stanje(x, y, smer) + "\n")
    datoteka.close()

