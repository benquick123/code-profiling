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
    pot = [(0, 0, 'N')]
    x = 0
    y = 0
    smer = "N"

    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        if vrstica.split()[0] == "DESNO":
            p = premik("R", x, y, smer)
            pot.append(p)
            x = p[0]
            y = p[1]
            smer = p[2]
        elif vrstica.split()[0] == "LEVO":
            p = premik("L", x, y, smer)
            pot.append(p)
            x = p[0]
            y = p[1]
            smer = p[2]
        elif vrstica.split()[0] == "NAPREJ":
            p = premik(int(vrstica.split()[1]), x, y, smer)
            pot.append(p)
            x = p[0]
            y = p[1]
            smer = p[2]
    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:>3}:{:<3} ^".format(x, y)
    elif smer == "E":
        return "{:>3}:{:<3} >".format(x, y)
    elif smer == "S":
        return "{:>3}:{:<3} v".format(x, y)
    elif smer == "W":
        return "{:>3}:{:<3} <".format(x, y)

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    print(datoteka)

    for element in seznam:
        datoteka.write(opisi_stanje(element[0], element[1], element[2]) + '\n')
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        oklepaj_in_x = "(" + str(x)
        return "^ {:>4}:{})".format(oklepaj_in_x, y)
    elif smer == "E":
        oklepaj_in_x = "(" + str(x)
        return "> {:>4}:{})".format(oklepaj_in_x, y)
    elif smer == "S":
        oklepaj_in_x = "(" + str(x)
        return "v {:>4}:{})".format(oklepaj_in_x, y)
    elif smer == "W":
        oklepaj_in_x = "(" + str(x)
        return "< {:>4}:{})".format(oklepaj_in_x, y)


#PRINT

ime_datoteke = "primer.txt"
print(izvedi(ime_datoteke))

print(opisi_stanje(0, 12, "N"))

ime_vhoda = "ukazi.txt"
ime_izhoda = "stanja.txt"
print(prevedi(ime_vhoda, ime_izhoda))

print(opisi_stanje_2(0, 3, "N"))


#TESTI

