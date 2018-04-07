

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


# print(premik("L", 5,3,"N"))


def izvedi(ime_datoteke):
    stanja=[(0,0,"N")]
    x=0
    y=0
    smer="N"
    for vrstica in open(ime_datoteke):
        vrstica=vrstica.strip()
        if vrstica=="DESNO":
            ukaz="R"
        elif vrstica=="LEVO":
            ukaz="L"
        else:
            ukaz=int(vrstica[7:])
        xn, yn, smern=premik(ukaz, x,y, smer)
        x=xn
        y=yn
        smer=smern
        stanja.append((x,y,smer))
    return stanja

# print(izvedi("primer.txt"))

def opisi_stanje(x,y,smer):
    slovar_smeri={"N":"^","S":"v","E":">","W":"<"}
    return "{:>3}:{:<3} {}".format(x,y,slovar_smeri[smer])

# print(opisi_stanje(0,12,"N"))


def prevedi(ime_vhoda,ime_izhoda):
    with open(ime_izhoda, "w") as file:
      for stanje in izvedi(ime_vhoda):
          file.write(opisi_stanje(*stanje)+"\n")

# print(prevedi("primer.txt", "stanja.txt"))

def opisi_stanje_2(x,y,smer):
    slovar_smeri={"N":"^","S":"v","E":">","W":"<"}
    z="("+str(x)
    return "{}{:>5}:{})".format(slovar_smeri[smer],z,y)