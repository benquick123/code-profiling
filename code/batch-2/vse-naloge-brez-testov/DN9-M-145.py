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
#------------------------------------------------------------- NALOGA SE ZACNE TUKAJ -------------------------------------------------------------
def izvedi(ime_datoteke):
    x=0
    y=0
    smer="N"
    datoteka=open(ime_datoteke)
    ukazi=[]
    for vrstica in datoteka:
        ukazi.append(vrstica.strip())
    datoteka.close()
    premiki=[]
    premiki.append((x,y,smer))
    for ukaz in ukazi:
        if (ukaz == 'DESNO'):
            ukaz = "R"
            x,y,smer = premik(ukaz, int(x), int(y), smer)
            premiki.append((x, y, smer))
        elif (ukaz == 'LEVO'):
            ukaz = "L"
            x, y, smer = premik(ukaz, int(x), int(y), smer)
            premiki.append((x, y, smer))
        else:
            ukaz=ukaz.split(" ")
            x, y, smer = premik(int(ukaz[1]), int(x), int(y), smer)
            premiki.append((x, y, smer))
    return premiki
def opisi_stanje(x, y, smer):
    dx=""
    dy=""
    smeri=["N", "E", "S", "W"]
    ukazi=["^",">","v","<"]
    for i in range(3, len(str(x)), -1):
        dx+= " "
    for i in range(3, len(str(y))-1, -1):
        dy+= " "
    return(dx+str(x)+":"+str(y)+dy+ukazi[(smeri.index(smer))])

def prevedi(ime_vhoda, ime_izhoda):
    premiki = izvedi(ime_vhoda)
    ukazi=[]
    for premik in premiki:
        ukazi.append(opisi_stanje(premik[0], premik[1], premik[2]))
    datoteka = open(ime_izhoda, "w")
    for ukaz in ukazi:
        datoteka.write(ukaz+"\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
    dx = ""
    dy = ""
    smeri = ["N", "E", "S", "W"]
    ukazi = ["^", ">", "v", "<"]
    for i in range(4, len(str(x)), -1):
        dx += " "
    return (ukazi[(smeri.index(smer))]+ dx + "("+ str(x) + ":" + str(y)+")")
#------------------------------------------------------------- NALOGA SE KONCA TUKAJ -------------------------------------------------------------
