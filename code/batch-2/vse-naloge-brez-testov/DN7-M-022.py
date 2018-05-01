# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6

import collections

def sosedov(x, y, mine):
    return len([(y0, y) for x0, y0 in mine if abs(x0 - x) <= 1 and abs(y0 - y) <= 1 and (x0, y0) != (x, y)])

def najvec_sosedov(mine, s, v):
    return max({(x, y):sosedov(x, y, mine) for x, y in vsa_polja(s, v)}, key = lambda i: {(x, y):sosedov(x, y, mine) for x, y in vsa_polja(s, v)}[i])


def brez_sosedov(mine, s, v):
    return set([(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0])
    
def po_sosedih(mine, s, v):
    a = {}
    for i in range(9):
        a[i] = set([(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i])
    return a

########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs((x0 + y0) - (x1 + y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    if y0 == y1:
        return all([True if (x0, y0) not in mine else False for x0 in range(min(x0, x1), max(x0, x1) + 1) if y0 == y1])
    return all([True if (x0, y0) not in mine else False for y0 in range(min(y0, y1), max(y0, y1) + 1)])

def varna_pot(pot, mine):
    if pot and pot[0] not in mine:
        return all([True if varen_premik(x0, y0, x1, y1, mine) else False for (x0, y0), (x1, y1) in zip(pot, pot[1:])])
    elif not pot:
        return True
    return False

########################
# Za oceno 8

def polje_v_mine(polje):
    return set([(k, key) for key, word in enumerate(polje.split()) for k, char in enumerate(word) if char == "X"]), len(polje.split()[0]), len(polje.split())

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


