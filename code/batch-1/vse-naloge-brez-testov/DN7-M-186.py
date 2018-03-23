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
    stevilo_min = 0
    for x1, y1 in mine:
        if (x == x1 +1 or x == x1 -1) and (y == y1 - 1 or y == y1 + 1):
            stevilo_min = stevilo_min + 1
        if (x == x1 and y == y1 - 1) or (x == x1 and y == y1 + 1):
            stevilo_min = stevilo_min + 1
        if (y == y1 and x == x1 + 1) or (y == y1 and x == x1 - 1):
            stevilo_min = stevilo_min + 1
    return stevilo_min




def najvec_sosedov(mine, s, v):
    vsa_polja = []
    g = 0
    x2 = y2 = 0
    for y in range(v):
        for x in range (s):
            z = (x, y)
            vsa_polja.append(z)
    for x1, y1 in vsa_polja:
        e = sosedov(x1,y1,mine)
        if e > g:
            g = e
            x2 = x1
            y2 = y1
    return (x2, y2)




def brez_sosedov(mine, s, v):
    vsa_polja = []
    h = set()
    for y in range(v):
        for x in range (s):
            z = (x, y)
            vsa_polja.append(z)
    for x1, y1 in vsa_polja:
        e = sosedov(x1,y1,mine)
        if e == 0:
            g = (x1, y1)
            h.add(g)
    return h

def po_sosedih(mine, s, v):
    slovar = {}
    for x in range(0, 9):
        slovar[x] = set()
    for z in range(s):
        for y in range(v):
            x1 = sosedov(z, y, mine)
            slovar[x1].add((z, y))
    return slovar

########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    """
    Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.

    Args:
        x0 (int): koordinata x začetnega polja
        y0 (int): koordinata y začetnega polja
        x1 (int): koordinata x končnega polja
        y1 (int): koordinata y končnega polja
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je premik varen, `False`, če ni.
    """


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


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


