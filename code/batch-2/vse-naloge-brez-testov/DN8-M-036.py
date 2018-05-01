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
    datoteka = open(ime_datoteke)
    vsebina_datoteke = []
    rezultat = []

    x = 0
    y = 0

    trenutna_smer = "N"

    zacetno_st = premik(0, x, y, trenutna_smer)

    rezultat.append(zacetno_st)

    for vrstica in datoteka:
        vsebina_datoteke.append(vrstica.strip())

    for i in range(len(vsebina_datoteke)):
        # dobimo trenutni ukaz
        trenutuni_ukaz = (vsebina_datoteke[i]).split()[0]

        counter = i + 1

        if trenutuni_ukaz == "DESNO":
            trenutuni_ukaz = "R"
            rez = premik(trenutuni_ukaz, x, y, trenutna_smer)


        elif trenutuni_ukaz == "LEVO":
            trenutuni_ukaz = "L"
            rez = premik(trenutuni_ukaz, x, y, trenutna_smer)

        elif trenutuni_ukaz == "NAPREJ":
            trenutni_premik = int((vsebina_datoteke[i]).split()[1])
            rez = premik(trenutni_premik, x, y, trenutna_smer)


        rezultat.append(rez)

        x = rezultat[counter][0]
        y = rezultat[counter][1]
        trenutna_smer = rezultat[counter][2]

        # rezultat.append(trentuni_ukaz, 0, 0, )

    datoteka.close()
    return rezultat

def opisi_stanje(x, y, smer):
    znak = ""
    if smer == "N":
        znak = "^"
    elif smer == "E":
        znak = ">"
    elif smer == "S":
        znak = "v"
    else:
        znak = "<"

    return("{x:>3}:{y:<3} {smer}").format(x = x, y = y, smer = znak)

def prevedi(ime_vhoda, ime_izhoda):
    datoteka_v = open(ime_vhoda)
    datoteka_i = open(ime_izhoda, "w")
    vsebina_v_datoteke = izvedi(ime_vhoda)

    for x, y, smer in vsebina_v_datoteke:
        datoteka_i.write(opisi_stanje(x, y, smer) + "\n")

    datoteka_i.close()
    datoteka_v.close()

