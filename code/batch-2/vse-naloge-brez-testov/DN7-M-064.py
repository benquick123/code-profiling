# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from collections import defaultdict
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
    c = 0
    for e in mine:
        if e[0] + 1 == x and e[1] + 1 == y:
            c += 1
        if e[0] - 1 == x and e[1] - 1 == y:
            c += 1
        if e[0] - 1 == x and e[1] + 1 == y:
            c += 1
        if e[0] + 1 == x and e[1] - 1 == y:
            c += 1
        if e[0] == x and e[1] + 1 == y:
            c += 1
        if e[0] + 1 == x and e[1] == y:
            c += 1
        if e[0] - 1 == x and e[1] == y:
            c += 1
        if e[0] == x and e[1] - 1 == y:
            c += 1
    return c


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
    c = 0
    t = (0,0)
    for i in range(s):
        for d in range(v):


         if sosedov(i, d, mine) > c:
             c = sosedov(i, d, mine)
             t = (i, d)

    return t

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
    k = []

    for i in range(s):
        for d in range(v):

            if sosedov(i, d, mine) == 0:
                g = (i, d)
                k.append(g)

    return set(k)

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
    k = defaultdict(list)
    for i in range(s):
        for d in range(v):
            for o in range(9):
                if sosedov(i, d, mine) == o:
                    g = (i, d)
                    k[o].append(g)
    for r in range(9):

        k[r] = set(k[r])

    return k

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
    x = 0
    for e in zip(pot, pot[1::]):

        a = abs(e[0][0] - e[1][0])
        b = abs(e[0][1] - e[1][1])
        s = a + b
        x += s


    return x

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
    a = abs(x0 - x1)
    b = abs(y0 - y1)
    if x0 == x1:
        for i in range(b + 1):
            g = (x0, min(y0, y1) + i)
            if g in mine:
                return False
    if y0 == y1:
        for o in range(a + 1):
            f = (min(x0, x1) + o, y0)
            if f in mine:
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
    for t in pot:
        if t in mine:
            return False
    if len(pot) <= 1:
            return True
    for e in zip(pot, pot[1::]):



        a = varen_premik(e[0][0], e[0][1], e[1][0], e[1][1], mine)
        if a == False:
            return a
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
    a = polje.split(" ")
    x = 0
    s = []
    r = len(a)
    for p in a:
        t = len(p)



    i = 0
    for o in a:
        for e in o:



            if e == ".":
                x += 1
                if x >= t:
                    x = 0
                    i += 1
            elif e == "X":
                g = (x, i)
                s.append(g)



                x += 1
                if x >= t:
                    x = 0
                    i += 1

    return set(s), t, r

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


