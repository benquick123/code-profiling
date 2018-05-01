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
    with open(ime_datoteke, "r+") as dat:
        temp = []
        koordinate = (0, 0, "N")

        ukazi = [koordinate]

        for vrstica in dat:
            x, y, direct = koordinate
            temp = vrstica.split()
            if temp[0] == "DESNO":
                ukazi.append(premik("R", x, y, direct))
                koordinate = premik("R", x, y, direct)
            elif temp[0] == "LEVO":
                ukazi.append(premik("L", x, y, direct))
                koordinate = premik("L", x, y, direct)
            else:
                ukazi.append(premik(int(temp[1]), x, y, direct))
                koordinate = premik(int(temp[1]), x, y, direct)


    return ukazi


def opisi_stanje(x, y, smer):
    smeri = "NESW"
    premiki = "^>v<"
    return "{0:>3}:{1:<3}{2:>2}".format(x, y, premiki[smeri.index(smer)])


def prevedi(ime_vhoda, ime_izhoda):
    ukazi = izvedi(ime_vhoda)
    pisi = open(ime_izhoda, "w")

    for x, y, smer in ukazi:
        pisi.write(opisi_stanje(x, y, smer)+"\n")
    pisi.close()

def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    premiki = "^>v<"
    return "{2:<2}{0:>4}:{1:<})".format("("+str(x), y, premiki[smeri.index(smer)])

