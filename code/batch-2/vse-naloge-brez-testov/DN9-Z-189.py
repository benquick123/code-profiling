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
    pot=[(0,0,"N")]
    for vrstica in open(ime_datoteke):
        if vrstica=="DESNO\n":
            pot.append((premik("R", pot[-1][0], pot[-1][1], pot[-1][2])))
        elif vrstica=="LEVO\n":
            pot.append((premik("L", pot[-1][0], pot[-1][1], pot[-1][2])))
        else:
            p=int(vrstica.split()[1])
            pot.append((premik(p,pot[-1][0], pot[-1][1], pot[-1][2])))
    return pot

def opisi_stanje(x, y, smer):
    if smer=="N":
        smer="^"
    elif smer=="E":
        smer=">"
    elif smer == "S":
        smer ="v"
    elif smer == "W":
        smer ="<"
    return "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    t=izvedi(ime_vhoda)
    shrani = open(ime_izhoda, "wt")
    for e in t:
        shrani.write(opisi_stanje(e[0], e[1], e[2]) + "\n")

####Dodatna naloga#####

def opisi_stanje_2(x, y, smer):
    if smer=="N":
        smer="^"
    elif smer=="E":
        smer=">"
    elif smer == "S":
        smer ="v"
    elif smer == "W":
        smer ="<"
    koordinata_x="({:}".format(x)
    return "{} {:>4}:{})".format(smer, koordinata_x, y)

