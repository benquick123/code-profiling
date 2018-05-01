# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from itertools import product
from collections import defaultdict
from math import *
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
    counter = 0
    for x0, y0 in product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if ((x0, y0) in mine and (x0, y0) != (x, y)):
            counter = counter + 1
    return counter

def najvec_sosedov(mine, s, v):
    najvecji = 0
    coordinates = (0 , 0)
    for sirina, visina in product(range(s), range(v)):
        stevilo = sosedov(sirina, visina, mine)
        while stevilo > najvecji:
            najvecji = stevilo
            coordinates = (sirina, visina)
    return (coordinates)

def brez_sosedov(mine, s, v):
    my_set = set()
    for sirina, visina in product(range(s), range(v)):
        stevilo = sosedov(sirina, visina, mine)
        if stevilo == 0:
            my_set.add((sirina, visina))
    return my_set

def po_sosedih(mine, s, v):
    sosedi = defaultdict(set)
    moznosti = [(prva, druga) for prva in range(s) for druga in range(v)]
    for i in range(0, 9):
        sosedi[i]
    for terka1, terka2 in moznosti:
        stevilo = sosedov(terka1, terka2, mine)
        sosedi[stevilo].add((terka1, terka2))
    return dict(sosedi)


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


