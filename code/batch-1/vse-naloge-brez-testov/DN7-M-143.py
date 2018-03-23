#coding=utf-8
#from __future__ import unicode_literals
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


########################x2 == x or x2 == x - 1 or x2 == x + 1) and (y2 == y or y2 == y + 1 or y2 == y - 1
# Za oceno 6

def sosedov(x, y, mine):
    """
    Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
    Polje samo ne šteje.

    Args:
        x (int): koordinata x
        y (int): koordinata y
        mine (set of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """

    return len([1 for x2, y2 in mine if (x2 == x or x2 == x - 1 or x2 == x + 1) and (y2 == y or y2 == y + 1 or y2 == y - 1) and (y2 != y or x2 != x)])


def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja .get(sosedov(x, y, vsa_polja(s, v)))

    """
    return {sosedov(x, y, mine) : (x, y) for x, y in vsa_polja(s, v)}.get(max(  sosedov(x, y, mine) for x, y in vsa_polja(s, v)  ))



def brez_sosedov(mine, s, v):
    """
    Vrni množico koordinat polj brez min na sosednjih poljih. Polje samo lahko
    vsebuje mino.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        set of tuple: polja brez min na sosednjih poljih
    """

    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        dict: (glej zgoraj)
    """

    return {i : {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i}  for i in range(9)}

########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.      pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti

        aja kle bi loh un zip uporabu
    """

    return sum([    (abs(pot[i][0] - pot[i-1][0]) + abs(pot[i][1] - pot[i-1][1])) for i in range(1, len(pot))    ])

def varen_premik(x0, y0, x1, y1, mine):
    """
    Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.

    Args:
        x0 (int): koordinata x začetnega polja
        y0 (int): koordinata y začetnega polja
        x1 (int): koordinata x končnega polja
        y1 (int): koordinata y končnega polja
    print([ False for x, y in ([(x0 + i, y0) for i in range(0, x1 - x0) if y0 == y1] + [(x0, y0 + i) for i in range(0, y1 - y0) if x0 == x1])   if ({x, y} in mine) ] + [ True for x, y in ([(x0 + i, y0) for i in range(0, x1 - x0) if y0 == y1] + [(x0, y0 + i) for i in range(0, y1 - y0) if x0 == x1])   if not(({x, y} in mine)) ])


        mine (set of tuple of int): koordinate min
+ [ True for x, y in ([(x0 + i, y0) for i in range(0, x1 - x0) if y0 == y1] + [(x0, y0 + i) for i in range(0, y1 - y0) if x0 == x1])   if not(({x, y} in mine)) ]
    Returns:
        bool: `True`, če je premik varen, `False`, če ni.          if not({x0 + i, y} in mine)
    """
    return            all([ False for x, y in ([(x0 + i, y0) for i in range(0, x1 - x0) if y0 == y1] + [(x0, y0 + i) for i in range(0, y1 - y0) if x0 == x1])   if ({x, y} in mine) ] )



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


