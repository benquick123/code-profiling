def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * int(ukaz[7:])
        y += dy * int(ukaz[7:])
    return x, y, smer

def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke)
    ukazi = [(0, 0, "N")]
    i = 0
    for ukaz in datoteka:
        ukazi.append(premik(ukaz.strip(), ukazi[i][0], ukazi[i][1], ukazi[i][2]))
        i += 1
    return ukazi

def opisi_stanje(x, y, smer):
    znaki = {'N':'^','E':'>','W':'<','S':'v'}
    return ("{:>3}:{:<3} {}".format(x, y, znaki[smer]))

def prevedi(ime_vhoda, ime_izhoda):
    vdat = ime_vhoda
    idat = open(ime_izhoda, "w")
    for ukaz in izvedi(vdat):
        idat.write(opisi_stanje(ukaz[0],ukaz[1],ukaz[2])+"\n")
    idat.close()

def opisi_stanje_2(x, y, smer):
    x = "(" + str(x)
    znaki = {'N':'^','E':'>','W':'<','S':'v'}
    return ("{}{" ":>5}:{})".format(znaki[smer],x, y))






