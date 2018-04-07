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

#OBVEZNA NALOGA
#začetno (0, 0, N)!!
def izvedi(ime_datoteke):
    sez = [(0, 0, 'N')]
    for vrstica in open(ime_datoteke):
        x,y,smer = sez[-1]
        if "DESNO" in vrstica:
                sez.append(premik("R",x,y,smer))
        elif "LEVO" in vrstica:
                sez.append(premik("L",x,y,smer))
        elif "NAPREJ" in vrstica:
            m = vrstica.split()
            n = int(m[-1])
            sez.append(premik(n,x,y,smer))
    return sez

def opisi_stanje(x,y,smer):
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak ="<"
    return ("{:>3.0f}:{:<3.0f} {}".format(x,y,znak))

def prevedi(ime_vhoda, ime_izhoda):
    zacetek = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for koordinate in zacetek:
        x, y, smer = koordinate
        datoteka.write(opisi_stanje(x, y, smer)+"\n")
    datoteka.close()

#DODATNA NALOGA

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak ="<"
    return ("{znak} {x: >4}:{y}".format(znak = znak, x ='('+str(x), y = str(y)+')'))
