def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6

def sosedov(x, y, mine):
    return len([x0 for x0, y0 in mine if (sqrt((x0 - x)**2 + (y0 - y)**2) < 2) and (x0, y0) != (x, y)])

def najvec_sosedov(mine, s, v):
    return dict(zip([(sosedov(x, y, mine)) for x, y in vsa_polja(s, v)],[(x, y) for x, y in vsa_polja(s, v)]))[max(dict(zip([(sosedov(x, y, mine)) for x, y in vsa_polja(s, v)],[(x, y) for x, y in vsa_polja(s, v)])))]

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return  {i:{(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i} for i in range(0, 9)}
########################
# Za oceno 7

def dolzina_poti(pot):
    return sum(sqrt((x-x1)**2+(y-y1)**2) for (x, y), (x1, y1) in list(zip(pot, pot[1:])))

def varen_premik(x0, y0, x1, y1, mine):
    return all((list(not(min(y0,y1) <= ym <= max(y0,y1)) for [xm, ym] in mine if x0 == x1 == xm) or list(not(min(x0,x1) <= xm <= max(x0,x1)) for [xm, ym] in mine if y0 == y1 == ym)))

def varna_pot(pot, mine):
    return all(all(list(varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in list(zip(pot, pot[1:])) if len(pot) > 1)) and (xt, yt) not in mine for (xt,yt) in pot)

########################
# Za oceno 8

def polje_v_mine(polje):
    maxs = 0
    maxv = 0
    s = 0
    v = 0
    mine = set()
    x = polje
    for e in x:
        if e == ".":
            s += 1
        if e == "X":
            mine.add((s,v))
            s += 1
        if s > maxs:
            maxs = s
        if v + 1 > maxv:
            maxv = v + 1
        if e == " ":
            if s > maxs:
                maxs = s
            s = 0
            v += 1
    return mine, maxs, maxv

########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.

########################
# Za oceno 10

def preberi_pot(ukazi):
    start = s = (0,0)
    route = [start]
    current_possition = cs = start
    axis = a = 3 #1 is positive y, 2 is negative x, 3 is negative y, 4 is positive x

    for ukaz in ukazi.split():
        if ukaz == "DESNO":
            a += 1
            if a > 4:
                a = a - 4
        elif ukaz == "LEVO":
            a -= 1
            if a == 0:
                a = 4
        else:
            if a == 1:
                cs = (cs[0], cs[1] + int(ukaz))
            if a == 2:
                cs = (cs[0] - int(ukaz), cs[1])
            if a == 3:
                cs = (cs[0], cs[1] - int(ukaz))
            if a == 4:
                cs = (cs[0] + int(ukaz), cs[1])
            route.append(cs)
    return route


def zapisi_pot(pot):
    start = s = (0, 0)
    route = ""
    current_possition = cs = start
    i = 0
    u = 1  # x and y axis switch; x is 0, y is 1
    axis = a = 3  # 1 is positive y, 2 is negative x, 3 is negative y, 4 is positive x

    while i+1 < len(pot):
        if pot[i][u] == pot[i + 1][u]:
            u += 1
            a += 1
            if u == 2:
                u = 0
            if a > 4:
                a = a - 4
            route += " DESNO"
        move = pot[i + 1][u] - pot[i][u]

        if a == 1:
            if move < 0:
                route += " DESNO" + " DESNO " + str(-move)
                a += 2
                if a > 4:
                    a = a - 4
            if move > 0:
                route += " " + str(move)
        elif a == 2:
            if move > 0:
                route += " DESNO" + " DESNO " + str(move)
                a += 2
                if a > 4:
                    a = a - 4
            if move < 0:
                route += " " + str(move)
        elif a == 3:
            if move > 0:
                route += " DESNO" + " DESNO " + str(move)
                a += 2
                if a > 4:
                    a = a- 4
            if move < 0:
                route += " " + str(move)
        elif a == 4:
            if move > 0:
                route += " " + str(move)
            if move < 0:
                route += " DESNO" + " DESNO " + str(-move)
                a += 2
                if a > 4:
                    a = a - 4
        i += 1
    return route


