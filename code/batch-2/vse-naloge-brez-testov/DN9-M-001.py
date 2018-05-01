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
    file1 = open(ime_datoteke)
    path = [(0,0, 'N')]
    c = 0
    for line in file1:
        if line.split()[0] == "DESNO":
            path.append(premik('R', path[c][0], path[c][1], path[c][2]))
        elif line.split()[0] == "LEVO":
            path.append(premik('L', path[c][0], path[c][1], path[c][2]))
        else:
            num = line.split()[1]
            path.append(premik(int(num), path[c][0], path[c][1], path[c][2]))
        c += 1
    file1.close()
    return path

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{0:>3}:{1:<3}{2:>2}".format(x, y, "^")
    elif smer == "E":
        return "{0:>3}:{1:<3}{2:>2}".format(x, y, ">")
    elif smer == "S":
        return "{0:>3}:{1:<3}{2:>2}".format(x, y, "v")
    elif smer == "W":
        return "{0:>3}:{1:<3}{2:>2}".format(x, y, "<")

def prevedi(ime_vhoda, ime_izhoda):
    file1 = open(ime_izhoda, 'w')
    for x, y, smer in izvedi(ime_vhoda):
        file1.write("{0}".format(opisi_stanje(x, y, smer)))
        file1.write("\n")
    file1.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return "{0:<4}({1}:{2:>2})".format("^", x, y)
    elif smer == "E":
        return "{0:<2}({1}:{2:>1})".format(">", x, y)
    elif smer == "S":
        return "{0:<3}({1}:{2:>2})".format("v", x, y)
    elif smer == "W":
        return "{0:<4}({1}:{2:>1})".format("<", x, y)






