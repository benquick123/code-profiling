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
    datoteka = open(ime_datoteke,"r")
    for vrstica in datoteka:
        vrstica = vrstica.strip().split()
        if len(vrstica)>1:
            ukaz = int(vrstica[1])
        else:
            if vrstica[0] == "DESNO":
                ukaz = "R"
            if vrstica[0] == "LEVO":
                ukaz = "L"
        seznam.append(premik(ukaz,x,y,smer))
        x = premik(ukaz,x,y,smer)[0]
        y = premik(ukaz, x, y, smer)[1]
        smer = premik(ukaz, x, y, smer)[2]
    return seznam

def opisi_stanje(x, y, smer):
     smeri = "NESW"
     smeri1 = "^>v<"
     ismer = smeri.index(smer)
     return "{:>3}:{:<3} {}".format(x,y,smeri1[ismer])

def prevedi(ime_vhoda, ime_izhoda):
    nova = open(ime_izhoda,"w")
    pot = izvedi(ime_vhoda)
    for (x,y,smer) in pot:
        nova.write("{}\n".format(opisi_stanje(x,y,smer)))

def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    smeri1 = "^>v<"
    ismer = smeri.index(smer)
    return "{}{:>5}:{})".format(smeri1[ismer],"("+str(x), y, )

