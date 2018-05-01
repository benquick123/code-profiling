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
    return sum(1 for (x1, y1) in mine if ((x1 in range(x - 1, x + 2)) and (y1 in range(y - 1, y + 2)) and (x1, y1) != (x, y)))


def najvec_sosedov(mine, s, v):
    return [(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == max(sosedov(x, y, mine) for x, y in vsa_polja(s, v))][0]

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}


def po_sosedih(mine, s, v):
    return {i: {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i} for i in range(9)}



########################
# Za oceno 7

def dolzina_poti(pot):
    return sum(abs((x1-x2)+(y1-y2)) for (x1, y1), (x2, y2) in zip(pot, pot[1:]))




def varen_premik(x0, y0, x1, y1, mine):
    return all([all([(x, y0) not in mine for x in range(x0, x1 + 1)]), all([(x, y0) not in mine for x in range(x0, x1 - 1, -1)]), all([(x0, y) not in mine for y in range(y0, y1 + 1)]), all([(x0, y) not in mine for y in range(y0, y1 - 1, -1)]), (x0, y0) not in mine])







def varna_pot(pot, mine):
        return all([all((x, y) not in mine for x, y in pot), all(varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))])




########################
# Za oceno 8

def polje_v_mine(polje):
    polje = list(polje.split())
    v = len(polje)
    y = 0
    koordinate = set()
    for vrstica in polje:
        x = 0
        for znak in list(vrstica):
            if znak == "X":
                koordinate.add((x, y))
            x += 1
        y += 1
    return (koordinate, x, v)




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


