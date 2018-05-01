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
    ukazi = {"DESNO":"R", "LEVO":"L"}
    dat = open(ime_datoteke)
    for ukaz in dat:
        ukaz = ukaz.strip()
        if ukaz in ukazi:
            stanja.append(premik(ukazi[ukaz], stanja[-1][0], stanja[-1][1], stanja[-1][2]))
        else:
            stanja.append(premik(int(ukaz.split()[1]), stanja[-1][0], stanja[-1][1], stanja[-1][2]))
    return stanja

def opisi_stanje(x, y, smer):
    return "{:>3}:{:<3} {}".format(x, y, {"N":"^", "E":">", "S":"v", "W":"<"}[smer])

def prevedi(ime_vhoda, ime_izhoda):
    dat = open(ime_izhoda,"w")
    for x, y, smer in izvedi(ime_vhoda):
       dat.write(opisi_stanje(x, y, smer)+"\n")
    dat.close()

def opisi_stanje_2(x, y, smer):
    stanje = {"N":"^", "E":">", "S":"v", "W":"<"}
    return "{}{:>5}:{})".format(stanje[smer], "("+str(x), y)

