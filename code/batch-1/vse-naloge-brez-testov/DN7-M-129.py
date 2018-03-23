__author__ = 'bj6205'
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

def vsa_polja_v_okolici(x, y):
    a = []
    for y1 in range(y-1, y+2):
        for x1 in range(x-1, x+2):
            a.append((x1, y1))
    return a

########################
# Za oceno 6


def sosedov(x, y, mine):
    stev = 0
    seznam = vsa_polja_v_okolici(x, y)
    for a in mine:
        if a in seznam and a != (x, y):
            stev += 1
    return stev

def najvec_sosedov(mine, s, v):
    naj = 0
    c = 0
    d = 0
    for a, b in vsa_polja(s, v):
        if sosedov(a, b, mine) > naj:
            naj = sosedov(a, b, mine)
            c = a
            d = b
    return c, d

def brez_sosedov(mine, s, v):
    seznam = set()
    for a,b in vsa_polja(s, v):
        if sosedov(a,b, mine) == 0:
            seznam.add((a,b))
    return seznam


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
    polja = vsa_polja(s, v)
    seznam = {i: set() for i in range(9)}
    for x,y in polja:
        i = sosedov(x, y, mine)
        seznam[i].update([(x,y)])
    return seznam
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
    stev = 0
    for a in range(len(pot)):
        x,y = pot[a]
        if a+1 < len(pot):
            x1, y1 = pot[a+1]
            stev += abs(x-x1 + y-y1)
    return stev

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
    a = x1, y1
    b = x0, y0
    if a in mine:
        return False
    if b in mine:
        return False
    if x0 == x1:
        if y0 < y1:
            for y in range(min(y0, y1+1), max(y0 ,y1+1)):
                a = (x0, y)
                if a in mine1:
                    return False
        else:
            for i in range(min(y0, y1+1), max(y0, y1+1)):
                a = (x0, i)
                if a in mine1:
                    return False
    elif y0 == y1:
        if x0 < x1:
            for i in range(min(x0,x1), max(x0,x1+1)):
                a = (i, y0)
                if a in mine1:
                    return False
        else:
            for i in range(min(x0,x1), max(x0,x1+1)):
                a = (i, y0)
                if a in mine1:
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
    for a in pot:
        if a in mine:
            return False
    for a in range(len(pot)):
        x,y = pot[a]
        if a+1 < len(pot):
            x1, y1 = pot[a+1]
            if varen_premik(x, y, x1, y1, mine) != True:
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
    seznam = polje.rsplit(" ")
    mine = set()
    s = len(seznam)
    v = len(seznam[0])
    for b in range(len(seznam)):
        for a, index in enumerate(seznam[b]):
            if index == "X":
                x = a
                y = b
                coords = x, y
                mine.add(coords)
    return mine, v, s


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


