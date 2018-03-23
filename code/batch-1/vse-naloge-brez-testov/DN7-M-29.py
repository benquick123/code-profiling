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
    stmin = 0
    for a, b in mine:
        if x-1 == a and y-1 == b:
            stmin += 1
        if x == a and y-1 == b:
            stmin += 1
        if x+1 == a and y-1 == b:
            stmin += 1
        if x-1 == a and y == b:
            stmin += 1
        if x+1 == a and y == b:
            stmin += 1
        if x-1 == a and y+1 == b:
            stmin += 1
        if x == a and y+1 == b:
            stmin += 1
        if x+1 == a and y+1 == b:
            stmin += 1
    return stmin

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
    najvec = 0
    najs = 0
    najv = 0
    for c in range(s):
        for d in range(v):
            st = sosedov(c,d, mine)
            if st > najvec:
                najs = c
                najv = d
                najvec = st
    return (najs, najv)

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
    a = tuple()
    rez = set()
    for c in range(s):
        for d in range(v):
            st = sosedov(c,d, mine)
            if st == 0:
                a = (c,d)
                rez.add(a)
    return rez

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

def po_sosedihHelp(mine, s, v, h):
    a = tuple()
    rez = set()
    for c in range(s):
        for d in range(v):
            st = sosedov(c,d, mine)
            if st == h:
                a = (c,d)
                rez.add(a)
    return rez

def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(9):
        slovar[i] = set()
    for n in range(9):
        slovar[n] = po_sosedihHelp(mine, s, v, n)
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
    dolzina = 0
    a = -1
    b = -1
    for c, d in pot:
        if a < 0:
            a = c
            b = d
        elif c == a:
            dolzina += abs(d - b)
            a = c
            b = d
        elif d == b:
            dolzina += abs(c - a)
            a = c
            b = d
    return dolzina

    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    for a,b in mine:
        if a == x0 and b == y0 or a == x1 and b == y1:
            return False
        elif x0 == x1:
            if y0 < y1:
                for i in range(y0, y1):
                    if x0 == a and i == b:
                        return False
            else:
                for i in range(y1, y0):
                    if x0 == a and i == b:
                        return False
        elif y0 == y1:
            if x0 < x1:
                for j in range(x0,x1):
                    if j == a and y0 == b:
                        return False
            else:
                for j in range(x1,x0):
                    if j == a and y0 == b:
                        return False
    else:
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
    c = -1
    d = -1
    for a,b in pot:
        if c < 0:
            c = a
            d = b
            for g,h in mine:
                if c == g and d == h:
                    return False
        elif varen_premik(c, d, a, b, mine):
            c = a
            d = b
            continue
        else:
            return False
    else:
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
    polje = polje.rstrip()
    s = 0
    v = 0
    mine = set()
    for i in polje:
        if i == ".":
            s += 1
        elif i == "X":
            a = (s,v)
            mine.add(a)
            s += 1
        elif i == " ":
            s = 0
            v += 1
    if s == 0:
        s = 1
    return mine, s, v+1


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


