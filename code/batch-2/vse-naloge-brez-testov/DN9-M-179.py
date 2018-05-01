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
    x, y, smer = 0, 0, "N"
    stanje = [(x, y, smer),]
    for ukaz in datoteka:
        if ukaz.strip() == "DESNO":
            x, y, smer = premik("R", x, y, smer)
            stanje.append((x, y, smer))
        elif ukaz.strip() == "LEVO":
            x, y, smer = premik("L", x, y, smer)
            stanje.append((x, y, smer))
        else:
            ukaz = ukaz.split()
            x, y, smer = premik(int(ukaz[1]), x, y, smer)
            stanje.append((x, y, smer))
    datoteka.close()
    return stanje


def opisi_stanje(x, y, smer):
    smeri = "NESW"
    #ismeri pove na katerem mestu je "smer" v nizu smeri, potem pa glede na to določimo kateri elememnt iz niza vzeti
    ismer = smeri.index(smer)
    smeriIndikator = ["^", ">", "v", "<"]
    return "{x:>3.0f}:{y:<3.0f} {smer}".format(x=x, y=y, smer=smeriIndikator[ismer])


def prevedi(ime_vhoda, ime_izhoda):
    datoteka_izhod = open(ime_izhoda, "w")
    ukazi = izvedi(ime_vhoda)
    for ukaz in ukazi:
        x, y, smer = ukaz
        datoteka_izhod.write("{ukaz_izhoda}\n".format(ukaz_izhoda=opisi_stanje(x, y, smer)))
    datoteka_izhod.close()


def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    # ismeri pove na katerem mestu je "smer" v nizu smeri, potem pa glede na to določimo kateri elememnt iz niza vzeti
    ismer = smeri.index(smer)
    smeriIndikator = ["^", ">", "v", "<"]
    return "{smer}{x:>5}:{y})".format(x="("+str(x), y=y, smer=smeriIndikator[ismer])


