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

    number_of_mines = 0
    for i in range(1, -1, -1):
        # Top side
        if (x - i, y - 1) in mine:
            number_of_mines += 1

        # Right side
        if (x + 1, y - i) in mine:
            number_of_mines += 1

        # Down side
        if (x + i, y + 1) in mine:
            number_of_mines += 1

        # Left side
        if (x - 1, y + i) in mine:
            number_of_mines += 1

    return number_of_mines



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

    largest_number_of_mines = -1
    searched_coordinate = (-1, -1)
    for y in range(v):
        for x in range(s):
            number_of_mines = sosedov(x, y, mine)
            if number_of_mines > largest_number_of_mines:
                largest_number_of_mines = number_of_mines
                searched_coordinate = (x, y)

    return searched_coordinate


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

    coordinates_no_neighbor_mines = set()
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) == 0:
                coordinates_no_neighbor_mines.add((x, y))

    return coordinates_no_neighbor_mines

def number_of_neighbors(mines, width, height, number):
    # This is basically just a copy of the previous function
    # makes the function po_sosedih() way more readable
    coordinates_number_neighbor_mines = set()
    for y in range(height):
        for x in range(width):
            if sosedov(x, y, mines) == number:
                coordinates_number_neighbor_mines.add((x, y))

    return coordinates_number_neighbor_mines

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

    number_of_mines_dict = collections.defaultdict(set)
    for i in range(9):
        number_of_mines_dict[i] = number_of_neighbors(mine, s, v, i)

    return number_of_mines_dict


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

    path_length = 0
    for i in range(len(pot) - 1):
        # We add the difference between x and y of neighbor points in the path
        path_length += abs(pot[i + 1][0] - pot[i][0])
        path_length += abs(pot[i + 1][1] - pot[i][1])

    return path_length


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

    if (x0, y0) in mine:
        return False

    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    for i in range(dolzina_poti([(x0, y0), (x1, y1)]) + 1):
        x = x0
        y = y0
        if x0 != x1:
            x += i
        elif y0 != y1:
            y += i

        if (x, y) in mine:
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
        return varen_premik(pot[0][0], pot[0][1], pot[0][0], pot[0][1], mine)

    for i in range(len(pot) - 1):
        if not varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine):
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

    # Remove the last space if the user has 'Accidentally' left it there
    if polje[-1] == " ":
        polje = polje[:-1]

    mines = set()
    lines = polje.split(" ")
    width = 0
    height = len(lines)

    x = 0
    y = 0
    for line in lines:
        for char in line:
            if char == 'X':
                mines.add((x, y))
            x += 1

        width = x
        x = 0
        y += 1

    return mines, width, height





########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.

def sosedov(x, y, mine):
    return len([(x0, y0) for x0 in range(x - 1, x + 2) for y0 in range(y - 1, y + 2) if (x0, y0) in mine - {(x, y)}])

def najvec_sosedov(mine, s, v):
    return {sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s,v)}.get(max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}))

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {i:set([(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i]) for i in range(9)}

def dolzina_poti(pot):
    return sum([abs(pot[i + 1][0] - pot[i][0]) + abs(pot[i + 1][1] - pot[i][1]) for i in range(len(pot) - 1)])

def varen_premik(x0, y0, x1, y1, mine):
    return all([False if (x2, y2) in mine else True for x2 in range(min(x0, x1), max(x0, x1) + 1) for y2 in range(min(y0, y1), max(y0, y1) + 1)])

def varna_pot(pot, mine):
    return all([False if len(pot) == 1 and pot[0] in mine else True] + [varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine) for i in range(len(pot) - 1)])

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


