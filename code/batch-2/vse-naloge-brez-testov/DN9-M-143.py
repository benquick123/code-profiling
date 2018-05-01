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

def izvedi(datoteka):
    pot=[(0,0,'N')]
    i=0
    Trenutna_pot=[0,0,'N']
    file=open(datoteka)
    for vrstica in file:
        if vrstica.split()[0] == "DESNO":
            Trenutna_pot=premik("R",Trenutna_pot[0],Trenutna_pot[1],Trenutna_pot[2])
            pot.append(Trenutna_pot)
        elif vrstica.split()[0] == "LEVO":
            Trenutna_pot = premik("L", Trenutna_pot[0], Trenutna_pot[1], Trenutna_pot[2])
            pot.append(Trenutna_pot)
        elif vrstica.split()[0] == "NAPREJ":
            premik_stevilo= vrstica.split()[1]
            Trenutna_pot = premik(int(premik_stevilo),Trenutna_pot[0],Trenutna_pot[1],Trenutna_pot[2])
            pot.append(Trenutna_pot)
    file.close()
    return pot

def opisi_stanje(x,y,smer):
    if smer =="N":
        direction="^"
    elif smer =="E":
        direction=">"
    elif smer =="S":
        direction="v"
    elif smer == "W":
        direction="<"
    return('{:>3}:{:<3}{:>2}'.format(x,y,direction))

def prevedi(ime_vhoda, ime_izhoda):
    seznam=[]
    pot2=izvedi(ime_vhoda)
    file=open(ime_izhoda, 'w')
    for x,y,smer in pot2:
        item= opisi_stanje(x,y,smer)+"\n"
        seznam.append(item)
    for item in seznam:
        file.write(item)
    file.close()


