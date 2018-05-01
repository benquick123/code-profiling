def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz.strip() == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz.strip() == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * int(ukaz.strip().split()[1])
        y += dy * int(ukaz.strip().split()[1])
    return x, y, smer



#NALOGE ABLBLBLBBLBLBL
def izvedi(ime_datoteke):
    array=[]
    x=0
    y=0
    smer ="N"
    array.append((x,y,smer))
    for vrstica in open(ime_datoteke):
        array.append(premik(vrstica.strip(),x,y,smer))
        x=premik(vrstica,x,y,smer)[0]
        y=premik(vrstica,x,y,smer)[1]
        smer =premik(vrstica,x,y,smer)[2]
    return array


def opisi_stanje(x,y,smer):
    znak = ""
    if smer == "N":
        znak="^"
    elif smer == "S":
        znak="v"
    elif smer == "W":
        znak="<"
    else:
        znak=">"
    return("{x:>3}:{y:<3}{znak:>2}".format(x=x,y=y,znak=znak))

def prevedi(ime_vhoda,ime_izhoda):
    ukazi=izvedi(ime_vhoda)
    out=open(ime_izhoda,'w+')
    for ukaz in ukazi:
        out.write(opisi_stanje(ukaz[0],ukaz[1],ukaz[2])+"\n")
    

def opisi_stanje_2(x,y,smer):
    puscica = ""
    if smer == "N":
        puscica="^"
    elif smer == "S":
        puscica="v"
    elif smer == "W":
        puscica="<"
    else:
        puscica=">"
    x="("+str(x)
    return("{puscica}{x:>5}:{y})".format(puscica=puscica,x=x,y=y))


