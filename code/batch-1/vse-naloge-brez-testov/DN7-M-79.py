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
    stev = 0
    for i, j in mine:
        if (i + 1 == x or i - 1 == x or i == x) and (j + 1 == y or j - 1 == y or j == y) and (i != x or j != y):
            stev += 1
    return stev


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
    xy = []
    for x in range(s):
        for y in range(v):
            xy.append((x, y))
    naj = []
    polje = (0, 0)
    najvec = 0
    for x, y in xy:
        stev = 0
        for i, j in mine:
                if i <= s and j <= v:
                    if (i + 1 == x or i - 1 == x or i == x) and (j + 1 == y or j - 1 == y or j == y) and (i != x or j != y):
                        stev += 1
        if stev > najvec:
            najvec = stev
            naj.append((x, y))
    for item in naj:
        polje = item
    return polje


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
    xy = []
    for x in range(s):
        for y in range(v):
            xy.append((x, y))
    polje = set()
    for x, y in xy:
        stev = 0
        for i, j in mine:
                if i <= s and j <= v:
                    if (i + 1 == x or i - 1 == x or i == x) and (j + 1 == y or j - 1 == y or j == y) and (i != x or j != y):
                        stev += 1
        if stev == 0:
            polje.add((x, y))
    return polje


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
    xy = []
    for x in range(s):
        for y in range(v):
            xy.append((x, y))
    polje0 = set()
    polje1 = set()
    polje2 = set()
    polje3 = set()
    polje4 = set()
    polje5 = set()
    polje6 = set()
    polje7 = set()
    polje8 = set()
    for x, y in xy:
        stev = 0
        for i, j in mine:
                if i <= s and j <= v:
                    if (i + 1 == x or i - 1 == x or i == x) and (j + 1 == y or j - 1 == y or j == y) and (i != x or j != y):
                        stev += 1
        if stev == 0:
            polje0.add((x, y))
        elif stev == 1:
            polje1.add((x, y))
        elif stev == 2:
            polje2.add((x, y))
        elif stev == 3:
            polje3.add((x, y))
        elif stev == 4:
            polje4.add((x, y))
        elif stev == 5:
            polje5.add((x, y))
        elif stev == 6:
            polje6.add((x, y))
        elif stev == 7:
            polje7.add((x, y))
        elif stev == 8:
            polje8.add((x, y))

        slovar = {0: polje0, 1: polje1, 2: polje2, 3: polje3, 4: polje4, 5: polje5, 6: polje6, 7: polje7, 8: polje8}
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


