# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from collections import defaultdict


def vsa_polja(s, v):
    """
    Generiraj vse koordinate (x, y) za polje s podano širino in višino
    Args:
        s (int): širina
        v (int): višina

    Returns:
        generator parov polj
    """
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    return len(list((x1, y1) for x1 in range((x - 1), (x + 2)) for y1 in range((y - 1), (y + 2)) if (x1, y1) in mine - {(x, y)}))

def najvec_sosedov(mine, s, v):
    return max({(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}, key={(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.get)

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {i : set([(x,y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i]) for i in range(9)}


########################
# Za oceno 7

import math

def dolzina_poti(pot):
    return sum([int(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    return all([False if (i, j) in mine else True for i in range(min(x0, x1), max(x0, x1) + 1) for j in range(min(y0, y1), max(y0, y1) + 1)])

def varna_pot(pot, mine):
    return all([False if len(pot) == 1 and pot[0] in mine else True] + [False if not varen_premik(x, y, x2, y2, mine) else True for (x, y), (x2, y2) in zip(pot, pot[1:])])


########################
# Za oceno 8

def polje_v_mine(polje):
    t = set()
    x, y = 0, 0
    for str in polje.split():
        for x in range(len(str)):
            if str[x] == 'X':
                t.add((x, y))
            x += 1
        y += 1
    return t, x, y


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


