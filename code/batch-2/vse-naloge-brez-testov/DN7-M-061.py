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
    preveri = []
    preveri.append((x - 1, y))
    preveri.append((x - 1, y - 1))
    preveri.append((x, y - 1))
    preveri.append((x + 1, y - 1))
    preveri.append((x + 1, y))
    preveri.append((x + 1, y + 1))
    preveri.append((x, y + 1))
    preveri.append((x - 1, y + 1))
    bombe = 0
    for p in preveri:
        if p in mine:
            bombe += 1
    return bombe


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
    najvec_min = (0, 0)
    visina = 0
    while visina < v:
        sirina = 0
        while sirina < s:
            if sosedov(sirina, visina, mine) > najvec:
                najvec = sosedov(sirina, visina, mine)
                najvec_min = (sirina, visina)
            sirina += 1
        visina += 1
    return najvec_min


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
    osamljena_polja = set()
    visina = 0
    while visina < v:
        sirina = 0
        while sirina < s:
            if sosedov(sirina, visina, mine) == 0:
                osamljena_polja.add((sirina, visina))
            sirina += 1
        visina += 1
    return osamljena_polja


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
    po_sosedih_slovar = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
    visina = 0
    while visina < v:
        sirina = 0
        while sirina < s:
            po_sosedih_slovar[sosedov(sirina, visina, mine)].add((sirina, visina))
            sirina += 1
        visina += 1
    return po_sosedih_slovar


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
    c = 0
    while c < len(pot) - 1:
        if pot[c][0] == pot[c + 1][0]:
            if pot[c][1] < pot[c + 1][1]:
                dolzina += pot[c + 1][1] - pot[c][1]
            if pot[c][1] > pot[c + 1][1]:
                dolzina += pot[c][1] - pot[c + 1][1]
        if pot[c][1] == pot[c + 1][1]:
            if pot[c][0] < pot[c + 1][0]:
                dolzina += pot[c + 1][0] - pot[c][0]
            if pot[c][0] > pot[c + 1][0]:
                dolzina += pot[c][0] - pot[c + 1][0]
        c += 1
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
    c = 0
    c1 = 0
    navpicno = True
    if x0 == x1:
        if y0 < y1:
            c = y0
            c1 = y1
        else:
            c = y1
            c1 = y0
    if y0 == y1:
        navpicno = False
        if x0 < x1:
            c = x0
            c1 = x1
        else:
            c = x1
            c1 = x0
    while c <= c1:
        if navpicno:
            if (x0, c) in mine:
                return False
        else:
            if (c, y0) in mine:
                return False
        c += 1
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
    c = 0
    while c < len(pot) - 1:
        if not varen_premik(pot[c][0], pot[c][1], pot[c + 1][0], pot[c + 1][1], mine):
            return False
        c += 1
    if len(pot) == 1:
        if pot[0] in mine:
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
    bombe = set()
    vrstice = polje.split()
    vrstica_stevec = 0
    while vrstica_stevec < len(vrstice):
        stolpec_stevec = 0
        while stolpec_stevec < len(vrstice[vrstica_stevec]):
            if str.lower(vrstice[vrstica_stevec][stolpec_stevec]) == 'x':
                bombe.add((stolpec_stevec, vrstica_stevec))
            stolpec_stevec += 1
        vrstica_stevec += 1
    return bombe, len(vrstice[0]), len(vrstice)

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


