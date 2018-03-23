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
    stevilo = 0
    for (a, b) in mine:
        if x-1<=a<=x+1 and y-1<=b<=y+1 and (a,b) != (x,y):
            stevilo += 1
    return stevilo


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
    naj = (0, 0)
    st_sosedov = 0
    for (x, y) in vsa_polja(s, v):
        sosedi = sosedov(x, y, mine)
        if sosedi > st_sosedov:
            st_sosedov = sosedi
            naj = (x, y)
    return naj


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
    sosedless = set()
    for (x, y) in vsa_polja(s, v):
        if sosedov(x, y, mine) == 0:
            sosedless.add((x,y))
    return sosedless


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
    slovar = {i: set() for i in range(9)}
    for x, y in vsa_polja(s, v):
        for a in slovar:
            if a == sosedov(x, y, mine):
                slovar[a].add((x, y))
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
    vsota = 0
    if pot:
        (x1, y1) = pot[0]
    for (x, y) in pot:
        vsota += abs((x - x1) + (y - y1))
        x1, y1 = x, y
    return vsota

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
    premiki = set()
    premiki.add((x0,y0))
    premiki.add((x1,y1))
    if x0 == x1:
        for b in range(y0, y1):
            premiki.add((x0, b))
        for b in range(y0, y1, -1):
            premiki.add((x0, b))
    if y0 == y1:
        for a in range(x0, x1):
            premiki.add((a, y0))
        for a in range(x0, x1, -1):
            premiki.add((a, y0))
    if premiki & mine1:
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
    if pot:
        (a, b) = pot[0]
        for (a1, b1) in pot:
            if not varen_premik(a,b,a1,b1, mine):
                return False
            a, b = a1, b1
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
    mnozica = set()
    vrstice = polje.split(" ")
    visina = len(vrstice)
    sirina = (len(vrstice[0]))
    x = y = 0
    for vrsta in vrstice:
        x = 0
        for crka in vrsta:
            if crka == ".":
                x += 1
            if crka == "X":
                mnozica.add((x,y))
                x += 1
        y += 1
    return(mnozica, sirina, visina)

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


