def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

from math import sqrt
def sosedov(x, y, mine):
    v = 0
    for x1, y1 in mine:
        razdalja = sqrt((x1 - x) **2 + (y1 - y) ** 2)
        if x == x1 and y == y1:
            v -= 1
        if razdalja < 2:
            v += 1
    return v

def najvec_sosedov(mine, s, v):
    a = 0
    naj_koordinate = ()
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine) >= a:
            a = sosedov(x, y, mine)
            naj_koordinate = x, y
    return naj_koordinate


def brez_sosedov(mine, s, v):
    m = []
    for x, y in vsa_polja(s, v):
        koordinate = x, y
        if sosedov(x, y, mine) < 1:
            if koordinate not in m:
                m.append(koordinate)
    return set(m)


def po_sosedih(mine, s, v):
    a = {i: set() for i in range(9)}
    for (x, y) in vsa_polja(s, v):
        for i in range(9):
            if sosedov(x, y, mine) == i:
                a[i].add((x, y))
    return a

def dolzina_poti(pot):
    a = []
    b = []
    for i in range(1, len(pot)):
        a.append(abs(pot[i][0] - pot[i - 1][0]))
        b.append(abs(pot[i][1] - pot[i - 1][1]))
    return (sum(a) + sum(b))

def stopil_na_mino(x,y,mine):
    if (x,y) in mine:
        return True

def varen_premik(x0, y0, x1, y1, mine):
    if (y1 < y0):
        temp = y0
        y0 = y1
        y1 = temp
    if (x1 < x0):
        temp = x0
        x0 = x1
        x1 = temp
    if (x0==x1):
        for i in range(y0,y1+1):
            if (stopil_na_mino(x0, i, mine)):
                return False
    if (y0==y1):
        for i in range(x0, x1+1):
            if (stopil_na_mino(i, y0, mine)):
                return False
    return True


def varna_pot(pot, mine):
    if not pot:
        return True
    if stopil_na_mino(pot[0][0], pot[0][1], mine):
        return False
    for i in range(1, len(pot)):
        x0 = pot[i - 1][0]
        y0 = pot[i - 1][1]
        x1 = pot[i][0]
        y1 = pot[i][1]
        if not varen_premik(x0, y0, x1, y1, mine):
            return False
    return True


def polje_v_mine(polje):
    slika = polje.split(" ")
    s = len(slika[0])
    v = len(slika)
    mine = set()
    for i in range(0, len(slika)):
        for j in range(0, len(slika[0])):
            if(slika[i][j] == "X"):
                mine.add((j, i))
    return mine, s, v


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


