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

# Obvezna naloga 1:
def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke)
    seznam_ukazov = []
    for vrstica in datoteka:
        vrstica = vrstica.strip()
        seznam_ukazov.append(vrstica)
    ukazi = [(0, 0, 'N')]
    i = 0
    while i < len(seznam_ukazov):
        for ukaz in seznam_ukazov:
            if ukaz == 'DESNO':
                ukaz = "R"
            elif ukaz == "LEVO":
                ukaz = "L"
            else:
                ukaz = ukaz.split()
                ukaz = int(ukaz[1])
            koord = ukazi[i]
            x = koord[0]
            y = koord[1]
            smer = koord[2]
            i += 1
            ukazi.append(premik(ukaz, x, y, smer))
        return ukazi

# Obvezna naloga 2:
def opisi_stanje(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    return("{:>3}:{:<3} {}".format(x, y, smer))

# Obvezna naloga 3:
def prevedi(ime_vhoda, ime_izhoda):
    ukazi = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in ukazi:
        opis = opisi_stanje(x, y, smer)
        datoteka.write(opis + "\n")
    datoteka.close()

# Dodatna naloga:
def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer = "^"
    if smer == "E":
        smer = ">"
    if smer == "S":
        smer = "v"
    if smer == "W":
        smer = "<"
    x = "(" + str(x)
    return("{}{:>5}:{})".format(smer, x, y))

