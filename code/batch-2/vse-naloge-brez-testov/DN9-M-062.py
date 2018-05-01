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


def izvedi(x):
    a = open(x)
    a = a.read()
    a = a.split()
    x,y,s = 0,0,"N"
    robot = [(x,y,s)]
    indeks = 0
    b = ["N","E","S","W"]
    for i in a:
        if i == "DESNO":
            indeks += 1
            if indeks > 3:
                indeks = 0
            s = b[indeks]
        elif i == "LEVO":
            indeks -= 1
            if indeks < 0:
                indeks = 3
            s = b[indeks]
        if i.isdigit():
            i = int(i)
            if "N" in s:
                y -= i
            elif "E" in s:
                x += i
            elif "S" in s:
                y += i
            elif "W" in s:
                x -= i
        if i != "NAPREJ":
            robot.append((x,y,s))
    return robot

def opisi_stanje(x,y,smer):
    slovar = dict([("N", "^"), ("E", ">"), ("S", "v"),("W","<")])
    b = "{x:>3}:{y:<3} {slovar}".format(x=x, y=y, slovar=slovar[smer])
    return (b)

def prevedi(vhod,izhod):
    a = izvedi(vhod)
    b = open(izhod, "w")
    for x,y,z in a:
        b.write(opisi_stanje(x,y,z)+"\n")

def opisi_stanje_2(x,y,smer):
    slovar = dict([("N", "^"), ("E", ">"), ("S", "v"),("W","<")])
    b = "{slovar:<} {x:>4}:{y:<}".format(x="("+str(x), y=str(y)+")", slovar=slovar[smer])
    print(b)
    return b


