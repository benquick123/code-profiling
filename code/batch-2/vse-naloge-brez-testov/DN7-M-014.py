def sosedov(x, y, mine):
    m = []
    for e in [(a, b) for a in range(x - 1, x + 2) for b in range(y - 1, y + 2)]:
        if e in mine and e != (x, y):
            m.append(e)
    return len(m)

def najvec_sosedov(mine, s, v):
    k = {}
    for x in range(s):
        for y in range(v):
            k[sosedov(x, y, mine)] = (x, y)
    return k[max(k)]

def brez_sosedov(mine, s, v):
    seznam = {}
    brez = set()
    for x in range(s):
        for y in range(v):
            seznam[(x, y)] = sosedov(x, y, mine)
    for a, b in seznam.items():
        if b == 0:
            brez.add(a)
    return brez

def po_sosedih(mine, s, v):
    seznam = {}
    for k in range(9):
        kordinate = set()
        for x in range(s):
            for y in range(v):
                if k == (sosedov(x, y, mine)):
                    kordinate.add((x, y))
        seznam[k] = kordinate
    return seznam


