# Domača Naloga: Minobot (OK)

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
    prevod = {"DESNO": "R", "LEVO": "L"}
    vsi_premiki = []
    smer, x, y = "N", 0, 0
    vsi_premiki.append(tuple([x, y, smer]))
    with open(ime_datoteke) as datoteka:
        for en_premik in datoteka:
            if en_premik.strip() not in prevod:
                ukaz = int(en_premik.strip().split(" ")[1])
            else:
                ukaz = prevod[en_premik.strip()]
            x, y, smer = premik(ukaz, x, y, smer)
            vsi_premiki.append(tuple([x, y, smer]))
    return (vsi_premiki)


def opisi_stanje(x, y, smer):
    vse_smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return " " * (3 - len(str(x))) + str(x) + ":" + str(y) + " " * (3 - len(str(y))) + " " + vse_smeri[smer]


def prevedi(ime_vhoda, ime_izhoda):
    premiki = izvedi(ime_vhoda)
    with open(ime_izhoda, "w") as write:
        for x, y, smer in premiki:
            write.write(opisi_stanje(x, y, smer) + "\n")


def opisi_stanje_2(x, y, smer):
    vse_smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return vse_smeri[smer] + " " + " " * (3 - len(str(x))) + "(" + str(x) + ":" + str(y) + ")"


