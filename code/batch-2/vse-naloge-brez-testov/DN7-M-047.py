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
    st_min = 0
    for mina in mine:
        x2 = mina[0]
        y2 = mina[1]
        razdalja = math.sqrt(pow(x - x2, 2) + pow(y - y2, 2))
        if razdalja != 0 and razdalja < 2:
            st_min+= 1

    return st_min


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
    max_polje  = (0, 0)
    max_st_min = 0
    for x in range(0, s):
        for y in range(0, v):
            st_min = sosedov(x, y, mine)
            if st_min > max_st_min:
                max_polje  = (x, y)
                max_st_min = st_min

    return max_polje

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
    seznam = set()
    for x in range(0, s):
        for y in range(0, v):
            st_min = sosedov(x, y, mine)
            if st_min == 0:
                seznam.add((x, y))

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
    seznam = {}
    for i in range(0, 9):
        seznam[i] = set()

    for x in range(0, s):
        for y in range(0, v):
            st_min = sosedov(x, y, mine)
            seznam[st_min].add((x, y))

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
    razdalja = 0
    for i in range(len(pot) - 1):
        koordinata  = pot[i]
        koordinata1 = pot[i + 1]
        if koordinata[0] == koordinata1[0]:
            razlika = abs(koordinata[1] - koordinata1[1])
        else:
            razlika = abs(koordinata[0] - koordinata1[0])
        razdalja += razlika

    return razdalja




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
    varno = True
    if x0 == x1:
        if y0 < y1:
            min = y0
            max = y1 + 1
            for y in range(min, max):
                if (x0, y) in mine:
                    varno = False
        else:
            min = y1
            max = y0 + 1
            for y in range(min, max):
                if (x0, y) in mine:
                    varno = False
    else:
        if x0 < x1:
            min = x0
            max = x1 + 1
            for x in range(min, max):
                if (x, y0) in mine:
                    varno = False
        else:
            min = x1
            max = x0 + 1
            for x in range(min, max):
                if (x, y0) in mine:
                    varno = False

    return varno

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    if len(pot) > 1:
        for i in range(len(pot) - 1):
            x0 = pot[i][0]
            y0 = pot[i][1]
            x1 = pot[i + 1][0]
            y1 = pot[i + 1][1]
            if not varen_premik(x0, y0, x1, y1, mine):
                return False
    elif len(pot) == 1:
        if pot[0] in mine:
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
    x = y = 0
    mine  = set()
    for i in range(len(polje)):
        if polje[i] == 'X':
            mine.add((x, y))

        if polje[i] == ' ' and i != len(polje) - 1:
            x = 0
            y = y + 1
        else:
            x += 1

        if polje[i] == ' ' and i == len(polje) - 1:
            x -= 1
    y += 1

    return (mine, x, y)


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


