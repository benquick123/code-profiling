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
    ukazi=[]
    for line in datoteka:
        ukazi.append(line)
    premiki = [(0,0,'N')]
    c=0
    while c<len(ukazi):
        if ukazi[c].startswith('DESNO') or ukazi[c].startswith('LEVO'):
            if ukazi[c].startswith('DESNO'):
                premiki.append(premik('R',premiki[c][0] ,premiki[c][1], premiki[c][2]))
            else:
                premiki.append(premik('L', premiki[c][0], premiki[c][1], premiki[c][2]))
        else:
            dolzina = int(ukazi[c].split()[1])
            premiki.append(premik(dolzina,premiki[c][0], premiki[c][1], premiki[c][2]))
        c+=1
    return premiki

def opisi_stanje(x, y, smer):
    smeri, znaki="NESW", "^>v<"
    s="{X:>3}:{Y:<3} {S}"
    return s.format(X=x,Y=y,S=znaki[smeri.index(smer)])

def prevedi(ime_vhoda, ime_izhoda):
    premiki=izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for p in premiki:
        datoteka.write(opisi_stanje(p[0],p[1],p[2])+'\n')
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    #^   (0:12)
    smeri, znaki = "NESW", "^>v<"
    s = "{S} {X:>4}:{Y}"
    return s.format(X='('+str(x), Y=str(y)+')', S=znaki[smeri.index(smer)])

