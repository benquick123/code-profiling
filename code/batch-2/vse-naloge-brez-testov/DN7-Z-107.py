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

def sosedov(x, y, mine):
    return len([(x + a, x + b) for a in [-1, 0, 1] for b in [-1, 0, 1] if a or b != 0 if (x + a, y + b) in mine])


def najvec_sosedov(mine, s, v):
    return max([(sosedov(x, y, mine), (x, y))for x, y in vsa_polja(s, v)])[1]


def brez_sosedov(mine, s, v):
    return {(x, y)for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def seznam_sosedov(mine, s, v, a):
    return set((x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == a)

def po_sosedih(mine, s, v):
    return dict([(a, seznam_sosedov(mine, s, v, a)) for a in range(9)])


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs(x1 - x0) + abs(y1 - y0) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    if (x0 == x1):
        for a in range(min(y0, y1), max(y0, y1)+1):
            if (x0, a) in mine:
                return False
    else:
        for a in range(min(x0, x1), max(x0, x1)+1):
            if (a, y0) in mine:
                return False
    return True


def varna_pot(pot, mine):
    if len(pot) > 1:
        answer = all([varen_premik(x0, y0, x1, y1, mine) for(x0, y0), (x1, y1) in zip(pot, pot[1:])])
    elif len(pot) == 1:
        if pot[0] in mine:
            return False
        else:
            return True
    else:
        return True
    return answer



########################
# Za oceno 8

def polje_v_mine(polje):
    seznam_min = set()
    polje = polje.split(" ")
    x = 0
    while x < len(polje):
        y = 0
        while y < len(polje[x]):
            if polje[x][y] == "X":
                seznam_min.add((y, x))
            y += 1
        x += 1
    return (seznam_min, len(polje[0]), len(polje))






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


