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
    seznam = []
    x,y,direction = 0,0,"N"
    seznam.append((x,y,direction))
    for vrstica in open(ime_datoteke):
        if vrstica.strip() == "DESNO":
            nov_premik =(premik("R",x,y,direction))
            x,y,direction = nov_premik
            seznam.append(nov_premik)
        if vrstica.strip() == "LEVO":
            nov_premik =(premik("L",x,y,direction))
            x,y,direction = nov_premik
            seznam.append(nov_premik)
        if "NAPREJ" in vrstica.strip():
            premik_naprej =int((vrstica.strip().replace("NAPREJ", "").lstrip()))
            nov_premik = premik(premik_naprej,x,y,direction)
            x,y,direction = nov_premik
            seznam.append((nov_premik))
    return seznam

def opisi_stanje(x,y,smer):
    if smer == "N":
        stanje =  "{X:>3}:{Y:<3} ^"
        return stanje.format(X=x,Y=y)
    if smer == "E":
        stanje =  "{X:>3}:{Y:<3} >"
        return stanje.format(X=x,Y=y)
    if smer== "S":
        stanje =  "{X:>3}:{Y:<3} v"
        return stanje.format(X=x,Y=y)
    if smer == "W":
        stanje =  "{X:>3}:{Y:<3} <"
        return stanje.format(X=x,Y=y)


def prevedi(ime_vhoda, ime_izhoda):
    premiki = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x, y, directions in premiki:
        datoteka.write(opisi_stanje(x, y, directions) + "\n")

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        stanje =  "^   ({X:>}:{Y:<})"
        return stanje.format(X=x,Y=y)
    if smer == "E":
        stanje =  "> ({X:>}:{Y:<})"
        return stanje.format(X=x,Y=y)
    if smer== "S":
        stanje =  "v  ({X:>}:{Y:<})"
        return stanje.format(X=x,Y=y)
    if smer == "W":
        stanje =  "<   ({X:>}:{Y:<})"
        return stanje.format(X=x,Y=y)






