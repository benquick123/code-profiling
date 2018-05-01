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
    dat=open(ime_datoteke)
    sez=[]
    for line in dat:
        line=line.rstrip()
        if line[0]=="D":
            line="R"
        elif line[0]=="L":
            line="L"
        elif line.split(" ")[1].isalnum():
            line=int(line.split(" ")[1])
        sez.append(line)

    sez2=[]
    x,y,s=0,0,"N"
    sez2.append((x,y,s))
    for pomik in sez:
        move=premik(pomik,x,y,s)
        sez2.append(move)
        x,y,s=move

    dat.close()
    return sez2

def opisi_stanje(x,y,smer):
    if smer == "N":
        smer="^"
    elif smer == "E":
        smer=">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer="<"
    return ("{:>3}:{:<3} {}".format(x,y,smer))

def prevedi(ime_vhoda,ime_izhoda):
    dat=open(ime_izhoda,"w")
    sez=izvedi(ime_vhoda)
    for line in sez:
        x,y,s=line
        dat.write(opisi_stanje(x,y,s)+"\n")
    dat.close()

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        smer="^"
    elif smer == "E":
        smer=">"
    elif smer == "S":
        smer = "v"
    elif smer == "W":
        smer="<"
    return ("{} {:>4}:{:<})".format(smer,"("+str(x),y))

