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
    x = 0
    y = 0
    smer = "N"
    seznam = [premik(0, x, y, smer)]
    for vrstica in datoteka:
        if vrstica.strip() == "DESNO":
            temp = premik("R", x, y, smer)
            seznam.append(temp)
            x, y, smer = temp
        elif vrstica.strip() == "LEVO":
            temp = premik("L", x, y, smer)
            seznam.append(temp)
            x, y, smer = temp
        else:
            temp = premik(int(vrstica.strip().split(" ")[1]), x, y, smer)
            seznam.append(temp)
            x, y, smer = temp
    datoteka.close()
    return seznam

def opisi_stanje(x, y, smer):
    niz = "{x:>3}:{y:<3} {smer}"
    if smer == "N":
        niz = niz.format(x=x, y=y, smer="^")
    elif smer == "E":
        niz = niz.format(x=x, y=y, smer=">")
    elif smer == "S":
        niz = niz.format(x=x, y=y, smer="v")
    else:
        niz = niz.format(x=x, y=y, smer="<")
    return niz

def prevedi(ime_vhoda, ime_izhoda):
    izv = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for el in izv:
        datoteka.write(opisi_stanje(el[0], el[1], el[2]))
        datoteka.write("\n")
    datoteka.close()
    return None

def opisi_stanje_2(x, y, smer):
    niz = "{smer} {x:>4}:{y}"
    if smer == "N":
        niz = niz.format(smer="^", x="("+str(x), y=str(y)+")")
    elif smer == "E":
        niz = niz.format(smer=">", x="(" + str(x), y=str(y)+")")
    elif smer == "S":
        niz = niz.format(smer="v", x="(" + str(x), y=str(y)+")")
    else:
        niz = niz.format(smer="<", x="(" + str(x), y=str(y)+")")
    return niz

