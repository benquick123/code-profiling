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
    st = 0
    for a, b in mine:
        if (abs(x - a) == 1 or (abs(x - a) == 0 and y != b)) and (abs(y - b) == 1 or (abs(y - b) == 0 and x != a)):
            st += 1
    return st




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
    pr = 0
    dr = 0
    naj = 0
    for a in range(s):
        for b in range(v):
            if sosedov(a, b, mine) > naj:
                naj = sosedov(a, b, mine)
                pr = a
                dr = b
    return (pr,dr)



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
    mno = set()
    naj = 0
    for a in range(s):
        for b in range(v):
            if sosedov(a, b, mine) == naj:
                naj = sosedov(a, b, mine)
                pr = a
                dr = b
                c = (pr, dr)
                mno.add(c)
    return mno


import collections

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
    sl = {}
    for n in range(9):
        m = set()
        for a in range(s):
            for b in range(v):
                if sosedov(a, b, mine) == n:
                    m.add((a, b))
        sl[n] = m
    return sl


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
    st = 0
    for n in range(len(pot) - 1):
        st = st + abs(pot[n][0] - pot[n + 1][0]) + abs(pot[n][1] - pot[n + 1][1])

    return st


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
    for a in range((abs(x1 - x0) + abs(y1 - y0)) + 1):
        if x0 == x1 and y0 == y1:
            if (x0, y0) or (x1, y1) in mine:
                return False
        if x1 - x0 == 0 and y1 > y0:
            if (x0, y0 + a) in mine:
                return False
        elif x1 - x0 == 0 and y1 < y0:
            if (x0, y0 - a) in mine:
                return False
        elif y0 - y1 == 0 and x0 < x1:
            if (x0 + a, y0) in mine:
                return False
        elif y0 - y1 == 0 and x0 > x1:
            if (x0 - a, y0) in mine:
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
        if (pot[0][0], pot[0][1]) in mine:
            return False

    for n in range(len(pot) - 1):

        if varen_premik(pot[n][0], pot[n][1], pot[n + 1][0], pot[n + 1][1], mine) != True:
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
    a = polje
    mno = set()
    b = (a.split(" "))
    c = (len(a.split(" ")[0]))
    d = (len(a.split(" ")))

    for x in range(d):
        for e in range(c):
            if b[x][e] == "X":
                mno.add((e, x))
    return (mno, c, d)


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


