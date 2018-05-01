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
    f = open(ime_datoteke, 'r')
    terka = ()
    seznam=[]
    trenutni_x=0
    trenutni_y=0
    trenutna_smer='N'
    terka=(trenutni_x,trenutni_y,trenutna_smer)
    seznam.append(terka)
    besedilo = f.readlines()

    for vrstica in besedilo:
        #vrstica=vrstica.strip()
        vrstica=vrstica.strip()
        print(vrstica)
        if vrstica[:3] == "NAP":
            ukaz_splitan = vrstica.split(" ")
            terka=premik(int(ukaz_splitan[1]), trenutni_x, trenutni_y, trenutna_smer)
            trenutni_x=terka[0]
            trenutni_y = terka[1]
            seznam.append(terka)
            #print(vrstica)

        elif vrstica=="DESNO" or vrstica=="LEVO":
            trenutni_ukaz=""

            if vrstica=="DESNO":
                trenutni_ukaz="R"
            elif vrstica=="LEVO":
                trenutni_ukaz="L"

            terka=premik(trenutni_ukaz, trenutni_x,trenutni_y, trenutna_smer)
            trenutna_smer=terka[2]
            seznam.append(terka)
            #print(vrstica)

    f.close()
    return seznam
def opisi_stanje(x,y,smer):
    x_string = str(x)
    y_string = str(y)
    smeri1=['N','E','S','W']
    smeri2=['^','>', 'v', '<']
    smer=smeri2[smeri1.index(smer)]
    return ("{:>3}:{:<4}{}".format(x_string, y_string, smer))




def prevedi(ime_vhoda, ime_izhoda):
    seznamTerk = izvedi(ime_vhoda)
    f = open(ime_izhoda,'w')
    for terka in seznamTerk:
        vrstica=opisi_stanje(terka[0],terka[1],terka[2])+'\n'
        f.write(vrstica)
    f.close()

def opisi_stanje_2(x, y, smer):

    return ""

