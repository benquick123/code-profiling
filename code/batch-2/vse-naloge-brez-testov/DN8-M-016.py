import os

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
    output = [(0, 0, 'N')]


    f=""
    if ".txt" in ime_datoteke:
        f = ime_datoteke
    else:
        f = ime_datoteke+".txt"
    file = open(f, "r")

    x, y, smer = 0, 0, "N"

    for line in file.readlines():
        vrstica = line.split(" ")

        command = vrstica[0][0]
        ukaz = ""
        naprej = 0
        if command == "D":
            ukaz = "R"
        elif command == "L":
            ukaz = "L"
        else:
            ukaz =  "N"
            naprej = int(vrstica[1])

        """
        if ukaz == "N":
            print(naprej, x, y, smer)
        else:
            print(ukaz, x, y, smer)
"""

        if ukaz == "N":
            x, y, smer = (premik(naprej, x, y, smer))
            output.append((x, y, smer))
        else:
            x, y, smer = (premik(ukaz, x, y, smer))
            output.append((x, y, smer))
    return output

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    puscice = "^>v<"

    ismer = smeri.index(smer)
    puscica = puscice[ismer]

    x = str(x)
    y = str(y)

    #   12:0   ^

    return "{:>3}:{:<4}{}".format(x, y, puscica)

def prevedi(ime_vhoda, ime_izhoda):

    if ".txt" not in ime_vhoda:
        ime_vhoda = ime_vhoda+".txt"

    if ".txt" not in ime_izhoda:
        ime_izhoda = ime_izhoda+".txt"

    i = open(ime_izhoda, "w")

    output = izvedi(ime_vhoda)

    for x, y, smer in output:
        #print(x, y, smer)
        i.write(opisi_stanje(x, y, smer) + "\n")

    i.close()

def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    puscice = "^>v<"

    ismer = smeri.index(smer)
    puscica = puscice[ismer]

    x = str(x)
    y = str(y)
    #^   (0:12)

    print(x)

    if (len(x) == 1):
        return "{:<4}({}:{})".format(puscica, x, y)
    elif (len(x) == 2):
        return "{:<3}({}:{})".format(puscica, x, y)
    elif (len(x) == 3):
        return "{:<2}({}:{})".format(puscica, x, y)


