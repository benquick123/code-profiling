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
    a = 0
    b = 0
    nebo = 'N'
    s = [(0,0,'N')]

    for vrstica in open(ime_datoteke):
        m = vrstica.split()
        if m[0] == "DESNO":
            t = premik('R',a,b,nebo)
            s.append(t)
            nebo = t[2]

        elif m[0] == "LEVO":
            t = premik('L',a,b,nebo)
            s.append(t)
            nebo = t[2]

        else:
            if len(m) > 1:
                m =int(vrstica.split()[1])
                t = premik(m,a,b,nebo)
                s.append(t)
                a = t[0]
                b = t[1]


    return s


def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{:>3}:{:<3} ^".format(x,y)
    elif smer == "E":
        return "{:>3}:{:<3} >".format(x,y)
    elif smer == "S":
        return "{:>3}:{:<3} v".format(x,y)
    elif smer == "W":
        return "{:>3}:{:<3} <".format(x,y)

    return None

def prevedi(ime_vhoda, ime_izhoda):
    out = open(ime_izhoda, "w", encoding='utf8')
    for t in izvedi(ime_vhoda):
        out.write(opisi_stanje(t[0],t[1],t[2]) + "\n")
    out.close()




