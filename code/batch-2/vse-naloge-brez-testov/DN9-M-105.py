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
    koord = [(0, 0, 'N')]
    smer = {"DESNO": "R", "LEVO": "L"}
    with open(ime_datoteke) as d:
        for vrstica in d:
            x, y, s = koord[-1]
            vrstica = vrstica.rstrip()
            if len(vrstica.split()) == 1:
                koord.append((premik(smer[vrstica], x, y, s)))
            else:
                koord.append(premik(int(vrstica.split()[1]), x, y, s)) 
        return koord

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    premiki = ['^', '>', 'v', '<']
    ismer = premiki[smeri.index(smer)]
    return "{0:3}:{1:<3} {2}".format(x,y,ismer)

def prevedi(ime_vhoda, ime_izhoda):
    koord = izvedi(ime_vhoda)
    seznam = [opisi_stanje(x,y,s) for x,y,s in koord]
    with open(ime_izhoda, 'w') as d:
        for vnos in seznam:
            d.write(vnos+"\n")

def opisi_stanje_2(x, y, smer):
    return "{stanje[1]}{xk:>5}:{yk}".format(stanje=opisi_stanje(x,y,smer).split(), xk = "("+str(x), yk=str(y)+")")

