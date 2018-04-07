def izvedi(ime_datoteke):
    g = []
    e = []
    h = []
    gnwj = [(0, 0, "N")]
    v = [0, 0, "N"]
    datoteka = open(ime_datoteke)
    for ukaz in datoteka:
        g.append(ukaz)
    for ukaz in g:
        e.append(ukaz.rstrip('\n'))
    for ukaz in e:
        a = ukaz.split()
        if "DESNO" in a or "LEVO" in a:
            h.append(a[0])
        if "NAPREJ" in a:
            h.append(a[1])
    for ukaz in h:
        x = v[0]
        y = v[1]
        smer = v[2]
        v = premik(ukaz,x,y,smer)
        gnwj.append(v)

    return gnwj


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
        x += dx * int(ukaz)
        y += dy * int(ukaz)




    return x, y, smer

def opisi_stanje (x, y, smer):
    x1 = x
    y1 = y
    if smer == "N":
        return "{x1:>3}:{y1:<3} ^".format(x1=x,y1=y)
    if smer == "S":
        return "{x1:>3}:{y1:<3} v".format(x1=x,y1=y)
    if smer == "W":
        return "{x1:>3}:{y1:<3} <".format(x1=x,y1=y)
    if smer == "E":
        return "{x1:>3}:{y1:<3} >".format(x1=x,y1=y)

def prevedi(ime_vhoda, ime_izhoda):
    analusfatalus = izvedi(ime_vhoda)
    k = open(ime_izhoda, "w")
    for e in analusfatalus:
        x = e[0]
        y = e[1]
        smer = e[2]
        g = opisi_stanje(x, y, smer)
        k.write(g + "\n")







