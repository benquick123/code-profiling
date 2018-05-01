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
    seznam_stanja = [(0, 0, "N")]
    upute = open(ime_datoteke)
    for ukaz in upute:
        (a, b, c) = seznam_stanja[len(seznam_stanja)-1]
        en_ukaz = ukaz.strip()
        if en_ukaz == "DESNO":
            seznam_stanja.append(premik("R", a, b, c))
        elif en_ukaz == "LEVO":
            seznam_stanja.append(premik("L", a, b, c))
        else:
            seznam_stanja.append(premik(int(en_ukaz.split()[1]), a, b, c))
    return seznam_stanja


def opisi_stanje(x, y, smer):
    slovar = {"N": "^", "S": "v", "E": ">", "W": "<"}
    return "{:>3}:{:<3} {}".format(x, y, slovar[smer])


def prevedi(ime_vhoda, ime_izhoda):
    izhodna_datoteka = open(ime_izhoda, "w")
    seznam_vhoda = list(izvedi(ime_vhoda))
    seznam_izhoda = []
    for info in seznam_vhoda:
        (a, b, c) = info
        seznam_izhoda.append(opisi_stanje(a, b, c))
    izpis = "\n".join(seznam_izhoda)
    izhodna_datoteka.write(izpis)
    izhodna_datoteka.close()


def opisi_stanje_2(x, y, smer):
    slovar = {"N": "^", "S": "v", "E": ">", "W": "<"}
    return "{} {:>4}:{:<}".format(slovar[smer], "(" + str(x), str(y) + ")")


