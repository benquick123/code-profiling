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

def izvedi(ukazi):
    ukazi_raw = open(ukazi, "r")
    ukazi_list = [line.strip("\n") for line in ukazi_raw.readlines()]
    stanja = [(0, 0, "N")]

    for ukaz in ukazi_list:
        premik_input = ""
        if ukaz == 'DESNO':
            premik_input = "R"
        elif ukaz == 'LEVO':
            premik_input = "L"
        elif "NAPREJ" in ukaz:
            premik_input = int(ukaz.split()[-1])
        x, y, smer = stanja[-1]
        stanja.append(premik(premik_input, x, y, smer))
    return stanja

def opisi_stanje(x, y, smer):
    smeri_crke = "NESW"
    smeri_simboli =  "^>v<"
    pari = dict(zip (smeri_crke, smeri_simboli))
    return '{:>3}:{:<3} {}'.format(str(x), str(y), pari[smer])

def prevedi(ime_vhoda, ime_izhoda):
    f = open(ime_izhoda, "w+")

    for stanje in izvedi(ime_vhoda):
        f.write(opisi_stanje(*stanje)+ "\n" )
    f.close()

def opisi_stanje_2(x, y, smer):
    smeri_crke = "NESW"
    smeri_simboli =  "^>v<"
    pari = dict(zip (smeri_crke, smeri_simboli))
    return '{} {}:{})'.format(pari[smer], (3-len(str(x))) * " " + "(" + str(x), str(y))


# ^, >, v in < (za N, E, S in W)

