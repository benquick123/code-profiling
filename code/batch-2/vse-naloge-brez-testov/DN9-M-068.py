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

def angleski(ime_datoteke):
    t = open(ime_datoteke, encoding="utf - 8")
    s = t.read().split()
    popsez = []
    for i, x in enumerate(s):
        if x[0] == "D":
            popsez.append("R")
        if x[0] == "L":
            popsez.append(x[0])
        if x[0] == "N":
            popsez.append(s[i + 1])
    return popsez

def izvedi(ime_datoteke):
    x, y, smer = 0, 0, "N"
    stanja = []
    stanja.append((x, y, smer))
    for e in angleski(ime_datoteke):
        if e == "R" or e == "L":
            ukaz = e
        else:
            ukaz = int(e)
        stanja.append(premik(ukaz, x, y, smer))
        x, y, smer = premik(ukaz, x, y, smer)
    return stanja

def opisi_stanje(x, y, smer):
    s = {"N" : "^", "E" : ">",
        "S" : "v", "W" : "<" }
    return "{:>3}:{:<3}{:>2}".format(x,y,s[smer])

def prevedi(ime_vhoda, ime_izhoda):
    t = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        t.write(opisi_stanje(x, y, smer) + "\n")
    t.close()

def opisi_stanje_2(x, y, smer):
    s = {"N" : "^", "E" : ">",
            "S" : "v", "W" : "<"}
    if 99 > x > 9 or x < 0:
        return "{:<3}({:}:{:>})".format(s[smer], x ,y)
    if x > 99:
        return "{:<2}({:}:{:>})".format(s[smer], x ,y)
    else:
        return "{:<4}({:}:{:>})".format(s[smer], x ,y)



