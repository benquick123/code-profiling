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

def izvedi(file):
    zacetek = [(0, 0,"N")]
    st = 0
    data = open(file)
    for vrstica in data:
        x1 = zacetek[st][0]
        y1 = zacetek[st][1]
        v = vrstica.split()[0]
        if v == "DESNO":
            zacetek.append(premik("R",x1,y1,zacetek[st][2]))
        elif v == "LEVO":
            zacetek.append(premik("L",x1,y1,zacetek[st][2]))
        else:
            korak = int(vrstica.split()[1])
            zacetek.append(premik(korak,x1,y1,zacetek[st][2]))
        st += 1
    return zacetek

def opisi_stanje(x,y,smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    else:
        smer = "<"
    return("{:3}:{:<3} {}".format(x, y, smer))

def prevedi(ime_vhoda,ime_izhoda):
    dat = open(ime_izhoda, "w")
    for data in izvedi(ime_vhoda):
        dat.write("{}\n".format(opisi_stanje(data[0], data[1], data[2])))
    dat.close()

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    else:
        smer = "<"
    print ("{} {}({}:{:<}){}".format(smer, " "*(3-len(str(x))),x , y, " "*(1-len(str(y)))))
    return ("{} {}({}:{:<}){}".format(smer, " "*(3-len(str(x))),x , y, " "*(1-len(str(y)))))






