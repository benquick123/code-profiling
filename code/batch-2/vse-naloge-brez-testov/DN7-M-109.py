
# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Hvala Vam!

def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    return len([(a,b) for a,b in mine if a in range(x - 1, x + 2) and b in range(y - 1, y + 2) and (a,b) != (x,y)])




def najvec_sosedov(mine, s, v):
    return max([[sosedov(x,y,mine),(x,y)]for x,y in vsa_polja(s,v)])[1]





def brez_sosedov(mine, s, v):
    return {(a,b) for a,b in vsa_polja(s,v) if sosedov(a,b,mine)==0}


def po_sosedih(mine, s, v):
    return  {i: {(a[0],a[1]) for a in vsa_polja(s, v) if  sosedov(a[0],a[1],mine) == i} for i in range(9)}


########################
# Za oceno 7

import math
def dolzina_poti(pot):
    return sum([int(math.hypot(a[0] - b[0], a[1] - b[1])) for a,b in zip(pot,pot [1:])])

def varen_premik(x0, y0, x1, y1, mine):
    return False if False in [False if (x0 <= a <= x1 or x1 <= a <= x0) and (y0 <= b <= y1 or y1 <= b <= y0) else True for a, b in mine] else True


def varna_pot(pot, mine):
    return True if False not in [varen_premik(a0, a1, b0, b1, mine) for (a0,a1), (b0,b1) in zip(pot[1:], pot)] and len(pot) > 1 or len(pot) == 0 or pot[0] not in mine and len(pot) == 1  else False


########################
# Za oceno 8

def polje_v_mine(polje):
    mine=set()
    x = 0
    y = 0
    if " " in polje:
        s = len(polje[:polje.index(" ")])
    else:
        s = len(polje)
    for a in polje:
        if a == " ":
            y+=1
        if a == "X" or ".":
            if a == "X":
                mine.add((x, y))
            x += 1
        if a == " ":
            x = 0
    v=y+1
    if polje[-1] == " ":
        v=y
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


