# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from math import sqrt
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
    neighbours = 0
    for ix, iy in mine:
        dist = sqrt((x - ix) ** 2 + (y - iy) ** 2)
        if dist == 1 or dist == sqrt(2):
            neighbours += 1
    return neighbours

    #return sum([1 for ix, iy in mine if sqrt((x - ix) ** 2 + (y - iy) ** 2) <= 1])    #abs(y - iy) == 1 or abs(x - ix) == 1]

"""def st_sosed(mine, s, v):
    return {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}"""

def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """
    neighbours = {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}
    for i in neighbours:
        if max(neighbours.values()) == neighbours[i]:
            a = i
    return a



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
    neighbours = {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}
    return {i for i in neighbours if neighbours[i] == 0}


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
    #neighbours = st_sosed(mine, s, v)
    """ngb = {}
    for i in range(8):
        ngb[i] = set()
        for j in neighbours:
            if neighbours[j] == i:
                ngb[i].add(j)
    return ngb"""
    neighbours = {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}
    return {i: {a for a in neighbours if neighbours[a] == i} for i in range(9)}


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
    steps = 0
    for i in range(1, len(pot)):
        x0, y0 = pot[i]
        x1, y1 = pot[i - 1]
        steps += abs(x0 - x1) + abs(y0 - y1)
    return steps


"""def premik(x0, y0, x1 = 0, y1 = 0):
    if y0 == y1:
        x = [x0, x1]
        p, c = (min(x), max(x))
        pot = [(x, y0) for x in range(p, c + 1)]
    else:
        y = [y0, y1]
        p, c = (min(y), max(y))
        pot = [(x0, y) for y in range(p, c + 1)]
    return pot"""


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
    #mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

    if y0 == y1:
        p = min([x0, x1])
        c = max([x0, x1])
        pot = [(x, y0) for x in range(p, c + 1)]
    else:
        p = min([y0, y1])
        c = max([y0, y1])
        pot = [(x0, y) for y in range(p, c + 1)]


    for polje in pot:
        if polje in mine:
            return False
    else:
        return True


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    if len(pot):
        nova_pot = [pot[0]]
        for i in range(len(pot) - 1):
            x0, y0 = pot[i]
            x1, y1 = pot[i + 1]
            if y0 == y1:
                x = [x0, x1]
                p, c = (min(x), max(x))
                premik = [(x, y0) for x in range(p, c + 1)][1:]
            else:
                y = [y0, y1]
                p, c = (min(y), max(y))
                premik = [(x0, y) for y in range(p, c + 1)][1:]
            nova_pot.append(pot[i])
            nova_pot += premik
    else:
        nova_pot = pot

    for polje in nova_pot:
        if polje in mine:
            return False
    else:
        return True

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


