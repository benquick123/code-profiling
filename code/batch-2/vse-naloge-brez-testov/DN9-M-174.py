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
    d = open(ime_datoteke).read().split("\n")[:-1]
    x, y = 0, 0
    smer = "N"
    u = [(x, y, smer)]
    for z in d:
        if z[:6] == "NAPREJ":
            d = premik(int(z[7:]), x, y, smer)
            u.append(d)
            x, y, smer = d[0], d[1], d[2]
        else:
            d = premik(("R" if z[0] == "D" else "L"), x, y, smer)
            u.append(d)
            x, y, smer = d[0], d[1], d[2]
    return u


def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{: >3}:{: <3} {}".format(x, y, "^")
    elif smer == "W":
        return "{: >3}:{: <3} {}".format(x, y, "<")
    elif smer == "E":
        return "{: >3}:{: <3} {}".format(x, y, ">")
    else:
        return "{: >3}:{: <3} {}".format(x, y, "v")


def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    d = open(ime_izhoda, "w")
    for m in s:
        d.write(opisi_stanje(m[0], m[1], m[2]) + "\n")
    d.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        print("{} {x: >4}:{y: <1}".format("^", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format("^", x="(" + str(x), y=str(y) + ")")
    elif smer == "W":
        print("{} {x: >4}:{y: <1}".format("<", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format("<", x="(" + str(x), y=str(y) + ")")
    elif smer == "E":
        print("{} {x: >4}:{y: <1}".format(">", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format(">", x="(" + str(x), y=str(y) + ")")
    else:
        print("{} {x: >4}:{y: <1}".format("v", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format("v", x="(" + str(x), y=str(y) + ")")


