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
    """
    for koor_x in range(x-1, x+2):
        for koor_y in range(y-1, y+2):
            if (koor_x, koor_y) in mine and not (koor_x == x and koor_y == y):
                stevec_sosedov += 1
    """

    #return stevec_sosedov
    return sum(1 for koor_x in range(x-1, x+2) for koor_y in range(y-1, y+2) if (koor_x, koor_y) in mine and not (koor_x == x and koor_y == y))

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

    najvec_sosedkov = 0
    for x,y in vsa_polja(s, v):
        if sosedov(x, y, mine) >= najvec_sosedkov:
            najvec_sosedkov = sosedov(x, y, mine)
            tocka_najvec = (x,y)
    return tocka_najvec


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
    """
    res_mnozica = set()
    for x,y in vsa_polja(s, v):
        if not sosedov(x, y, mine):
            res_mnozica.add((x,y))

    return res_mnozica
    """
    return {(x,y) for x,y in vsa_polja(s, v) if not sosedov(x, y, mine)}

from collections import defaultdict

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

    prazen_slovar = defaultdict(int)

    for i in range (9):
        res_mnozica = set()
        for x, y in vsa_polja(s, v):
            if i == sosedov(x, y, mine):
                res_mnozica.add((x,y))
        prazen_slovar[i] = res_mnozica

    return prazen_slovar


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
    """
    stevec_poti = 0
    for (x1,y1),(x2, y2) in zip(pot, pot[1:]):
        stevec_poti+=abs(x2-x1) + abs(y2-y1)
        
        ali
        
        if x1 == x2:
            stevec_poti += abs(y2-y1)
        elif y1 == y2:
            stevec_poti += abs(x2-x1)
        
    return stevec_poti
    """
    return sum(abs(x2-x1) + abs(y2-y1) for (x1,y1),(x2, y2) in zip(pot, pot[1:]))

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

    for x, y in mine:
        if ((x0 == x1 == x) and ((y0 <= y <= y1) or (y1 <= y <= y0))) or ((y0 == y1 == y) and ((x0 <= x <= x1) or (x1 <= x <= x0))):
            return False
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
    for (x1, y1), (x2, y2) in zip(pot, pot[1:]):
        if not varen_premik(x1, y1, x2, y2, mine):
            return False

    if len(pot) == 1 and pot[0] in mine:
        return False
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
    prazen_seznam = []
    resitev = []
    mnozica = set()
    prazen_seznam = polje.split()
    s = len(prazen_seznam[0])
    v = len(prazen_seznam)
    for y in range (v):
        for x in range (s):
            if prazen_seznam[y][x] == "X":
                mnozica.add((x,y))

    return (mnozica, s, v)
    #return ({(x,y) for y in range (len(polje.split())) for x in range (len(polje.split()[0])) if polje.split()[y][x] == "X"}, len(polje.split()[0]), len(polje.split()))

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


