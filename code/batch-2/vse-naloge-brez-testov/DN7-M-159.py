import collections

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
    return len([42 for x0, y0 in mine if abs(x0 - x) <= 1 and abs(y0 - y) <= 1 and (x0, y0) != (x, y)])



# def najvec_sosedov(mine, s, v):
#     """
#     Vrni koordinati polja z največ sosednjih min
#
#     Args:
#         mine (set of (int, int)): koordinate min
#         s (int): širina polja
#         v (int): višina polja
#
#     Returns:
#         tuple of int: koordinati polja
#
#     """
#     return {sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}[max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)})]


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
    return max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}.items())[1]



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
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}


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
    return {i: set(elementi) for i, elementi in enumerate([[(x, y) for x, y in vsa_polja(s, v) \
                                                            if sosedov(x, y, mine) == j] for j in range(9)])}
#   Hahaha sigurn sm cist zakompliciru


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
    # dolzina = 0
    # for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
    #     dolzina += abs(x0 - x1) + abs(y0 - y1)
    # return dolzina
    return sum([abs(x0 - x1) + abs(y0 - y1) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])


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
    return not any([(x, y) in mine for x in range(min(x0, x1), max(x0, x1) + 1) for y in range(min(y0, y1), max(y0, y1) +1)])

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return pot[0] not in mine if len(pot) == 1 else True if len(pot) == 0 else all(varen_premik(x0, y0, x1, y1, mine)
           for (x0, y0), (x1, y1) in zip(pot, pot[1:]))



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
    v = -1
    s = -1
    mine = set()
    for vrsta in polje.split():
        v += 1
        s = -1
        for znak in vrsta:
            s += 1
            if znak == "X":
                mine.add((s, v))
    return mine, s + 1, v + 1


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
    pot = [(0, 0)]
    smer = 2 #2 y pada, 0 y narasca, 1 x narasca, 3 x pada
    sukazi = ukazi.split()
    x = 0
    y = 0
    for ukaz in sukazi:
        if ukaz == "DESNO":
            smer = (smer + 1) % 4
        elif ukaz == "LEVO":
            smer = abs((smer - 1) % 4)
        else:
            if smer == 0:
                y += int(ukaz)
            elif smer == 1:
                x -= int(ukaz)
            elif smer == 2:
                y -= int(ukaz)
            elif smer == 3:
                x += int(ukaz)
            pot.append((x, y))
    return pot



def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    ukazi = ""
    smer = 0 #y pada, 2 y narasca, 1 x narasca, 3 x pada
    for ((x0, y0), (x1, y1)) in zip(pot, pot[1:]):
        if x0 < x1:
            nova_smer = 1
        elif x0 > x1:
            nova_smer = 3
        elif y0 < y1:
            nova_smer = 2
        elif y0 > y1:
            nova_smer = 0
        while smer != nova_smer:
            ukazi += "DESNO "
            smer = (smer + 1) % 4
        ukazi += str(abs(x1 - x0 + y1 - y0)) + " "
        smer = nova_smer
    return ukazi[:-1]


