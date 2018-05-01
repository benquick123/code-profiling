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
    xi = 0
    yi = 0
    smeri = 'N'
    kor = [(0, 0, 'N')]
    for vrstica in datoteka:
        if vrstica.strip() == "DESNO":
            ukazi = "R"
        elif vrstica.strip() == "LEVO":
            ukazi = "L"
        else:
            ukazi = int(vrstica.split()[1])
        tup = premik(ukazi, xi, yi, smeri)
        xi = tup[0]
        yi = tup[1]
        smeri = tup[2]
        kor.append(tup)
    return kor

def opisi_stanje(x, y, smer):
    prevod = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
    return ("{:>3}:{:<3} {}").format(x, y, prevod[smer])

def prevedi(ime_vhoda, ime_izhoda):
    stanje = izvedi(ime_vhoda)
    dat = open(ime_izhoda, "w")
    for stan in stanje:
        dat.write(("{}{}").format(opisi_stanje(stan[0],stan[1],stan[2]),"\n"))

