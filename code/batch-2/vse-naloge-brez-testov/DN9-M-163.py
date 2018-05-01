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
    ukazi = datoteka.read().splitlines()
    x = 0
    y = 0
    zac_vrednost = 'N'
    s = [(x, y, zac_vrednost)]
    for vrstica in ukazi:
        if vrstica == 'DESNO':
            ukaz = 'R'
        elif vrstica == 'LEVO':
            ukaz = 'L'
        else:
            ukaz = int(vrstica.split()[1])
        x, y, zac_vrednost = premik(ukaz, x, y, zac_vrednost)
        s.append((x, y, zac_vrednost))

    return s
def opisi_stanje(x, y, smer):
    if smer == "N":
        ukaz = "^"
    elif smer == "W":
        ukaz = "<"
    elif smer == "E":
        ukaz = ">"
    else:
        ukaz = "v"

    return ("{:>3}:{:<3} {}".format(x,y,ukaz))

def prevedi(ime_vhoda, ime_izhoda):
    seznam = izvedi(ime_vhoda)
    odpri = open(ime_izhoda, "w")
    for x,y,smer in seznam:
        odpri.write(opisi_stanje(x,y,smer)+ "\n")
    odpri.close()




