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
    rez = [(0,0,'N')]
    x, y, smer = 0, 0, 'N'
    file = open(ime_datoteke)
    text = file.read()
    for ukaz in text.split():
        if (ukaz == "DESNO"):
            x, y, smer = premik("R", x, y, smer)
            rez.append((x, y, smer))
        if (ukaz == "LEVO"):
            x, y, smer = premik("L", x, y, smer)
            rez.append((x, y, smer))
        if (ukaz.isdigit()):
            x, y, smer = premik(int(ukaz), x, y, smer)
            rez.append((x, y, smer))
    return rez

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    smeri2 = "^>v<"
    return "{:>3}:{:<3} {}".format(x,y,smeri2[smeri.find(smer)])

def prevedi(ime_vhoda, ime_izhoda):
    pot=izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x,y,smer in pot:
        datoteka.write(opisi_stanje(x,y,smer)+"\n")
    datoteka.close()

