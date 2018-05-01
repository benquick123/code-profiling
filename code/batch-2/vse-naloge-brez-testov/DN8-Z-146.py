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

def izvedi(ime):
    datoteka = open(ime)
    start = (0, 0, "N")
    result = [start]
    for row in datoteka:
        x = row.split(" ")
        if x[0][:-1] == "DESNO":
            ukaz = "R"
        if x[0][:-1] == "LEVO":
            ukaz = "L"
        if x[0] == "NAPREJ":
            ukaz = int(x[1][:-1])
        start = premik(ukaz, start[0], start[1], start[2])
        result.append(start)
    return result

def opisi_stanje(x, y, smer):
    smeri1 = "NESW"
    smeri2 = "^>v<"
    z = smeri2[smeri1.index(smer)]
    c = "{x:>3}:{y:<3} ".format(x = x, y = y) + z
    return c

def prevedi(ime_vhoda, ime_izhoda):
    x = izvedi(ime_vhoda)
    y = []
    for a, b, smer in x:
        y.append(opisi_stanje(a, b, smer))
    datoteka = open(ime_izhoda, "w")
    for c in y:
        datoteka.write(c + "\n")
    datoteka.close()
    return



