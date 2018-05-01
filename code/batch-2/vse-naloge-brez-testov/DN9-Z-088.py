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

# Obvezna naloga

# 1
def izvedi(ime_datoteke):
    s = []
    datoteka = open(ime_datoteke)
    x,y = 0,0
    smer = "N"
    korak = (x, y, smer)
    s.append(korak)
    for vrstica in datoteka:
        if "DESNO" in vrstica:
            korak = premik("R",x,y,smer)
            s.append(korak)
            x, y, smer = korak
        elif "LEVO" in vrstica:
            korak = premik("L", x,y, smer)
            s.append(korak)
            x, y, smer = korak
        else:
            if "NAPREJ" in vrstica:
                stevilo = int(vrstica.split()[1])
                korak = premik(stevilo, x, y, smer)
                s.append(korak)
                x, y, smer = korak
    return s

def opisi_stanje(x, y, smer):
    smeri = {
    "N":"^",
    "E":">",
    "S":"v",
    "W":"<"
    }
    return "{:>3}:{:<3} {}".format(x,y,smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = izvedi(ime_vhoda)
    nova_datoteka = open(ime_izhoda, "w", encoding="utf-8")
    for vrstica in datoteka:
        nova_datoteka.write(opisi_stanje(vrstica[0], vrstica[1], vrstica[2])+"\n")
    nova_datoteka.close()

def opisi_stanje_2(x, y, smer):
    smeri = {
    "N":"^",
    "E":">",
    "S":"v",
    "W":"<"
    }
    s = 4 - len(str(x)) - 1
    presledek = " "*s
    return "{:<} {}({}:{})".format(smeri[smer], presledek, x, y)









