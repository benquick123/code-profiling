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

################################################################### ZA OCENO 6 ###################################################################

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
    return len([vsa_polja(s, v) for s in range(x - 1, x + 2) for v in range(y - 1, y + 2) if (s, v) in [element for element in mine] if (s, v) != (x, y)])


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
    return next(m for m in vsa_polja(s, v) if sosedov(m[0], m[1], mine) == max(sosedov(m[0], m[1], mine) for m in vsa_polja(s, v)))

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
    return {n: {(x, y) for (x, y) in vsa_polja(s, v) if sosedov(x, y, mine) == n} for n in range(9)}

################################################################### ZA OCENO 7 ###################################################################

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """
    return sum(x for x in (abs(pot[i][0] - pot[i + 1][0]) + abs(pot[i][1] - pot[i + 1][1]) for i in range(len(pot) - 1)))


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
    return all(max(y0, y1) < y or min(y0, y1) > y if x0 == x else max(x0, x1) < x or min(x0, x1) > x if y0 == y else True for (x, y) in mine)

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all(element not in mine if len(pot) <= 1 else all(varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine) for i in range(len(pot) - 1)) for element in pot)

################################################################### ZA OCENO 8 ###################################################################

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
    coordinates = []
    field_size = []
    splitted_map = polje.split(" ")
    for row, row_elements in enumerate(splitted_map):
        column = 0
        for element in row_elements:
            if element == ".":
                column += 1
            else:
                coordinates.append((column, row))
                column += 1
        if row == len(splitted_map) - 1:
            field_size.append(column)
            field_size.append(len(splitted_map))
    return (set(coordinates), field_size[0], field_size[1])

################################################################### ZA OCENO 9 ###################################################################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


################################################################### ZA OCENO 10 ###################################################################

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """
    a = ukazi.split()
    list_of_steps = []
    x = 0
    y = 0
    list_of_steps.append((x, y))
    orientation = 90
    for ukaz in a:
        if ukaz == "DESNO":
            orientation += 90
        elif ukaz == "LEVO":
            orientation -= 90
        else:
            step = int(ukaz)
            if orientation % 360 == 90:
                y -= step
                list_of_steps.append((x, y))
            elif orientation % 360 == 180:
                x += step
                list_of_steps.append((x, y))
            elif orientation % 360 == 270:
                y += step
                list_of_steps.append((x, y))
            elif orientation % 360 == 0:
                x -= step
                list_of_steps.append((x, y))
    return list_of_steps

### Auxiliary function
def orientation(orient_start, orient_fin):
    """
        Za podatene orientacije nam vrne ukaze in novo usmeritev, ki so potrebni, da pridemo do ciljne točke.

        Args:
            začetna orientacija (int): smer v katero je pot trenutno usmerjena
            željena_orientacija (int): smer v katero moramo iti, da pridemo do ciljne koordinate

        Returns:
            list of orders: ukazi
            int: smer v katero je pot na novo usmerjena
        """
    orders = []
    orientations = orient_start
    while orientations % 360 != orient_fin % 360:
        orientations += 90
        orders += ["DESNO"]
    return orders, orientations % 360


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    list_of_orders = []
    orientations = 90
    for i in range(len(pot) - 1):

        if pot[i + 1][0] > pot[i][0]:
            list_of_orders += orientation(orientations, 180)[0]
            orientations = orientation(orientations, 180)[1]
            list_of_orders += str((abs(pot[i + 1][0] - pot[i][0])))

        elif pot[i + 1][0] < pot[i][0]:
            list_of_orders += orientation(orientations, 0)[0]
            orientations = orientation(orientations, 0)[1]
            list_of_orders += str(abs(pot[i + 1][0] - pot[i][0]))

        elif pot[i + 1][1] > pot[i][1]:
            list_of_orders += orientation(orientations, 270)[0]
            orientations = orientation(orientations, 270)[1]
            list_of_orders += str(abs(pot[i + 1][1] - pot[i][1]))

        elif pot[i + 1][1] < pot[i][1]:
            list_of_orders += orientation(orientations, 90)[0]
            orientations = orientation(orientations, 90)[1]
            list_of_orders += str(abs(pot[i + 1][1] - pot[i][1]))

    return "\n".join(list_of_orders)


################################################################### TESTS ###################################################################
