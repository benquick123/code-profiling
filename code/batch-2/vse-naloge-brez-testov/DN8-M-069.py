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
    s=[]
    datoteka = open(ime_datoteke)
    obrnjen = "N"
    x_ko = 0
    y_ko = 0
    s.append((0,0,"N"))
    for a in datoteka:
        if "NAPREJ" in a:
            g = int(a[7:])
            s.append(premik(g, x_ko, y_ko, obrnjen))
            x_ko = premik(g, x_ko, y_ko, obrnjen)[0]
            y_ko = premik(g, x_ko, y_ko, obrnjen)[1]
            obrnjen = premik(g, x_ko, y_ko, obrnjen)[2]

        if "DESNO" in a:
            s.append(premik("R",x_ko,y_ko,obrnjen))
            x_ko = premik("R", x_ko, y_ko, obrnjen)[0]
            y_ko = premik("R", x_ko, y_ko, obrnjen)[1]
            obrnjen = premik("R", x_ko, y_ko, obrnjen)[2]

        if "LEVO" in a:
            s.append(premik("L", x_ko, y_ko, obrnjen))
            x_ko = premik("L", x_ko, y_ko, obrnjen)[0]
            y_ko = premik("L", x_ko, y_ko, obrnjen)[1]
            obrnjen = premik("L", x_ko, y_ko, obrnjen)[2]
    return s

def opisi_stanje(x, y, smer):
    znaki = ["^", ">", "v", "<"]
    crka = ["N", "E", "S", "W"]
    return '{:3}:{:<3} {}'.format(x,y,znaki[crka.index(smer)])

def prevedi(ime_vhoda, ime_izhoda):
    vhod = open(ime_vhoda, "r")
    nova_d = open(ime_izhoda, "w")
    for i in range(sum(1 for a in vhod)+1):
        nova_d.write(opisi_stanje(izvedi(ime_vhoda)[i][0], izvedi(ime_vhoda)[i][1], izvedi(ime_vhoda)[i][2]))
        nova_d.write('\n')
    nova_d.close()

