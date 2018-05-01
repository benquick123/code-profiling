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
    pravilni_korak = (0,0,'N') #zacnemo na (0,0,'N') po definiciji
    pravilna_pot = [pravilni_korak]
    for vrstice in open(ime_datoteke):
        trenutno_vrstica = vrstice.strip()
        zacetna_koordinata_x = pravilni_korak[0]
        zacetna_koordinata_y = pravilni_korak[1]
        zacetna_smer = pravilni_korak[2]
        if(trenutno_vrstica == 'DESNO'):
            pravilni_korak = premik("R", zacetna_koordinata_x, zacetna_koordinata_y, zacetna_smer)
            pravilna_pot.append(pravilni_korak)
        elif(trenutno_vrstica == 'LEVO'):
            pravilni_korak = premik("L", zacetna_koordinata_x, zacetna_koordinata_y, zacetna_smer)
            pravilna_pot.append(pravilni_korak)
        else:
            #odstranimo NAPREJ in spremenimo v integer
            aktivni_korak = int(trenutno_vrstica.replace("NAPREJ ", ""))
            pravilni_korak = premik(aktivni_korak, zacetna_koordinata_x, zacetna_koordinata_y, zacetna_smer)
            pravilna_pot.append(pravilni_korak)
    return pravilna_pot

def opisi_stanje(x, y, smer):
    if(smer == 'N'):
        smer = '^'
    elif (smer == 'E'):
        smer = '>'
    elif (smer == 'S'):
        smer = 'v'
    elif (smer == 'W'):
        smer = '<'
    return '{:3}:{:<3} {}'.format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    vhodni_podatek = izvedi(ime_vhoda)
    izhodna_datoteka = open(ime_izhoda, "w")
    for premik_ena in vhodni_podatek:
        lepi_zapis = opisi_stanje(premik_ena[0],premik_ena[1],premik_ena[2])
        izhodna_datoteka.write(lepi_zapis+"\n")

