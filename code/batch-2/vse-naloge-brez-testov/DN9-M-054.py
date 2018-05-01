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
    smer = "N"
    x = y = 0
    fajl = open(ime_datoteke, "r")
    moves = [(x, y, "N")]
    for line in fajl:
        lajn = line.split()
        if lajn[0] == "DESNO":
            moves.append(premik("R", x, y, smer))
            x, y, smer = premik("R", x, y, smer)
        elif lajn[0] == "LEVO":
            moves.append(premik("L", x, y, smer))
            x, y, smer = premik("L", x, y, smer)
        else:
            moves.append(premik(int(lajn[1]), x, y, smer))
            x, y, smer = premik(int(lajn[1]), x, y, smer)
    fajl.close()
    return moves

def opisi_stanje(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return "{x:>3}:{y:<3}{s:>2}".format(x=x, y=y, s=smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    outfile = open(ime_izhoda, "w")
    for line in izvedi(ime_vhoda):
        x, y, smer = line
        outfile.write(opisi_stanje(x, y, smer) + "\n")
    outfile.close()

def opisi_stanje_2(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    x_string = "("+str(x)
    return "{s:<2}{x:>4}:{y})".format(s=smeri[smer], x=x_string, y=y)


