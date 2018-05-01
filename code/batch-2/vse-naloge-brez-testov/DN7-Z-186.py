def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

def sosedov(x, y, mine):
   i = 0
   for a,b in mine:
       if a in range(x-1, x+2) and b in range(y-1, y+2) and (a,b) != (x,y):
           i +=1
   return i

def najvec_sosedov(mine, s, v):
    m = 0
    for x,y in vsa_polja(s,v):
        if sosedov(x, y, mine) >= m:
            m = sosedov(x, y, mine)
            a = x
            b = y
    return (a, b)

def brez_sosedov(mine, s, v):
    brez = set()
    for x,y in vsa_polja(s, v):
        if sosedov(x, y, mine) == 0:
            brez.add((x,y))
    return brez

def po_sosedih(mine, s, v):
    pos = {}
    for a in range(9):
        pos[a] = {(x,y) for x,y in vsa_polja(s,v) if a == sosedov(x,y, mine)}
    return pos

def dolzina_poti(pot):
    i = 0
    while i < len(pot):
        if pot[i][0] == pot[i+1][0]:
            d = abs(pot[i][1] - pot[i+1][1])
        else:
            d = abs(pot[i][0] - pot[i+1][0])
        i += 1
    return d


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


