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
    isky = y - 1
    stmin = 0
    while isky <= y + 1:
        iskx = x - 1
        while iskx <= x + 1:
            if (iskx, isky) in mine:
                stmin += 1
            iskx += 1
        isky += 1
    if (x, y) in mine:
        stmin -= 1
    return stmin



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
    y = 0
    maxmine = 0
    maxy, maxx = 0, 0
    while y <= v-1:
        x = 0
        while x <= s-1:
            if sosedov(x, y, mine) > maxmine:
                maxmine = sosedov(x, y, mine)
                maxy = y
                maxx = x
            x += 1
        y += 1
    return (maxx, maxy)

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
    y = 0
    mnozica = set()
    while y <= v - 1:
        x = 0
        while x <= s - 1:
            if sosedov(x, y, mine) == 0:
                mnozica.add((x, y))
            x += 1
        y += 1
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
    dictpoljamine = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
    stmin = 0
    while stmin <= 8:
        y = 0
        while y <= v - 1:
            x = 0
            while x <= s - 1:
                if sosedov(x, y, mine) == stmin:
                    dictpoljamine[stmin].add((x, y))
                x += 1
            y += 1
        stmin += 1
    return dictpoljamine

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
    dolzinapoti = 0
    i = 0
    j = 1
    while j < len(pot):
        dolzinapoti = dolzinapoti + abs(pot[j][0]-pot[i][0])
        dolzinapoti = dolzinapoti + abs(pot[j][1]- pot[i][1])
        j += 1
        i += 1
    return dolzinapoti

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
    if y0 == y1:
        if x0 < x1:
            while x0 <= x1:
                if (x0, y0) in mine:
                    return False
                x0 += 1
        else:
            while x0 >= x1:
                if (x0, y0) in mine:
                    return False
                x0 -= 1

    else:
        if y0 < y1:
            while y0 <= y1:
                if (x0, y0) in mine:
                    return False
                y0 += 1
        else:
            while y0 >= y1:
                if (x0, y0) in mine:
                    return False
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
    i = 0
    j = 1
    if len(pot) == 1:
        if pot[0] in mine:
            return False
        else:
            return True

    while j < len(pot):
        if varen_premik(pot[i][0],pot[i][1],pot[j][0], pot[j][1], mine) == True:
            i += 1
            j += 1
        else:
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
    spl1 = polje.split()
    koordmin = set()
    i = 0
    while i < len(spl1):
        spl2 = list(spl1[i])
        j = 0
        while j < len(spl2):
            if spl2[j] == "X":
                koordmin.add((j, i))
            j += 1
        i += 1

    return koordmin, len(spl2), len(spl1)



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


