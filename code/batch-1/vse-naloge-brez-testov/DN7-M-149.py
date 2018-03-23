





########################
# Za oceno 6
def lel(x, y, mine):
    k = 0
    for w, q in mine:
        if w == x or w == (x - 1) or w == (x + 1):
            if q == y or q == (y - 1) or q == (y + 1):
                k = k + 1
    return k


def sosedov(x, y, mine):
    k = 0
    for w, q in mine:
        if w == x or w == (x-1) or w == (x+1):
            if q == y or q == (y-1) or q == (y+1):
                if (w, q) != (x, y):
                    k = k + 1
    return k

def najvec_sosedov(mine, s, v):
    g = (0, 0)
    m = 0
    koord = []
    for x in range(0, (s+1)):
        for y in range(0, (v+1)):
            koord.append((x, y))
    for t ,z in koord:
        tsosedov = lel(t, z, mine)
        if tsosedov > m:
            g = (t, z)
            m = tsosedov
    return g


def brez_sosedov(mine, s, v):
    m = set()
    koord = []
    for x in range(0, (s)):
        for y in range(0, (v)):
            koord.append((x, y))
    for t, z in koord:
        tsosedov = sosedov(t, z, mine)
        if tsosedov == 0:
            m.add((t, z))
    return m

def po_sosedih(mine, s, v):
    g = set()
    m = {}
    koord = []
    for x in range(0, (s)):
        for y in range(0, (v)):
            koord.append((x, y))
    for p in range((9)):
        g = set()
        for t, z in koord:
            if sosedov(t, z, mine) == p:
                g.add((t, z))
        m.update({p: g})
    return m

########################
# Za oceno 7

from math import*
def razdalja_koordinat(x1, y1, x2, y2):
    x = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return x

pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]
def dolzina_poti(pot):
    if pot == []:
        dolzinapoti = 0
    else:
        dolzinapoti = 0
        x1, y1 = pot[0]
        for x , y in pot:
            x2 = x
            y2 = y
            dolzinapoti = dolzinapoti + razdalja_koordinat(x1, y1, x2, y2)
            x1 = x2
            y1 = y2
    return dolzinapoti

def varen_premik(x0, y0, x1, y1, mine):
    pot = []
    if y0 == y1 and x0 == x1:
        pot.append((x0,x1))
    if x0<x1:
        for x in range(x0,x1+1):
            pot.append((x,y0))
    if x0 > x1:
        for x in range(x1,x0+1):
            pot.append((x,y0))
    if y0 < y1:
        for y in range(y0,y1+1):
            pot.append((x0,y))
    if y0 > y1:
        for y in range(y1,y0+1):
            pot.append((x0,y))
    return not any([True for (x,y) in pot if (x,y) in mine])
def varna_pot(pot, mine):
    if len(pot) > 1:
        for (x,y),(x1,y1) in zip(pot,pot[1:]):
            if not varen_premik(x,y,x1,y1,mine):
                return False
    else:
        for premik in pot:
            if premik in mine:
                return False
    return True



########################
# Za oceno 8

def polje_v_mine(polje):
    """
    Vrni koordinate min v podanem polju.

    Niz polje opisuje polje tako, da so vodoravne "vrstice" polja ločene s
    presledki. Prosta polja so označena z znako `.`, mine z `X`.

    Args:
        polje (str): polje

    Returns:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja.
    """


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


