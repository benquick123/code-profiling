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
    file = open(ime_datoteke,"r",encoding='utf-8')
    t=file.readlines()
    i=0
    while i < len(t):
        t[i]=t[i][:-1]
        i=i+1

    i=0
    tabPremik=[(0,0,"N")]
    for neki in t:
        vrstica= neki.split()
        if vrstica[0] == "DESNO":
            smer="R"
        elif vrstica[0] == "LEVO":
            smer="L"
        else:
            smer=int(vrstica[1])
        tabPremik.append(premik(smer,tabPremik[i][0],tabPremik[i][1],tabPremik[i][2]))
        i=i+1
    file.close()
    return tabPremik

def opisi_stanje(x, y, smer):
    s="{}{}:{}{} {}"
    stevX = 3 - len(str(x))
    stevY = 3 - len(str(y))


    if smer == "N":
        return s.format(" "*stevX,x,y," "*stevY,"^")
    elif smer == "E":
        return s.format(" "*stevX,x,y," "*stevY,">")
    elif smer == "S":
        return s.format(" "*stevX,x,y," "*stevY,"v")
    else:
        return s.format(" "*stevX,x,y," "*stevY,"<")

def prevedi(ime_vhoda, ime_izhoda):
    tabPremik=izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for neki in tabPremik:
        file.write(opisi_stanje(neki[0],neki[1],neki[2])+"\n")
    file.close()

def opisi_stanje_2(x, y, smer):
    s = "{} {}({}:{})"
    stevX = 3 - len(str(x))

    if smer == "N":
        return s.format("^"," " * stevX, x, y)
    elif smer == "E":
        return s.format(">"," " * stevX, x, y)
    elif smer == "S":
        return s.format("v"," " * stevX, x, y)
    else:
        return s.format("<"," " * stevX, x, y)

