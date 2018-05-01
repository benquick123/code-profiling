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
    seznam = [(0, 0, 'N')]
    for vrstica in datoteka:
        x, y, smer = seznam[-1]
        for ukaz in vrstica.split():
            if ukaz == "LEVO":
                seznam.append(premik("L", x, y, smer))
            if ukaz == "DESNO":
                seznam.append(premik("R", x, y, smer))
            if ukaz == "NAPREJ":
                seznam.append(premik(int(vrstica.split()[1]), x, y, smer))
    return seznam

def opisi_stanje(x, y, smer):
    dict = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return "{:>3}:{:<4}{}".format(x, y, dict[smer])

def prevedi(ime_vhoda, ime_izhoda):
    izhod = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        izhod.write(opisi_stanje(x, y, smer) + "\n")
    izhod.close()

def opisi_stanje_2(x, y, smer):
    dict = {"N": "^", "E": ">", "S": "v", "W": "<"}
    a = ("(" + str(x))
    return "{} {:>4}:{})".format(dict[smer], a, y)

