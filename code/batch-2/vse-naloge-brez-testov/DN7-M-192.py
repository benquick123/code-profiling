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
    stevilo=0
    for koordinate in mine:
        x0, y0 = koordinate
        if (x0 == x + 1 or x0 == x - 1 or x0 == x) and (y0 == y + 1 or y0 == y - 1 or y0 == y):
            stevilo += 1
        if x0 == x and y0 == y:
            stevilo -= 1
    return stevilo
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


def najvec_sosedov(mine, s, v):
    max_sosedov = 0
    x0 = 0
    y0 = 0
    for y in range(v):
        for x in range(s):
            sosedi = sosedov(x, y, mine)
            if (sosedi > max_sosedov):
                max_sosedov = sosedi
                x0, y0 = x, y
    return (x0, y0)
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """


def brez_sosedov(mine, s, v):
    koordinate = set()
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) == 0:
                koordinate.add((x, y))
    return koordinate
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


def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(9):
        množice = set()
        for y in range(v):
            for x in range(s):
                if sosedov(x, y, mine) == i:
                    množice.add((x, y))
        slovar[i] = množice
    return slovar
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


########################
# Za oceno 7

def dolzina_poti(pot):
    import math
    dolzina = 0
    for i in range(0, len(pot) - 1, ):
        x, y = pot[i]
        x1, y1 = pot[i + 1]
        if x != x1:
            dolzina += math.sqrt((x1 - x) ** 2)
        if y != y1:
            dolzina += math.sqrt((y1 - y) ** 2)
    return int(dolzina)
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        if y0 < y1:
            max = y1
            min = y0
        else:
            max = y0
            min = y1
        for y in range(min, max + 1):
            if (x1, y) in mine:
                return False
    if y0 == y1:
        if x0 < x1:
            max = x1
            min = x0
        else:
            max = x0
            min = x1
        for x in range(min, max + 1):
            if (x, y1) in mine:
                return False
    return True
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
    if (len(pot)) == 1:
        x, y = pot[0]
        if varen_premik(x, y, x, y, mine) != True:
            return False
    for i in range(0, len(pot) - 1):
        x, y = pot[i]
        x1, y1 = pot[i + 1]
        if varen_premik(x, y, x1, y1, mine) != True:
            return False
    return True
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
    koordinate = polje.split(" ")
    tocke = set()
    x0 = len(koordinate[0])
    y0 = len(koordinate)
    i = 0
    for niz in koordinate:
        index = 0
        while index < len(niz):
            index = niz.find('X', index)
            if index == -1:
                break
            x = index
            y = i
            index += 1
            tocke.add((x, y))
        i += 1
    if "" in koordinate:
        y0 -= 1
    površina = (tocke, x0, y0)
    return površina
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


