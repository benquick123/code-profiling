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
    stanja = [(0, 0, 'N')]
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        if 'NAPREJ' in vrstica:
            smer = int(vrstica.strip().split(" ")[1])
        else:
            if 'LEVO' in vrstica:
                smer = "L"
            else:
                smer = "R"
        stanja.append(premik(smer, stanja[-1][0], stanja[-1][1], stanja[-1][2]))
    datoteka.close()
    return stanja

def opisi_stanje(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return "{:3}:{:4}{}".format(int(x), str(y), smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    stanja = open(ime_izhoda, "w+")
    s = izvedi(ime_vhoda)
    for x, y, smer in s:
        stanja.write(opisi_stanje(x, y, smer)+"\n")
    stanja.close()

def opisi_stanje_2(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    return "{}{:>5}:{})".format(smeri[smer], "("+str(x), y)


