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
    i = 0
    s = [(0, 0, 'N')]
    file = open(ime_datoteke,encoding="utf8",mode="r")
    for ukaz in file:
        if ukaz[0] == "N":
            s.append(premik(int(ukaz.split(" ")[1].strip()),s[i][0],s[i][1],s[i][2]))
        if ukaz[0] == "L":
            s.append(premik("L",s[i][0],s[i][1],s[i][2]))
        if ukaz[0] == "D":
            s.append(premik("R",s[i][0],s[i][1],s[i][2]))
        i += 1
    file.close()
    return s

def opisi_stanje(x, y, smer):
    s = (x,y,smer)
    smeri = "N","E","S","W"
    pus = " ^", ">", "v", "<"
    smr = smeri.index(smer)

    return "{:>3}{:<1}{:<3}{:>2}".format(x, ":", y, pus[smr])

def prevedi(ime_vhoda, ime_izhoda):

    with open(ime_izhoda,encoding="utf8",mode="w") as f:
        for vrstica in izvedi(ime_vhoda):
            x,y,smer = vrstica
            f.write(opisi_stanje(x,y,smer)+"\n")
        f.close()

def opisi_stanje_2(x, y, smer):
    s = (x,y,smer)
    smeri = "N","E","S","W"
    pus = " ^", ">", "v", "<"
    smr = smeri.index(smer)

    return "{:>2}{:<2}{:<2}{:<1}{:<2}{:>1}".format(pus[smr],"(",x,":",y,")")


