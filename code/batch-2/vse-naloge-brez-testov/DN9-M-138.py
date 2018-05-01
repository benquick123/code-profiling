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

#Obvezne naloge
def izvedi(ime_datoteke):
    primer = open(ime_datoteke)
    navodila = primer.read()
    terka = (0, 0, "N")
    seznam_terk = [terka]
    for ukaz in navodila.split():
        if ukaz == "DESNO":
            ukaz = "R"
        elif ukaz == "LEVO":
            ukaz = "L"
        elif not ukaz.isalpha():
            ukaz = int(ukaz)
        else:
            continue
        terka = (premik(ukaz, terka[0], terka[1], terka[2]))
        seznam_terk.append(terka)
    return seznam_terk
    primer.close()

def opisi_stanje(x,y,smer):
    if smer == "N":
        smer = "^"
    elif smer == "E":
        smer = ">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer = "<"
    koordinate =  "{:>3}:{:<3}".format(x,y)
    return koordinate + " " + smer

def prevedi(ime_vhoda, ime_izhoda):
    vhod = open(ime_vhoda)
    izhod = open(ime_izhoda, "w")
    for x,y,smer in izvedi(ime_vhoda):
        izhod.write(opisi_stanje(x,y,smer)+"\n")

