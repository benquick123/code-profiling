# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6

def sosedov(x, y, mine):
    """stevilo_sosedov = 0
    for x1, y1 in mine:
        x2 = abs(x - x1)
        y2 = abs(y - y1)
        if x2 <= 1 and y2 <= 1:
            if (x2, y2) != (0, 0):
                stevilo_sosedov += 1
    return stevilo_sosedov"""
    return sum(1 if abs(x-x1) <=1 and abs(y-y1) <=1 and ((abs(x-x1), abs(y-y1)) != (0, 0)) else 0 for x1,y1 in mine)

def najvec_sosedov(mine, s, v):
    """max = 0
    polje =(0,0)
    for x in range(s):
        for y in range(v):
            stevilo_sosedov = sosedov(x, y, mine)
            if max <= stevilo_sosedov:
                max = stevilo_sosedov
                polje = (x,y)
    return (polje)"""
    return [(x, y) for x in range(s) for y in range(v) if max([sosedov(x1, y1, mine) for x1 in range(s) for y1 in range(v)]) <= sosedov(x,y,mine)][0]

def brez_sosedov(mine, s, v):
    return {(x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {k:{(x,y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == k} for k in range(9)}

########################
# Za oceno 7

def dolzina_poti(pot):
    """korak = 0
    for (x1,y1),(x2,y2) in zip(pot,pot[1:]):
            if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2):
                korak += abs(y2 - y1) or abs(x2 - x1)
    return korak"""
    return sum(abs(y2 - y1) or abs(x2 - x1) for (x1, y1), (x2, y2) in zip(pot, pot[1:]) if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2))


def varen_premik(x0, y0, x1, y1, mine):
    """for e in range(min(y0, y1), max(y0, y1)+1):
        if (x0,e) in mine:
            return False
    for b in range(min(x0, x1), max(x0, x1)+1):
        if (b,y0) in mine:
            return False
    return True"""
    return False if any((x0, e) in mine for e in range(min(y0, y1), max(y0, y1) + 1)) or any((b, y0) in mine for b in range(min(x0, x1), max(x0, x1) + 1)) else True


def varna_pot(pot, mine):
    return all(varen_premik(x1,y1,x2,y2, mine) for (x1, y1), (x2, y2) in zip(pot, pot[1:])) and all((x1, y1) not in mine for (x1, y1) in pot)

########################
# Za oceno 8

def polje_v_mine(polje):
    mnozica=set()
    for indeks, niz in enumerate(polje.split()):
        v = len(polje.split())
        s = len(niz)
        for x in range(s):
            if niz[x] == "X":
                mnozica.add((x,indeks))
    return (mnozica, s, v)


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


