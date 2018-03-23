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
    return len([(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if (i, j) in mine and (i, j) != (x, y)])


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
    return {sosedov(i, j, mine): (i, j) for i in range(0, s) for j in range(0, v)}[max([sosedov(i, j, mine) for i in range(0, s) for j in range(0, v)])]

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
    return {(i, j) for i in range(0, s) for j in range(0, v) if sosedov(i, j, mine) == 0}

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
    return {n: {(i, j) for i in range(0, s) for j in range(0, v) if sosedov(i, j, mine) == n} for n in range(0, 9)}


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
    return sum([abs((pot[i][0] - pot[i - 1][0]) + (pot[i][1] - pot[i - 1][1])) for i in reversed(range(1, len(pot)))])


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
    return all([(i, j) not in mine for i in range(min(x0, x1), max(x0, x1) + 1) for j in range(min(y0, y1), max(y0, y1) + 1)])


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all([varen_premik(pot[i][0], pot[i][1], pot[i - 1][0], pot[i - 1][1], mine) for i in reversed(range(1, len(pot)))] + [pot[i] not in mine for i in reversed(range(0, len(pot)))])


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
    x = 0
    y = 0
    mi = set()
    polje = [x for x in polje.split(" ") if x]
    print(polje)
    for vr in polje:
        for zn in vr:
            if zn == "X":
                mi.add((x, y))
            x += 1
        y += 1
        x = 0
    return (mi, len(polje[0]), len(polje))


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def shift(l, n):
    return l[n:] + l[:n]

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """
    x = y = 0
    smer = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pot = [(x, y)]
    ukazi = [x for x in ukazi.split("\n") if x]
    for ukaz in ukazi:
        if ukaz == "DESNO":
            smer = shift(smer, 1)
        elif ukaz == "LEVO":
            smer = shift(smer, -1)
        else:
            x = x + int(ukaz) * smer[0][0]
            y = y + int(ukaz) * smer[0][1]
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
    smer = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pot_opis = ""
    i = 0
    while (i < len(pot) - 1):
        n = abs((pot[i + 1][0] - pot[i][0]) + (pot[i + 1][1] - pot[i][1]))
        x = pot[i][0] + n * smer[0][0]
        y = pot[i][1] + n * smer[0][1]
        if x == pot[i + 1][0] and y == pot[i + 1][1]:
            pot_opis = pot_opis + str(n) + "\n"
        else:
            smer = shift(smer, 1)
            pot_opis = pot_opis + "DESNO\n"
            i -= 1
        i += 1
    return pot_opis


