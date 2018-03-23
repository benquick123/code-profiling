# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

import collections
mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

def sosedov(x, y, mine):
    okolica = ((x - 1, y - 1),(x - 1, y),(x - 1, y + 1), (x, y - 1),(x, y + 1), (x+ 1, y - 1), (x + 1, y), (x + 1, y + 1,))
    stevilo_sosedov = set()
    for m in mine:
        for o in okolica:
            if m == o:
                stevilo_sosedov.add(o)
            else:
                None
    return len(list(stevilo_sosedov))

def najvec_sosedov(mine, s, v):
    bum = 0
    koordinate = (0,0)
    for x,y in vsa_polja(s,v):
        if sosedov(x,y,mine) > bum:
            bum = sosedov(x,y,mine)
            koordinate = (x,y)
    return koordinate


def brez_sosedov(mine, s, v):
    g = set()
    bum = 0
    for x,y in vsa_polja(s,v):
        if sosedov(x,y,mine) == bum:
            bum = sosedov(x,y,mine)
            koordinate = x,y
            g.add(koordinate)
    return (g)

def po_sosedih(mine, s, v):
    slovar = collections.defaultdict(list)
    for g in range(0,9):
        for x,y in vsa_polja(s,v):
            if g not in slovar:
                slovar[g] = set()
            if sosedov(x,y,mine) == g:
                slovar[g].add((x,y))
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


