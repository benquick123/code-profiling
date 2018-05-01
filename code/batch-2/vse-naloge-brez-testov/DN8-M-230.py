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
    x,y = 0,0
    smer = "N"
    pot = [(x,y,smer)]
    file = open(ime_datoteke)
    for i in file:
        i = i.strip()
        if i == "DESNO":
            ukaz = "R"
            x,y,smer = premik(ukaz,x,y,smer)
            pot.append((x,y,smer,))
        elif i == "LEVO":
            ukaz = "L"
            x, y, smer = premik(ukaz, x, y, smer)
            pot.append((x, y, smer,))
        elif i[:6] == "NAPREJ":
            ukaz = int(i[7:])
            x, y, smer = premik(ukaz, x, y, smer)
            pot.append((x, y, smer,))
    file.close()
    return pot

def opisi_stanje(x,y,smer):
    return ("{:>3}:{:<3} {}".format(x,y,("^" if smer == "N" else "v" if smer == "S" else ">" if smer == "E" else "<")))

def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x,y,smer in s:
        datoteka.write(opisi_stanje(x,y,smer) + "\n")
    datoteka.close()

#There's a fundamental truth to our nature
#Man must explore
#~David R. Scott

def opisi_stanje_2(x,y,smer):
    return ("{} {:>4}:{:<2}".format(("^" if smer == "N" else "v" if smer == "S" else ">" if smer == "E" else "<"), "(" + str(x),str(y) + ")"))

