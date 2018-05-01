
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
    stevec = 1
    dat = open(ime_datoteke, encoding="utf8")
    x = y = 0
    s = [(0,0,"N")]
    smer = "N"
    for vrstica in dat:
        vrstica = vrstica.rstrip()
        if vrstica == "DESNO":
            ukaz = "R"
        elif vrstica == "LEVO":
            ukaz = "L"
        else:
            a = vrstica.split(" ")
            ukaz = a[1]
            ukaz = int(ukaz)

        s.append(premik(ukaz, x, y, smer))
        x = s[stevec][0]
        y = s[stevec][1]
        smer = s[stevec][2]
        stevec +=1
    return s

def opisi_stanje(x, y, smer):
    if smer == "N":
        puscica = "^"
    elif smer == "S":
        puscica = "v"
    elif smer == "E":
        puscica = ">"
    elif smer == "W":
        puscica = "<"
    return ("{x:>3}:{y:<4}{puscica}".format(x=x,y=y,puscica=puscica))

def prevedi(ime_vhoda, ime_izhoda):
    dat = open(ime_vhoda, encoding="utf8")
    u = open(ime_izhoda,"w", encoding="utf8")
    b = izvedi(ime_vhoda)
    for x, y, smer in b:
        print(opisi_stanje(x,y,smer),file=u)

    dat.close()
    u.close()





def opisi_stanje_2(x, y, smer):
    if smer == "N":
        puscica = "^"
    elif smer == "S":
        puscica = "v"
    elif smer == "E":
        puscica = ">"
    elif smer == "W":
        puscica = "<"
    return ("{puscica}{x:>5}:{y})".format(x=("("+str(x)),y=y,puscica=puscica))









