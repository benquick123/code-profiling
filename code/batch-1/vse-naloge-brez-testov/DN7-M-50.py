# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
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

import collections

def sosedov(x, y, mine):
    s = 0
    for x2 in range((x - 1), (x + 2)):
        for y2 in range((y - 1), (y + 2)):
            if (x2, y2) in mine and (x2, y2) != (x, y):
                s += 1
    return s

def najvec_sosedov(mine, s, v):
    najvec_s = 0
    koordinata_x = 0
    koordinata_y = 0
    for x in range(0, s):
        for y in range(0, v):
            a = sosedov(x, y, mine)
            if a > najvec_s:
                najvec_s = a
                koordinata_x = x
                koordinata_y = y
    return (koordinata_x, koordinata_y)

def brez_sosedov(mine, s, v):
    m = set()
    for x in range(0, s):
        for y in range(0, v):
            a = sosedov(x, y, mine)
            if a == 0:
                m.add((x, y))
    return m


def po_sosedih(mine, s, v):
    slovar = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
    for x in range(0, s):
        for y in range(0, v):
            a = sosedov(x, y, mine)
            slovar[a].add((x,y))
    return slovar

########################
# Za oceno 7

from math import sqrt

def dolzina_poti(pot):
    skupaj = 0
    for a, b in zip(pot, pot[1:]):
            x0, y0 = a
            x1, y1 = b
            dolzina = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            skupaj = skupaj + dolzina
    return int(skupaj)



def varen_premik(x0, y0, x1, y1, mine):
    if x1 < x0 and y1 < y0:
        for x in range(x1, x0 +1):
            for y in range(y1, y0 +1):
                if (x, y) in mine:
                    return False

    if x0 < x1 and y0 < y1:
        for x in range(x0, x1 +1):
            for y in range(y0, y1 +1):
                if (x, y) in mine:
                    return False

    if x1 < x0 and y0 < y1:
        for x in range(x1, x0 +1):
            for y in range(y0, y1 +1):
                if (x, y) in mine:
                    return False

    if x0 < x1 and y1 < y0:
        for x in range(x0, x1 +1):
            for y in range(y1, y0 +1):
                if (x, y) in mine:
                    return False

    if x0 == x1 or y0 == y1:
        if (x0, y0) in mine:
            return False

    return True



def varna_pot(pot, mine):
    for a, b in zip(pot, pot[1:]):
        x0, y0 = a
        x1, y1 = b
        c = varen_premik(x0, y0, x1, y1, mine)


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


