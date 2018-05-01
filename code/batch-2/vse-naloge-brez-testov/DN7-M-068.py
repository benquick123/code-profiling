
########################
# Za oceno 6

from math import sqrt

def sosedov(x,y,mine):
    return len([(a,b) for a,b in mine \
                if sqrt((x - a) ** 2 + (y - b) ** 2) < 2 \
               and (x,y) != (a,b)])

def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

def najvec_sosedov(mine, s, v):
    a, b = 0, 0
    najvec = 0
    for (x, y) in list(vsa_polja(s, v)):
            if sosedov(x, y, mine) > najvec:
                najvec = sosedov(x, y, mine)
                a, b = x, y
    return a, b

def brez_sosedov(mine, s, v):
    return set((x,y) for x,y in list(vsa_polja(s,v)) if sosedov(x,y,mine) == 0)

def po_sosedih(mine, s, v):
    c = {}
    for e in range(0,9):
        for x,y in vsa_polja(s,v):
            if e not in c:
                c[e] = set()
            if sosedov(x,y,mine) == e:
                c[e].add((x,y))
    return c

########################
# Za oceno 7

def dolzina_poti(pot):
    return sum(abs((x2-x1) + (y2-y1)) for (x1,y1),(x2,y2) in list(zip(pot, pot[1:len(pot)])))

def varen_premik(x0,y0,x1,y1,mine):
    for x,y in mine:
        if (y1 == y0 == y and x0<=x<=x1) or (x0 == x1 == x and y0 <= y <= y1):
            return False
        elif (x0 == x1 == x and y1 <= y <= y0) or (y1 == y0 == y and x1 <= x <= x0):
            return False
    return True

def varna_pot(pot, mine):
    return all(varen_premik(x0,y0,x1,y1,mine) for (x0, y0), (x1, y1) in zip(pot[:1]+pot, pot))

########################
# Za oceno 8

def polje_v_mine(polje):
    seznam = []
    c = polje.split()
    v=len(c)
    s=0
    for e in enumerate(c):
        s = len(e[1])
        for f,h in list(enumerate(e[1])):
            if h == "X":
                seznam.append((f, e[0]))
    return set(seznam), s, v

########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


