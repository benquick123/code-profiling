def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6

def sosedov(x, y, mine):
    vrni = 0 #stevilo sosedov
    for koordinate in mine:
        if koordinate == (x, y+1):
            vrni += 1
        elif koordinate == (x, y-1):
            vrni += 1
        elif koordinate == (x+1, y):
            vrni += 1
        elif koordinate == (x+1, y+1):
            vrni += 1
        elif koordinate == (x+1, y-1):
            vrni += 1
        elif koordinate == (x-1, y-1):
            vrni += 1
        elif koordinate == (x-1, y):
            vrni += 1
        elif koordinate == (x-1, y+1):
            vrni += 1
    return vrni

def najvec_sosedov(mine, s, v):
    vrni = 0, 0
 #terka s koordinatama polja
    max = 0 #max stevilo sosedov
    for x1 in range(0, int(s)):
        for y1 in range(0, v):
            st_sosedov = sosedov(x1, y1, mine)
            if st_sosedov > max:
                max = st_sosedov
                vrni = x1, y1
    return vrni

def brez_sosedov(mine, s, v):
    vrni = set()
    for x1 in range(0, int(s)):
        for y1 in range(0, v):
            st_sosedov = sosedov(x1, y1, mine)
            if st_sosedov == 0:
                koordinate = x1, y1
                vrni.add(koordinate)
    return vrni


def po_sosedih(mine, s, v):
    vrni = {0: set() , 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set() }
    for x1 in range(0, int(s)):
        for y1 in range(0, int(v)):
            st_sosedov = sosedov(x1, y1, mine)
            koordinate = x1, y1
            vrni[st_sosedov].add(koordinate)
    return (vrni)


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


