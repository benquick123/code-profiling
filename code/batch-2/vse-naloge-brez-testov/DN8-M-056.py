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
    datoteka = open(ime_datoteke)
    sez = [(0,0,"N")]
    smeri = {"DESNO":"R","LEVO":"L"}
    for vrstica in datoteka:
        a = vrstica.split()
        if a[0] == "NAPREJ":
            ukaz = int(a[1])
        else:
            ukaz = smeri[a[0]]
        sez.append(premik(ukaz,*sez[-1]))
    return(sez)
def opisi_stanje(x, y, smer):
    dicti = {"N":"^","W":"<","E":">","S":"v"}
    return("{:>3}:{:<3}{:>2}".format(str(x),str(y),dicti[smer]))

def prevedi(ime_vhoda, ime_izhoda):
    sez = izvedi(ime_vhoda)
    ime_izhoda = open(ime_izhoda,"w")
    for i in sez:
        ime_izhoda.write(opisi_stanje(*i))
        ime_izhoda.write("\n")
    ime_izhoda.close()
def opisi_stanje_2(x, y, smer):
    dicti = {"N": "^", "W": "<", "E": ">", "S": "v"}
    return ("{:<2}{:>4}:{})".format(dicti[smer],"".join(["(",str(x)]),str(y)))

