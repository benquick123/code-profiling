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
    ukaz = []
    x = 0
    y = 0
    smer = 0
    smeri = "NESW"
    koraki = [(0, 0, "N")]
    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip()
        if "NAPREJ" in vrstica:
            vrstica = vrstica.split(" ")
            ukaz.append(int(vrstica[1]))
        else:
            ukaz.append(vrstica)
    for n in ukaz:
        if n == "DESNO":
            smer = smer+1
            if smer > 3:
                smer = 0
        elif n == "LEVO":
            smer = smer-1
            if smer < 0:
                smer = 3
        else:
            if smer == 0:
                y = y - n
            elif smer == 1:
                x = x + n
            elif smer == 2:
                y = y + n
            else:
                x = x - n
        koraki.append((x, y, smeri[smer]))
    return koraki



def opisi_stanje(x,y,smer):
    smeri = [("N","^"),("E",">"),("S","v"),("W","<")]
    for a,b in smeri:
        if a == smer:
            return "{x:>3}:{y:<3} {b}".format(x = x,y = y, b=b)

def prevedi(ime_vhoda, ime_izhoda):
    koraki = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for x,y,s in koraki:
        file.write("{}\n".format(opisi_stanje(x,y,s)))


def opisi_stanje_2(x, y, smer):
    z = ""
    for n in range(3 - len(str(x))):
        z = z + " "
    smeri = [("N","^"),("E",">"),("S","v"),("W","<")]
    for a,b in smeri:
        if a == smer:
            return "%s " % b + z + "(%d:%d)" % (x, y)


