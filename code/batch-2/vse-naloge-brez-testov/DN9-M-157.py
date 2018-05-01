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
    o = open(ime_datoteke)
    o = o.readlines()
    z = (0,0,"N")
    l = [z]
    x,y = 0,0
    smer = "N"
    smeri = "NESW"
    ismer = smeri.index(smer)
    for u in o:
        if u == "DESNO\n":
            t_u = "R"
            l.append(premik(t_u,x,y,smer))
            x,y,smer = premik(t_u,x,y,smer)
        elif u == "LEVO\n":
            t_u = "L"
            l.append(premik(t_u,x,y,smer))
            x, y, smer = premik(t_u, x, y, smer)
        elif u[:6] == "NAPREJ":
            t_u = int(u[-3:])
            l.append(premik(t_u, x, y, smer))
            x, y, smer = premik(t_u, x, y, smer)
    return l

def opisi_stanje(x,y,smer):
    if smer == "N":
        s = " ^"
    elif smer == "E":
        s = " >"
    elif smer == "S":
        s = " v"
    elif smer == "W":
        s = " <"
    return "{:3}:{:<3}{}".format(x, y, s)

def prevedi(ime_vhoda, ime_izhoda):
    v = open(ime_vhoda, "r")
    o = open(ime_izhoda, "w")
    for t in izvedi(ime_vhoda):
        o.write(opisi_stanje(t[0], t[1], t[2]) + "\n")



