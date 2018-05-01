import collections
import math

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
    return sum(x in mine for x in [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)])



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
    return collections.Counter({c: sosedov(c[0], c[1], mine) for c in vsa_polja(s, v)}).most_common(1)[0][0]

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
    return {c for c in vsa_polja(s, v) if sosedov(c[0], c[1], mine) == 0 }


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
    return {i:{c for c in vsa_polja(s, v) if sosedov(c[0], c[1], mine) == i } for i in range(9)}




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
    return sum(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2) for x, y in zip(pot, pot[1:]))


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
    return not any([x in mine for x in ([(x0, i) for i in range(min(y0,y1), max(y0, y1) + 1)] if x0 == x1 else [(i,y0) for i in range(min(x0, x1), max(x0, x1)+1)])])

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

    return all(varen_premik(x[0], x[1], y[0], y[1], mine) for x, y in zip(pot, pot[1:])) if len(pot) != 1 else not pot[0] in mine



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
    return {(i, vrstica) for vrstica, niz in enumerate(polje.split()) for i, j in enumerate(niz) if j == 'X'},len(polje.split()[0]), len(polje.split())


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
    smer = (0, -1)
    lega = (0,0)
    seznam = [(0,0)]
    sloD = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
    sloL = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
    for x in ukazi.split('\n'):
        if x == 'LEVO' or x == 'DESNO':
            smer = sloD[smer] if x == 'DESNO' else sloL[smer]
        else:
            lega = (lega[0] + smer[0]*int(x), lega[1] + smer[1]*int(x))
            seznam.append(lega)
    return seznam



def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    niz = ''
    smer = (0,-1)
    sloD = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
    for x in ((y[0]-x[0], y[1]-x[1]) for x, y in zip(pot,pot[1:])):
        smer1 = (x[0]/(abs(x[0]) or 1),x[1]/(abs(x[1]) or 1))
        while smer1 != smer:
            niz+='\nDESNO'
            smer = sloD[smer]
        niz= niz + '\n' + str(max(x) if max(x) > 0 else abs(min(x)))
    return niz[1:]















