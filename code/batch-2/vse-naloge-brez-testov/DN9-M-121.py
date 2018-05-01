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
    seznam = [(0,0,"N")]
    indeks = 0
    for ukaz in datoteka:
        if ukaz.strip() == "DESNO":
            terka = premik("R", seznam[indeks][0],seznam[indeks][1], seznam[indeks][2])
            seznam.append(terka)
        elif ukaz.strip() == "LEVO":
            terka = premik("L", seznam[indeks][0],seznam[indeks][1], seznam[indeks][2])
            seznam.append(terka)
        else:
            n, c = ukaz.split()
            cifra = int(c)
            terka = premik(cifra, seznam[indeks][0],seznam[indeks][1], seznam[indeks][2])
            seznam.append(terka)
        indeks+=1


    return seznam

def opisi_stanje(x, y, smer):
    if smer == "E":
         niz = "{:3}:{:<3} >".format(x, y)
    if smer == "W":
         niz = "{:3}:{:<3} <".format(x, y)
    if smer == "N":
         niz = "{:3}:{:<3} ^".format(x, y)
    if smer == "S":
         niz = "{:3}:{:<3} v".format(x, y)
    return niz

def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    i = open(ime_izhoda, "w")
    for x, y, smer in s:
        i.write(opisi_stanje(x, y, smer))
        i.write("\n")
    i.close()
    return None











