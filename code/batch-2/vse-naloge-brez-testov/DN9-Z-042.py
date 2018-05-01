__author__ = 'Dolores'
def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke, "r")
    vrstice = datoteka.read().splitlines()
    stanja=[(0,0,'N')]
    x=0
    y=0
    smer = 'N'
    for i in vrstice:
        if i=="DESNO":
            x, y, smer = premik('R',x,y,smer)
            stanja.append((x, y, smer))
        if i=="LEVO":
            x,y,smer = premik('L', x, y, smer)
            stanja.append((x, y, smer))
        if i.split()[0] == "NAPREJ":
            x, y, smer = premik(int(i.split()[1]), x, y, smer)
            stanja.append((x,y,smer))
    return stanja

def opisi_stanje(x, y, smer):
    znak = ''
    if smer == 'N':
        znak = '^'
    if smer == 'E':
        znak = '>'
    if smer == 'W':
        znak = '<'
    if smer == 'S':
        znak = 'v'
    niz=("{:>3}".format(x)+ ":" +"{:<4}".format(y)+znak)
    return niz

def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda,'w')
    for i in stanja:
        datoteka.write(opisi_stanje(i[0], i[1], i[2]) +"\n")




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


