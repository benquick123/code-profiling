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
    datoteka = open(ime_datoteke)
    izpis = [(0,0,"N")]
    x = 0
    y = 0
    smer = "N"
    for vsak in datoteka:
        if vsak[0] == "D":
            izpis.append(premik("R", x, y, smer))
            x = premik("R", x, y, smer)[0]
            y = premik("R", x, y, smer)[1]
            smer = premik("R", x, y, smer)[2]
        elif vsak[0] == "L":
            izpis.append(premik("L", x, y, smer))
            x = premik("L", x, y, smer)[0]
            y = premik("L", x, y, smer)[1]
            smer = premik("L", x, y, smer)[2]
        else:
            nov = vsak.split()
            izpis.append(premik(int(nov[1]), x, y, smer))
            x = premik(int(nov[1]), x, y, smer)[0]
            y = premik(int(nov[1]), x, y, smer)[1]
            smer = premik(int(nov[1]), x, y, smer)[2]
    return izpis
print(izvedi("primer.txt"))

def opisi_stanje(x, y, smer):
    if smer == "N":
        smer2 = "^"
    elif smer == "E":
        smer2 = ">"
    elif smer == "S":
        smer2 = "v"
    elif smer == "W":
        smer2 = "<"
    return ("{:>3}:{:<3}{:>2}".format(x, y, smer2))
print(opisi_stanje(0, 12, "N")) #"  0:12  ^"

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for terka in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(terka[0], terka[1], terka[2]) + "\n")
print(prevedi("primer.txt", "stanja.txt"))

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        smer2 = "^"
    elif smer == "E":
        smer2 = ">"
    elif smer == "S":
        smer2 = "v"
    elif smer == "W":
        smer2 = "<"
    return ("{:<2}{:>4}:{})".format(smer2, "(" + str(x), y))
print(opisi_stanje_2(0, 12, "N")) #"^   (0:12)"

