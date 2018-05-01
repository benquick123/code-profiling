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

import math

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
    return sum([True for mina in mine if 1 <= math.sqrt((mina[0] - x) ** 2 + (mina[1] - y) ** 2) <= math.sqrt(2)])


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
    return [(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == max([sosedov(x, y, mine) for x, y in vsa_polja(s, v)])][0]


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
    return {num : set([(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == num]) for num in range(9)}

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
    return sum([abs(sum(pot[i]) - sum(pot[i + 1])) for i in range(len(pot) - 1)])

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
    return False if False in [False for polje in [(min(x0, x1) + i, min(y0, y1) + j) for i in range(abs(x0 - x1) + 1) for j in range(abs(y0 - y1) + 1)] if polje in mine] else True

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return False if (False in [varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine) for i in range(len(pot) - 1)] or (len(pot) == 1 and pot[0] in mine)) else True

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
    grid = str.split(polje)
    mine = set()
    for v in range(len(grid)):
        for s in range(len(grid[v])):
            if grid[v][s] == 'X':
                mine.add((s, v))
    return mine, len(grid[0]), len(grid)


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
    smer = 0
    x = 0
    y = 0
    seznam_polj = [(0, 0)]
    for ukaz in str.split(ukazi):
        if ukaz == 'DESNO':
            smer =(smer + 1) % 4
        elif ukaz == 'LEVO':
            if smer > 0:
                smer -= 1
            else:
                smer = 3
        else:
            if smer == 0:
                y -= int(ukaz)
            elif smer == 1:
                x += int(ukaz)
            elif smer == 2:
                y += int(ukaz)
            else:
                x -= int(ukaz)

            seznam_polj.append((x, y))

    return seznam_polj


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    seznam_ukazov = list()
    smer = 0
    for i in range(len(pot) - 1):
        if pot[i][0] > pot[i + 1][0]:
            while smer != 3:
                seznam_ukazov.append("DESNO")
                smer = (smer + 1) % 4
            seznam_ukazov.append(str(abs(pot[i][0] - pot[i + 1][0])))
        if pot[i][0] < pot[i + 1][0]:
            while smer != 1:
                seznam_ukazov.append("DESNO")
                smer = (smer + 1) % 4
            seznam_ukazov.append(str(abs(pot[i][0] - pot[i + 1][0])))
        if pot[i][1] < pot[i + 1][1]:
            while smer != 2:
                seznam_ukazov.append("DESNO")
                smer = (smer + 1) % 4
            seznam_ukazov.append(str(abs(pot[i][1] - pot[i + 1][1])))
        if pot[i][1] > pot[i + 1][1]:
            while smer != 0:
                seznam_ukazov.append("DESNO")
                smer = (smer + 1) % 4
            seznam_ukazov.append(str(abs(pot[i][1] - pot[i + 1][1])))
    return ' '.join(seznam_ukazov)


