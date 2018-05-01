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
    seznam = []
    x = 0
    y = 0
    smer = "N"
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        s = vrstica.split(" ")
        if len(s) == 1:
            if s[0][0] == "D":
                seznam.append((x, y, smer))
                z = premik("R", x, y, smer)
                x, y, smer = z
            else:
                seznam.append((x, y, smer))
                l = premik("L", x, y, smer)
                x, y, smer = l
        else:
            seznam.append((x,y,smer))
            re = int(s[1])
            n = premik(re, x, y, smer)
            x, y, smer = n
    seznam.append((x, y, smer))
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:>3}:{:<3} ^".format(x, y)
    if smer == "S":
        return "{:>3}:{:<3} v".format(x, y)
    if smer == "W":
        return "{:>3}:{:<3} <".format(x, y)
    if smer == "E":
        return "{:>3}:{:<3} >".format(x, y)

def prevedi(ime_vhoda, ime_izhoda):
    file = open(ime_izhoda, "w")
    for e in izvedi(ime_vhoda):
        file.write(opisi_stanje(e[0], e[1], e[2]) + "\n")

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return "^ {:>4}:{}".format("(" + str(x), str(y) + ")")
    if smer == "S":
        return "v {:>4}:{}".format("(" + str(x), str(y) + ")")
    if smer == "W":
        return "< {:>4}:{}".format("(" + str(x), str(y)+ ")")
    if smer == "E":
        return "> {:>4}:{}".format("(" + str(x), str(y) + ")")


