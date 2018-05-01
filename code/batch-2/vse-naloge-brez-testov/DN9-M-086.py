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

    seznam = [(0,0,"N")]
    stevec = 1
    for ukaz in datoteka:
        ukaz = ukaz.rstrip()
        if ukaz == "DESNO":
            r = "R"

        elif ukaz == "LEVO":
            r = "L"

        else:
            b = ukaz.split(" ")
            r = int(b[1])

        klic = premik(r,seznam[stevec-1][0],seznam[stevec-1][1],seznam[stevec-1][2])
        stevec = stevec+1
        klic = tuple(klic)
        seznam.append(klic)
    datoteka.close()
    return seznam

def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = "^"
    if smer == "E":
        znak = ">"
    if smer == "S":
        znak = "v"
    if smer == "W":
        znak = "<"
    niz = ("{:>3}:{:<4}{}".format(x,y,znak))
    return niz

def prevedi(ime_vhoda, ime_izhoda):
    a = open(ime_vhoda)
    b= open(ime_izhoda, "w")
    c = izvedi(ime_vhoda)
    for d,e,f in c:
        b.write(opisi_stanje(d, e , f))
        b.write("\n")

