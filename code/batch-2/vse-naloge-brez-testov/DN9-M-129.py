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
    x=0
    y=0
    smer="N"
    t=[]
    t.append((x,y,smer))
    z=open(ime_datoteke,encoding = "utf-8")
    for vrstica in z:
        if "DESNO" in vrstica:
            ukaz = "R"
        if "LEVO" in vrstica:
            ukaz = "L"
        if "NAPREJ" in vrstica:
            vrstica = vrstica.split()
            ukaz = int(vrstica[1])
        x,y,smer=premik(ukaz,x,y,smer)
        t.append((x,y,smer))
    z.close()
    return t

def opisi_stanje(x,y,smer):
    if smer=="N":
        smer="^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    return "{:>3}:{:<4}{}".format(x,y,smer)

def prevedi(ime_vhoda, ime_izhoda):
    t=izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for e in t:
        datoteka.write(opisi_stanje(e[0],e[1],e[2])+"\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer=="N":
        smer="^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    x="("+str(x)
    return "{}{:>5}:{:>})".format(smer,x,y)

