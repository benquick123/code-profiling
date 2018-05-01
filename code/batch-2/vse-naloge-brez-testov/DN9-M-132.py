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
    stanja = [(0, 0, "N")]
    file = open(ime_datoteke, "r")
    for line in file:
        x, y, smer = stanja[-1][0], stanja[-1][1], stanja[-1][2]
        if line.startswith("DESNO"):
            stanja.append(premik("R", x, y, smer))
        elif line.startswith("LEVO"):
            stanja.append(premik("L", x, y, smer))
        elif line.startswith("NAPREJ"):
            velikost_premika = int(line.split()[1])
            stanja.append(premik(velikost_premika, x, y, smer))
    file.close()
    return stanja

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    preslikave = "^>v<"
    znak_smeri = preslikave[smeri.index(smer)]
    return "{x:3}:{y:<4}{smer}".format(x=x, y=y, smer=znak_smeri)

def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    izhodna_datoteka = open(ime_izhoda, "w")
    for x, y, smer in stanja:
        izhodna_datoteka.write(opisi_stanje(x, y, smer) + "\n")
    izhodna_datoteka.close()

def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    preslikave = "^>v<"
    x_str = "(" + str(x)
    y_str = str(y) + ")"
    znak_smeri = preslikave[smeri.index(smer)]
    return "{smer}{x:>5}:{y}".format(smer=znak_smeri, x=x_str, y=y_str)



