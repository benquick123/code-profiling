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
    koraki = 0
    a_x = 0
    b_y = 0
    zacetek = (0, 0, "N")
    skokov = 0
    pot = []
    pot.append(zacetek)
    seznam = []
    kompas = zacetek[2]
    premiki = open(ime_datoteke, 'r', encoding='utf8')
    for vrstica in premiki:
        seznam.append(vrstica.strip())
    #print(seznam)
    for korak in seznam:
        if korak == "DESNO":
            ukaz1 = "R"
            premikd = premik(ukaz1,a_x,b_y,kompas)
            kompas = premikd[2]
            kompas = kompas.strip()
            pot.append(premikd)
        if korak == "LEVO":
            ukaz2 = "L"
            premikl = premik(ukaz2,a_x,b_y,kompas)
            kompas = premikl[2]
            kompas = kompas.strip()
            pot.append(premikl)
        #if korak.find("NAPREJ"+str(koraki)) != -1:
        if korak.find("NAPREJ") != -1:
            #print("kompas=>",kompas,"<")
            skokov = int(korak.split()[1])
            if kompas == "N":
                #print("kompas_za N ali S=",kompas)
                b_y -= skokov
                #a_x = 0
                pot.append((a_x, b_y,kompas))
            if kompas == "E":
                #print("kompas_za E ali V=", kompas)
                a_x += skokov
                #b_y = 0
                pot.append((a_x, b_y, kompas))
            if kompas == "S":
                #print("kompas_za N ali S=",kompas)
                b_y += skokov
                #a_x = 0
                pot.append((a_x, b_y,kompas))
            if kompas == "W":
                #print("kompas_za E ali V=", kompas)
                a_x -= skokov
                #b_y = 0
                pot.append((a_x, b_y, kompas))
    premiki.close()
    #print(pot)
    return pot

def opisi_stanje(x,y,smer):
    #stanjepolja = []
    if smer == "N":
        smer = "^"
    if smer == "S":
        smer = "v"
    if smer == "E":
        smer = ">"
    if smer == "W":
        smer = "<"
    a = str(x)
    b = str(y)
    #stanjepolja = "  "+a+":"+b+"  "+smer
    stanjepolja = '{:3d}'.format(int(a)) + ":" + '{:<3d}'.format(int(b)) + " " + smer
    #stanjepolja.append(str(x))
    #stanjepolja.append(":")
    #stanjepolja.append(str(y))
    #stanjepolja.append(smer)
    #stanjepolja = " ".join(stanjepolja)
    #stanjepolja = stanjepolja.append((" %s",stanjepolja))
    #stanjepolja = stanjepolja.replace(" ", "")
    #stanjepolja = stanjepolja.rjust(7)
    #stanjepolja = str(stanjepolja)
    #print(str(stanjepolja))
    return stanjepolja

def prevedi(ime_vhoda, ime_izhoda):
    pisanje = open(ime_izhoda, "w", encoding="utf-8")
    vrstice = izvedi(ime_vhoda)
    #print(vrstice)
    for korak in vrstice:
        #print(korak)
        novformat = opisi_stanje(korak[0],korak[1],korak[2])
        #print(novformat)
        pisanje.write(novformat)
        pisanje.write("\n")
    pisanje.close()


    #for poti in ime_vhoda:
        #opis = opisi_stanje(poti)
    #print(opis)
    #print(ime_izhoda)



