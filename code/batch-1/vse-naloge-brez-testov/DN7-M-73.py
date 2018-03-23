# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from math import sqrt


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

    return sum(
        [1 for c in mine if sqrt(((int(c[0]) - x) ** 2) + ((int(c[1]) - y) ** 2)) <= 1.5 and sqrt(
            ((int(c[0]) - x) ** 2) + ((int(c[1]) - y) ** 2)) > 0])


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

    return tuple([(x, y) for x in range(s) for y in range(v) if
                  sosedov(x, y, mine) == max([(sosedov(m, n, mine)) for m in range(s) for n in range(v)])])[0]


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

    return set([(x, y) for x in range(s) for y in range(v) if
                sosedov(x, y, mine) == 0])


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

    return {c: set([(x, y) for x in range(s) for y in range(v) if
                    sosedov(x, y, mine) == c]) for c in range(0, 9)}


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

    return sum(
        [sqrt(((pot[x][0] - pot[x - 1][0]) ** 2) + ((pot[x][1] - pot[x - 1][1]) ** 2)) for x in range(1, len(pot)) if
         pot[x][0] == pot[x - 1][0] or pot[x][1] == pot[x - 1][1]])


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

    return all([(x, y) not in [(m[0], m[1]) for m in mine]
                for x in range(min(x0, x1), max(x0, x1) + 1) for y in range(min(y0, y1), max(y0, y1) + 1)])


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

    #return all([varen_premik(pot[x][0], pot[x][1], pot[x+1][0], pot[x+1][1], mine) for x in range(0, len(pot)-1)])

    return True if all([True for (x0, y0), (x1, y1) in zip(pot, pot[1:]) if varen_premik(x0, y0, x1, y1, mine)] +
                       [False for (x0, y0), (x1, y1) in zip(pot, pot[1:]) if not varen_premik(x0, y0, x1, y1, mine)] +
                       [False for i in pot if (i[0], i[1]) in mine]) else False


########################
# Za oceno 8

def dolzina(polje):
    for x in range(len(polje)):
        if polje[x] == ' ':
            return x
    else:
        return len(polje)


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
    m = ()

    for c in range(len(polje)):
        if polje[c] == 'X':
            m += (x, y),
        x += 1
        if polje[c] == ' ':
            y += 1
            x = 0

        if polje[len(polje) - 1] == ' ' and c == len(polje) - 1:
            y -= 1

    return (set(m), dolzina(polje), y + 1)


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
    x_k = 0
    y_k = 0

    p = 1
    pot = []
    pot += (0, 0),

    ukazi = ukazi.split('\n')

    for m in ukazi:

        if m == "DESNO":
            if p == 1:
                p = 4
            else:
                p -= 1
        elif m == "LEVO":
            if p == 4:
                p = 1
            else:
                p += 1
        elif m.isalnum():
            if p == 3:
                y_k += int(m)
            elif p == 4:
                x_k += int(m)
            elif p == 1:
                y_k -= int(m)
            elif p == 2:
                x_k -= int(m)
            pot += (x_k, y_k),

    return pot


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    u = ()
    p = 1
    for c in range(1, len(pot)):
        if pot[c][1] > pot[c - 1][1]:
            if p == 2:
                p = 3
                u += 'LEVO',
            elif p == 4:
                p = 3
                u += 'DESNO',
            elif p == 1:
                p = 3
                u += 'DESNO', 'DESNO'
            u += str(pot[c][1] - pot[c - 1][1]),
        elif pot[c][1] < pot[c - 1][1]:
            if p == 2:
                p = 1
                u += 'DESNO',
            elif p == 4:
                p = 1
                u += 'LEVO',
            elif p == 3:
                p = 1
                u += 'DESNO', 'DESNO'
            u += str(pot[c - 1][1] - pot[c][1]),
        elif pot[c][0] > pot[c - 1][0]:
            if p == 1:
                p = 4
                u += 'DESNO',
            elif p == 3:
                p = 4
                u += 'LEVO',
            elif p == 2:
                p = 4
                u += 'DESNO', 'DESNO'
            u += str(pot[c][0] - pot[c - 1][0]),
        elif pot[c][0] < pot[c - 1][0]:
            if p == 1:
                p = 2
                u += 'LEVO',
            elif p == 3:
                p = 2
                u += 'DESNO',
            elif p == 4:
                p = 2
                u += 'DESNO', 'DESNO'
            u += str(pot[c - 1][0] - pot[c][0]),
        c += 1

    return '\n'.join(u)


