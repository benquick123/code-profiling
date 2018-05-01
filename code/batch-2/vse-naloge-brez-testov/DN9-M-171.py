def prevedi(ime_vhoda, ime_izhoda):
    preberi = izvedi(ime_vhoda)
    pisi = open(ime_izhoda, "w")

    for element in preberi:
        x,y,smer = element
        stanje = opisi_stanje(x,y,smer)
        pisi.write(stanje+"\n")

    pisi.close()


def opisi_stanje(x, y, smer):
    kam = None
    if smer == "N":
        kam = "^"
    if smer == "S":
        kam = "v"
    if smer == "W":
        kam = "<"
    if smer == "E":
        kam = ">"
    vrni = "{:3}:{:<4}{}".format(x,y,kam)
    return vrni





def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke)
    x = 0
    y = 0
    smer = "N"

    vrni = [(0,0,"N")]
    for vrstica in datoteka:
        uredi = vrstica.strip("\n")
        sezv = vrstica.split()
        if sezv[0] == "DESNO":
            ukaz = "R"
            x,y,smer = premik(ukaz,x,y,smer)
            vrni.append((x,y,smer))
        if sezv[0] == "LEVO":
            ukaz = "L"
            x, y, smer = premik(ukaz, x, y, smer)
            vrni.append((x, y, smer))
        if sezv[0] == "NAPREJ":
            ukaz = int(sezv[1])
            x, y, smer = premik(ukaz, x, y, smer)
            vrni.append((x, y, smer))

    datoteka.close()
    return vrni



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


