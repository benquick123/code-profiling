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
    a=[(0,0,'N')]
    for vrsta in datoteka:
        x,y,s=a[-1]
        v = vrsta.split()
        if v[0] == 'NAPREJ':
            a.append(premik(int(v[1]),x,y,s))
        else:
            if v[0]=='DESNO':
                a.append(premik('R',x,y,s))
            else:
                a.append(premik('L', x, y, s))
    datoteka.close()
    return a

def opisi_stanje(x, y, smer):
    if smer=="N":
        s="^"
    elif smer=="E":
        s = ">"
    elif smer=="W":
        s = "<"
    elif smer=="S":
        s = "v"
    return "{:>3}:{:<3} {}".format(x,y,s)

def prevedi(ime_vhoda, ime_izhoda):
    a=izvedi(ime_vhoda)
    datoteka=open(ime_izhoda, "w")
    for x,y,s in a:
        datoteka.write(opisi_stanje(x,y,s)+"\n")
    datoteka.close()


def opisi_stanje_2(x, y, smer):
    if smer=="N":
        s="^"
    elif smer=="E":
        s = ">"
    elif smer=="W":
        s = "<"
    elif smer=="S":
        s = "v"
    return ("{} {:>4}:{}".format(s,"("+str(x),str(y)+")"))



