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
    '''
    koordinate_sosedov = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1),
                          (x, y + 1), (x + 1, y + 1)]
    return sum([1 for sosed in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1),
                          (x, y + 1), (x + 1, y + 1)] if sosed in mine])'''

    return sum([1 for x_ in range(x - 1, x + 2) for y_ in range(y - 1, y + 2) if (not(x_ == x and y_ == y)) and (x_, y_) in mine])


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
    return [(x_, y_) for x_, y_, st_sosedov_ in [[x, y, sosedov(x, y, mine)] for x in range(s) for y in range(v)] if st_sosedov_ == max([e2 for e0, e1, e2 in [[x, y, sosedov(x, y, mine)] for x in range(s) for y in range(v)]])][0]


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
    return {(x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == 0}


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
    return {stevec: {(x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == stevec} for stevec in range(9)}


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
    return sum(abs(pot[i+1][0]-pot[i][0])+abs(pot[i+1][1]-pot[i][1]) for i, _ in enumerate(pot) if i < len(pot)-1)


def celotna_pot(x0, y0, x1, y1, delna_pot):
    seznam = []
    for i in range(0, len(delna_pot)-1):
        for x in range(delna_pot[i][0], delna_pot[i+1][0]):
            seznam.append((x, delna_pot[i][1]))
        for y in range(delna_pot[i][1], delna_pot[i+1][1]):
            seznam.append((delna_pot[i][0], y))
    return seznam

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
    return all([False if (x_,y_) in mine else True for x_, y_ in zip([x for x in (range(min(x0, x1), max(x0, x1)+1) if x0 != x1 else [x0] * (abs(y1 - y0) + 1))], [y for y in (range(min(y0, y1), max(y0, y1)+1) if y0 != y1 else [y0] * (abs(x1 - x0) + 1))])])

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all([varen_premik(xy0[0], xy0[1], xy1[0], xy1[1], mine) for xy0, xy1 in zip(pot, pot[1:] if len(pot) > 1 else pot)])


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
    mine = []
    mnozica = set()

    polja = [x for x in polje.split(" ") if x]
    print(polja)
    print("konec")
    for vrstica in range(len(polja)):
        for stolpec in range(len(polja[vrstica])):
            if polja[vrstica][stolpec] == "X":
                mnozica.add((stolpec, vrstica))
    mine.append(mnozica)
    mine.append(stolpec + 1)
    mine.append(vrstica + 1)
    return tuple(mine)


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
    koordinate = [0, 0]
    smer = 0
    # 0 = GOR
    # 1 = DESNO
    # 2 = DOL
    # 3 = LEVO

    for ukaz in ukazi.splitlines():
        if not ukaz.isnumeric():
            if ukaz == "DESNO":
                smer += 1
            elif ukaz == "LEVO":
                smer -= 1
            if smer > 3:
                smer = 0
            if smer < 0:
                smer = 3
        else:
            st = int(ukaz)
            if smer == 0:
                koordinate[1] -= st
            elif smer == 1:
                koordinate[0] += st
            elif smer == 2:
                koordinate[1] += st
            elif smer == 3:
                koordinate[0] -= st
            pot.append(tuple(koordinate))
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

    smer = 0
    # 0 = GOR
    # 1 = DESNO
    # 2 = DOL
    # 3 = LEVO

    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
            if x1 > x0:
                while smer != 1:
                    smer += 1
                    ukazi += ("DESNO\n")
                    if smer > 3:
                        smer = 0
                ukazi += (str(abs(x1-x0))) + "\n"
            if y1 > y0:
                while smer != 2:
                    smer += 1
                    ukazi += ("DESNO\n")
                    if smer > 3:
                        smer = 0
                ukazi += (str(abs(y1-y0))) + "\n"

            if x0 > x1:
                while smer != 3:
                    smer += 1
                    ukazi += ("DESNO\n")
                    if smer > 3:
                        smer = 0
                ukazi += (str(abs(x1-x0))) + "\n"

            if y0 > y1:
                while smer != 0:
                    smer += 1
                    ukazi += ("DESNO\n")
                    if smer > 3:
                        smer = 0
                ukazi += (str(abs(y1-y0))) + "\n"

    return ukazi



