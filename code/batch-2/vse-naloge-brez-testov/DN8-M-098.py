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
    retseznam = [(0,0,"N")]
    datoteka = open(ime_datoteke)
    for x in datoteka:
        if x.startswith("D"):
            retseznam.append(premik("R", retseznam[len(retseznam)-1][0], retseznam[len(retseznam)-1][1], retseznam[len(retseznam)-1][2]))
        if x.startswith("L"):
            retseznam.append(premik("L", retseznam[len(retseznam) - 1][0], retseznam[len(retseznam) - 1][1], retseznam[len(retseznam) - 1][2]))
        if x.startswith("N"):
            premiknap = int(x.split()[1])
            retseznam.append(premik(premiknap, retseznam[len(retseznam) - 1][0], retseznam[len(retseznam) - 1][1], retseznam[len(retseznam) - 1][2]))
    return retseznam

def opisi_stanje(x, y, smer):
    smerineba = "NESW"
    smeripuscic = "^>v<"
    smerpusc = smeripuscic[smerineba.index(smer)]
    retstr = "{0:>3}:{1:<3} {2}"

    return retstr.format(x, y, smerpusc)



def prevedi(ime_vhoda, ime_izhoda):
    seznamv = izvedi(ime_vhoda)
    dat = open(ime_izhoda, "w")
    for i in seznamv:
        dat.write(opisi_stanje(i[0], i[1], i[2])+'\n')
    dat.close()

def opisi_stanje_2(x, y, smer):
    smerineba = "NESW"
    smeripuscic = "^>v<"
    smerpusc = smeripuscic[smerineba.index(smer)]
    strx = str(x)
    niz = "("
    niz += strx
    retstr = "{0:<2}{1:>4}:{2})"
    return retstr.format(smerpusc, niz, y)


