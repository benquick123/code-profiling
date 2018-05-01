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
    x, y = 0, 0
    smer = "N"
    zaporedje = [(x, y, smer)]
    for vrstica in open(ime_datoteke):
        svrstica = vrstica.strip()
        ukaz = "R" if svrstica == "DESNO" else "L" if svrstica == "LEVO" else int(svrstica.split()[1])
        rezultat_premika = premik(ukaz, x, y, smer)
        zaporedje.append(rezultat_premika)
        x, y, smer = rezultat_premika
    return zaporedje


def opisi_stanje(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return "{:>3}:{:<3} {}".format(x, y, smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    dat = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        dat.write(opisi_stanje(x, y, smer) + "\n")

def opisi_stanje_2(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return "{} {:>4}:{:<})".format(smeri[smer], "(" + str(x), y)

