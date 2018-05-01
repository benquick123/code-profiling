import re
def izvedi(datoteka):
    vrne=[]
    datotek=open(datoteka)
    zacetek = (0, 0, 'N')
    smer="N"
    x=0
    y=0
    vrne.append(zacetek)
    for vrstica in datotek:
        print(vrstica.strip())
        if vrstica.strip()=="DESNO":
            vrne.append(premik("R", x, y, smer))
            x, y, smer = premik("R", x, y, smer)

        elif vrstica.strip()=="LEVO":
            vrne.append(premik("L", x, y, smer))
            x,y,smer=premik("L", x, y, smer)
        elif "NAPREJ" in vrstica.strip():
           ukaz=re.findall('\d+',vrstica.strip() )
           real=int(ukaz[0])
           vrne.append(premik(real,x,y,smer))
           x, y, smer = premik(real, x, y, smer)
    return vrne


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
def opisi_stanje(x,y,smer):

    if smer== "N":

        niz="{:>3}:{:<3} {}".format(x,y,"^")

    elif smer== "E":

        niz = "{:>3}:{:<3} {}".format(x, y, ">")

    elif smer== "W":

        niz = "{:>3}:{:<3} {}".format(x, y, "<")
    elif smer == "S":

        niz = "{:>3}:{:<3} {}".format(x, y, "v")


    return niz
def prevedi(vhod, izhod):
    vrne=izvedi(vhod)
    datoteka=open(izhod,"w")
    for lol in vrne:
        x,y,smer=lol
        datoteka.write(opisi_stanje(x,y,smer)+"\n")
    datoteka.close
