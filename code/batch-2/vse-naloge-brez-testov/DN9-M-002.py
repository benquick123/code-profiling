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
    seznam = [(0,0,"N")]
    x = 0
    y = 0
    smer = "N"
    datoteka2 = open(ime_datoteke)
    for vrstica in datoteka2:
        vrstica = vrstica.split()
        if vrstica[0] == 'DESNO':
            seznam.append(premik("R", x, y, smer))
            x,y,smer = premik("R",x,y,smer)
        elif vrstica[0] == "LEVO":
            seznam.append(premik("L", x, y, smer))
            x, y, smer = premik("L", x, y, smer)
        elif vrstica[0] == "NAPREJ":
            seznam.append(premik(int(vrstica[1]), x, y, smer))
            x, y, smer = premik(int(vrstica[1]), x, y, smer)
    return seznam

def opisi_stanje(x,y,smer):
    znak = ""
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    elif smer == "W":
        znak = "<"

    s = "{:>3}:{:<3} {}"
    return(s.format(x,y,znak))

def prevedi(ime_vhoda, ime_izhoda):
    file = open(ime_izhoda,"w")
    seznam = izvedi(ime_vhoda)
    for x,y,smer in seznam:
        file.write(opisi_stanje(x,y,smer)+"\n")
    file.close()



