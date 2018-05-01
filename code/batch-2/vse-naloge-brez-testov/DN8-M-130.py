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
    i = 0
    seznam = [(0, 0, "N")]
    for vrstica in datoteka:
        if vrstica.strip() == "DESNO":
            x, y, smer = seznam[i]
            seznam.append(premik("R",x, y, smer ))
        elif vrstica.strip() == "LEVO":
            x, y, smer = seznam[i]
            seznam.append(premik("L",x, y, smer ))
        else:
            a = vrstica.strip().split()
            b= int(a[1])
            x, y, smer = seznam[i]
            seznam.append(premik(b, x, y, smer ))
        i +=1
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        return"{:>3}:{:<3} {}".format(x, y, "^")
    elif smer == "E":
        return"{:>3}:{:<3} {}".format(x, y, ">")
    elif smer == "S":
        return"{:>3}:{:<3} {}".format(x, y, "v")
    elif smer == "W":
        return"{:>3}:{:<3} {}".format(x, y, "<")

def prevedi(ime_vhoda, ime_izhoda):

    polja = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in polja:
        datoteka.write("{}\n".format(opisi_stanje(x, y, smer)))
    datoteka.close()


