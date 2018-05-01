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
    sky="NESW"
    x=y=smer=0
    r = [(x, y,sky[0])]
    dat = open(ime_datoteke)
    ukazi = dat.read().split("\n")
    dat.close()
    for ukaz in ukazi:
        if ukaz == "LEVO":
            smer = (smer + 3) % 4
            r.append((x, y, sky[smer]))
        elif ukaz == "DESNO":
            smer = (smer + 1) % 4
            r.append((x, y, sky[smer]))
        elif ukaz.split(" ")[0] == "NAPREJ":
            razdalja = int(ukaz.split(" ")[1])
            x += (smer % 2) * (2 - smer) * razdalja
            y += (1 - smer % 2) * (smer - 1) * razdalja
            r.append((x, y, sky[smer]))
    return r

def opisi_stanje(x, y, smer):
    pos = {"N":"^","E":">","S":"v","W":"<"}
    ret = "{:>3}:{:<3} {}"
    return ret.format(x,y,pos[smer])

def prevedi(ime_vhoda, ime_izhoda):
    r = izvedi(ime_vhoda)
    s = open(ime_izhoda,"w")
    for x,y,z in r:
        s.write(opisi_stanje(x,y,z)+"\n")

def opisi_stanje_2(x, y, smer):
    pos = {"N":"^","E":">","S":"v","W":"<"}
    ret = "{}{}({}:{})"
    return ret.format(pos[smer],(4-len(str(x)))*" ",x,y)



