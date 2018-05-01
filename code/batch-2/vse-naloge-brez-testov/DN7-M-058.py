def vsa_polja(s, v):
    return [(x, y) for x in range(s) for y in range(v)]

def sosedov(x, y, mine):
    sosedi = 0
    for x0, y0 in mine:
        if x0 == x:
            if y0 == y - 1:
               sosedi += 1
            elif y0 == y + 1:
                sosedi += 1
        elif y0 == y:
            if x0 == x - 1:
                sosedi += 1
            elif x0 == x + 1:
                sosedi += 1
        elif y0 == y - 1:
            if x0 == x - 1:
                sosedi += 1
            elif x0 == x + 1:
                sosedi += 1
        elif y0 == y + 1:
            if x0 == x - 1:
                sosedi += 1
            elif x0 == x + 1:
                sosedi += 1
    return sosedi

def najvec_sosedov(mine, s, v):
    naj_sosedov = 0
    naj_polje = (0, 0)
    for x, y in vsa_polja(s, v):
        sosedi = sosedov(x, y, mine)
        if sosedi > naj_sosedov:
            naj_sosedov = sosedi
            naj_polje = (x, y)
    return naj_polje

def brez_sosedov(mine, s, v):
    nima_sosedov = set()
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine) == 0:
            nima_sosedov.add((x, y))
    return nima_sosedov

def po_sosedih(mine, s, v):
    st_sosedov = {}
    for x in range(9):
        st_sosedov[x] = set()
    for x, y in vsa_polja(s, v):
        for x0 in range(9):
            if sosedov(x, y, mine) == x0:
                st_sosedov[x0].add((x, y))
    return st_sosedov

