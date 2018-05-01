########################
# Za oceno 6

def sosedov(x, y, mine):
    stevec = 0
    for a, b in mine:
        if (abs(y - b) == 1 or (abs(y - b) == 0 and x != a)) and (abs(x - a) == 1 or (abs(x - a) == 0 and y != b)):
            stevec += 1
    return stevec


def najvec_sosedov(mine, s, v):

    najvecje_stevilo = 0
    koordinata1 = 0
    koordinata2 = 0
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) > najvecje_stevilo:
                najvecje_stevilo = sosedov(x, y, mine)
                koordinata1 = x
                koordinata2 = y
    return (koordinata1, koordinata2)


def brez_sosedov(mine, s, v):
    mnozica = set()
    najvecja = 0
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == najvecja:
                najvecja = sosedov(x, y, mine)
                koordinata1 = x
                koordinata2 = y
                tocka = (koordinata1, koordinata2)
                mnozica.add(tocka)
    return mnozica

def po_sosedih(mine, s, v):
    slovar = {}
    mnozica = set()
    for i in range(9):
        for x in range(s):
            for y in range(v):
                stevilo_sosedov = sosedov(x, y, mine)
                if stevilo_sosedov == i:
                    mnozica.add((x, y))
        slovar[i] = mnozica
        mnozica = set()

    return slovar

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


