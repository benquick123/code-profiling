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
    s = [(0, 0, "N")]
    for vrstica in datoteka:
        vrstica = vrstica.strip()
        x, y, sm = s[-1]
        if vrstica == "DESNO":
            s.append(premik("R", x, y, sm)) 
        elif vrstica == "LEVO":
            s.append(premik("L", x, y, sm)) 
        else: 
            st = int(vrstica.split( )[1])
            s.append(premik(st, x, y, sm))
    return s

def opisi_stanje(x, y, smer):
    niz = 0
    znaki = ["^", "v",">", "<"]
    if smer == "N":
        niz = "{x:>3}:{y:<4}{znaki[0]}".format(x=x,y=y,znaki=znaki)
    elif smer == "S":
        niz = "{x:>3}:{y:<4}{znaki[1]}".format(x=x,y=y,znaki=znaki)
    elif smer == "E":
        niz = "{x:>3}:{y:<4}{znaki[2]}".format(x=x,y=y,znaki=znaki)
    elif smer == "W":
        niz = "{x:>3}:{y:<4}{znaki[3]}".format(x=x,y=y,znaki=znaki)
    return niz

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    stanja = izvedi(ime_vhoda)
    for i in stanja:
        x, y, sm = i
        datoteka.write(opisi_stanje(x, y, sm) + "\n")
prevedi("primer.txt","stanja.txt")



