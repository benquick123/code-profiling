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
    a = open(ime_datoteke)
    x = 0
    y = 0
    smer = "N" 
    b = [(x, y, smer)]
    for i in a.readlines():
        if i == "DESNO\n":
            c = premik("R",x, y, smer)
            x = c[0]
            y = c[1]
            smer = c[2]
        elif i == "LEVO\n":
            c = premik("L", x, y, smer)
            x = c[0]
            y = c[1]
            smer = c[2]
        else:
            d = ""
            for k in i:
                if k.isnumeric():
                    d = d + k
            d = int(d)
            c = premik(d, x, y, smer)
            x = c[0]
            y = c[1]
            smer = c[2]
        b.append((x, y, smer))
    a.close()
    return b
            
def opisi_stanje(x, y, smer):
    m = 3-len(str(x))
    n = 3-len(str(y))
    s = " "*m+str(x)+":"+str(y)+" "*n+" "
    if smer == "N":
        s = s + "^"
    elif smer == "E":
        s = s + ">"
    elif smer == "S":
        s = s + "v"
    elif smer == "W":
        s = s + "<"
    return s

def prevedi(ime_vhoda, ime_izhoda):
    a = izvedi(ime_vhoda)
    b = []
    for i in a:
        c = opisi_stanje(i[0], i[1], i[2])
        b.append(c)
    d = open(ime_izhoda, 'w')
    for i in b:
        d.write(i+"\n") 
    d.close()






