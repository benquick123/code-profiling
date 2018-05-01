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
    komp = {"0": "N","1": "E","2":"S","3":"W"}
    x,y,kompas = 0,0,0
    seznam = [(x,y,komp[str(kompas)])]
    for content in open(ime_datoteke):
        content = content.rstrip()
        print(content)
        if content == "DESNO": #obrat v desno - pointDir()
            kompas +=1
            if kompas > 3:
                kompas = 0
        elif content == "LEVO": #obrat v levo - pointDir()
            kompas -=1
            if kompas < 0:
                kompas = 3
        else: #premik po x,y glede na kompas - pointDis()
            beseda,smer = content.split()
            if kompas == 0:
                y -= int(smer)
            if kompas == 1:
                x += int(smer)
            if kompas == 2:
                y += int(smer)
            if kompas == 3:
                x -= int(smer)
        seznam.append((x,y,komp[str(kompas)]))
    return seznam

def opisi_stanje(x,y,smer):
    kompas = {"N": "^", "E": ">", "S":"v", "W":"<"}
    return '{:>3}:{:<3} {}'.format(x,y,kompas[smer])

def prevedi(ime_vhoda, ime_izhoda):
    d = open(ime_izhoda, "w")
    for a in izvedi(ime_vhoda):
        x,y,smer = a
        d.write(opisi_stanje(x,y,smer) + "\n")





