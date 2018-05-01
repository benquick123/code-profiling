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
    rezultat = []
    ukaz = 0
    kon = "N"
    x,y = 0,0
    rezultat.append((premik(ukaz,x,y,kon)))

    with open(ime_datoteke) as f:
        vsebina = f.read().splitlines()
        #print(vsebina)

    for i in vsebina:
        n = i[-1:]
        for u in n:
            if u.isdigit():
                a = i[-2:]
                a = int(a)
                #print (a)
                break

        crka = i[0]
        if crka == "D":
            crka = "R"
        #print (crka)

        if crka == "N":
            rezultat.append((premik(a, x, y, kon)))
            for e in rezultat:
                x,y,kon = e

        elif crka == "D" or "L":
            rezultat.append((premik(crka, x, y, kon)))
            for e in rezultat:
                x, y, kon = e
        print(rezultat)
    return rezultat


def opisi_stanje(x,y,smer):

    if smer =="N":
        smer = "^"

    elif smer =="W":
        smer = "<"

    elif smer =="S":
        smer = "v"

    elif smer =="E":
        smer = ">"
    return("{:>3}:{:<3} {}".format(x,y,smer))


def prevedi(ime_vhoda, ime_izhoda):

    datoteka = open(ime_izhoda,"w")
    a = izvedi(ime_vhoda)
    for i in a:
        x,y,smer = i
        c = opisi_stanje(x,y,smer)
        datoteka.write(c)
        datoteka.write("\n")
    datoteka.close()
    return





def opisi_stanje_2(x, y, smer):
    a = []
    if smer =="N":
        smer = "^"

    elif smer =="W":
        smer = "<"

    elif smer =="S":
        smer = "v"

    elif smer =="E":
        smer = ">"
    b = "({}:".format(x)
    c = "{})".format(y)

    a.append(smer)
    a.append(b)
    a.append(c)

    return ("{a[0]}{a[1]:"">6}{a[2]}".format(a = a))


































