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
    datoteka = open(ime_datoteke).read()
    prazen_seznam = []                      #prazen_seznam = datoteka.split() - krajša varianta
    prazen_seznam = datoteka.splitlines()
    res_seznam = []

    x1, y1, smer1 = (0,0,"N")
    res_seznam.append(( x1, y1, smer1))

    for i in prazen_seznam:
        if i == "DESNO":
            ukaz = "R"

        elif i == "LEVO":
            ukaz = "L"

        else:
            ukaz = int(i.split()[1])

        x1, y1, smer1 = premik(ukaz, x1, y1, smer1)

        res_seznam.append((x1, y1, smer1))

    return res_seznam


def opisi_stanje(x,y,smer):
    if smer == "N":            # sever
        nova = "^"
    if smer == "E":            # vzhod
        nova = ">"
    if smer == "S":            # jug
        nova = "v"
    if smer == "W":            # zahod
        nova = "<"

    return "{:>3}:{:<3} {}".format(x, y, nova)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = izvedi(ime_vhoda)
    nova_dat = open(ime_izhoda, "w")
    for i in datoteka:
        nova_dat.write(opisi_stanje(i[0],i[1],i[2])+"\n")

# Dodatna naloga:
def opisi_stanje_2(x, y, smer):
    if smer == "N":            # sever
        nova = "^"
    if smer == "E":            # vzhod
        nova = ">"
    if smer == "S":            # jug
        nova = "v"
    if smer == "W":            # zahod
        nova = "<"

    xokl = "("+str(x)
    return "{} {:>4}:{})".format(nova,xokl,y)




