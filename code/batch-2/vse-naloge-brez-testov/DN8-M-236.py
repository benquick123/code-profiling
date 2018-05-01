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

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda


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
    x = 0
    y = 0
    smeri = "NESW"
    ismer = 0
    smer = (smeri[ismer])
    seznam = []
    seznam.append(premik(0, x, y, smer))
    for vrstica in datoteka:

        if (izloci_besedo(vrstica) == "DESNO"):
            seznam.append(premik("R", x, y, smeri[ismer]))
            if (ismer < 3):
                ismer += 1
            else:
                ismer = 0

        if (izloci_besedo(vrstica) == "LEVO"):
            seznam.append(premik("L", x, y, smeri[ismer]))
            if (ismer > 0):
                ismer -= 1
            else:
                ismer = 3

        if (vrstica.split(" ")[0] == "NAPREJ"):
            seznam.append(premik(int(vrstica.split(" ")[1]), x, y, smeri[ismer]))
            x = seznam[len(seznam) - 1][0]
            y = seznam[len(seznam) - 1][1]

    return seznam


def opisi_stanje(x,y,smer):
    znak=""
    if(smer=="N"):
        znak="^"
    if(smer=="E"):
        znak=">"
    if(smer=="S"):
        znak="v"
    if(smer=="W"):
        znak="<"

    return("{a:>3}:{b:<4}".format(a=x, b=y)+znak)


def prevedi(ime_vhoda,ime_izhoda):
    datoteka2 = open(ime_izhoda, "w+")

    for i in izvedi(ime_vhoda):
        datoteka2.write(opisi_stanje(i[0], i[1], i[2])+"\n")



def opisi_stanje_2(x,y,smer):
    znak = ""
    if (smer == "N"):
        znak = "^"
    if (smer == "E"):
        znak = ">"
    if (smer == "S"):
        znak = "v"
    if (smer == "W"):
        znak = "<"
    x="("+str(x)
    y= str(y)+")"
    return(znak+"{a:>5}:{b}".format(a=x, b=y))



