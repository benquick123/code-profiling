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

# 1.)
def sosedov(x, y, mine):
    stevilo_sosedov = 0
    for x2,y2 in mine:
        if x2 in range(x-1,x+2) and y2 in range(y-1,y+2) and (x != x2 or y != y2):
            stevilo_sosedov += 1
    return stevilo_sosedov

# 2.)
def najvec_sosedov(mine, s, v):
    st_sosedov = 0
    polje = vsa_polja(s, v)
    for x, y in polje:
        sosed = sosedov(x, y, mine)
        if st_sosedov < sosed:
            st_sosedov = sosed
            x2 = x
            y2 = y
    if st_sosedov:
        return x2, y2
    else:
        return x, y

# 3.)
def brez_sosedov(mine, s, v):
    brez_sosedov = set()
    polje = vsa_polja(s, v)
    for x, y in polje:
        sosed = sosedov(x, y, mine)
        if sosed == 0:
            koord = (x, y)
            brez_sosedov.add(koord)
    return brez_sosedov

# 4.)
def po_sosedih(mine, s, v):
    vse_mine = {}
    for i in range (0,9):
        mnozica = set()
        for x, y in vsa_polja(s, v):
            if sosedov(x, y, mine) == i:
               mnozica.add((x, y))
        vse_mine[i] = mnozica
    return vse_mine

########################
# Za oceno 7

# 1.)
def dolzina_poti(pot):
    i, dolzina = 0, 0
    while i < len(pot)-1:
        dolzina += abs(sum(pot[i+1]) - sum(pot[i]))
        i += 1
    return dolzina

# 2.)
def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        abs(y0 - y1)

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

