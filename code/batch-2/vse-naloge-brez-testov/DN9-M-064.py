def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "L":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "R":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer


def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke)
    s = [(0, 0, 'N')]
    for vrstica in datoteka:
        if "DESNO" in vrstica:
            ukaz = "L"
        if "LEVO" in vrstica:
            ukaz = "R"
        if vrstica.split()[0] == "NAPREJ":
            ukaz = int(vrstica.split()[1])

        x = s[::-1][0][0]
        y = s[::-1][0][1]
        smer = s[::-1][0][2]
        t = premik(ukaz, x, y, smer)
        s.append(t)

    return s



def opisi_stanje(x, y, smer):
    smeri = {"N": "^", "S": "v", "E": ">", "W": "<"}
    stanje = ("{j: >3}:{k: <4}{i}".format(j = x, k = y, i = smeri[smer]))
    return stanje


def prevedi(ime_vhoda, ime_izhoda):
    datoteka2 = open(ime_izhoda, "w")
    datoteka1 = izvedi(ime_vhoda)
    print(datoteka1)
    for e in datoteka1:
        r = opisi_stanje(e[0], e[1], e[2])
        datoteka2.write(r + "\n")


    datoteka2.close()

def opisi_stanje_2(x, y, smer):
    smeri = {"N": "^", "S": "v", "E": ">", "W": "<"}
    stanje = ("{i}{j:>5}:{k})".format(j = "(" + str(x), k = y, i = smeri[smer]))
    return stanje









