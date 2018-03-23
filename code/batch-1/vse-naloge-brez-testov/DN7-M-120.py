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
    z = 0
    for mina in mine:
        if mina[0] == x:
            if mina[1] == (y + 1) or mina[1] == (y - 1):
                z += 1
        elif mina[0] == (x + 1) or mina[0] == (x - 1):
            if mina[1] == (y + 1) or mina[1] == (y - 1) or mina[1] == y:
                z += 1
    return z

def najvec_sosedov(mine, s, v):
    koordinati = (0, 0)
    max = 0
    for x in range(0, s):
        for y in range(0, v):
            z = sosedov(x, y, mine)
            if z > max:
                max = z
                koordinati = (x, y)
    return koordinati

def brez_sosedov(mine, s, v):
    seznam = set()
    for x in range(0, s):
        for y in range(0, v):
            z = sosedov(x, y, mine)
            if z == 0:
                seznam.add((x, y))
    return seznam

def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(0, 9):
        slovar[i] = set()
    for x in range(0, s):
        for y in range(0, v):
            z = sosedov(x, y, mine)
            slovar[z].add((x, y))
    return slovar

def dolzina_poti(pot):
    if pot:
        print(pot[0][0])
        x0 = pot[0][0]
        y0 = pot[0][1]
        d = 0
        for x, y in pot:
            x1 = abs(x - x0)
            y1 = abs(y - y0)
            d += x1 + y1
            x0 = x
            y0 = y
        return d
    return 0

def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        for x, y in mine:
            if y0 <= y1:
                if x == x0 and y <= y1 and y >= y0:
                    return False
            else:
                if x == x0 and y >= y1 and y <= y0:
                    return False
    elif y0 == y1:
        for x, y in mine:
            if x0 <= x1:
                if y == y0 and x <= x1 and x >= x0:
                    return False
            else:
                if y == y0 and x >= x1 and x <= x0:
                    return False
    return True

def varna_pot(pot, mine):
    if pot:
        x0 = pot[0][0]
        y0 = pot[0][1]
        for x1, y1 in pot:
            if not varen_premik(x0, y0, x1, y1, mine):
                return False
            x0 = x1
            y0 = y1
    return True

def polje_v_mine(polje):
    mnozica = set()
    vrstice = polje.split(" ")
    y = len(vrstice)
    x = len(vrstice[0])
    for i in range(0, y):
        for j in range(0, x):
            if polje.split(" ")[i][j] == 'X':
                mnozica.add((j, i))
    return (mnozica, x, y)


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


