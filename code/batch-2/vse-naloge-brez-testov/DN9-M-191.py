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
    output=[(0, 0, 'N')]
    ukazi=[]
    trenutni_x=trenutni_y=0
    trenutna_smer="N"
    datoteka=open(ime_datoteke)
    for vrstica in datoteka:
        razclenjena_vrstica=vrstica.strip().split()
        ukazi.append(razclenjena_vrstica)
    for niz in ukazi:
        if niz[0]=="DESNO":
            output.append(premik("R",trenutni_x,trenutni_y,trenutna_smer))
            if trenutna_smer=="N":
                trenutna_smer="E"

            elif trenutna_smer=="E":
                trenutna_smer="S"

            elif trenutna_smer=="S":
                trenutna_smer="W"

            elif trenutna_smer=="W":
                trenutna_smer="N"
        if niz[0]=="LEVO":
            output.append(premik("L",trenutni_x,trenutni_y,trenutna_smer))
            if trenutna_smer=="N":
                trenutna_smer="W"

            elif trenutna_smer=="W":
                trenutna_smer="S"

            elif trenutna_smer=="S":
                trenutna_smer="E"

            elif trenutna_smer=="E":
                trenutna_smer="N"
        if niz[0]=="NAPREJ":
            output.append(premik(int(niz[1]),trenutni_x,trenutni_y,trenutna_smer))
            if trenutna_smer=="N":
                trenutni_y=trenutni_y-int(niz[1])

            elif trenutna_smer=="W":
                trenutni_x=trenutni_x-int(niz[1])

            elif trenutna_smer=="S":
                trenutni_y=trenutni_y+int(niz[1])

            elif trenutna_smer=="E":
                trenutni_x=trenutni_x+int(niz[1])
    return output

def opisi_stanje(x, y, smer):
    smeri={"N":"^", "E":">","W":"<","S":"v"}
    return "{x:>3}:{y:<3} {z}".format(x=x,y=y,z=smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    ukazi=izvedi(ime_vhoda)
    datoteka=open(ime_izhoda,"w")
    for element in ukazi:
        datoteka.write(opisi_stanje(element[0],element[1],element[2]))
        datoteka.write("\n")
    datoteka.close()


def opisi_stanje_2(x, y, smer):
    smeri={"N":"^", "E":">","W":"<","S":"v"}
    string=""
    if len(str(x))==1:
        string=smeri[smer]+"   ("+str(x)+":"+str(y)+")"
    if len(str(x))==2:
        string=smeri[smer]+"  ("+str(x)+":"+str(y)+")"
    if len(str(x))==3:
        string=smeri[smer]+" ("+str(x)+":"+str(y)+")"
    return string


