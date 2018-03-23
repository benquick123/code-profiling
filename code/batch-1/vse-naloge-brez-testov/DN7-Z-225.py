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
    Vrni število sosedov polja s koordinatafmi `(x, y)` na katerih je mina.
    Polje samo ne šteje.

    Args:
        x (int): koordinata x
        y (int): koordinata y
        mine (set of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """
    mina = 0
    for koordinata in mine:
        if koordinata == (x-1, y-1) in mine or koordinata == (x, y-1) in mine or koordinata == (x+1, y-1) in mine or \
                                koordinata == (x-1, y) in mine or koordinata == (x+1, y) in mine or \
                                koordinata == (x-1, y+1) in mine or koordinata == (x, y+1) in mine or koordinata == (x+1, y+1) in mine:
            mina += 1
    return mina

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
    najvec = 0
    a = 0
    b = 0
    for y in range(v):
        for x in range(s):
            sos = sosedov(x, y, mine)
            if najvec < sos:
                najvec = sos
                a = x
                b = y
    return (a, b)

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
    mnozica = set()
    for y in range(v):
        for x in range(s):
            sos = sosedov(x, y, mine)
            if sos == 0:
                mnozica.add((x, y))
    return mnozica

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
    for i in range(9):
        slovar[i] = set()
    for y in range(v):
        for x in range(s):
            slovar[sosedov(x, y, mine)].add((x, y))
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

    dolzina = 0
    for i in range(len(pot) - 1):
        if pot[i][0] != pot[i + 1][0]:  # x prve terke je pot[i][0], x druge...
            dolzina += abs(pot[i][0] - pot[i + 1][0])
        if pot[i][1] != pot[i + 1][1]:  # y prve terke ... [1]
            dolzina += abs(pot[i][1] - pot[i + 1][1])
    return dolzina

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
    #razdalja = 0
    if x0 == x1:
        razdalja = y0 - y1
        for i in range(razdalja):
            s = [x0, y0 + 1]
            if tuple(s) in mine:
                return False
    if y0 == y1:
        razdalja = x0 - x1
        for i in range(razdalja):
            s = [x0 + 1, y0]
            if tuple(s) in mine:
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


