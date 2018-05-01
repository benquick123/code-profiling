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
    stanja=[(0, 0, "N")]
    datoteka=open(ime_datoteke)
    x, y = 0, 0
    smer="N"
    for vrstica in datoteka:
        if "DESNO"in vrstica:
            h=premik("R", x, y, smer)
            stanja.append(h)
            smer = list(h)[2]
        if "LEVO" in vrstica:
            h=premik("L", x, y, smer)
            stanja.append(h)
            smer = list(h)[2]
        if "NAPREJ" in vrstica:
            vrstica=vrstica.strip()
            vrstica=vrstica.strip("NAPREJ")
            if smer == "N" or smer == "S":
                h = premik(int(vrstica), x, y, smer)
                stanja.append(h)
                smer = list(h)[2]
                if y!=list(h)[1]:
                    y += list(h)[1]-y
            if smer == "E" or smer=="W":
                h = premik(int(vrstica), x, y, smer)
                smer = list(h)[2]
                stanja.append(h)
                if x!=list(h)[0]:
                    x += list(h)[0]-x
    return stanja

def opisi_stanje(x, y, smer):
    if smer=="N":
        z="^"
    if smer=="E":
        z=">"
    if smer=="S":
        z="v"
    if smer=="W":
        z="<"
    return "{:3}:{:<3} {}".format(x, y, z)

def prevedi(ime_vhoda, ime_izhoda):
    vhod=open(ime_vhoda)
    seznam=izvedi(ime_vhoda)
    izhod=open(ime_izhoda, "w")
    for x, y, smer in seznam:
        izhod.write(opisi_stanje(x, y, smer)+"\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    x="("+str(x)
    if smer=="N":
        z="^"
    if smer=="E":
        z=">"
    if smer=="S":
        z="v"
    if smer=="W":
        z="<"
    return "{}{:>5}:{})".format(z, x, y)

