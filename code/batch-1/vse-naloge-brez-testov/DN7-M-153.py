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
    return sum(True for polje in mine if polje in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),(x + 1, y + 1), ])

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
    return max((x,y) for x,y in vsa_polja(s, v) if sosedov(x,y,mine) == max(sosedov(x1,y1,mine) for x1, y1 in vsa_polja(s,v)))

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
    return set(tuple((x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0))

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
    return dict((k, set(tuple(n for n in vsa_polja(s, v) if sosedov(n[0], n[1], mine) == k))) for k in range(9))

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
    return sum(int(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2))for (x0, y0), (x1, y1) in zip(pot, pot[1:]))

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
    return all([False for y in range(y0, y1 + 1, 1) if (x0, y) in mine] +
               [False for y in range(y0, y1 - 1, -1) if (x0, y) in mine] +
               [False for x in range(x0, x1 + 1, 1) if (x, y0)  in mine] +
               [False for x in range(x0, x1 - 1, -1) if (x, y0)  in mine])

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all([varen_premik(x0,y0,x1,y1,mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])] +
               [True if len(pot) == 0 or pot[0] not in mine else False])


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
    polje = polje.split()
    visina = len(polje)
    sirina = len(polje[0])
    mine = set()
    koordinate = (0, 0)
    for y in range(visina):
        for x in range (sirina):
            if polje[y][x] == "X":
                koordinate = x, y
                mine.add(koordinate)
    return mine, sirina, visina

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
    pot = [(0,0),]
    x, y = 0, 0
    smer = 90
    ukazi = ukazi.split()
    for ukaz in ukazi:
        if ukaz == "DESNO":
            smer -= 90
            if smer < 0:
                smer = 270
        elif ukaz == "LEVO":
            smer += 90
            if smer == 360:
                smer = 0
        else:
            if smer == 90:
                x,y = x, y - int(ukaz)
                pot.append((x, y))
            if smer == 0:
                x, y = x + int(ukaz), y
                pot.append((x, y))
            if smer == 270:
                x, y = x, y + int(ukaz)
                pot.append((x, y))
            if smer == 180:
                x, y = x - int(ukaz), y
                pot.append((x, y))
    return pot

def premik(smer):
    smer -= 90
    if smer < 0:
        smer = 270
    return smer

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    smer = 90
    koncnaPot = ""
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if x0 == x1:
            if y0 < y1:
                while smer != 270:
                    koncnaPot += "DESNO\n"
                    smer = premik(smer)
                koncnaPot += str(y1 - y0) + "\n"
            if y0 > y1:
                while smer != 90:
                    koncnaPot += "DESNO\n"
                    smer = premik(smer)
                koncnaPot += str(y0 - y1) + "\n"
        if y0 == y1:
            if x0 < x1:
                while smer != 0:
                    koncnaPot += "DESNO\n"
                    smer = premik(smer)
                koncnaPot += str(x1 - x0) + "\n"
            if x0 > x1:
                while smer != 180:
                    koncnaPot += "DESNO\n"
                    smer = premik(smer)
                koncnaPot += str(x0 - x1) + "\n"
    return koncnaPot

