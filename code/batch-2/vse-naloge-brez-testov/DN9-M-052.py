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
    pot = [(0, 0, "N")]
    x, y, smer = 0, 0, "N"
    datoteka = open(ime_datoteke)
    for element in datoteka:
        if element.strip() == "DESNO":
            pot.append(premik("R", x, y, smer))
            x, y, smer = premik("R", x, y, smer)
        elif element.strip() == "LEVO":
            pot.append(premik("L", x, y, smer))
            x, y, smer = premik("L", x, y, smer)
        else:
            naprej = element.strip()
            ukaz = int(naprej.split(" ")[1])
            pot.append(premik(ukaz, x, y, smer))
            x, y, smer = premik(ukaz, x, y, smer)
    return pot

def opisi_stanje(x, y, smer):
    smeri = {"N":"^","W":"<","S":"v","E":">"}
    levaStran = str(x).rjust(3)
    desnaStran = str(y).ljust(3)
    return (levaStran+":"+desnaStran+" "+smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x, y, smer)+"\n")
    datoteka.close()

