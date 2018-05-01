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
    datoteka = open(ime_datoteke)
    x = 0
    y = 0
    smer = "N"
    s = [(x, y, smer)]
    for vrstica in datoteka:
        if "DESNO" in vrstica:
            s.append(premik("R",x,y,smer))
            t = (premik("R",x,y,smer))
            x,y,smer = t

        elif "LEVO" in vrstica:
            s.append(premik("L",x,y,smer))
            t = (premik("L",x,y,smer))
            x,y,smer = t
        else:
            ukaz = int(vrstica[7:])
            t = (premik(ukaz,x,y,smer))
            x,y,smer = t
            s.append(t)
    return s

def opisi_stanje(x,y,smer):
    str(x)
    str(y)
    s = "{:>3}:{:<3} {}"
    if smer == "N":
        a = "^"
    if smer =="E":
        a = ">"
    if smer =="S":
        a = "v"
    if smer =="W":
        a = "<"
    return s.format(x,y,a)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda,"w")
    a = izvedi(ime_vhoda)
    for x,y,smer in a:
        b = opisi_stanje(x,y,smer)
        datoteka.write(b)
        datoteka.write("\n")

