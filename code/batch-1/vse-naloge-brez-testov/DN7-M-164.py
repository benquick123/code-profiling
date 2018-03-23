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
    
    ctr = 0
    for i in mine:
        if i in {(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)}:
            ctr += 1
    return ctr


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
    
    maximum = 0
    najvec = (0, 0)
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine) > maximum:
            najvec = (x, y)
            maximum = sosedov(x, y, mine)
    return najvec
    

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

    najmanj = set()
    for x in range(0, s):
        for y in range(0, v):
            if sosedov(x, y, mine) == 0:
                najmanj.add((x, y))    
    return najmanj


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

    slovar = {}
    for i in range(0, 9):
        for x, y in vsa_polja(s, v):
            if i not in slovar:
                slovar[i] = set()
            if sosedov(x, y, mine) == i:
                slovar[i].add((x, y))
    return slovar
        

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
    
    skupnaPot = 0
    for i in range(0, len(pot) - 1):
        if pot[i][0] != pot[i + 1][0]:
            skupnaPot += abs(pot[i + 1][0] - pot[i][0])
        if pot[i][1] != pot[i + 1][1]:
            skupnaPot += abs(pot[i + 1][1] - pot[i][1])
    return skupnaPot
    

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
    
    for i in range(len(mine)):
        if (x0, y0) in mine or (x1, y1) in mine:
            return False
        else:
            if x0 < x1:
                x0 += 1
            elif x0 > x1:
                x0 -= 1
            elif y0 < y1:
                y0 += 1
            elif y0 > y1:
                y0 -= 1
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

    if pot != []:
        if pot[0] in mine:
            return False
        else:
            for i in range(0, len(pot) - 1):
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

    mine = set()
    minskoPolje = polje.split()

    for index, value in enumerate(minskoPolje):
        for i, x in enumerate(value):
            if x == 'X':
                mine.add((i, index))
            
    return ((mine, len(value), len(minskoPolje)))

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


