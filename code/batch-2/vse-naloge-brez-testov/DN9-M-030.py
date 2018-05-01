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
    tekst = open(ime_datoteke)
    x = 0
    y = 0
    smer = "N"
    smeri = "NESW"
    seznam_premikanja = [(0, 0, 'N')]
    for vrstica in tekst:
        ismer = smeri.index(smer)
        if vrstica[0] == "D":
            ukaz = "R"
            smer = smeri[(ismer + 1) % 4]
        if vrstica[0] == "L":
            ukaz = "L"
            smer = smeri[(ismer - 1) % 4]
        if vrstica[0] == "N":
            stevilo = vrstica[7:].rstrip("\n")
            stevilo = int(stevilo)
            ukaz = stevilo
            if smer == "N":
                y = y - stevilo
            if smer == "S":
                y = y + stevilo
            if smer == "W":
                x = x - stevilo
            if smer == "E":
                x = x + stevilo
        terka = x, y, smer
        seznam_premikanja.append(terka)
    return seznam_premikanja
def opisi_stanje(x,y,smer):
    if smer == "N":
        oznaka = " ^"
    if smer == "S":
        oznaka = " v"
    if smer == "E":
        oznaka = " >"
    if smer == "W":
        oznaka = " <"
    s = "{:3}:{:<3}{:2}"
    return s.format(x,y,oznaka)
def prevedi(ime_vhoda,ime_izhoda):
    ime_izhodne_datoteke = open(ime_izhoda,"w")
    for x, y, smer in izvedi(ime_vhoda):
        ime_izhodne_datoteke.write(opisi_stanje(x,y,smer)+"\n")
    ime_izhodne_datoteke.close()

