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
    datoteka, zaporedje, trenutno, ukazi = open(ime_datoteke), [(0, 0, "N")], (0, 0, "N"), []
    for komanda in datoteka:
        if komanda.startswith("NAPREJ"):
            ukazi.append(int(komanda[-3: ].strip()))
        elif komanda.startswith("DESNO"):
            ukazi.append("R")
        elif komanda.startswith("LEVO"):
            ukazi.append("L")
    for ukaz in ukazi:
        x, y, smer = trenutno
        novo = premik(ukaz, x, y, smer)
        zaporedje.append(novo)
        trenutno = novo
    return zaporedje

def opisi_stanje(x, y, smer):
    usmeritve = {"N": "^", "W":"<", "S":"v", "E":">"}
    return "{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer=usmeritve[smer])

def prevedi(ime_vhoda, ime_izhoda):
    polozaji, izhod = izvedi(ime_vhoda), open(ime_izhoda, "w")
    for polozaj in polozaji:
        x, y, smer = polozaj
        izhod.write(opisi_stanje(x, y, smer) + "\n")
    return

def opisi_stanje_2(x, y, smer):
    usmeritve = {"N": "^", "W": "<", "S": "v", "E": ">"}
    x1, y1 = "(" + str(x), str(y) + ")"
    return "{smer} {x:>4}:{y:<}".format(smer=usmeritve[smer], x=x1, y=y1)










