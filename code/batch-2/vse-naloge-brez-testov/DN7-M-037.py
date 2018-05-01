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
    return sum([1 for k1 in range(x-1, x+2) for k2 in range(y-1, y+2) if (k1, k2) in mine and (k1, k2) != (x, y)])

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
   return {sosedov(v1, v2, mine): (v1, v2) for v1, v2 in vsa_polja(s, v)}[max({sosedov(v1, v2, mine): (v1, v2) for v1, v2 in vsa_polja(s, v)})]
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
    return {(z1, z2) for z1, z2 in vsa_polja(s, v) if sosedov(z1, z2, mine) == 0}


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
    return {i: {(x, y) for x,y in vsa_polja(s, v) if sosedov(x, y, mine) == i} for i in range(9)}




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
    return sum([abs(x2-x1)+abs(y2-y1) for (x1, y1), (x2, y2) in zip(pot, pot[1:])])

"""
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    return not any([True for x in range(min([x0, x1]), max([x0, x1]) + 1) for y in range(min([y0, y1]), max([y0, y1]) + 1) if (x, y) in mine])

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
    return all(varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in (zip(pot, pot[1:]) if len(pot) > 1 else zip(pot, pot)))
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
    visina = 0
    mine = set()
    for vrsta in polje.split():
        i = 0
        for kvadratek in vrsta:
            if kvadratek == "X":
                mine.add((i, visina))
            i += 1
        visina += 1
    return (mine, len(vrsta), visina)

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
    zac_tocka = x, y = (0 ,0)
    pot = [zac_tocka]
    smer = 0
    for ukaz in ukazi.split():
        if ukaz == "DESNO":
            smer += 90
        elif ukaz == "LEVO":
            smer -= 90
        elif ukaz.isdigit():
            while smer // 360 > 0:
                smer -= 360
            if smer == 0:
                y -= int(ukaz)
            elif abs(smer) == 180:
                y += int(ukaz)
            elif smer == -90 or smer == 270:
                x -= int(ukaz)
            elif smer == 90 or smer == -270:
                x += int(ukaz)
            pot.append((x, y))
    return pot


"""
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
"""


def zapisi_pot(pot):
    smer = 0
    ukazi = []
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if smer // 360 > 0:
            smer -= 360
        if x1 > x0:
            while smer != 90 and smer != -270:
                if smer == 180:
                    smer = 90
                    ukazi.append("LEVO")
                else:
                    smer += 90
                    ukazi.append("DESNO")
            ukazi.append((x1 - x0))
        elif x0 > x1:
            while smer != 270 and smer != 0-90:
                if smer == 0 or smer == 360:
                    smer = -90
                    ukazi.append("LEVO")
                else:
                    smer += 90
                    ukazi.append("DESNO")
            ukazi.append((x0 - x1))
        elif y1 > y0:
            while smer != 180 and smer != -180:
                if smer == 270 or smer == -90:
                    smer = 180
                    ukazi.append("LEVO")
                else:
                    smer += 90
                    ukazi.append("DESNO")
            ukazi.append((y1 - y0))
        elif y0 > y1:
            while smer != 0 and smer != 360:
                if smer == 90 or smer == -270:
                    smer = 0
                    ukazi.append("LEVO")
                else:
                    smer += 90
                    ukazi.append("DESNO")
            ukazi.append((y0 - y1))
    return "\n".join(str(x) for x in ukazi)


"""
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
"""



