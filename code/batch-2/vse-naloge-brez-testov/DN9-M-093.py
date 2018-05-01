def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * int(ukaz.split()[1])
        y += dy * int(ukaz.split()[1])
    return x, y, smer

def izvedi(ime_datoteke):
    x, y = 0 , 0
    smer = "N"
    s = [(0, 0, "N")]
    ukazi = open(ime_datoteke)
    for line in ukazi:
        s.append(premik(line.strip(), x, y, smer))
        x,y = premik(line.strip(), x, y, smer)[0], premik(line.strip(), x, y, smer)[1]
        smer = premik(line.strip(), x, y, smer)[2]
    return s

def opisi_stanje(x, y, smer):
    podatki = (x, y, smer)
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    smer = smeri[smer]
    return "{podatki[0]:>3}:{podatki[1]:<3} {smer}".format(podatki = podatki, smer = smer)

def prevedi(ime_vhoda, ime_izhoda):
    beri = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for x, y, smer in beri:
        datoteka.write(opisi_stanje(x, y, smer) + "\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    podatki = (x, y, smer)
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    smer = smeri[smer]
    x = "(" + str(podatki[0])
    return "{smer} {x:>4}:{podatki[1]})".format(podatki=podatki, smer=smer, x=x)



#======================================   TESTI   ===========================================#


