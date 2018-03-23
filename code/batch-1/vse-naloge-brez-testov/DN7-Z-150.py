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
    sosedne = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1),(x + 1, y + 1)]
    r=0
    for a, b in sosedne:
        if (a, b) in mine:
            r = r + 1
    return r
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
    a=0
    b=0
    maxsos=0
    for (x, y) in vsa_polja(s, v):
        if sosedov(x, y, mine) > maxsos:
            a = x
            b = y
            maxsos=sosedov(x, y, mine)
    return (a, b)
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
    return {(x,y) for (x,y) in vsa_polja(s, v) if sosedov(x,y,mine) == 0}
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

def po_sosedih(mine, s, v):
    r = {i: set() for i in range(9)}
    for x, y in vsa_polja(s, v):
        r[sosedov(x, y, mine)].add((x, y))

    return r

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
    a="a"
    b="a"
    r=0
    for x,y in pot:
       if a == "a":
           a = x
           b = y
           continue
       r = r + abs(a + b - x - y)
       a=x
       b=y
    return r
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1 and y0 == y1:
        if (x0, y0) in mine:
            return False
    elif y0 == y1 and list(range(x1, x0+1)) == []:
        for x in list(range(x0, x1+1)):
            if (x, y0) in mine:
                return False
    elif x0 == x1 and list(range(y1, y0+1)) == []:
        for y in list(range(y0, y1+1)):
            if (x0, y) in mine:
                return False
    elif y0 == y1 and list(range(x0, x1+1)) == []:
        for x in list(range(x1, x0+1)):
            if (x, y0) in mine:
                return False
    elif x0 == x1 and list(range(y0, y1+1)) == []:
        for y in list(range(y1, y0+1)):
            if (x0, y) in mine:
                return False
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
    a="a"
    b="a"
    for x,y in pot:
        if (x, y) in mine:
            return False
        if a == "a":
            a=x
            b=y
            continue

        if varen_premik(a, b, x, y, mine) == False:
            return False
        else:
            a=x
            b=y
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
    x = polje.split(" ")
    y = len(x)
    z = len(x[0])
    r = set()
    for i in range(y):
        d=0
        for a in x[i]:
            if a == "X":
                r.add((d, i))
            d += 1
    return r, z, y
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


