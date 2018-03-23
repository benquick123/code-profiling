# coding=utf-8
from math import *


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


def evklidska(x, y, x1, y1):
    e = sqrt(pow((x - x1), 2) + pow((y - y1), 2))
    return e


# 1.Naloga
def sosedov(x, y, mine):
    mina = 0
    for x1, y1 in mine:
        if 0 < evklidska(x, y, x1, y1) <= sqrt(2):
            mina = mina + 1
    return mina


def najvec_sosedov(mine, s, v):
    max = 0
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    while x < s:
        while y < v:
            sosedi = sosedov(x, y, mine)
            if sosedi > max:
                max = sosedi
                x1 = x
                y1 = y
            y += 1
        x += 1
        y = 0
    return x1, y1


def brez_sosedov(mine, s, v):
    brez = set()
    x = 0
    y = 0
    while x < s:
        while y < v:
            sosedi = sosedov(x, y, mine)
            if sosedi == 0:
                x_y = (x, y)
                brez.add(x_y)
            y += 1
        y = 0
        x += 1
    return brez


def po_sosedih(mine, s, v):
    vse_koordinate = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
    x = 0
    y = 0
    while x < s:
        while y < v:
            x_y = (x, y)
            vse_koordinate[sosedov(x, y, mine)].add(x_y)
            y += 1
        y = 0
        x += 1
    return vse_koordinate


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


