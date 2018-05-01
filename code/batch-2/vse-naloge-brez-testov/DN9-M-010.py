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


def izvedi(f):
    file = open(f, "r", encoding="utf-8").read()
    ukazi = file.split("\n")[0:-1]
    x = 0
    y = 0
    smer = "N"
    ukaz = 0
    pot = [(0, 0, "N")]
    for v in ukazi:
        if "DESNO" in v:
            ukaz = "R"
        elif "LEVO" in v:
            ukaz = "L"
        elif "NAPREJ" in v:
            ukaz = int(v.split()[1])
        podkorak = premik(ukaz, x, y, smer)
        x = podkorak[0]
        y = podkorak[1]
        smer = podkorak[2]
        pot.append(podkorak)
    return pot


def opisi_stanje(x, y, smer):
    smeri = "NESW"
    smeri_znakovno = "^>v<"
    return "{x:>3}:{y:<3}{z:>2}".format(x=x, y=y, z=smeri_znakovno[smeri.index(smer)])


def prevedi(ime_vhoda, ime_izhoda):
    komande = izvedi(ime_vhoda)
    f = open(ime_izhoda, "w", encoding="utf-8")
    for k in komande:
        print(opisi_stanje(k[0], k[1], k[2]), file=f)
    f.close()


def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    smeri_znakovno = "^>v<"
    return "{z:<2}{x:>4}:{y})".format(x="("+str(x), y=y, z=smeri_znakovno[smeri.index(smer)])


