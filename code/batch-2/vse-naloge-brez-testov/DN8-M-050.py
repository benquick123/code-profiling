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

def  izvedi(ime_datoteke):
    elementi = open(ime_datoteke).read().split("\n")
    smer = "N"
    x=0
    y=0
    nov = []

    nov.append(premik(0,x,y,smer))

    for element in elementi:

        if element == "DESNO":
            ukaz = "R"

        elif element== "LEVO":
            ukaz = "L"

        elif element.__len__()>6:

            if element.__len__()<7:
                ukaz = int(element[7])
            else:
                ukaz = int(element[7:])

        vpisi = premik(ukaz, x, y, smer)
        x=vpisi[0]
        y=vpisi[1]
        smer = vpisi[2]
        nov.append(vpisi)

    return nov[:len(nov)-1]

def opisi_stanje(x,y,smer):

    if smer=="N":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s="^")
    if smer=="E":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s=">")
    if smer=="S":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s="v")
    if smer=="W":
        return "{c:>3}:{d:<4}{s}".format(c=x,d=y,s="<")

def  prevedi(ime_vhoda,ime_izhoda):

    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")

    for element in seznam:
        datoteka.write(opisi_stanje(element[0],element[1],element[2])+"\n")
    datoteka.close()

def opisi_stanje_2(x,y,smer):

    if smer=="N":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s="^")
    if smer=="E":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s=">")
    if smer=="S":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s="v")
    if smer=="W":
        return "{s:} {c:>4}:{d:})".format(c="("+str(x),d=y,s="<")





