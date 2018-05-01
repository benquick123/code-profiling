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
    datoteka = open(ime_datoteke,encoding='utf8')
    x = 0
    y = 0
    smer = "N"
    seznam = []
    seznam.append((x, y, smer))
    for vrstica in datoteka.readlines():
        vrstica = vrstica.split(" ")
        vrstica[0] = vrstica[0].strip()
        print(vrstica[0])
        if vrstica[0] == "DESNO":
            x,y,smer = premik("R",x,y,smer)
        elif vrstica[0] == "LEVO":
            x, y, smer = premik("L", x, y, smer)
        else:
            vrstica[1] = vrstica[1].strip()
            x, y, smer = premik(int(vrstica[1]),x,y,smer)
        seznam.append((x,y,smer))
    return seznam

def opisi_stanje(x, y, smer):
    slovar_smeri = {"N":"^","E":">","S":"v","W":"<"}
    return ("{:>3}:{:<3} ".format(x,y)+slovar_smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda,"w",encoding="utf8")
    for stanje in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(stanje[0],stanje[1],stanje[2])+"\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    slovar_smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return (slovar_smeri[smer]+"{:>5}:{})".format("("+str(x),y))


