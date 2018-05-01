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
    ukaz_s={"DESNO":"R","LEVO":"L"}
    datoteka=open(ime_datoteke,"r")
    vrstica=[]
    polje=[(0,0,"N")]
    x=0
    y=0
    smer="N"
    for v in datoteka:
        vrstica.append(v.strip())
    c=0
    while c<len(vrstica):
        if vrstica[c]=="DESNO":
            ukaz=ukaz_s["DESNO"]
        elif vrstica[c]=="LEVO":
            ukaz=ukaz_s["LEVO"]
        else:
            ukaz=int(vrstica[c].split(" ")[1])
        x,y,smer = premik(ukaz,x,y,smer)
        polje.append((x,y,smer))
        c=c+1
    datoteka.close()
    return polje

#print(izvedi("primer.txt"))
def opisi_stanje(x,y,smer):
    smer_s={"N":"^","E":">","S":"v","W":"<"}
    return "{x:>3}:{y:<3} {smer}".format(x=x,y=y,smer=smer_s[smer])

def prevedi(ime_vhoda, ime_izhoda):
    polje=izvedi(ime_vhoda)
    ime_izhoda=open(ime_izhoda,"w")
    for x,y,smer in polje:
        ime_izhoda.write(opisi_stanje(x,y,smer)+"\n")
    ime_izhoda.close()


def opisi_stanje_2(x,y,smer):
    smer_s={"N":"^","E":">","S":"v","W":"<"}
    return "{smer}{x: >5}:{y}".format(smer=smer_s[smer],x="("+str(x),y=str(y)+")")

