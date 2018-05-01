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
        x += dx * int(ukaz)
        y += dy * int(ukaz)
    return x, y, smer
    print(x,y,smer)

def izvedi(ime_datoteke):
    m = []
    smeri = []
    polja = [(0,0,'N')]
    for i in open(ime_datoteke):
        a = i.strip().split()
        m.append(a)
    for a in m:
        if a[0] == 'DESNO':
            smeri.append("R")
        if a[0] == 'LEVO':
            smeri.append("L")
        if a[0] == 'NAPREJ':
            smeri.append(a[1])
    x0 = 0
    y0 = 0
    smer0 = "N"
    for c in smeri:
        klic = premik(c, x0, y0, smer0)
        x0, y0, smer0 = klic
        polja.append(klic)
    return polja


def opisi_stanje(x, y, smer):
    smeri = "NESW"
    smeri_puscic = "^>v<"
    ismer = smeri.index(smer)
    return "{x:>3}:{y:<3} {p}".format(x=x, y=y, p=(smeri_puscic[ismer]))


def prevedi(ime_vhoda, ime_izhoda):
    preberi = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for i in preberi:
        spremeni = opisi_stanje(i[0],i[1],i[2])
        datoteka.write(spremeni + "\n")
    datoteka.close()

