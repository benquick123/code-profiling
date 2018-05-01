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
    s = open(ime_datoteke)
    j = "N"
    o=[(0,0,"N")]
    i=0
    u=0
    for a in s:
        b="".join(a.strip().split(" ")[1:])
        if b:
            b=b
        else:
            b = 0
        b = int(b)
        if a[0] == "D":
            b = "R"
        elif a[0] == "L":
            b = "L"
        k = premik(b, 0, 0, j)
        j = k[2]
        i += k[0]
        u += k[1]
        o.append((i,u,j))
    #print(o)
    return o

def opisi_stanje(x,y,smer):
    string = ""
    if smer == "N":
        string += "{:>3}:{:<3} ^".format(x,y)
    elif smer == "E":
        string += "{:>3}:{:<3} >".format(x, y)
    elif smer == "S":
        string += "{:>3}:{:<3} v".format(x, y)
    elif smer == "W":
        string += "{:>3}:{:<3} <".format(x, y)
    #print(string)
    return string

def prevedi(ime_vhoda, ime_izhoda):
    s = open(ime_izhoda, "w")
    i = izvedi(ime_vhoda)
    #print(i)
    for a in i:
       # print(a)
        k = opisi_stanje(a[0],a[1],a[2])
        print(k)
        s.write(k+"\n")
    s.close()

def opisi_stanje_2(x,y,smer):
    string = ""
    if smer == "N":
        string += "^{:>5}:{})".format(("("+str(x)), y)
    elif smer == "E":
        string += ">{:>5}:{})".format(("("+str(x)), y)
    elif smer == "S":
        string += "v{:>5}:{})".format(("("+str(x)), y)
    elif smer == "W":
        string += "<{:>5}:{})".format(("("+str(x)), y)
    print(string)
    return string



