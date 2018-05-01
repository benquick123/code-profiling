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
    s = [(0, 0, "N")]
    tmp = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            x, y, smer = s[tmp]
            if vrstica.strip() == "DESNO":
                s.append(premik("R", x, y, smer))

            elif vrstica.strip() == "LEVO":
                s.append(premik("L", x, y, smer))

            else:
                stevilka = int(vrstica.split()[1])
                s.append(premik(stevilka, x, y, smer))
            tmp += 1
    return s

def opisi_stanje(x, y, smer):
    return {"N": "{:>3}:{:<3}".format(x, y) + " ^", "E": "{:>3}:{:<3}".format(x, y) + " >",
            "S": "{:>3}:{:<3}".format(x, y) + " v", "W": "{:>3}:{:<3}".format(x, y) + " <"}[smer]


def prevedi(ime_vhoda, ime_izhoda):
    nova_dat = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        nova_dat.write(opisi_stanje(x,y,smer) + "\n")
    nova_dat.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        a = "^ " + "{:>4}:{})".format(x, y)
    elif smer == "E":
        a = "> " + "{:>4}:{})".format(x, y)
    elif smer == "S":
        a = "v " + "{:>4}:{})".format(x, y)
    else:
        a = "< " + "{:>4}:{})".format(x, y)

    i = a.index(str(x)[0]) #najdem indeks prvega znaka številke, pred ta znak rabim zamenjat presledek z (
    return a[:i - 1] + "(" + a[i:]   #tu zamenjam presledek pred znakom številka z (





















