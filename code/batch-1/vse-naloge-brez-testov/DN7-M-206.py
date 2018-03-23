# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import collections
import math
def vsa_polja(s, v):

    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6
mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}


def sosedov(x, y, mine):

    return len([xm for xm, ym in mine if (math.sqrt((xm - x) ** 2 + (ym - y) ** 2) >= 1) and (math.sqrt((xm - x) ** 2 + (ym - y) ** 2) <= math.sqrt(2))])

def najvec_sosedov(mine, s, v):

    return max([(x, y) for x, y in vsa_polja(s, v) if ( sosedov(x, y, mine) >= max([sosedov(xvse, yvse, mine) for xvse, yvse in vsa_polja(s, v)]))  ])

def brez_sosedov(mine, s, v):

    return {(x, y) for x, y in vsa_polja(s, v) if ( sosedov(x, y, mine) == 0)}


def po_sosedih(mine, s, v):

    return {i: {(x, y) for x, y in vsa_polja(s, v) if (sosedov(x, y, mine) == i)} for i in range(9)}


########################
# Za oceno 7
pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]
def dolzina_poti(pot):

    return sum([abs(x0-x1) + abs(y0-y1) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    #a si naletel na mino?
    return not any([(x0 == x1 == xm and (y0 <= ym <= y1 or y1 <= ym <= y0)) or (y0 == y1 == ym and (x0 <= xm <= x1 or x1 <= xm <= x0)) for xm, ym in mine])

def varna_pot(pot, mine):

    return ((len(pot) == 0) or (len(pot) == 1 and pot[0] not in mine) or (len(pot) > 1 and all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])))



########################
# Za oceno 8

def polje_v_mine(polje):

    st_vrstic = 0
    st_stolpcev = 0

    mine = []
    vrstice = polje.split(" ")


    for vr in vrstice:
        #če je prazen set
        if not vr:
            continue

        st_stolpcev = 0

        for znak in vr:
            if (znak == "X"):
                mine.append((st_stolpcev, st_vrstic))
            st_stolpcev += 1
        st_vrstic += 1

    return (set(mine), st_stolpcev, st_vrstic)

print(polje_v_mine("...X...X.X....X."))

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


