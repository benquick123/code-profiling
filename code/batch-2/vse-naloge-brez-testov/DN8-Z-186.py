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
    trojke = [(0, 0, 'N')]
    ukazi = []
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        n = vrstica.strip()
        if n == 'DESNO' :
            ukazi.append("R")
        elif n == 'LEVO' :
            ukazi.append("L")
        else:
            ukazi.append(int(n[7:]))
    for ukaz in ukazi:
        for x, y, smer in trojke:
            a = premik(ukaz, x, y, smer)
        trojke.append(a)
    datoteka.close()
    return trojke

def opisi_stanje(x, y, smer):
    smeri = {"N" : "^", "S" : "v", "E" : ">", "W" : "<"}
    return ("{: >3}:{: <3}{: >2}".format(x, y, smeri[smer]))

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        datoteka.write(opisi_stanje(x, y, smer)+"\n")
    datoteka.close()

