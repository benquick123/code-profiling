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
    sos = 0
    if (x-1, y) in mine:
        sos += 1

    if (x, y-1) in mine:
        sos += 1

    if (x-1, y-1) in mine:
        sos += 1

    if (x+1, y) in mine:
        sos += 1

    if (x, y+1) in mine:
        sos += 1

    if (x+1, y+1) in mine:
        sos += 1

    if (x-1, y+1) in mine:
        sos += 1

    if (x+1, y-1) in mine:
        sos += 1

    return sos

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
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """
    m = {}
    naj = 0
    najk = (0,0)
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) > naj:
                naj = sosedov(x, y, mine)
                najk = (x, y)
    return najk


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
    brez = set()
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) == 0:
               brez.add((x,y))
    return brez



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
    pos = {}
    a = set()
    for i in range(9):
        for y in range(v):
            for x in range(s):
                if sosedov(x, y, mine) == i:
                    a.add((x, y))
        pos[i] = a
        a = set()
    return pos

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
    if not pot:
        return 0

    x2, y2 = pot[0]
    dol = 0
    for x, y in pot:
        dol += abs(x2-x) + abs(y2-y)
        x2 = x
        y2 = y
    return dol

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

    if x0 == x1 and y0 < y1:
        for i in range(y0,y1+1):
            if (x0, i) in mine:
                return False

    if x0 == x1 and y0 > y1:
        for i in range(y1,y0+1):
            if (x0, i) in mine:
                return False

    if y0 == y1 and x0 < x1:
        for i in range(x0,x1+1):
            if (i, y0) in mine:
                return False

    if y0 == y1 and x0 > x1:
        for i in range(x1,x0+1):
            if (i, y0) in mine:
                return False

    if y0 == y1 and x0 == x1:
        if (x0, y0) in mine:
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
    if len(pot) == 1:
        x, y = pot[0]
        if (x, y) in mine:
            return False
        else:
            return True

    for i in range(len(pot)-1):
        x0, y0 = pot[i]
        x1, y1 = pot[i+1]
        if not varen_premik(x0,y0,x1,y1,mine):
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

    mine = set()
    v = 0
    polja = polje.split(" ")
    for pol in polja:
        s = len(pol)
        for i in range(len(pol)):
            if pol[i] == "X":
                mine.add((i, v))
        v += 1

    return mine, s, v

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


