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
    vrni = [(0, 0, 'N')]
    ukazi = []
    a = 0
    for vrstice in open(ime_datoteke):
        ukazi.append(vrstice.split())
    for ukaz in ukazi:
        trenutna_smer = vrni[a][2]
        x = vrni[a][0]
        y = vrni[a][1]
        if len(ukaz) == 1:
            if ukaz == ['DESNO']:
                smer = 'R'
                trenutna_pozicija = premik(smer, x, y, trenutna_smer)
                vrni.append(trenutna_pozicija)
            if ukaz == ['LEVO']:
                smer = 'L'
                trenutna_pozicija = premik(smer, x, y, trenutna_smer)
                vrni.append(trenutna_pozicija)

        if len(ukaz)  == 2:
            if trenutna_smer == 'N':
                y = y - int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
            elif trenutna_smer == 'S':
                y = y + int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
            elif trenutna_smer == 'W':
                x = x - int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
            elif trenutna_smer == 'E':
                x = x + int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
        a+=1
    return vrni

def opisi_stanje(x, y, smer):
    smeri = {'N' : ' ^', 'E' : ' >', 'S' : ' v', 'W' : ' <'}
    for smer_ in smeri.items():
        if smer_[0] == smer:
            return("{:3}:{:<3}{:2}".format(x, y, smer_[1]))

def prevedi(ime_vhoda, ime_izhoda):
    vh_dat = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for element in vh_dat:
        a, b, c, = element
        file.write(opisi_stanje(a, b, c))
        file.write("\n")
    file.close()

